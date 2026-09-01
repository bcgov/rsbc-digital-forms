import json
from datetime import datetime
from unittest.mock import MagicMock, patch

import pytest
from flask import Flask

from python.prohibition_web_svc.middleware import user_middleware


@pytest.fixture
def mock_db():
    return MagicMock()


@pytest.fixture
def mock_request():
    request = MagicMock()
    return request


@pytest.fixture
def app():
    """Create and configure a test Flask app."""
    app = Flask(__name__)
    app.config['TESTING'] = True
    return app


@pytest.fixture
def app_context(app):
    """Create an app context for testing."""
    with app.app_context():
        yield app


class DummyAgency:
    def __init__(self, agency_name="Vancouver"):
        self.agency_name = agency_name


class DummyUser:
    def __init__(self, user_guid, username, display_name, login, badge_number, agency_id):
        self.user_guid = user_guid
        self.username = username
        self.display_name = display_name
        self.login = login
        self.badge_number = badge_number
        self.agency_id = agency_id
        self.first_name = "John"
        self.last_name = "Doe"
        self.business_guid = None
        self.last_active = None
        self.agency_ref = DummyAgency()

    @staticmethod
    def serialize(user):
        if user is None:
            return None
        return {
            "user_guid": user.user_guid,
            "username": user.username,
            "display_name": user.display_name,
            "login": user.login,
            "badge_number": user.badge_number,
            "agency": user.agency_ref.agency_name if user.agency_ref else None,
        }


class TestUserHasNotAppliedPreviously:
    def test_user_has_not_applied_success(self, monkeypatch):
        mock_db = MagicMock()
        mock_db.session.query().filter().count.return_value = 0
        monkeypatch.setattr(user_middleware, "db", mock_db)

        kwargs = {"user_guid": "user-123"}
        result, out_kwargs = user_middleware.user_has_not_applied_previously(**kwargs)

        assert result is True
        assert out_kwargs["user_guid"] == "user-123"

    def test_user_has_already_applied(self, monkeypatch):
        mock_db = MagicMock()
        mock_db.session.query().filter().count.return_value = 1
        monkeypatch.setattr(user_middleware, "db", mock_db)

        kwargs = {"user_guid": "user-123"}
        result, out_kwargs = user_middleware.user_has_not_applied_previously(**kwargs)

        assert result is False
        assert out_kwargs["user_guid"] == "user-123"

    def test_user_check_exception_handling(self, monkeypatch):
        mock_db = MagicMock()
        mock_db.session.query.side_effect = Exception("db error")
        monkeypatch.setattr(user_middleware, "db", mock_db)

        kwargs = {"user_guid": "user-123"}
        result, out_kwargs = user_middleware.user_has_not_applied_previously(**kwargs)

        assert result is False


class TestUpdateTheUser:
    def test_update_user_success(self, monkeypatch):
        mock_db = MagicMock()
        user = DummyUser(
            user_guid="user-123",
            username="jdoe",
            display_name="John Doe",
            login="jdoe@idir",
            badge_number="AB1234",
            agency_id=1,
        )
        mock_db.session.query().filter().first.return_value = user
        monkeypatch.setattr(user_middleware, "db", mock_db)

        kwargs = {
            "user_guid": "user-123",
            "username": "newuser",
            "display_name": "New User",
            "login": "newuser@idir",
            "payload": {
                "badge_number": "CD5678",
                "agency": {"id": 2},
                "first_name": "New",
                "last_name": "User",
            },
        }
        result, out_kwargs = user_middleware.update_the_user(**kwargs)

        assert result is True
        mock_db.session.commit.assert_called_once()
        assert user.username == "newuser"
        assert user.badge_number == "CD5678"

    def test_update_user_exception_handling(self, monkeypatch):
        mock_db = MagicMock()
        mock_db.session.query.side_effect = Exception("db error")
        monkeypatch.setattr(user_middleware, "db", mock_db)

        kwargs = {"user_guid": "user-123"}
        result, out_kwargs = user_middleware.update_the_user(**kwargs)

        assert result is False


