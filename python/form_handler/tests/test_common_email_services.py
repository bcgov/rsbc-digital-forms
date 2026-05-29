"""
Unit tests for python.form_handler.common_email_services
"""
from __future__ import annotations

import json
from unittest.mock import MagicMock, patch, call

import pytest

from python.form_handler.common_email_services import (
    send_email,
    _send,
    get_common_services_access_token,
    _log_sent_email_response,
)


# ---------------------------------------------------------------------------
# Shared fixtures / helpers
# ---------------------------------------------------------------------------

def _make_config(
    bcc="",
    environment="DEV",
    reply_from="noreply@example.com",
    comm_serv_api_root="https://api.example.com",
    comm_serv_auth_url="https://auth.example.com/",
    comm_serv_client_id="client-id",
    comm_serv_realm="myrealm",
    comm_serv_client_secret="secret",
    minio_cert_file="/etc/ssl/certs/ca.crt",
):
    cfg = MagicMock()
    cfg.BCC_EMAIL_ADDRESSES = bcc
    cfg.ENVIRONMENT = environment
    cfg.REPLY_EMAIL_ADDRESS = reply_from
    cfg.COMM_SERV_API_ROOT_URL = comm_serv_api_root
    cfg.COMM_SERV_AUTH_URL = comm_serv_auth_url
    cfg.COMM_SERV_CLIENT_ID = comm_serv_client_id
    cfg.COMM_SERV_REALM = comm_serv_realm
    cfg.COMM_SERV_CLIENT_SECRET = comm_serv_client_secret
    cfg.MINIO_CERT_FILE = minio_cert_file
    return cfg


# ---------------------------------------------------------------------------
# _log_sent_email_response
# ---------------------------------------------------------------------------

class TestLogSentEmailResponse:
    def test_logs_success_info(self):
        payload = {"to": ["a@b.com"], "subject": "Hello", "bcc": ["c@d.com"]}
        response = {"msgId": "abc123"}
        with patch("python.form_handler.common_email_services.logging") as mock_log:
            _log_sent_email_response("evt-1", payload, response)
        mock_log.info.assert_called_once()
        logged = json.loads(mock_log.info.call_args[0][0])
        assert logged["email"] == "success"
        assert logged["eventid"] == "evt-1"
        assert logged["to"] == ["a@b.com"]
        assert logged["bcc"] == ["c@d.com"]
        assert logged["subject"] == "Hello"
        assert logged["response"] == {"msgId": "abc123"}

    def test_returns_none(self):
        with patch("python.form_handler.common_email_services.logging"):
            result = _log_sent_email_response("evt-2", {"to": [], "subject": ""}, {})
        assert result is None

    def test_missing_bcc_key_defaults_to_none(self):
        payload = {"to": ["a@b.com"], "subject": "Hi"}  # no 'bcc' key
        with patch("python.form_handler.common_email_services.logging") as mock_log:
            _log_sent_email_response("", payload, {})
        logged = json.loads(mock_log.info.call_args[0][0])
        assert logged["bcc"] is None

    def test_empty_eventid(self):
        with patch("python.form_handler.common_email_services.logging") as mock_log:
            _log_sent_email_response("", {"to": [], "subject": ""}, {})
        logged = json.loads(mock_log.info.call_args[0][0])
        assert logged["eventid"] == ""


# ---------------------------------------------------------------------------
# get_common_services_access_token
# ---------------------------------------------------------------------------

class TestGetCommonServicesAccessToken:
    def test_returns_access_token(self):
        cfg = _make_config()
        mock_keycloak = MagicMock()
        mock_keycloak.token.return_value = {"access_token": "tok-abc"}
        with patch(
            "python.form_handler.common_email_services.KeycloakOpenID",
            return_value=mock_keycloak,
        ) as mock_cls:
            token = get_common_services_access_token(cfg)
        assert token == "tok-abc"

    def test_keycloak_constructed_with_config_values(self):
        cfg = _make_config(
            comm_serv_auth_url="https://auth.example.com/",
            comm_serv_client_id="my-client",
            comm_serv_realm="myrealm",
            comm_serv_client_secret="s3cr3t",
        )
        mock_keycloak = MagicMock()
        mock_keycloak.token.return_value = {"access_token": "tok"}
        with patch(
            "python.form_handler.common_email_services.KeycloakOpenID",
            return_value=mock_keycloak,
        ) as mock_cls:
            get_common_services_access_token(cfg)
        mock_cls.assert_called_once_with(
            server_url="https://auth.example.com/",
            client_id="my-client",
            realm_name="myrealm",
            client_secret_key="s3cr3t",
            verify=False,
        )

    def test_token_called_with_client_credentials(self):
        cfg = _make_config()
        mock_keycloak = MagicMock()
        mock_keycloak.token.return_value = {"access_token": "t"}
        with patch(
            "python.form_handler.common_email_services.KeycloakOpenID",
            return_value=mock_keycloak,
        ):
            get_common_services_access_token(cfg)
        mock_keycloak.token.assert_called_once_with("", "", "client_credentials")

    def test_ssl_cert_file_reset_to_minio_cert(self):
        import os
        cfg = _make_config(minio_cert_file="/my/cert.crt")
        mock_keycloak = MagicMock()
        mock_keycloak.token.return_value = {"access_token": "t"}
        with patch(
            "python.form_handler.common_email_services.KeycloakOpenID",
            return_value=mock_keycloak,
        ):
            get_common_services_access_token(cfg)
        assert os.environ.get("SSL_CERT_FILE") == "/my/cert.crt"


