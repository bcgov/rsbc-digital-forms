import json
from datetime import datetime
from unittest.mock import MagicMock, patch

import pytest
from flask import Flask

from python.prohibition_web_svc.middleware import admin_user_middleware


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
        monkeypatch.setattr(admin_user_middleware, "db", mock_db)

        kwargs = {"payload": {"user_guid": "user-123"}}
        result, out_kwargs = admin_user_middleware.user_has_not_applied_previously(**kwargs)

        assert result is True
        assert out_kwargs["payload"]["user_guid"] == "user-123"

    def test_user_has_already_applied(self, monkeypatch):
        mock_db = MagicMock()
        mock_db.session.query().filter().count.return_value = 1
        monkeypatch.setattr(admin_user_middleware, "db", mock_db)

        kwargs = {"payload": {"user_guid": "user-123"}}
        result, out_kwargs = admin_user_middleware.user_has_not_applied_previously(**kwargs)

        assert result is False
        assert out_kwargs["payload"]["user_guid"] == "user-123"

    def test_user_check_exception_handling(self, monkeypatch):
        mock_db = MagicMock()
        mock_db.session.query.side_effect = Exception("db error")
        monkeypatch.setattr(admin_user_middleware, "db", mock_db)

        kwargs = {"payload": {"user_guid": "user-123"}}
        result, out_kwargs = admin_user_middleware.user_has_not_applied_previously(**kwargs)

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
        monkeypatch.setattr(admin_user_middleware, "db", mock_db)

        kwargs = {
            "payload": {
                "user_guid": "user-123",
                "username": "newuser",
                "display_name": "New User",
                "login": "newuser@idir",
                "badge_number": "CD5678",
                "agency": {"id": 2},
                "first_name": "New",
                "last_name": "User",
            }
        }
        result, out_kwargs = admin_user_middleware.update_the_user(**kwargs)

        assert result is True
        mock_db.session.commit.assert_called_once()
        assert user.username == "newuser"
        assert user.badge_number == "CD5678"

    def test_update_user_exception_handling(self, monkeypatch):
        mock_db = MagicMock()
        mock_db.session.query.side_effect = Exception("db error")
        monkeypatch.setattr(admin_user_middleware, "db", mock_db)

        kwargs = {"payload": {"user_guid": "user-123"}}
        result, out_kwargs = admin_user_middleware.update_the_user(**kwargs)

        assert result is False


class TestAdminCreateAUser:
    def test_create_user_success(self, monkeypatch):
        mock_db = MagicMock()
        monkeypatch.setattr(admin_user_middleware, "db", mock_db)

        kwargs = {
            "payload": {
                "user_guid": "user-456",
                "username": "newuser",
                "display_name": "New User",
                "login": "newuser@idir",
                "badge_number": "EF9012",
                "agency": {"id": 3},
                "first_name": "New",
                "last_name": "User",
                "business_guid": "biz-123",
            }
        }
        result, out_kwargs = admin_user_middleware.admin_create_a_user(**kwargs)

        assert result is True
        mock_db.session.add.assert_called_once()
        mock_db.session.commit.assert_called_once()

    def test_create_user_exception_handling(self, monkeypatch):
        mock_db = MagicMock()
        mock_db.session.add.side_effect = Exception("db error")
        monkeypatch.setattr(admin_user_middleware, "db", mock_db)

        kwargs = {
            "payload": {
                "user_guid": "user-456",
                "username": "newuser",
                "display_name": "New User",
                "login": "newuser@idir",
                "badge_number": "EF9012",
                "agency": {"id": 3},
                "first_name": "New",
                "last_name": "User",
            }
        }
        result, out_kwargs = admin_user_middleware.admin_create_a_user(**kwargs)

        assert result is False


