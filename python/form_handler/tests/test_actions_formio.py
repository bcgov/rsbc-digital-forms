import logging
from types import SimpleNamespace
from unittest.mock import MagicMock, call

import requests
import pytest

from python.common.enums import ErrorCode
from python.form_handler import actions_formio


@pytest.fixture(autouse=True)
def configure_verbose_logging(monkeypatch):
    monkeypatch.setattr(logging, "verbose", MagicMock(), raising=False)


def _config():
    return SimpleNamespace(
        FORMIO_API_URL="https://formio.example.test",
        FORMIO_TOKEN_HEADER="x-jwt-token",
        FORMIO_ROOT_EMAIL="root@example.test",
        FORMIO_ROOT_PASSWORD="root-password",
    )


def _app_context_mock():
    app = MagicMock()
    app.app_context.return_value.__enter__ = MagicMock(return_value=None)
    app.app_context.return_value.__exit__ = MagicMock(return_value=False)
    return app


def test_send_to_formio_creates_submission_and_persists_id(monkeypatch):
    app = _app_context_mock()
    db = MagicMock()
    offline_submission = SimpleNamespace(status="processing", submission_id=None)
    db.session.query.return_value.filter_by.return_value.first.return_value = offline_submission
    login_response = MagicMock()
    login_response.headers.get.return_value = "formio-token"
    submission_response = MagicMock()
    submission_response.json.return_value = {"_id": "formio-submission-123"}
    post = MagicMock(side_effect=[login_response, submission_response])
    monkeypatch.setattr(actions_formio.requests, "post", post)
    submission_data = {
        "form_id": "form-123",
        "submission_id": None,
        "payload": {
            "data": {"firstName": "Ada"},
            "metadata": {"source": "offline"},
            "state": "submitted",
            "_vnote": "saved locally",
        },
    }
    message = {"id": 42}

    result, out_args = actions_formio.send_to_formio(
        app=app,
        db=db,
        config=_config(),
        message=message,
        submission_data=submission_data,
        offline_submission_id=42,
    )

    assert result is True
    assert out_args["formio_submission_id"] == "formio-submission-123"
    assert post.call_args_list == [
        call(
            "https://formio.example.test/user/login",
            json={"data": {"email": "root@example.test", "password": "root-password"}},
        ),
        call(
            "https://formio.example.test/form/form-123/submission",
            json={
                "data": {"firstName": "Ada", "submitted_offline": True},
                "metadata": {"source": "offline"},
                "state": "submitted",
                "_vnote": "saved locally",
            },
            headers={"x-jwt-token": "formio-token"},
        ),
    ]
    submission_response.raise_for_status.assert_called_once_with()
    db.session.query.assert_called_once_with(actions_formio.FormsflowOfflineSubmission)
    db.session.query.return_value.filter_by.assert_called_once_with(id=42)
    assert offline_submission.status == "sent_to_formio"
    assert offline_submission.submission_id == "formio-submission-123"
    db.session.commit.assert_called_once_with()


def test_send_to_formio_skips_existing_formio_submission(monkeypatch):
    post = MagicMock()
    monkeypatch.setattr(actions_formio.requests, "post", post)
    args = {
        "config": _config(),
        "submission_data": {
            "form_id": "form-123",
            "submission_id": "already-created",
            "payload": {"data": {"firstName": "Ada"}},
        },
    }

    result, out_args = actions_formio.send_to_formio(**args)

    assert result is True
    assert out_args["formio_submission_id"] == "already-created"
    post.assert_not_called()


def test_send_to_formio_returns_error_when_login_request_fails(monkeypatch):
    post = MagicMock(side_effect=requests.RequestException("Form.io unavailable"))
    monkeypatch.setattr(actions_formio.requests, "post", post)
    message = {"id": 42}

    result, out_args = actions_formio.send_to_formio(
        app=_app_context_mock(),
        db=MagicMock(),
        config=_config(),
        message=message,
        submission_data={
            "form_id": "form-123",
            "submission_id": None,
            "payload": {"data": {"firstName": "Ada"}},
        },
        offline_submission_id=42,
    )

    assert result is False
    assert out_args["error"] == {
        "error_code": ErrorCode.O07,
        "error_details": "Form.io unavailable",
        "event_id": None,
        "event_type": "offline_submission",
        "submission_id": 42,
        "payload": '{"id": 42}',
        "func": actions_formio.send_to_formio,
    }
    post.assert_called_once_with(
        "https://formio.example.test/user/login",
        json={"data": {"email": "root@example.test", "password": "root-password"}},
    )