# ---------------------------------------------------------------------------
# _send
# ---------------------------------------------------------------------------

class TestSend:
    def _mock_response(self, status_code=201, json_data=None):
        resp = MagicMock()
        resp.status_code = status_code
        resp.json.return_value = json_data or {"msgId": "x"}
        resp.text = "error text"
        return resp

    def _patches(self, token="tok", post_return=None, post_side_effect=None,
                 api_root="https://api.example.com", log_fn=None):
        """Return a list of context-manager patches shared across _send tests."""
        post_mock = MagicMock(return_value=post_return or self._mock_response(201))
        if post_side_effect:
            post_mock.side_effect = post_side_effect
        patches = [
            patch(
                "python.form_handler.common_email_services.get_common_services_access_token",
                return_value=token,
            ),
            patch("python.form_handler.common_email_services.requests.post", post_mock),
            patch("python.form_handler.common_email_services.logging"),  # hides logging.verbose
            patch("python.form_handler.common_email_services.Config"),
        ]
        if log_fn is not None:
            patches.append(
                patch(
                    "python.form_handler.common_email_services._log_sent_email_response",
                    log_fn,
                )
            )
        return patches, post_mock

    def _apply(self, patches):
        """Enter all patches and set Config.COMM_SERV_API_ROOT_URL."""
        from contextlib import ExitStack
        stack = ExitStack()
        mocks = [stack.enter_context(p) for p in patches]
        # The Config patch is always the 4th entry (index 3)
        mocks[3].COMM_SERV_API_ROOT_URL = "https://api.example.com"
        return stack, mocks

    def test_returns_true_on_201(self):
        cfg = _make_config()
        patches, _ = self._patches(post_return=self._mock_response(201))
        with self._apply(patches)[0]:
            result = _send({"to": ["a@b.com"]}, cfg, "evt-1")
        assert result is True

    def test_returns_false_on_non_201(self):
        cfg = _make_config()
        patches, _ = self._patches(post_return=self._mock_response(500))
        with self._apply(patches)[0]:
            result = _send({"to": ["a@b.com"]}, cfg, "evt-1")
        assert result is False

    def test_returns_false_on_assertion_error(self):
        cfg = _make_config()
        patches, _ = self._patches(post_side_effect=AssertionError("no connection"))
        # Also patch json to avoid json.dumps(AssertionError) failing in the except block
        patches.append(patch("python.form_handler.common_email_services.json"))
        with self._apply(patches)[0]:
            result = _send({"to": ["a@b.com"]}, cfg)
        assert result is False

    def test_uses_bearer_token_in_header(self):
        cfg = _make_config()
        patches, post_mock = self._patches(token="my-token")
        with self._apply(patches)[0]:
            _send({}, cfg)
        _, kwargs = post_mock.call_args
        assert kwargs["headers"] == {"Authorization": "Bearer my-token"}

    def test_posts_to_correct_url(self):
        cfg = _make_config()
        patches, post_mock = self._patches()
        with self._apply(patches)[0]:
            _send({}, cfg)
        args, _ = post_mock.call_args
        assert args[0] == "https://api.example.com/api/v1/email"

    def test_calls_log_sent_email_response_on_success(self):
        cfg = _make_config()
        payload = {"to": ["a@b.com"], "subject": "Hi"}
        response_data = {"msgId": "abc"}
        mock_log_fn = MagicMock()
        patches, _ = self._patches(
            post_return=self._mock_response(201, response_data),
            log_fn=mock_log_fn,
        )
        with self._apply(patches)[0]:
            _send(payload, cfg, "evt-99")
        mock_log_fn.assert_called_once_with("evt-99", payload, response_data)

    def test_default_eventid_is_empty_string(self):
        cfg = _make_config()
        mock_log_fn = MagicMock()
        patches, _ = self._patches(log_fn=mock_log_fn)
        with self._apply(patches)[0]:
            _send({}, cfg)
        mock_log_fn.assert_called_once_with("", {}, mock_log_fn.call_args[0][2])