class TestRequestContainsAPayload:
    def test_request_with_json_payload(self, mock_request):
        payload = {
            "user_guid": "user-789",
            "username": "user",
            "agency": {"id": 1, "name": "Vancouver"},
        }
        mock_request.get_json.return_value = payload

        kwargs = {"request": mock_request}
        result, out_kwargs = admin_user_middleware.request_contains_a_payload(**kwargs)

        assert result is True
        assert out_kwargs["payload"] == payload

    def test_request_with_agency_as_json_string(self, mock_request):
        payload = {
            "user_guid": "user-789",
            "username": "user",
            "agency": '{"id": 1, "name": "Vancouver"}',
        }
        mock_request.get_json.return_value = payload

        kwargs = {"request": mock_request}
        result, out_kwargs = admin_user_middleware.request_contains_a_payload(**kwargs)

        assert result is True
        assert out_kwargs["payload"]["agency"] == {"id": 1, "name": "Vancouver"}

    def test_request_with_invalid_agency_json_string(self, mock_request):
        payload = {
            "user_guid": "user-789",
            "username": "user",
            "agency": "not-valid-json",
        }
        mock_request.get_json.return_value = payload

        kwargs = {"request": mock_request}
        result, out_kwargs = admin_user_middleware.request_contains_a_payload(**kwargs)

        assert result is True
        assert out_kwargs["payload"]["agency"] == "not-valid-json"

    def test_request_with_no_payload(self, mock_request):
        mock_request.get_json.return_value = None

        kwargs = {"request": mock_request}
        result, out_kwargs = admin_user_middleware.request_contains_a_payload(**kwargs)

        assert result is False

    def test_request_payload_exception_handling(self, mock_request):
        mock_request.get_json.side_effect = Exception("request error")

        kwargs = {"request": mock_request}
        result, out_kwargs = admin_user_middleware.request_contains_a_payload(**kwargs)

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
        monkeypatch.setattr(admin_user_middleware, "db", mock_db)

        kwargs = {"payload": {"user_guid": "user-123"}}
        result, out_kwargs = admin_user_middleware.get_user(**kwargs)

        assert result is True
        assert "response" in out_kwargs
        # response is a Flask Response object from make_response(jsonify(...), 200)
        response = out_kwargs["response"]
        assert response.status_code == 200

    def test_get_user_exception_handling(self, monkeypatch):
        mock_db = MagicMock()
        mock_db.session.query.side_effect = Exception("db error")
        monkeypatch.setattr(admin_user_middleware, "db", mock_db)

        kwargs = {"payload": {"user_guid": "user-123"}}
        result, out_kwargs = admin_user_middleware.get_user(**kwargs)

        assert result is False


class TestValidateUpdateLastActiveRequest:
    def test_valid_user_guid_provided(self):
        kwargs = {"payload": {"user_guid": "user-456"}}
        result, out_kwargs = admin_user_middleware.validate_update_last_active_request(**kwargs)

        assert result is True

    def test_missing_user_guid_raises_key_error(self):
        """The actual function raises KeyError when user_guid is missing."""
        kwargs = {"payload": {}}
        with pytest.raises(KeyError):
            admin_user_middleware.validate_update_last_active_request(**kwargs)

    def test_empty_user_guid_returns_false(self):
        """When user_guid is empty string, returns False."""
        kwargs = {"payload": {"user_guid": ""}}
        result, out_kwargs = admin_user_middleware.validate_update_last_active_request(**kwargs)

        assert result is False
        assert out_kwargs["response"][0]["error"] == "user_guid is required"


class TestUpdateUserLastActive:
    def test_update_last_active_success(self, monkeypatch, app_context):
        mock_user = MagicMock()
        mock_user.last_active = None
        mock_db = MagicMock()
        mock_db.session.commit.return_value = None
        
        # Mock User.query.get to return the mock_user
        mock_query = MagicMock()
        mock_query.get.return_value = mock_user
        
        monkeypatch.setattr(admin_user_middleware, "db", mock_db)
        monkeypatch.setattr("python.prohibition_web_svc.middleware.admin_user_middleware.User.query", mock_query)

        kwargs = {"payload": {"user_guid": "user-789"}}
        result, out_kwargs = admin_user_middleware.update_user_last_active(**kwargs)

        assert result is True
        assert out_kwargs["response"][0]["message"] == "Last active time updated successfully"
        assert mock_user.last_active is not None

    def test_user_not_found(self, monkeypatch, app_context):
        mock_db = MagicMock()
        mock_query = MagicMock()
        mock_query.get.return_value = None
        
        monkeypatch.setattr(admin_user_middleware, "db", mock_db)
        monkeypatch.setattr("python.prohibition_web_svc.middleware.admin_user_middleware.User.query", mock_query)

        kwargs = {"payload": {"user_guid": "nonexistent"}}
        result, out_kwargs = admin_user_middleware.update_user_last_active(**kwargs)

        assert result is False
        assert out_kwargs["response"][0]["error"] == "User not found"

    def test_update_last_active_exception_handling(self, monkeypatch, app_context):
        mock_user = MagicMock()
        mock_db = MagicMock()
        mock_db.session.commit.side_effect = Exception("db error")
        
        mock_query = MagicMock()
        mock_query.get.return_value = mock_user
        
        monkeypatch.setattr(admin_user_middleware, "db", mock_db)
        monkeypatch.setattr("python.prohibition_web_svc.middleware.admin_user_middleware.User.query", mock_query)

        kwargs = {"payload": {"user_guid": "user-789"}}
        result, out_kwargs = admin_user_middleware.update_user_last_active(**kwargs)

        assert result is False
        assert "error" in out_kwargs["response"][0]


