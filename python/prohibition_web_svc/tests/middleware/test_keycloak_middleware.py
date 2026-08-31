from types import SimpleNamespace

import pytest

from python.prohibition_web_svc.middleware import keycloak_middleware


class DummyRequest:
    def __init__(self, authorization_header=None):
        self.headers = {}
        if authorization_header is not None:
            self.headers["Authorization"] = authorization_header


def test_get_authorization_header_from_request_success():
    request = DummyRequest("Bearer test-token")

    result, kwargs = keycloak_middleware.get_authorization_header_from_request(request=request)

    assert result is True
    assert kwargs["auth_header"] == ["Bearer", "test-token"]


def test_get_authorization_header_from_request_missing_header():
    request = DummyRequest()

    result, kwargs = keycloak_middleware.get_authorization_header_from_request(request=request)

    assert result is False
    assert "auth_header" not in kwargs


def test_get_token_from_authorization_header_success():
    result, kwargs = keycloak_middleware.get_token_from_authorization_header(auth_header=["Bearer", "abc123"])

    assert result is True
    assert kwargs["access_token"] == "abc123"


def test_get_token_from_authorization_header_invalid_scheme():
    result, kwargs = keycloak_middleware.get_token_from_authorization_header(auth_header=["Basic", "abc123"])

    assert result is False
    assert kwargs["access_token"] == "abc123"


def test_get_token_from_authorization_header_missing_value():
    result, kwargs = keycloak_middleware.get_token_from_authorization_header(auth_header=["Bearer"])

    assert result is False
    assert "access_token" not in kwargs


def test_get_keycloak_certificates_success(monkeypatch):
    mock_signing_key = SimpleNamespace(key="secret-key")
    mock_client = SimpleNamespace()
    mock_client.get_signing_key_from_jwt = lambda token: mock_signing_key
    monkeypatch.setattr(keycloak_middleware, "jwks_client", mock_client)

    result, kwargs = keycloak_middleware.get_keycloak_certificates(access_token="abc123")

    assert result is True
    assert kwargs["signing_key"] == "secret-key"


def test_get_keycloak_certificates_failure(monkeypatch):
    class BrokenClient:
        def get_signing_key_from_jwt(self, token):
            raise RuntimeError("bad jwks")

    monkeypatch.setattr(keycloak_middleware, "jwks_client", BrokenClient())

    result, kwargs = keycloak_middleware.get_keycloak_certificates(access_token="abc123")

    assert result is False
    assert "error" in kwargs
    assert "bad jwks" in kwargs["error"]


def test_decode_keycloak_access_token_success(monkeypatch):
    decoded = {"preferred_username": "user@example.com"}
    monkeypatch.setattr(keycloak_middleware.jwt, "decode", lambda *args, **kwargs: decoded)

    result, kwargs = keycloak_middleware.decode_keycloak_access_token(
        access_token="abc123",
        signing_key="secret-key",
    )

    assert result is True
    assert kwargs["decoded_access_token"] == decoded


def test_decode_keycloak_access_token_failure(monkeypatch):
    def boom(*args, **kwargs):
        raise ValueError("invalid token")

    monkeypatch.setattr(keycloak_middleware.jwt, "decode", boom)

    result, kwargs = keycloak_middleware.decode_keycloak_access_token(
        access_token="bad-token",
        signing_key="secret-key",
    )

    assert result is False
    assert "decoded_access_token" not in kwargs


def test_get_username_from_decoded_access_token_bceid():
    token = {
        "preferred_username": "bceid-user",
        "display_name": "BCeID User",
        "identity_provider": "bceid",
        "bceid_user_guid": "guid-123",
        "bceid_username": "bceid-user",
    }

    result, kwargs = keycloak_middleware.get_username_from_decoded_access_token(decoded_access_token=token)

    assert result is True
    assert kwargs["username"] == "bceid-user"
    assert kwargs["display_name"] == "BCeID User"
    assert kwargs["identity_provider"] == "bceid"
    assert kwargs["login"] == "bceid-user@bceid"