# ---------------------------------------------------------------------------
# send_email
# ---------------------------------------------------------------------------

class TestSendEmail:
    def _run(self, config, to=None, subject="Test", template="<p>body</p>",
             eventid="evt-1", attachments=None, mock_send_return=True):
        to = to or ["user@example.com"]
        with patch(
            "python.form_handler.common_email_services._send",
            return_value=mock_send_return,
        ) as mock_send:
            result = send_email(to, subject, config, template, eventid, attachments)
        return result, mock_send

    # --- subject prefix ---

    def test_subject_prefixed_with_env_when_not_prod(self):
        cfg = _make_config(environment="DEV")
        _, mock_send = self._run(cfg, subject="My Subject")
        payload = mock_send.call_args[0][0]
        assert payload["subject"] == "[DEV] - My Subject"

    def test_subject_prefixed_uppercase_env(self):
        cfg = _make_config(environment="staging")
        _, mock_send = self._run(cfg, subject="Alert")
        payload = mock_send.call_args[0][0]
        assert payload["subject"] == "[STAGING] - Alert"

    def test_subject_not_prefixed_when_prod(self):
        cfg = _make_config(environment="PROD")
        _, mock_send = self._run(cfg, subject="Production Notice")
        payload = mock_send.call_args[0][0]
        assert payload["subject"] == "Production Notice"

    def test_subject_not_prefixed_when_env_contains_prod(self):
        cfg = _make_config(environment="PRODUCTION")
        _, mock_send = self._run(cfg, subject="Notice")
        payload = mock_send.call_args[0][0]
        assert payload["subject"] == "Notice"

    # --- BCC handling ---

    def test_bcc_included_in_payload_when_set(self):
        cfg = _make_config(bcc="bcc1@x.com,bcc2@x.com")
        _, mock_send = self._run(cfg)
        payload = mock_send.call_args[0][0]
        assert payload["bcc"] == ["bcc1@x.com", "bcc2@x.com"]

    def test_bcc_not_in_payload_when_empty(self):
        cfg = _make_config(bcc="")
        _, mock_send = self._run(cfg)
        payload = mock_send.call_args[0][0]
        assert "bcc" not in payload

    def test_bcc_not_in_payload_when_none(self):
        cfg = _make_config(bcc=None)
        cfg.BCC_EMAIL_ADDRESSES = None
        _, mock_send = self._run(cfg)
        payload = mock_send.call_args[0][0]
        assert "bcc" not in payload

    def test_single_bcc_address(self):
        cfg = _make_config(bcc="solo@x.com")
        _, mock_send = self._run(cfg)
        payload = mock_send.call_args[0][0]
        assert payload["bcc"] == ["solo@x.com"]

    # --- payload shape ---

    def test_payload_contains_body_and_from(self):
        cfg = _make_config(reply_from="from@example.com")
        _, mock_send = self._run(cfg, template="<b>hello</b>")
        payload = mock_send.call_args[0][0]
        assert payload["bodyType"] == "html"
        assert payload["body"] == "<b>hello</b>"
        assert payload["from"] == "from@example.com"
        assert payload["encoding"] == "utf-8"

    def test_payload_contains_to(self):
        cfg = _make_config()
        _, mock_send = self._run(cfg, to=["a@b.com", "c@d.com"])
        payload = mock_send.call_args[0][0]
        assert payload["to"] == ["a@b.com", "c@d.com"]

    # --- attachments ---

    def test_attachments_added_to_payload_when_provided(self):
        cfg = _make_config()
        attachments = [{"content": "base64data", "filename": "file.pdf"}]
        _, mock_send = self._run(cfg, attachments=attachments)
        payload = mock_send.call_args[0][0]
        assert payload["attachments"] == attachments

    def test_attachments_not_in_payload_when_none(self):
        cfg = _make_config()
        _, mock_send = self._run(cfg, attachments=None)
        payload = mock_send.call_args[0][0]
        assert "attachments" not in payload

    # --- delegation to _send ---

    def test_returns_true_when_send_succeeds(self):
        cfg = _make_config()
        result, _ = self._run(cfg, mock_send_return=True)
        assert result is True

    def test_returns_false_when_send_fails(self):
        cfg = _make_config()
        result, _ = self._run(cfg, mock_send_return=False)
        assert result is False

    def test_passes_eventid_to_send(self):
        cfg = _make_config()
        _, mock_send = self._run(cfg, eventid="my-event-42")
        assert mock_send.call_args[0][2] == "my-event-42"

    def test_passes_config_to_send(self):
        cfg = _make_config()
        _, mock_send = self._run(cfg)
        assert mock_send.call_args[0][1] is cfg
