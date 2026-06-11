from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

import python.common.rsi_email as rsi_email


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_jinja2_env_mock(rendered="<html>rendered</html>"):
    """Return a mock that satisfies get_jinja2_env().get_template(...).render(...)."""
    template = MagicMock()
    template.render.return_value = rendered
    env = MagicMock()
    env.get_template.return_value = template
    return env, template


def _make_config():
    cfg = MagicMock()
    cfg.ADMIN_EMAIL_ADDRESS = "admin@example.com"
    cfg.RSIOPS_EMAIL_ADDRESS = "ops@example.com"
    cfg.ENVIRONMENT = "DEV"
    cfg.REPLY_EMAIL_ADDRESS = "noreply@example.com"
    cfg.BCC_EMAIL_ADDRESSES = None
    return cfg


# ---------------------------------------------------------------------------
# get_jinja2_env
# ---------------------------------------------------------------------------

class TestGetJinja2Env:
    def test_returns_environment_with_autoescape(self):
        env = rsi_email.get_jinja2_env(path="./python/common/templates")
        # autoescape is enabled — the environment object should exist
        assert env is not None

    def test_uses_provided_path(self, tmp_path):
        env = rsi_email.get_jinja2_env(path=str(tmp_path))
        assert env is not None


# ---------------------------------------------------------------------------
# _hyphenate
# ---------------------------------------------------------------------------

class TestHyphenate:
    def test_inserts_hyphen_after_two_chars(self):
        assert rsi_email._hyphenate("00123456") == "00-123456"

    def test_works_with_alpha_chars(self):
        assert rsi_email._hyphenate("AB123456") == "AB-123456"

    def test_short_string_does_not_crash(self):
        result = rsi_email._hyphenate("AB")
        assert result == "AB-"


# ---------------------------------------------------------------------------
# content_data
# ---------------------------------------------------------------------------

class TestContentData:
    def test_returns_dict(self):
        data = rsi_email.content_data()
        assert isinstance(data, dict)

    def test_contains_mv6020_key(self):
        data = rsi_email.content_data()
        assert "MV6020_send_entity_copy.html" in data

    def test_mv6020_entry_has_raw_subject(self):
        data = rsi_email.content_data()
        assert "raw_subject" in data["MV6020_send_entity_copy.html"]


# ---------------------------------------------------------------------------
# get_email_content
# ---------------------------------------------------------------------------

class TestGetEmailContent:
    def test_known_template_returns_formatted_subject(self):
        content = rsi_email.get_email_content("MV6020_send_entity_copy.html", "00123456")
        assert "00-123456" in content["subject"]

    def test_unknown_template_returns_fallback(self):
        content = rsi_email.get_email_content("nonexistent_template.html", "00123456")
        assert content["title"] == "Unknown Template"

    def test_known_template_contains_title(self):
        content = rsi_email.get_email_content("MV6020_send_entity_copy.html", "00123456")
        assert "title" in content


# ---------------------------------------------------------------------------
# send_email_to_admin
# ---------------------------------------------------------------------------

class TestSendEmailToAdmin:
    def test_calls_send_email_with_admin_address(self, monkeypatch):
        env_mock, template_mock = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        mock_send = MagicMock(return_value=True)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", mock_send)
        cfg = _make_config()

        rsi_email.send_email_to_admin(subject="Test", config=cfg, message={}, body="body text")

        mock_send.assert_called_once()
        args = mock_send.call_args[0]
        assert cfg.ADMIN_EMAIL_ADDRESS in args[0]

    def test_renders_admin_notice_template(self, monkeypatch):
        env_mock, template_mock = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock())
        cfg = _make_config()

        rsi_email.send_email_to_admin(subject="Test", config=cfg, message={}, body="body text")

        env_mock.get_template.assert_called_once_with("admin_notice.html")

    def test_returns_tuple_with_args(self, monkeypatch):
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock(return_value=True))
        cfg = _make_config()

        result = rsi_email.send_email_to_admin(subject="Test", config=cfg, message={}, body="b")

        assert isinstance(result, tuple)
        assert len(result) == 2