class TestValidateAdminCreateUserPayload:
    def test_valid_payload(self):
        payload = {
            "user_guid": "user-123",
            "username": "jdoe",
            "agency": {"id": 1},
            "badge_number": "AB1234",
            "first_name": "John",
            "last_name": "Doe",
            "login": "jdoe@idir",
            "display_name": "John Doe",
        }
        kwargs = {"payload": payload}
        result, out_kwargs = admin_user_middleware.validate_admin_create_user_payload(**kwargs)

        assert result is True

    def test_valid_payload_with_business_guid(self):
        payload = {
            "user_guid": "user-123",
            "username": "jdoe",
            "agency": {"id": 1},
            "badge_number": "AB1234",
            "first_name": "John",
            "last_name": "Doe",
            "login": "jdoe@idir",
            "display_name": "John Doe",
            "business_guid": "biz-456",
        }
        kwargs = {"payload": payload}
        result, out_kwargs = admin_user_middleware.validate_admin_create_user_payload(**kwargs)

        assert result is True

    def test_missing_required_field_user_guid(self):
        payload = {
            "username": "jdoe",
            "agency": {"id": 1},
            "badge_number": "AB1234",
            "first_name": "John",
            "last_name": "Doe",
            "login": "jdoe@idir",
        }
        kwargs = {"payload": payload}
        result, out_kwargs = admin_user_middleware.validate_admin_create_user_payload(**kwargs)

        assert result is False
        assert "validation_errors" in out_kwargs

    def test_invalid_badge_number_format(self):
        payload = {
            "user_guid": "user-123",
            "username": "jdoe",
            "agency": {"id": 1},
            "badge_number": "invalid",
            "first_name": "John",
            "last_name": "Doe",
            "login": "jdoe@idir",
        }
        kwargs = {"payload": payload}
        result, out_kwargs = admin_user_middleware.validate_admin_create_user_payload(**kwargs)

        assert result is False
        assert "validation_errors" in out_kwargs

    def test_valid_badge_number_6_digits(self):
        payload = {
            "user_guid": "user-123",
            "username": "jdoe",
            "agency": {"id": 1},
            "badge_number": "123456",
            "first_name": "John",
            "last_name": "Doe",
            "login": "jdoe@idir",
        }
        kwargs = {"payload": payload}
        result, out_kwargs = admin_user_middleware.validate_admin_create_user_payload(**kwargs)

        assert result is True

    def test_string_too_short(self):
        payload = {
            "user_guid": "a",
            "username": "j",
            "agency": {"id": 1},
            "badge_number": "AB1234",
            "first_name": "J",
            "last_name": "D",
            "login": "j",
        }
        kwargs = {"payload": payload}
        result, out_kwargs = admin_user_middleware.validate_admin_create_user_payload(**kwargs)

        assert result is False
        assert "validation_errors" in out_kwargs

    def test_missing_agency_field(self):
        payload = {
            "user_guid": "user-123",
            "username": "jdoe",
            "badge_number": "AB1234",
            "first_name": "John",
            "last_name": "Doe",
            "login": "jdoe@idir",
        }
        kwargs = {"payload": payload}
        result, out_kwargs = admin_user_middleware.validate_admin_create_user_payload(**kwargs)

        assert result is False
        assert "validation_errors" in out_kwargs

    def test_unknown_fields_not_allowed(self):
        payload = {
            "user_guid": "user-123",
            "username": "jdoe",
            "agency": {"id": 1},
            "badge_number": "AB1234",
            "first_name": "John",
            "last_name": "Doe",
            "login": "jdoe@idir",
            "unknown_field": "should fail",
        }
        kwargs = {"payload": payload}
        result, out_kwargs = admin_user_middleware.validate_admin_create_user_payload(**kwargs)

        assert result is False
        assert "validation_errors" in out_kwargs
