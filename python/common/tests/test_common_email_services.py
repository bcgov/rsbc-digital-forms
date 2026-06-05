from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

import python.common.common_email_services as ces


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_config(environment="DEV", bcc=None):
    cfg = MagicMock()
    cfg.ENVIRONMENT = environment
    cfg.REPLY_EMAIL_ADDRESS = "noreply@example.com"
    cfg.BCC_EMAIL_ADDRESSES = bcc
    cfg.COMM_SERV_AUTH_URL = "http://keycloak:8080/auth/"
    cfg.COMM_SERV_CLIENT_ID = "test-client"
    cfg.COMM_SERV_REALM = "master"
    cfg.COMM_SERV_CLIENT_SECRET = "secret"
    return cfg


def _make_response(status_code=201, json_data=None):
    resp = MagicMock()
    resp.status_code = status_code
    resp.json.return_value = json_data or {"messages": []}
    resp.text = "error text"
    return resp


# ---------------------------------------------------------------------------
# send_email — subject prefixing
# ---------------------------------------------------------------------------

class TestSendEmailSubjectPrefixing:
    def test_non_prod_subject_gets_env_prefix(self, monkeypatch):
        captured = {}

        def _fake_send(payload, config, ticket_no):
            captured["subject"] = payload["subject"]
            return True

        monkeypatch.setattr(ces, "_send", _fake_send)
        cfg = _make_config(environment="DEV")

        ces.send_email(["to@example.com"], "My Subject", cfg, "<html/>")

        assert captured["subject"].startswith("[DEV]")
        assert "My Subject" in captured["subject"]

    def test_prod_subject_is_not_prefixed(self, monkeypatch):
        captured = {}

        def _fake_send(payload, config, ticket_no):
            captured["subject"] = payload["subject"]
            return True

        monkeypatch.setattr(ces, "_send", _fake_send)
        cfg = _make_config(environment="PROD")

        ces.send_email(["to@example.com"], "My Subject", cfg, "<html/>")

        assert captured["subject"] == "My Subject"

    def test_staging_subject_gets_env_prefix(self, monkeypatch):
        captured = {}

        def _fake_send(payload, config, ticket_no):
            captured["subject"] = payload["subject"]
            return True

        monkeypatch.setattr(ces, "_send", _fake_send)
        cfg = _make_config(environment="STAGING")

        ces.send_email(["to@example.com"], "My Subject", cfg, "<html/>")

        assert "[STAGING]" in captured["subject"]


# ---------------------------------------------------------------------------
# send_email — payload construction
# ---------------------------------------------------------------------------

class TestSendEmailPayload:
    def test_payload_includes_to(self, monkeypatch):
        captured = {}

        def _fake_send(payload, config, ticket_no):
            captured["payload"] = payload
            return True

        monkeypatch.setattr(ces, "_send", _fake_send)
        cfg = _make_config()

        ces.send_email(["officer@example.com"], "Subject", cfg, "<html/>")

        assert captured["payload"]["to"] == ["officer@example.com"]

    def test_payload_includes_body(self, monkeypatch):
        captured = {}

        def _fake_send(payload, config, ticket_no):
            captured["payload"] = payload
            return True

        monkeypatch.setattr(ces, "_send", _fake_send)
        cfg = _make_config()

        ces.send_email(["to@example.com"], "Subject", cfg, "<html>body</html>")

        assert captured["payload"]["body"] == "<html>body</html>"
        assert captured["payload"]["bodyType"] == "html"

    def test_payload_includes_from_address(self, monkeypatch):
        captured = {}

        def _fake_send(payload, config, ticket_no):
            captured["payload"] = payload
            return True

        monkeypatch.setattr(ces, "_send", _fake_send)
        cfg = _make_config()

        ces.send_email(["to@example.com"], "Subject", cfg, "<html/>")

        assert captured["payload"]["from"] == cfg.REPLY_EMAIL_ADDRESS

    def test_payload_bcc_split_on_comma(self, monkeypatch):
        captured = {}

        def _fake_send(payload, config, ticket_no):
            captured["payload"] = payload
            return True

        monkeypatch.setattr(ces, "_send", _fake_send)
        cfg = _make_config(bcc="a@example.com,b@example.com")

        ces.send_email(["to@example.com"], "Subject", cfg, "<html/>")

        assert captured["payload"]["bcc"] == ["a@example.com", "b@example.com"]

    def test_payload_bcc_is_none_when_not_set(self, monkeypatch):
        captured = {}

        def _fake_send(payload, config, ticket_no):
            captured["payload"] = payload
            return True

        monkeypatch.setattr(ces, "_send", _fake_send)
        cfg = _make_config(bcc=None)

        ces.send_email(["to@example.com"], "Subject", cfg, "<html/>")

        assert captured["payload"]["bcc"] is None

    def test_payload_includes_attachments_when_provided(self, monkeypatch):
        captured = {}

        def _fake_send(payload, config, ticket_no):
            captured["payload"] = payload
            return True

        monkeypatch.setattr(ces, "_send", _fake_send)
        cfg = _make_config()
        attachments = [{"content": "base64", "filename": "doc.pdf"}]

        ces.send_email(["to@example.com"], "Subject", cfg, "<html/>", attachments=attachments)

        assert captured["payload"]["attachments"] == attachments

    def test_payload_excludes_attachments_key_when_none(self, monkeypatch):
        captured = {}

        def _fake_send(payload, config, ticket_no):
            captured["payload"] = payload
            return True

        monkeypatch.setattr(ces, "_send", _fake_send)
        cfg = _make_config()

        ces.send_email(["to@example.com"], "Subject", cfg, "<html/>", attachments=None)

        assert "attachments" not in captured["payload"]

    def test_returns_result_of_send(self, monkeypatch):
        monkeypatch.setattr(ces, "_send", lambda payload, config, ticket_no: True)
        cfg = _make_config()

        result = ces.send_email(["to@example.com"], "Subject", cfg, "<html/>")

        assert result is True


