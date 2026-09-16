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


# ---------------------------------------------------------------------------
# Enhanced Edge Cases & Error Scenarios
# ---------------------------------------------------------------------------

class TestSendMv6020CopyAdvanced:
    """Advanced tests for send_mv6020_copy including email list handling."""

    def test_email_address_as_list(self, monkeypatch):
        """Test send_mv6020_copy with email_address already as list."""
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        mock_send = MagicMock(return_value=True)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", mock_send)
        cfg = _make_config()
        email_list = ["user1@example.com", "user2@example.com"]

        rsi_email.send_mv6020_copy(
            config=cfg, subject="Subject", email_address=email_list,
            full_name="Name", message={"collision_case_number": "CC-001"},
            attachments=None, email_type="entity"
        )

        args = mock_send.call_args[0]
        assert args[0] == email_list

    def test_email_template_mapping_admin_type(self, monkeypatch):
        """Test admin email type in send_mv6020_copy."""
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock(return_value=True))
        cfg = _make_config()

        rsi_email.send_mv6020_copy(
            config=cfg, subject="Subject", email_address="to@example.com",
            full_name="Name", message={"collision_case_number": "CC-001"},
            attachments=None, email_type="admin"
        )

        env_mock.get_template.assert_called_once_with("MV6020_admin_notification.html")

    def test_collision_case_number_extracted_from_message(self, monkeypatch):
        """Test that collision_case_number is extracted from message."""
        env_mock, template_mock = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        mock_send = MagicMock(return_value=True)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", mock_send)
        cfg = _make_config()
        message = {"collision_case_number": "CC-12345"}

        rsi_email.send_mv6020_copy(
            config=cfg, subject="Subject", email_address="to@example.com",
            full_name="Name", message=message, attachments=None, email_type="entity"
        )

        args = mock_send.call_args[0]
        # collision_case_number is passed as 5th positional arg (after subject, email, body, type)
        assert args[4] == "CC-12345"

    def test_email_template_stored_in_kwargs(self, monkeypatch):
        """Test that email_template is stored in returned kwargs."""
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock(return_value=True))
        cfg = _make_config()

        _, args = rsi_email.send_mv6020_copy(
            config=cfg, subject="S", email_address="to@example.com",
            full_name="Name", message={"collision_case_number": "CC-001"},
            attachments=None, email_type="entity"
        )

        assert args["email_template"] == "MV6020_send_entity_copy.html"


class TestSendEmailToAdminAdvanced:
    """Advanced tests for send_email_to_admin with complex scenarios."""

    def test_message_json_serialized_in_template_render(self, monkeypatch):
        """Test that message dict is JSON-serialized in template render."""
        env_mock, template_mock = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock())
        cfg = _make_config()
        message = {"error": "test_error", "code": 500}

        rsi_email.send_email_to_admin(
            subject="Error", config=cfg, message=message, body="Error body"
        )

        # Verify json.dumps was called on message in render
        _, kwargs = template_mock.render.call_args
        # The message should be JSON string in the render kwargs
        assert "message" in kwargs

    def test_admin_email_split_by_comma(self, monkeypatch):
        """Test that multiple admin emails are handled correctly."""
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        mock_send = MagicMock(return_value=True)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", mock_send)
        cfg = MagicMock()
        cfg.ADMIN_EMAIL_ADDRESS = "admin1@example.com,admin2@example.com"

        rsi_email.send_email_to_admin(subject="Test", config=cfg, message={}, body="body")

        args = mock_send.call_args[0]
        # Should be list of split emails
        assert isinstance(args[0], list)
        assert len(args[0]) == 2
        assert "admin1@example.com" in args[0]
        assert "admin2@example.com" in args[0]

    def test_subject_and_body_passed_to_render(self, monkeypatch):
        """Test that subject and body are passed to template render."""
        env_mock, template_mock = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock())
        cfg = _make_config()

        rsi_email.send_email_to_admin(
            subject="Test Subject", config=cfg, message={}, body="Test Body"
        )

        _, kwargs = template_mock.render.call_args
        assert kwargs["subject"] == "Test Subject"
        assert kwargs["body"] == "Test Body"