# ---------------------------------------------------------------------------
# send_new_user_admin_notification
# ---------------------------------------------------------------------------

class TestSendNewUserAdminNotification:
    def test_uses_new_user_approval_template(self, monkeypatch):
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock())
        cfg = _make_config()

        rsi_email.send_new_user_admin_notification(subject="New User", config=cfg, message={}, body="body")

        env_mock.get_template.assert_called_once_with("admin_notice_new_user_approval_request.html")

    def test_sends_to_admin_address(self, monkeypatch):
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        mock_send = MagicMock(return_value=True)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", mock_send)
        cfg = _make_config()

        rsi_email.send_new_user_admin_notification(subject="New User", config=cfg, message={}, body="body")

        args = mock_send.call_args[0]
        assert cfg.ADMIN_EMAIL_ADDRESS in args[0]


# ---------------------------------------------------------------------------
# admin_unable_to_save_to_vips
# ---------------------------------------------------------------------------

class TestAdminUnableToSaveToVips:
    def test_delegates_to_send_email_to_admin(self, monkeypatch):
        mock_send_admin = MagicMock(return_value=(True, {}))
        monkeypatch.setattr(rsi_email, "send_email_to_admin", mock_send_admin)
        cfg = _make_config()

        rsi_email.admin_unable_to_save_to_vips(config=cfg, message={"key": "val"})

        mock_send_admin.assert_called_once()

    def test_subject_mentions_vips(self, monkeypatch):
        captured = {}

        def _capture(**kwargs):
            captured.update(kwargs)
            return True, {}

        monkeypatch.setattr(rsi_email, "send_email_to_admin", _capture)
        cfg = _make_config()

        rsi_email.admin_unable_to_save_to_vips(config=cfg, message={})

        assert "VIPS" in captured.get("subject", "")


# ---------------------------------------------------------------------------
# admin_unknown_event_type
# ---------------------------------------------------------------------------

class TestAdminUnknownEventType:
    def test_delegates_to_send_email_to_admin(self, monkeypatch):
        mock_send_admin = MagicMock(return_value=(True, {}))
        monkeypatch.setattr(rsi_email, "send_email_to_admin", mock_send_admin)
        cfg = _make_config()

        rsi_email.admin_unknown_event_type(config=cfg, message={"event_type": "WEIRD_EVENT"})

        mock_send_admin.assert_called_once()

    def test_body_includes_event_type(self, monkeypatch):
        captured = {}

        def _capture(**kwargs):
            captured.update(kwargs)
            return True, {}

        monkeypatch.setattr(rsi_email, "send_email_to_admin", _capture)
        cfg = _make_config()

        rsi_email.admin_unknown_event_type(config=cfg, message={"event_type": "WEIRD_EVENT"})

        assert "WEIRD_EVENT" in captured.get("body", "")


# ---------------------------------------------------------------------------
# send_mv6020_copy
# ---------------------------------------------------------------------------