class TestCreateAUser:
    def test_create_user_success(self, monkeypatch):
        mock_db = MagicMock()
        monkeypatch.setattr(user_middleware, "db", mock_db)

        kwargs = {
            "username": "newuser",
            "user_guid": "user-456",
            "business_guid": "biz-123",
            "display_name": "New User",
            "login": "newuser@idir",
            "payload": {
                "badge_number": "EF9012",
                "agency": {"id": 3},
                "first_name": "New",
                "last_name": "User",
            },
        }
        result, out_kwargs = user_middleware.create_a_user(**kwargs)

        assert result is True
        mock_db.session.add.assert_called_once()
        mock_db.session.commit.assert_called_once()

    def test_create_user_exception_handling(self, monkeypatch):
        mock_db = MagicMock()
        mock_db.session.add.side_effect = Exception("db error")
        monkeypatch.setattr(user_middleware, "db", mock_db)

        kwargs = {
            "username": "newuser",
            "user_guid": "user-456",
            "display_name": "New User",
            "login": "newuser@idir",
            "payload": {
                "badge_number": "EF9012",
                "agency": {"id": 3},
                "first_name": "New",
                "last_name": "User",
            },
        }
        result, out_kwargs = user_middleware.create_a_user(**kwargs)

        assert result is False


class TestRequestContainsAPayload:
    def test_request_with_json_payload(self, mock_request):
        payload = {
            "badge_number": "AB1234",
            "agency": {"id": 1},
            "first_name": "John",
            "last_name": "Doe",
        }
        mock_request.get_json.return_value = payload

        kwargs = {"request": mock_request}
        result, out_kwargs = user_middleware.request_contains_a_payload(**kwargs)

        assert result is True
        assert out_kwargs["payload"] == payload

    def test_request_with_no_payload(self, mock_request):
        mock_request.get_json.return_value = None

        kwargs = {"request": mock_request}
        result, out_kwargs = user_middleware.request_contains_a_payload(**kwargs)

        assert result is False

    def test_request_payload_exception_handling(self, mock_request):
        mock_request.get_json.side_effect = Exception("request error")

        kwargs = {"request": mock_request}
        result, out_kwargs = user_middleware.request_contains_a_payload(**kwargs)

        assert result is False


class TestGetUser:
    def test_get_user_success(self, monkeypatch, app_context):
        mock_db = MagicMock()
        user = DummyUser(
            user_guid="user-123",
            username="jdoe",
            display_name="John Doe",
            login="jdoe@idir",
            badge_number="AB1234",
            agency_id=1,
        )
        mock_db.session.query().filter().first.return_value = user
        monkeypatch.setattr(user_middleware, "db", mock_db)

        kwargs = {"user_guid": "user-123"}
        result, out_kwargs = user_middleware.get_user(**kwargs)

        assert result is True
        assert "response" in out_kwargs
        # response is a Flask Response object from make_response(jsonify(...), 200)
        response = out_kwargs["response"]
        assert response.status_code == 200

    def test_get_user_exception_handling(self, monkeypatch):
        mock_db = MagicMock()
        mock_db.session.query.side_effect = Exception("db error")
        monkeypatch.setattr(user_middleware, "db", mock_db)

        kwargs = {"user_guid": "user-123"}
        result, out_kwargs = user_middleware.get_user(**kwargs)

        assert result is False