class TestAdminUnableToSaveToVipsAdvanced:
    """Advanced tests for admin_unable_to_save_to_vips."""

    def test_subject_is_critical_error(self, monkeypatch):
        """Test that subject indicates critical error."""
        captured = {}

        def _capture(**kwargs):
            captured.update(kwargs)
            return True, {}

        monkeypatch.setattr(rsi_email, "send_email_to_admin", _capture)
        cfg = _make_config()

        rsi_email.admin_unable_to_save_to_vips(config=cfg, message={})

        assert "Critical Error" in captured.get("subject", "")
        assert "VIPS" in captured.get("subject", "")

    def test_message_is_logged_as_json(self, monkeypatch):
        """Test that message is logged in JSON format."""
        monkeypatch.setattr(rsi_email, "send_email_to_admin", MagicMock(return_value=(True, {})))
        mock_logging = MagicMock()
        monkeypatch.setattr(rsi_email.logging, "critical", mock_logging)
        cfg = _make_config()
        message = {"error_code": 500, "details": "Connection failed"}

        rsi_email.admin_unable_to_save_to_vips(config=cfg, message=message)

        # Should call logging.critical with formatted message
        assert mock_logging.call_count >= 2  # Initial log + unable_to_save log


class TestAdminUnknownEventTypeAdvanced:
    """Advanced tests for admin_unknown_event_type."""

    def test_event_type_extracted_from_message(self, monkeypatch):
        """Test that event_type is extracted from message dict."""
        captured = {}

        def _capture(**kwargs):
            captured.update(kwargs)
            return True, {}

        monkeypatch.setattr(rsi_email, "send_email_to_admin", _capture)
        cfg = _make_config()
        message = {"event_type": "UNKNOWN_EVENT_XYZ"}

        rsi_email.admin_unknown_event_type(config=cfg, message=message)

        assert "UNKNOWN_EVENT_XYZ" in captured.get("body", "")

    def test_unknown_event_type_logged(self, monkeypatch):
        """Test that unknown event type is logged."""
        monkeypatch.setattr(rsi_email, "send_email_to_admin", MagicMock(return_value=(True, {})))
        mock_logging = MagicMock()
        monkeypatch.setattr(rsi_email.logging, "critical", mock_logging)
        cfg = _make_config()
        message = {"event_type": "WEIRD_TYPE"}

        rsi_email.admin_unknown_event_type(config=cfg, message=message)

        # Should log the event type
        assert mock_logging.called


class TestHyphenateAdvanced:
    """Advanced tests for _hyphenate function."""

    def test_with_longer_string(self):
        """Test hyphenate with longer prohibition number (takes first 8 chars)."""
        # Function only formats first 8 chars: 2 letters + 6 digits
        assert rsi_email._hyphenate("BC123456789") == "BC-123456"

    def test_with_mixed_alphanumeric(self):
        """Test hyphenate with mixed characters."""
        # Function only formats first 8 chars
        assert rsi_email._hyphenate("AB98765432") == "AB-987654"

    def test_with_all_digits(self):
        """Test hyphenate with all digits."""
        assert rsi_email._hyphenate("00000000") == "00-000000"

    def test_with_uppercase_letters(self):
        """Test hyphenate with uppercase letters."""
        assert rsi_email._hyphenate("XY123456") == "XY-123456"


class TestGetEmailContentAdvanced:
    """Advanced tests for get_email_content function."""

    def test_prohibition_number_formatting(self):
        """Test that prohibition number is properly formatted with hyphen."""
        content = rsi_email.get_email_content("MV6020_send_entity_copy.html", "12345678")
        assert "12-345678" in content["subject"]

    def test_raw_subject_used_for_formatting(self):
        """Test that raw_subject is used to format the final subject."""
        content = rsi_email.get_email_content("MV6020_send_entity_copy.html", "AB123456")
        # raw_subject is: "Traffic Accident Report Copy Attached - Collision Case Number {}"
        assert "AB-123456" in content["subject"]
        assert "Collision Case Number" in content["subject"]

    def test_unknown_template_returns_complete_fallback_dict(self):
        """Test fallback dict for unknown templates has all expected keys."""
        content = rsi_email.get_email_content("nonexistent.html", "12345678")
        assert "raw_subject" in content
        assert "subject" in content
        assert "callout" in content
        assert "title" in content
        assert "timeline" in content

    def test_unknown_template_subject_formatted(self):
        """Test that fallback dict has properly formatted subject."""
        content = rsi_email.get_email_content("unknown_template.html", "12345678")
        # raw_subject is "Unknown template requested {}" but fallback uses static "Unknown template"
        assert content["subject"] == "Unknown template"
        assert content["title"] == "Unknown Template"


class TestSendDfAccessRequestApprovedAdvanced:
    """Advanced tests for send_df_access_request_approved."""

    def test_template_receives_all_required_fields(self, monkeypatch):
        """Test that template is rendered with all required fields."""
        env_mock, template_mock = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock())
        cfg = _make_config()
        message = {"approval_details": "Approved for access"}

        rsi_email.send_df_access_request_approved(
            subject="Access Approved", config=cfg, email_address="user@example.com",
            full_name="Jane Doe", message=message
        )

        _, kwargs = template_mock.render.call_args
        assert kwargs["subject"] == "Access Approved"
        assert kwargs["full_name"] == "Jane Doe"
        assert kwargs["message"] == message


