import logging
from types import SimpleNamespace
from unittest.mock import MagicMock, call

import pytest
import requests

from python.common.enums import ErrorCode
from python.form_handler import actions_formsflow


@pytest.fixture(autouse=True)
def configure_verbose_logging(monkeypatch):
    monkeypatch.setattr(logging, "verbose", MagicMock(), raising=False)


def _config():
    return SimpleNamespace(
        KEYCLOAK_URL="https://keycloak.example.test",
        KEYCLOAK_REALM="forms",
        KEYCLOAK_CLIENT_ID="offline-worker",
        KEYCLOAK_CLIENT_SECRET="client-secret",
        FORMIO_API_URL="https://formio.example.test",
        FORMSFLOW_API_URL="https://formsflow.example.test",
        WEB_APP_URL="https://forms.example.test",
    )


def _app_context_mock():
    app = MagicMock()
    app.app_context.return_value.__enter__ = MagicMock(return_value=None)
    app.app_context.return_value.__exit__ = MagicMock(return_value=False)
    return app


def _token_response(access_token="keycloak-token"):
    response = MagicMock()
    response.text = "token response"
    response.json.return_value = {"access_token": access_token}
    return response


def _args(submission_data, **overrides):
    args = {
        "app": _app_context_mock(),
        "db": MagicMock(),
        "config": _config(),
        "message": {"id": 42},
        "submission_data": submission_data,
        "offline_submission_id": 42,
        "formio_submission_id": "formio-submission-17",
    }
    args.update(overrides)
    return args


def _submission_data(**overrides):
    data = {
        "form_id": "form-123",
        "application_id": None,
        "username": "officer@example.test",
        "payload": {
            "data": {"firstName": "Ada", "lastName": "Lovelace"},
            "serverDraftId": None,
        },
    }
    data.update(overrides)
    return data


def test_send_to_formsflow_creates_application_and_persists_id(monkeypatch):
    args = _args(_submission_data())
    offline_submission = SimpleNamespace(status="sent_to_formio", application_id=None)
    args["db"].session.query.return_value.filter_by.return_value.first.return_value = offline_submission
    create_response = MagicMock(status_code=201, text="created")
    create_response.json.return_value = {"id": "application-55"}
    post = MagicMock(side_effect=[_token_response(), create_response])
    monkeypatch.setattr(actions_formsflow.requests, "post", post)

    result, out_args = actions_formsflow.send_to_formsflow(**args)

    assert result is True
    assert out_args == args
    assert post.call_args_list == [
        call(
            "https://keycloak.example.test/auth/realms/forms/protocol/openid-connect/token",
            data={
                "grant_type": "client_credentials",
                "client_id": "offline-worker",
                "client_secret": "client-secret",
            },
        ),
        call(
            "https://formsflow.example.test/application/create",
            json={
                "formId": "form-123",
                "submissionId": "formio-submission-17",
                "formUrl": "https://formio.example.test/form/form-123/submission/formio-submission-17",
                "webFormUrl": "https://forms.example.test/form/form-123/submission/42",
                "data": {"firstName": "Ada", "lastName": "Lovelace"},
                "createdBy": "officer@example.test",
            },
            headers={"Authorization": "Bearer keycloak-token"},
        ),
    ]
    create_response.raise_for_status.assert_called_once_with()
    args["db"].session.query.assert_called_once_with(
        actions_formsflow.FormsflowOfflineSubmission
    )
    args["db"].session.query.return_value.filter_by.assert_called_once_with(id=42)
    assert offline_submission.status == "sent_to_formsflow"
    assert offline_submission.application_id == "application-55"
    args["db"].session.commit.assert_called_once_with()