class TestValidateCreateUserPayload:
    def test_valid_payload(self):
        payload = {
            "badge_number": "AB1234",
            "agency": {"id": 1},
            "first_name": "John",
            "last_name": "Doe",
        }
        kwargs = {"payload": payload}
        result, out_kwargs = user_middleware.validate_create_user_payload(**kwargs)

        assert result is True

    def test_valid_payload_6_digit_badge(self):
        payload = {
            "badge_number": "123456",
            "agency": {"id": 1},
            "first_name": "Jane",
            "last_name": "Smith",
        }
        kwargs = {"payload": payload}
        result, out_kwargs = user_middleware.validate_create_user_payload(**kwargs)

        assert result is True

    def test_missing_required_field_badge_number(self):
        payload = {
            "agency": {"id": 1},
            "first_name": "John",
            "last_name": "Doe",
        }
        kwargs = {"payload": payload}
        result, out_kwargs = user_middleware.validate_create_user_payload(**kwargs)

        assert result is False
        assert "validation_errors" in out_kwargs

    def test_invalid_badge_number_format(self):
        payload = {
            "badge_number": "invalid",
            "agency": {"id": 1},
            "first_name": "John",
            "last_name": "Doe",
        }
        kwargs = {"payload": payload}
        result, out_kwargs = user_middleware.validate_create_user_payload(**kwargs)

        assert result is False
        assert "validation_errors" in out_kwargs

    def test_badge_number_partial_letters(self):
        payload = {
            "badge_number": "A12345",
            "agency": {"id": 1},
            "first_name": "John",
            "last_name": "Doe",
        }
        kwargs = {"payload": payload}
        result, out_kwargs = user_middleware.validate_create_user_payload(**kwargs)

        assert result is False
        assert "validation_errors" in out_kwargs

    def test_string_too_short_first_name(self):
        payload = {
            "badge_number": "AB1234",
            "agency": {"id": 1},
            "first_name": "J",
            "last_name": "Doe",
        }
        kwargs = {"payload": payload}
        result, out_kwargs = user_middleware.validate_create_user_payload(**kwargs)

        assert result is False
        assert "validation_errors" in out_kwargs

    def test_string_too_long_last_name(self):
        payload = {
            "badge_number": "AB1234",
            "agency": {"id": 1},
            "first_name": "John",
            "last_name": "D" * 31,  # 31 chars, max is 30
        }
        kwargs = {"payload": payload}
        result, out_kwargs = user_middleware.validate_create_user_payload(**kwargs)

        assert result is False
        assert "validation_errors" in out_kwargs

    def test_missing_agency_field(self):
        payload = {
            "badge_number": "AB1234",
            "first_name": "John",
            "last_name": "Doe",
        }
        kwargs = {"payload": payload}
        result, out_kwargs = user_middleware.validate_create_user_payload(**kwargs)

        assert result is False
        assert "validation_errors" in out_kwargs

    def test_unknown_fields_not_allowed(self):
        payload = {
            "badge_number": "AB1234",
            "agency": {"id": 1},
            "first_name": "John",
            "last_name": "Doe",
            "unknown_field": "should fail",
        }
        kwargs = {"payload": payload}
        result, out_kwargs = user_middleware.validate_create_user_payload(**kwargs)

        assert result is False
        assert "validation_errors" in out_kwargs


class TestValidateUpdateLastActiveRequest:
    def test_valid_user_guid_provided(self):
        kwargs = {"user_guid": "user-456"}
        result, out_kwargs = user_middleware.validate_update_last_active_request(**kwargs)

        assert result is True

    def test_empty_user_guid_returns_false(self):
        kwargs = {"user_guid": ""}
        result, out_kwargs = user_middleware.validate_update_last_active_request(**kwargs)

        assert result is False
        assert out_kwargs["response"][0]["error"] == "user_guid is required"

    def test_missing_user_guid_returns_false(self):
        kwargs = {}
        result, out_kwargs = user_middleware.validate_update_last_active_request(**kwargs)

        assert result is False
        assert out_kwargs["response"][0]["error"] == "user_guid is required"


class TestUpdateUserLastActive:
    def test_update_last_active_success(self, monkeypatch, app_context):
        mock_user = MagicMock()
        mock_user.last_active = None
        mock_db = MagicMock()
        mock_db.session.commit.return_value = None

        mock_query = MagicMock()
        mock_query.get.return_value = mock_user

        monkeypatch.setattr(user_middleware, "db", mock_db)
        monkeypatch.setattr("python.prohibition_web_svc.middleware.user_middleware.User.query", mock_query)

        kwargs = {"user_guid": "user-789"}
        result, out_kwargs = user_middleware.update_user_last_active(**kwargs)

        assert result is True
        assert out_kwargs["response"][0]["message"] == "Last active time updated successfully"
        assert mock_user.last_active is not None

    def test_user_not_found(self, monkeypatch, app_context):
        mock_db = MagicMock()
        mock_query = MagicMock()
        mock_query.get.return_value = None

        monkeypatch.setattr(user_middleware, "db", mock_db)
        monkeypatch.setattr("python.prohibition_web_svc.middleware.user_middleware.User.query", mock_query)

        kwargs = {"user_guid": "nonexistent"}
        result, out_kwargs = user_middleware.update_user_last_active(**kwargs)

        assert result is False
        assert out_kwargs["response"][0]["error"] == "User not found"

    def test_update_last_active_exception_handling(self, monkeypatch, app_context):
        mock_user = MagicMock()
        mock_db = MagicMock()
        mock_db.session.commit.side_effect = Exception("db error")

        mock_query = MagicMock()
        mock_query.get.return_value = mock_user

        monkeypatch.setattr(user_middleware, "db", mock_db)
        monkeypatch.setattr("python.prohibition_web_svc.middleware.user_middleware.User.query", mock_query)

        kwargs = {"user_guid": "user-789"}
        result, out_kwargs = user_middleware.update_user_last_active(**kwargs)

        assert result is False
        assert "error" in out_kwargs["response"][0]