# ---------------------------------------------------------------------------
# _send
# ---------------------------------------------------------------------------

class TestInternalSend:
    def test_returns_true_on_201(self, monkeypatch):
        monkeypatch.setattr(ces, "get_common_services_access_token", lambda cfg: "token")
        monkeypatch.setattr(ces.requests, "post", MagicMock(return_value=_make_response(201)))
        monkeypatch.setattr(ces, "_log_sent_email_response", MagicMock())
        cfg = _make_config()

        result = ces._send({"subject": "s", "to": ["x@example.com"]}, cfg, "ticket-1")

        assert result is True

    def test_returns_false_on_non_201(self, monkeypatch):
        monkeypatch.setattr(ces, "get_common_services_access_token", lambda cfg: "token")
        monkeypatch.setattr(ces.requests, "post", MagicMock(return_value=_make_response(500)))
        cfg = _make_config()

        result = ces._send({"subject": "s", "to": ["x@example.com"]}, cfg, "ticket-1")

        assert result is False

    def test_returns_false_on_assertion_error(self, monkeypatch):
        monkeypatch.setattr(ces, "get_common_services_access_token", lambda cfg: "token")
        monkeypatch.setattr(ces.requests, "post", MagicMock(side_effect=AssertionError("no response")))
        cfg = _make_config()

        result = ces._send({"subject": "s"}, cfg, "ticket-1")

        assert result is False

    def test_calls_log_on_success(self, monkeypatch):
        monkeypatch.setattr(ces, "get_common_services_access_token", lambda cfg: "token")
        monkeypatch.setattr(ces.requests, "post", MagicMock(return_value=_make_response(201, {"id": "abc"})))
        mock_log = MagicMock()
        monkeypatch.setattr(ces, "_log_sent_email_response", mock_log)
        cfg = _make_config()

        ces._send({"subject": "s", "to": ["x@example.com"]}, cfg, "ticket-1")

        mock_log.assert_called_once()

    def test_does_not_call_log_on_failure(self, monkeypatch):
        monkeypatch.setattr(ces, "get_common_services_access_token", lambda cfg: "token")
        monkeypatch.setattr(ces.requests, "post", MagicMock(return_value=_make_response(400)))
        mock_log = MagicMock()
        monkeypatch.setattr(ces, "_log_sent_email_response", mock_log)
        cfg = _make_config()

        ces._send({"subject": "s"}, cfg, "ticket-1")

        mock_log.assert_not_called()

    def test_sends_bearer_token_in_header(self, monkeypatch):
        monkeypatch.setattr(ces, "get_common_services_access_token", lambda cfg: "my-token")
        mock_post = MagicMock(return_value=_make_response(201))
        monkeypatch.setattr(ces.requests, "post", mock_post)
        monkeypatch.setattr(ces, "_log_sent_email_response", MagicMock())
        cfg = _make_config()

        ces._send({"subject": "s"}, cfg, None)

        _, kwargs = mock_post.call_args
        assert kwargs["headers"]["Authorization"] == "Bearer my-token"

    def test_posts_to_email_endpoint(self, monkeypatch):
        monkeypatch.setattr(ces, "get_common_services_access_token", lambda cfg: "token")
        mock_post = MagicMock(return_value=_make_response(201))
        monkeypatch.setattr(ces.requests, "post", mock_post)
        monkeypatch.setattr(ces, "_log_sent_email_response", MagicMock())
        cfg = _make_config()

        ces._send({"subject": "s"}, cfg, None)

        url = mock_post.call_args[0][0]
        assert url.endswith("/api/v1/email")