def test_send_to_formsflow_submits_existing_draft(monkeypatch):
    args = _args(
        _submission_data(payload={"data": {"answer": "yes"}, "serverDraftId": "draft-7"})
    )
    offline_submission = SimpleNamespace(status="sent_to_formio", application_id=None)
    args["db"].session.query.return_value.filter_by.return_value.first.return_value = offline_submission
    token_response = _token_response()
    draft_response = MagicMock(status_code=200, text="submitted")
    draft_response.json.return_value = {"id": "application-55"}
    post = MagicMock(return_value=token_response)
    put = MagicMock(return_value=draft_response)
    monkeypatch.setattr(actions_formsflow.requests, "post", post)
    monkeypatch.setattr(actions_formsflow.requests, "put", put)

    result, out_args = actions_formsflow.send_to_formsflow(**args)

    assert result is True
    assert out_args == args
    put.assert_called_once_with(
        "https://formsflow.example.test/draft/draft-7/submit",
        json={
            "formId": "form-123",
            "submissionId": "formio-submission-17",
            "formUrl": "https://formio.example.test/form/form-123/submission/formio-submission-17",
            "webFormUrl": "https://forms.example.test/form/form-123/submission/42",
            "data": {"answer": "yes"},
            "createdBy": "officer@example.test",
        },
        headers={"Authorization": "Bearer keycloak-token"},
    )
    draft_response.raise_for_status.assert_called_once_with()
    args["db"].session.query.assert_called_once_with(
        actions_formsflow.FormsflowOfflineSubmission
    )
    args["db"].session.query.return_value.filter_by.assert_called_once_with(id=42)
    assert offline_submission.status == "sent_to_formsflow"
    assert offline_submission.application_id == "application-55"
    args["db"].session.commit.assert_called_once_with()


def test_send_to_formsflow_skips_application_creation_when_id_exists(monkeypatch):
    args = _args(_submission_data(application_id="existing-application"))
    post = MagicMock(return_value=_token_response())
    monkeypatch.setattr(actions_formsflow.requests, "post", post)

    result, out_args = actions_formsflow.send_to_formsflow(**args)

    assert result is True
    assert out_args == args
    post.assert_called_once()
    args["db"].session.query.assert_not_called()


@pytest.mark.parametrize(
    ("post_side_effect", "expected_details"),
    [
        (requests.RequestException("Keycloak unavailable"), "Keycloak unavailable"),
        (None, "Failed to obtain access token from Keycloak"),
    ],
)
def test_send_to_formsflow_returns_error_when_token_request_fails(
    monkeypatch, post_side_effect, expected_details
):
    args = _args(_submission_data())
    response = _token_response(access_token=None)
    post = MagicMock()
    if post_side_effect is not None:
        post.side_effect = post_side_effect
    else:
        post.return_value = response
    monkeypatch.setattr(actions_formsflow.requests, "post", post)

    result, out_args = actions_formsflow.send_to_formsflow(**args)

    assert result is False
    assert out_args["error"]["error_code"] is ErrorCode.O08
    assert out_args["error"]["error_details"] == expected_details
    assert out_args["error"]["submission_id"] == 42
    assert out_args["error"]["payload"] == '{"id": 42}'
    assert out_args["error"]["func"] is actions_formsflow.send_to_formsflow
    post.assert_called_once()


def test_send_to_formsflow_returns_error_when_application_creation_fails(monkeypatch):
    args = _args(_submission_data())
    create_response = MagicMock(status_code=500, text="server error")
    create_response.raise_for_status.side_effect = requests.HTTPError("create failed")
    post = MagicMock(side_effect=[_token_response(), create_response])
    monkeypatch.setattr(actions_formsflow.requests, "post", post)

    result, out_args = actions_formsflow.send_to_formsflow(**args)

    assert result is False
    assert out_args["error"]["error_code"] is ErrorCode.O08
    assert out_args["error"]["error_details"] == "create failed"
    args["db"].session.query.assert_not_called()


def test_send_to_formsflow_returns_error_when_draft_submission_fails(monkeypatch):
    args = _args(
        _submission_data(payload={"data": {"answer": "yes"}, "serverDraftId": "draft-7"})
    )
    draft_response = MagicMock(status_code=500, text="server error")
    draft_response.raise_for_status.side_effect = requests.HTTPError("draft failed")
    monkeypatch.setattr(actions_formsflow.requests, "post", MagicMock(return_value=_token_response()))
    monkeypatch.setattr(actions_formsflow.requests, "put", MagicMock(return_value=draft_response))

    result, out_args = actions_formsflow.send_to_formsflow(**args)

    assert result is False
    assert out_args["error"]["error_code"] is ErrorCode.O08
    assert out_args["error"]["error_details"] == "draft failed"
    args["db"].session.query.assert_not_called()