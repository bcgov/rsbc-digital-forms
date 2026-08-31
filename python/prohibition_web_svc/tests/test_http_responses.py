import json

import pytest
from flask import Flask

from python.prohibition_web_svc import http_responses


@pytest.fixture
def flask_app():
    app = Flask(__name__)
    with app.app_context():
        yield app


def invoke_response_helper(app, func, **kwargs):
    with app.app_context():
        return func(**kwargs)


@pytest.mark.parametrize(
    "func, expected_status",
    [
        (http_responses.successful_create_response, 201),
        (http_responses.successful_update_response, 200),
        (http_responses.not_changed_response, 304),
        (http_responses.server_error_response, 500),
        (http_responses.record_not_found, 400),
        (http_responses.unauthorized, 401),
        (http_responses.unable_to_retrieve_keycloak_certificates, 500),
        (http_responses.keycloak_token_not_valid, 401),
        (http_responses.keycloak_no_username, 500),
        (http_responses.no_user_guid, 500),
        (http_responses.no_user_roles, 500),
        (http_responses.user_already_exists, 400),
        (http_responses.payload_missing, 403),
        (http_responses.no_payload, 400),
        (http_responses.not_found_response, 404),
        (http_responses.officer_not_found, 404),
        (http_responses.detachment_not_found, 400),
        (http_responses.duplicate_detachment_request, 400),
        (http_responses.forbidden_detachment, 403),
        (http_responses.detachment_conflict, 409),
    ],
)
def test_response_helpers_return_expected_status(flask_app, func, expected_status):
    ok, kwargs = invoke_response_helper(flask_app, func, response_dict={"message": "ok"})

    assert ok is True
    assert kwargs["response"].status_code == expected_status


def test_successful_create_response_uses_payload_and_status(flask_app):
    ok, kwargs = invoke_response_helper(flask_app, http_responses.successful_create_response, response_dict={"id": 7})

    assert ok is True
    assert kwargs["response"].status_code == 201
    assert json.loads(kwargs["response"].get_data(as_text=True)) == {"id": 7}


def test_bad_request_response_includes_error_details(flask_app):
    ok, kwargs = invoke_response_helper(flask_app, http_responses.bad_request_response, response_dict={"error_details": "missing field"})

    assert ok is True
    assert kwargs["response"].status_code == 400
    assert json.loads(kwargs["response"].get_data(as_text=True)) == {
        "error": "bad request",
        "error_details": "missing field",
    }


def test_bad_request_response_without_details_has_none_detail(flask_app):
    ok, kwargs = invoke_response_helper(flask_app, http_responses.bad_request_response, response_dict={})

    assert ok is True
    assert kwargs["response"].status_code == 400
    assert json.loads(kwargs["response"].get_data(as_text=True))["error_details"] is None


def test_application_already_exists_response_status_409(flask_app):
    ok, kwargs = invoke_response_helper(flask_app, http_responses.application_already_exists, payload={"ff_application_id": "abc-123"})

    assert ok is True
    assert kwargs["response"].status_code == 409
    assert json.loads(kwargs["response"].get_data(as_text=True))["error"] == "application already exists"


def test_form_number_already_exists_response_uses_error_details(flask_app):
    ok, kwargs = invoke_response_helper(flask_app, http_responses.form_number_already_exists, error={"error_details": "duplicate form number"})

    assert ok is True
    assert kwargs["response"].status_code == 409
    assert json.loads(kwargs["response"].get_data(as_text=True)) == {"error": "duplicate form number"}


def test_role_already_exists_non_service_account_uses_400(flask_app):
    ok, kwargs = invoke_response_helper(flask_app, http_responses.role_already_exists, username="user1", identity_provider="idir")

    assert ok is True
    assert kwargs["response"].status_code == 400
    assert json.loads(kwargs["response"].get_data(as_text=True))["error"] == "role already exists"


def test_role_already_exists_service_account_uses_409(flask_app):
    ok, kwargs = invoke_response_helper(flask_app, http_responses.role_already_exists, payload={"username": "service-user"}, identity_provider="service_account")

    assert ok is True
    assert kwargs["response"].status_code == 409
    assert json.loads(kwargs["response"].get_data(as_text=True))["error"] == "role already exists"


def test_failed_validation_response(flask_app):
    ok, kwargs = invoke_response_helper(flask_app, http_responses.failed_validation, validation_errors=["field missing", "bad format"])

    assert ok is True
    assert kwargs["response"].status_code == 400
    assert json.loads(kwargs["response"].get_data(as_text=True)) == {
        "message": "failed validation",
        "errors": ["field missing", "bad format"],
    }


def test_successful_get_response_returns_response_wrapper(flask_app):
    ok, kwargs = invoke_response_helper(flask_app, http_responses.successful_get_response, response_dict={"items": [1, 2]})

    assert ok is True
    assert kwargs["response"].status_code == 200
    assert kwargs["response"].get_json() == {"items": [1, 2]}