# ---------------------------------------------------------------------------
# get_common_services_access_token
# ---------------------------------------------------------------------------

class TestGetCommonServicesAccessToken:
    def test_returns_access_token_from_keycloak(self, monkeypatch):
        mock_keycloak = MagicMock()
        mock_keycloak.token.return_value = {"access_token": "the-token"}
        monkeypatch.setattr(ces, "KeycloakOpenID", lambda **kw: mock_keycloak)
        cfg = _make_config()

        token = ces.get_common_services_access_token(cfg)

        assert token == "the-token"

    def test_uses_client_credentials_grant(self, monkeypatch):
        mock_keycloak = MagicMock()
        mock_keycloak.token.return_value = {"access_token": "tok"}
        monkeypatch.setattr(ces, "KeycloakOpenID", lambda **kw: mock_keycloak)
        cfg = _make_config()

        ces.get_common_services_access_token(cfg)

        mock_keycloak.token.assert_called_once_with("", "", "client_credentials")

    def test_initializes_keycloak_with_config_values(self, monkeypatch):
        captured = {}

        def _fake_keycloak(**kwargs):
            captured.update(kwargs)
            mock = MagicMock()
            mock.token.return_value = {"access_token": "tok"}
            return mock

        monkeypatch.setattr(ces, "KeycloakOpenID", _fake_keycloak)
        cfg = _make_config()

        ces.get_common_services_access_token(cfg)

        assert captured["server_url"] == cfg.COMM_SERV_AUTH_URL
        assert captured["client_id"] == cfg.COMM_SERV_CLIENT_ID
        assert captured["realm_name"] == cfg.COMM_SERV_REALM
        assert captured["client_secret_key"] == cfg.COMM_SERV_CLIENT_SECRET


# ---------------------------------------------------------------------------
# _log_sent_email_response
# ---------------------------------------------------------------------------

class TestLogSentEmailResponse:
    def test_calls_splunk_log(self, monkeypatch):
        mock_splunk = MagicMock()
        monkeypatch.setattr(ces.splunk, "log_to_splunk", mock_splunk)
        cfg = _make_config()

        ces._log_sent_email_response(
            "ticket-1",
            {"to": ["to@example.com"], "bcc": None, "subject": "Test"},
            {"messages": []},
            cfg
        )

        mock_splunk.assert_called_once()

    def test_splunk_payload_contains_email_sent_event(self, monkeypatch):
        captured = {}

        def _fake_splunk(**kwargs):
            captured.update(kwargs)

        monkeypatch.setattr(ces.splunk, "log_to_splunk", _fake_splunk)
        cfg = _make_config()
        payload = {"to": ["to@example.com"], "bcc": None, "subject": "Test"}

        ces._log_sent_email_response("ticket-1", payload, {}, cfg)

        data = captured["splunk_data"]
        assert data["event"] == "email sent success"

    def test_splunk_payload_includes_ticket_no(self, monkeypatch):
        captured = {}

        def _fake_splunk(**kwargs):
            captured.update(kwargs)

        monkeypatch.setattr(ces.splunk, "log_to_splunk", _fake_splunk)
        cfg = _make_config()
        payload = {"to": ["to@example.com"], "bcc": None, "subject": "Test"}

        ces._log_sent_email_response("ticket-42", payload, {}, cfg)

        data = captured["splunk_data"]
        assert data["ticket_no"] == "ticket-42"

    def test_splunk_payload_includes_to_and_subject(self, monkeypatch):
        captured = {}

        def _fake_splunk(**kwargs):
            captured.update(kwargs)

        monkeypatch.setattr(ces.splunk, "log_to_splunk", _fake_splunk)
        cfg = _make_config()
        payload = {"to": ["to@example.com"], "bcc": None, "subject": "My Subject"}

        ces._log_sent_email_response("t-1", payload, {}, cfg)

        data = captured["splunk_data"]
        assert data["to"] == ["to@example.com"]
        assert data["subject"] == "My Subject"

    def test_config_passed_to_splunk(self, monkeypatch):
        captured = {}

        def _fake_splunk(**kwargs):
            captured.update(kwargs)

        monkeypatch.setattr(ces.splunk, "log_to_splunk", _fake_splunk)
        cfg = _make_config()

        ces._log_sent_email_response("t-1", {"to": [], "bcc": None, "subject": "s"}, {}, cfg)

        assert captured["config"] is cfg