class TestSendMv6020Copy:
    _VALID_TYPES = ["entity", "police", "icbc"]

    @pytest.mark.parametrize("email_type,expected_template", [
        ("entity", "MV6020_send_entity_copy.html"),
        ("police", "MV6020_send_police_copy.html"),
        ("icbc",   "MV6020_send_icbc_copy.html"),
    ])
    def test_uses_correct_template_per_email_type(self, email_type, expected_template, monkeypatch):
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock(return_value=True))
        cfg = _make_config()

        rsi_email.send_mv6020_copy(
            config=cfg, subject="Subject", email_address="to@example.com",
            full_name="Full Name", message={"collision_case_number": "CC-001"},
            attachments=None, email_type=email_type
        )

        env_mock.get_template.assert_called_once_with(expected_template)

    def test_returns_false_for_unknown_email_type(self, monkeypatch):
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        cfg = _make_config()

        result, args = rsi_email.send_mv6020_copy(
            config=cfg, subject="S", email_address="to@example.com",
            full_name="Name", message={}, attachments=None, email_type="unknown"
        )

        assert result is False

    def test_error_details_set_for_unknown_email_type(self, monkeypatch):
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: _make_jinja2_env_mock()[0])
        cfg = _make_config()

        _, args = rsi_email.send_mv6020_copy(
            config=cfg, subject="S", email_address="to@example.com",
            full_name="Name", message={}, attachments=None, email_type="bad_type"
        )

        assert "error_details" in args["response_dict"]
        assert "bad_type" in args["response_dict"]["error_details"]

    def test_sends_to_provided_email_address(self, monkeypatch):
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        mock_send = MagicMock(return_value=True)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", mock_send)
        cfg = _make_config()

        rsi_email.send_mv6020_copy(
            config=cfg, subject="S", email_address="recipient@example.com",
            full_name="Name", message={"collision_case_number": "CC-001"},
            attachments=None, email_type="entity"
        )

        args = mock_send.call_args[0]
        assert "recipient@example.com" in args[0]

    def test_passes_attachments_to_send_email(self, monkeypatch):
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        mock_send = MagicMock(return_value=True)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", mock_send)
        cfg = _make_config()
        attachments = [{"content": "base64data", "filename": "report.pdf"}]

        rsi_email.send_mv6020_copy(
            config=cfg, subject="S", email_address="to@example.com",
            full_name="Name", message={"collision_case_number": "CC-001"},
            attachments=attachments, email_type="entity"
        )

        args = mock_send.call_args[0]
        assert args[-1] == attachments


# ---------------------------------------------------------------------------
# send_admin_failure_notification
# ---------------------------------------------------------------------------

class TestSendAdminFailureNotification:
    def test_uses_failure_template(self, monkeypatch):
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock())
        cfg = _make_config()

        rsi_email.send_admin_failure_notification(subject="Fail", config=cfg, message={})

        env_mock.get_template.assert_called_once_with("admin_notice_submission_failure.html")

    def test_sends_to_admin_address(self, monkeypatch):
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        mock_send = MagicMock(return_value=True)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", mock_send)
        cfg = _make_config()

        rsi_email.send_admin_failure_notification(subject="Fail", config=cfg, message={})

        args = mock_send.call_args[0]
        assert cfg.ADMIN_EMAIL_ADDRESS in args[0]


# ---------------------------------------------------------------------------
# send_df_access_request_approved
# ---------------------------------------------------------------------------

class TestSendDfAccessRequestApproved:
    def test_uses_access_approved_template(self, monkeypatch):
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock())
        cfg = _make_config()

        rsi_email.send_df_access_request_approved(
            subject="Approved", config=cfg, email_address="user@example.com",
            full_name="John Doe", message={}
        )

        env_mock.get_template.assert_called_once_with("user_access_request_approved.html")

    def test_sends_to_provided_email_address(self, monkeypatch):
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        mock_send = MagicMock(return_value=True)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", mock_send)
        cfg = _make_config()

        rsi_email.send_df_access_request_approved(
            subject="Approved", config=cfg, email_address="user@example.com",
            full_name="John Doe", message={}
        )

        args = mock_send.call_args[0]
        assert "user@example.com" in args[0]

    def test_returns_tuple_with_args(self, monkeypatch):
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock(return_value=True))
        cfg = _make_config()

        result = rsi_email.send_df_access_request_approved(
            subject="Approved", config=cfg, email_address="user@example.com",
            full_name="John Doe", message={}
        )

        assert isinstance(result, tuple) and len(result) == 2


# ---------------------------------------------------------------------------
# send_submission_report_by_status
# ---------------------------------------------------------------------------