def test_get_username_from_decoded_access_token_idir():
    token = {
        "preferred_username": "idir-user",
        "display_name": "IDIR User",
        "identity_provider": "idir",
        "idir_user_guid": "guid-456",
        "idir_username": "idir-user",
    }

    result, kwargs = keycloak_middleware.get_username_from_decoded_access_token(decoded_access_token=token)

    assert result is True
    assert kwargs["username"] == "idir-user"
    assert kwargs["identity_provider"] == "idir"
    assert kwargs["login"] == "idir-user@idir"


def test_get_username_from_decoded_access_token_service_account():
    token = {
        "preferred_username": "svc-account",
        "display_name": "Service Account",
        "identity_provider": "service_account",
    }

    result, kwargs = keycloak_middleware.get_username_from_decoded_access_token(decoded_access_token=token)

    assert result is True
    assert kwargs["identity_provider"] == "service_account"
    assert kwargs["login"].endswith("@service_account")


def test_get_username_from_decoded_access_token_missing_required_claims():
    token = {"display_name": "No username"}

    result, kwargs = keycloak_middleware.get_username_from_decoded_access_token(decoded_access_token=token)

    assert result is False
    assert "error" in kwargs
    assert "preferred_username or login not present" in kwargs["error"]


def test_get_user_guid_from_decoded_access_token_bceid():
    token = {
        "bceid_user_guid": "guid-123",
        "bceid_business_guid": "business-456",
    }

    result, kwargs = keycloak_middleware.get_user_guid_from_decoded_access_token(decoded_access_token=token)

    assert result is True
    assert kwargs["business_guid"] == "business-456"
    assert kwargs["user_guid"] == "guid-123"


def test_get_user_guid_from_decoded_access_token_idir():
    token = {"idir_user_guid": "guid-789"}

    result, kwargs = keycloak_middleware.get_user_guid_from_decoded_access_token(decoded_access_token=token)

    assert result is True
    assert kwargs["user_guid"] == "guid-789"


def test_get_user_guid_from_decoded_access_token_service_account():
    token = {"preferred_username": "svc-account", "identity_provider": "service_account"}

    result, kwargs = keycloak_middleware.get_user_guid_from_decoded_access_token(decoded_access_token=token)

    assert result is True
    assert kwargs["user_guid"] == "svc-account"


def test_get_user_guid_from_decoded_access_token_fallback_username():
    token = {"preferred_username": "github-user"}
    kwargs = {"username": "github-user"}

    result, out_kwargs = keycloak_middleware.get_user_guid_from_decoded_access_token(decoded_access_token=token, **kwargs)

    assert result is True
    assert out_kwargs["user_guid"] == "github-user"


def test_get_user_guid_from_decoded_access_token_no_guid():
    token = {"identity_provider": "github"}

    result, kwargs = keycloak_middleware.get_user_guid_from_decoded_access_token(decoded_access_token=token)

    assert result is False
    assert kwargs["user_guid"] is None


def test_get_user_roles_from_decoded_access_token_success():
    token = {"role": ["user", "admin"]}

    result, kwargs = keycloak_middleware.get_user_roles_from_decoded_access_token(decoded_access_token=token)

    assert result is True
    assert kwargs["user_roles"] == ["user", "admin"]


def test_get_user_roles_from_decoded_access_token_missing_role():
    token = {"preferred_username": "user"}

    result, kwargs = keycloak_middleware.get_user_roles_from_decoded_access_token(decoded_access_token=token)

    assert result is False
    assert "user_roles" not in kwargs


def test_check_user_is_authorized_success():
    result, kwargs = keycloak_middleware.check_user_is_authorized(
        username="user1",
        required_permission="view_submissions",
        user_roles=["realm:rsbc_user", "realm:view_submissions"],
    )

    assert result is True
    assert kwargs["username"] == "user1"


def test_check_user_is_authorized_requires_any_permission_from_csv():
    result, kwargs = keycloak_middleware.check_user_is_authorized(
        username="user1",
        required_permission="read,write",
        user_roles=["realm:reader"],
    )

    assert result is True
    assert kwargs["username"] == "user1"


def test_check_user_is_authorized_denied():
    result, kwargs = keycloak_middleware.check_user_is_authorized(
        username="user1",
        required_permission="admin",
        user_roles=["realm:user"],
    )

    assert result is False
    assert kwargs["username"] == "user1"
    assert kwargs["required_permission"] == "admin"