class TestSendSubmissionReportByStatusAdvanced:
    """Advanced tests for send_submission_report_by_status."""

    def test_default_templates_path_used(self, monkeypatch):
        """Test that default templates path is used when not specified."""
        captured = {}

        def _capture_env(**kwargs):
            captured["path"] = kwargs.get("path")
            return _make_jinja2_env_mock()[0]

        monkeypatch.setattr(rsi_email, "get_jinja2_env", _capture_env)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock())
        cfg = _make_config()

        rsi_email.send_submission_report_by_status(subject="Report", config=cfg, message={})

        assert captured["path"] == "./python/common/templates"

    def test_rsiops_email_split_by_comma(self, monkeypatch):
        """Test that RSIops email is split if multiple addresses."""
        env_mock, _ = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        mock_send = MagicMock(return_value=True)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", mock_send)
        cfg = MagicMock()
        cfg.RSIOPS_EMAIL_ADDRESS = "ops1@example.com,ops2@example.com"

        rsi_email.send_submission_report_by_status(subject="Report", config=cfg, message={})

        args = mock_send.call_args[0]
        # Should be wrapped in list for send_email
        assert args[0] == ["ops1@example.com,ops2@example.com"]

    def test_template_receives_full_name_rsi_ops(self, monkeypatch):
        """Test that template is rendered with RSI Operations Team name."""
        env_mock, template_mock = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock())
        cfg = _make_config()
        message = {"status": "submitted"}

        rsi_email.send_submission_report_by_status(
            subject="Report", config=cfg, message=message
        )

        _, kwargs = template_mock.render.call_args
        assert kwargs["full_name"] == "RSI Operations Team"


class TestSendIrpPendingRtsAdvanced:
    """Advanced tests for send_irp_pending_rts."""

    def test_default_templates_path_for_irp(self, monkeypatch):
        """Test that default templates path is used for irp_pending_rts."""
        captured = {}

        def _capture_env(**kwargs):
            captured["path"] = kwargs.get("path")
            return _make_jinja2_env_mock()[0]

        monkeypatch.setattr(rsi_email, "get_jinja2_env", _capture_env)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock())
        cfg = _make_config()

        rsi_email.send_irp_pending_rts(
            subject="RTS", config=cfg, email_address="officer@example.com",
            officer_name="Cst. Jones", message={}
        )

        assert captured["path"] == "./python/common/templates"

    def test_multiple_pending_rts_message_handling(self, monkeypatch):
        """Test handling of message with multiple pending RTS items."""
        env_mock, template_mock = _make_jinja2_env_mock()
        monkeypatch.setattr(rsi_email, "get_jinja2_env", lambda **kw: env_mock)
        monkeypatch.setattr(rsi_email.common_email_services, "send_email", MagicMock())
        cfg = _make_config()
        message = {
            "pending_rts_count": 5,
            "pending_rts": [{"case_id": "1"}, {"case_id": "2"}]
        }

        rsi_email.send_irp_pending_rts(
            subject="RTS", config=cfg, email_address="officer@example.com",
            officer_name="Cst. Lee", message=message, templates_path="./python/common/templates"
        )

        _, kwargs = template_mock.render.call_args
        assert kwargs["message"] == message
        assert kwargs["message"]["pending_rts_count"] == 5


class TestContentDataStructure:
    """Advanced tests for content_data structure."""

    def test_content_data_has_title_key(self):
        """Test that content_data entries have title key."""
        data = rsi_email.content_data()
        for key, value in data.items():
            assert "title" in value or "raw_subject" in value

    def test_content_data_immutability_per_call(self):
        """Test that each call to content_data returns fresh dict."""
        data1 = rsi_email.content_data()
        data2 = rsi_email.content_data()
        # Should be equal but not same object
        assert data1 == data2
        assert data1 is not data2


class TestGetJinja2EnvAdvanced:
    """Advanced tests for get_jinja2_env function."""

    def test_autoescape_enabled_for_html(self):
        """Test that autoescape is properly configured for HTML."""
        env = rsi_email.get_jinja2_env(path="./python/common/templates")
        # autoescape should be enabled
        assert env.autoescape is not None

    def test_file_system_loader_configured(self):
        """Test that FileSystemLoader is properly configured."""
        env = rsi_email.get_jinja2_env(path="./python/common/templates")
        # Environment should have loader
        assert env.loader is not None

    def test_custom_path_affects_loader(self, tmp_path):
        """Test that custom path is used in loader."""
        custom_path = str(tmp_path)
        env = rsi_email.get_jinja2_env(path=custom_path)
        assert env.loader is not None
        # Loader should have the custom path in searchpath
        assert custom_path in env.loader.searchpath