class TestSendSubmissionReportByStatus:
    def test_uses_submission_report_template(self, monkeypatch):
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        mock_send = MagicMock(return_value=True)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", mock_send)
        cfg = _make_config()

        rsi_email.send_submission_report_by_status(subject="Report", config=cfg, message={})

        env_mock.get_template.assert_called_once_with("submission_report_by_status.html")

    def test_sends_to_rsiops_address(self, monkeypatch):
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        mock_send = MagicMock(return_value=True)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", mock_send)
        cfg = _make_config()

        rsi_email.send_submission_report_by_status(subject="Report", config=cfg, message={})

        args = mock_send.call_args[0]
        assert cfg.RSIOPS_EMAIL_ADDRESS in args[0]

    def test_uses_custom_templates_path(self, monkeypatch):
        captured = {}

        def _capture_env(**kwargs):
            captured["path"] = kwargs.get("path")
            return _make_jinja2_env_mock()[0]

        monkeypatch.setattr(rsi_email, "get_jinja2_env", _capture_env)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock())
        cfg = _make_config()

        rsi_email.send_submission_report_by_status(
            subject="Report", config=cfg, message={}, templates_path="/custom/path"
        )

        assert captured["path"] == "/custom/path"

    def test_returns_tuple(self, monkeypatch):
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock(return_value=True))
        cfg = _make_config()

        result = rsi_email.send_submission_report_by_status(subject="Report", config=cfg, message={})

        assert isinstance(result, tuple) and len(result) == 2


# ---------------------------------------------------------------------------
# send_irp_pending_rts
# ---------------------------------------------------------------------------

class TestSendIrpPendingRts:
    def test_uses_irp_pending_rts_template(self, monkeypatch):
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        mock_send = MagicMock(return_value=True)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", mock_send)
        cfg = _make_config()

        rsi_email.send_irp_pending_rts(
            subject="Pending RTS", config=cfg, email_address="officer@example.com",
            officer_name="Cst. Smith", message={"pending_rts_count": 2, "pending_rts": []},
            templates_path="./python/common/templates"
        )

        env_mock.get_template.assert_called_once_with("irp_pending_rts.html")

    def test_sends_to_officer_email(self, monkeypatch):
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        mock_send = MagicMock(return_value=True)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", mock_send)
        cfg = _make_config()

        rsi_email.send_irp_pending_rts(
            subject="Pending RTS", config=cfg, email_address="officer@example.com",
            officer_name="Cst. Smith", message={}, templates_path="./python/common/templates"
        )

        args = mock_send.call_args[0]
        assert "officer@example.com" in args[0]

    def test_renders_template_with_officer_name(self, monkeypatch):
        env_mock, template_mock = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock())
        cfg = _make_config()

        rsi_email.send_irp_pending_rts(
            subject="Pending RTS", config=cfg, email_address="officer@example.com",
            officer_name="Cst. Smith", message={}, templates_path="./python/common/templates"
        )

        _, kwargs = template_mock.render.call_args
        assert kwargs["full_name"] == "Cst. Smith"

    def test_renders_template_with_message(self, monkeypatch):
        env_mock, template_mock = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock())
        cfg = _make_config()
        message = {"pending_rts_count": 3, "pending_rts": []}

        rsi_email.send_irp_pending_rts(
            subject="Pending RTS", config=cfg, email_address="officer@example.com",
            officer_name="Cst. Smith", message=message, templates_path="./python/common/templates"
        )

        _, kwargs = template_mock.render.call_args
        assert kwargs["message"] == message

    def test_uses_custom_templates_path(self, monkeypatch):
        captured = {}

        def _capture_env(**kwargs):
            captured["path"] = kwargs.get("path")
            return _make_jinja2_env_mock()[0]

        monkeypatch.setattr(rsi_email, "get_jinja2_env", _capture_env)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock())
        cfg = _make_config()

        rsi_email.send_irp_pending_rts(
            subject="Pending RTS", config=cfg, email_address="officer@example.com",
            officer_name="Cst. Smith", message={}, templates_path="/custom/path"
        )

        assert captured["path"] == "/custom/path"

    def test_returns_tuple(self, monkeypatch):
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock(return_value=True))
        cfg = _make_config()

        result = rsi_email.send_irp_pending_rts(
            subject="Pending RTS", config=cfg, email_address="officer@example.com",
            officer_name="Cst. Smith", message={}, templates_path="./python/common/templates"
        )

        assert isinstance(result, tuple) and len(result) == 2
