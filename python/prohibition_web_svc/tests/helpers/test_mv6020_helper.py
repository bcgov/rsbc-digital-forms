import base64
from unittest.mock import MagicMock

import pytest
import python.prohibition_web_svc.helpers.mv6020_helper as helper


#
# ---------------------------
# Fixtures
# ---------------------------
#

@pytest.fixture
def base_kwargs():
    return {
        "payload": {
            "data": {
                "collision_case_num": "C12345",
                "date_collision": "2025-09-21T00:00:00-08:00",
                "time_collision": "10:30",
                "time_collision_unknown": False,
                "print_options": {"type": "icbc", "email": "icbc@example.com"},
            }
        }
    }


#
# ---------------------------
# Tests for helper: proper_case
# ---------------------------
#

def test_proper_case_normal():
    assert helper.proper_case("JOHN DOE") == "John Doe"
    assert helper.proper_case("john doe") == "John Doe"

def test_proper_case_empty():
    assert helper.proper_case(None) == "Officer"
    assert helper.proper_case("") == "Officer"
    assert helper.proper_case("   ") == "Officer"


#
# ---------------------------
# Tests for helper: format_collision_datetime
# ---------------------------
#

def test_format_collision_datetime_normal_pst():
    """Ensure PST date + time combine correctly without UTC rollover."""
    date_str = "2025-11-20T00:00:00-08:00"
    time_str = "17:00"
    date_fmt, time_fmt = helper.format_collision_datetime(date_str, time_str, False)

    assert date_fmt == "November 20, 2025"
    assert time_fmt == "5:00 PM"

def test_format_collision_datetime_time_unknown():
    date_str = "2025-11-20T00:00:00-08:00"
    time_str = "27:00"
    date_fmt, time_fmt = helper.format_collision_datetime(date_str, time_str, True)

    assert date_fmt == "November 20, 2025"
    assert time_fmt == "(Time Unknown)"

def test_format_collision_datetime_bad_time():
    date_str = "2025-11-20T00:00:00-08:00"
    time_str = "invalid"
    date_fmt, time_fmt = helper.format_collision_datetime(date_str, time_str, False)

    assert date_fmt == "November 20, 2025"
    assert time_fmt == "invalid"   # fallback




# ---------------------------
# Tests for helper: entity data
# ---------------------------
#
def test_get_entity_data_found():
    data = {
        "entities": [
            {"entity_num": 1, "given_name": "John", "surname": "Doe", "contact_email": "john@example.com"}
        ],
        "print_options": {"entity_num": 1},
    }
    name = helper.get_entity_data(data)
    assert name == "John Doe"


def test_get_entity_data_not_found():
    data = {
        "entities": [{"entity_num": 2, "given_name": "Jane"}],
        "print_options": {"entity_num": 1},
    }
    name = helper.get_entity_data(data) #wrong entity number supplied in print options
    assert name == ""



# ---------------------------
# Tests for helper: send email to recipients
# ---------------------------
#
def test_send_mv6020_copy_success_icbc(monkeypatch):
    """ICBC → full_name should be 'ICBC'."""
    payload = {
        "payload": {
            "data": {
                "collision_case_num": "12345",
                "date_collision": "2025-11-20T00:00:00-08:00",
                "time_collision": "17:00",
                "time_collision_unknown": False,
                "print_options": {"type": "icbc", "email": "officer@example.com"},
            }
        }
    }

    # Mocks
    monkeypatch.setattr(helper.print_middleware, "set_event_type", lambda **kw: (True, kw))
    monkeypatch.setattr(helper.print_middleware, "render_document_with_playwright",
        lambda **kw: (True, {"rendered_content": b"PDF", "filename": "mv.pdf", "content_type": "application/pdf"})
    )
    monkeypatch.setattr(helper.rsi_email, "send_mv6020_copy", lambda **kw: True)

    success, result = helper.send_mv6020_copy(**payload)
    assert success is True
    assert "Successfully sent email" in result["response_dict"]["message"]


def test_send_mv6020_copy_success_police(monkeypatch):
    """Police → full_name should be proper_case()."""
    payload = {
        "payload": {
            "data": {
                "collision_case_num": "99999",
                "completed_by_name": "TIGER SCOTT",
                "date_collision": "2025-11-20T00:00:00-08:00",
                "time_collision": "09:15",
                "time_collision_unknown": False,
                "print_options": {"type": "police", "email": "police@example.com"},
            }
        }
    }

    monkeypatch.setattr(helper.print_middleware, "set_event_type", lambda **kw: (True, kw))
    monkeypatch.setattr(helper.print_middleware, "render_document_with_playwright",
        lambda **kw: (True, {"rendered_content": b"PDF", "filename": "mv.pdf", "content_type": "application/pdf"})
    )
    monkeypatch.setattr(helper.rsi_email, "send_mv6020_copy", lambda **kw: True)

    success, result = helper.send_mv6020_copy(**payload)
    assert success is True
    assert "Successfully sent email to Tiger Scott" in result["response_dict"]["message"]


def test_send_mv6020_copy_success_entity(monkeypatch):
    """Entity recipient should come from entity list."""
    payload = {
        "payload": {
            "data": {
                "collision_case_num": "AB123",
                "date_collision": "2025-11-20T00:00:00-08:00",
                "time_collision": "08:00",
                "time_collision_unknown": False,
                "entities": [
                    {"entity_num": 7, "given_name": "Alice", "surname": "Smith", "email_address": "alice@example.com"}
                ],
                "print_options": {"type": "entity", "email": "", "entity_num": 7},
            }
        }
    }

    monkeypatch.setattr(helper.print_middleware, "set_event_type", lambda **kw: (True, kw))
    monkeypatch.setattr(helper.print_middleware, "render_document_with_playwright",
        lambda **kw: (True, {"rendered_content": b"PDF", "filename": "mv.pdf", "content_type": "application/pdf"})
    )
    monkeypatch.setattr(helper.rsi_email, "send_mv6020_copy", lambda **kw: True)

    success, result = helper.send_mv6020_copy(**payload)
    assert success is True
    assert "Successfully sent email to Alice Smith" in result["response_dict"]["message"]


def test_send_mv6020_copy_success_admin(monkeypatch):
    """Admin copy should collect attachments and send to configured admins."""
    payload = {
        "payload": {
            "data": {
                "collision_case_num": "AB123",
                "collision_type": "0",
                "date_collision": "2025-11-20T00:00:00-08:00",
                "time_collision": "08:00",
                "time_collision_unknown": False,
                "icbc_submission_date": "2025-11-19",
                "police_file_num": "PF-77",
                "prime_file_vjur": {"label": "VJ-9"},
                "print_options": {"type": "admin", "email": ""},
            }
        }
    }

    monkeypatch.setattr(helper.print_middleware, "set_event_type", lambda **kw: (True, kw))
    monkeypatch.setattr(
        helper,
        "_get_user_data",
        lambda **kw: (
            True,
            {
                **kw,
                "user_data": {
                    "display_name": "Officer Example",
                    "badge_number": "42",
                    "agency_id": 99,
                },
            },
        ),
    )
    monkeypatch.setattr(
        helper,
        "_get_admin_emails",
        lambda **kw: (True, {**kw, "email_address": ["admin1@example.com", "admin2@example.com"]}),
    )
    monkeypatch.setattr(
        helper,
        "generate_all_PDF_attachments",
        lambda **kw: (
            True,
            {
                **kw,
                "attachments": [
                    {
                        "content": "cGRm",
                        "contentType": "application/pdf",
                        "encoding": "base64",
                        "filename": "MV6020-AB123-police-copy.pdf",
                    }
                ],
            },
        ),
    )

    captured = {}

    def fake_send_mv6020_copy(**kw):
        captured.update(kw)
        return True, kw

    monkeypatch.setattr(helper.rsi_email, "send_mv6020_copy", fake_send_mv6020_copy)

    success, result = helper.send_mv6020_copy(**payload)

    assert success is True
    assert result["response_dict"]["message"] == "Successfully sent admin copy email to ['admin1@example.com', 'admin2@example.com']"
    assert captured["subject"] == "MV6020 - AB123 - PF-77"
    assert captured["email_address"] == ["admin1@example.com", "admin2@example.com"]
    assert captured["email_type"] == "admin"
    assert captured["message"]["collision_case_number"] == "AB123"
    assert captured["message"]["submission_date"] == "2025-11-19"
    assert captured["attachments"][0]["filename"] == "MV6020-AB123-police-copy.pdf"


def test_send_mv6020_copy_admin_without_admin_emails(monkeypatch):
    """Admin copy should succeed without sending when no admin emails exist."""
    payload = {
        "payload": {
            "data": {
                "collision_case_num": "AB123",
                "date_collision": "2025-11-20T00:00:00-08:00",
                "time_collision": "08:00",
                "time_collision_unknown": False,
                "print_options": {"type": "admin", "email": ""},
            }
        }
    }

    monkeypatch.setattr(helper.print_middleware, "set_event_type", lambda **kw: (True, kw))
    monkeypatch.setattr(helper, "_get_user_data", lambda **kw: (True, {**kw, "user_data": {"agency_id": 99}}))
    monkeypatch.setattr(helper, "_get_admin_emails", lambda **kw: (True, {**kw, "email_address": None}))

    generate_mock = MagicMock(return_value=(True, {}))
    send_mock = MagicMock(return_value=(True, {}))
    monkeypatch.setattr(helper, "generate_all_PDF_attachments", generate_mock)
    monkeypatch.setattr(helper.rsi_email, "send_mv6020_copy", send_mock)

    success, result = helper.send_mv6020_copy(**payload)

    assert success is True
    assert result["response_dict"]["message"] == "No admin email found, skipping admin copy email sending."
    generate_mock.assert_not_called()
    send_mock.assert_not_called()


def test_send_all_copy_success(monkeypatch):
    kwargs = {
        "subject": "MV6020 - Non-reportable - AB123 - VJ-9 - PF-77",
        "payload": {
            "data": {
                "collision_case_num": "AB123",
                "date_collision": "2025-11-20T00:00:00-08:00",
                "time_collision": "08:00",
                "time_collision_unknown": False,
                "print_options": {"type": "all", "email": "officer@example.com"},
            }
        },
    }

    monkeypatch.setattr(
        helper,
        "generate_all_PDF_attachments",
        lambda **kw: (
            True,
            {
                **kw,
                "attachments": [
                    {
                        "content": "cGRm",
                        "contentType": "application/pdf",
                        "encoding": "base64",
                        "filename": "MV6020_AB123_PF-77_20251120_police_Copy.pdf",
                    }
                ],
            },
        ),
    )

    captured = {}

    def fake_send_mv6020_copy(**kw):
        captured.update(kw)
        return True

    monkeypatch.setattr(helper.rsi_email, "send_mv6020_copy", fake_send_mv6020_copy)

    success, result = helper._send_all_copy(**kwargs)

    assert success is True
    assert result["response_dict"]["message"] == "Successfully sent email to officer@example.com"
    assert captured["subject"] == "MV6020 - Non-reportable - AB123 - VJ-9 - PF-77"
    assert captured["email_address"] == "officer@example.com"
    assert captured["email_type"] == "police"
    assert captured["message"]["collision_case_number"] == "AB123"
    assert captured["attachments"][0]["filename"] == "MV6020_AB123_PF-77_20251120_police_Copy.pdf"


def test_send_all_copy_generate_all_pdf_attachments_failure(monkeypatch):
    kwargs = {
        "subject": "MV6020 - Non-reportable - AB123 - VJ-9 - PF-77",
        "payload": {
            "data": {
                "collision_case_num": "AB123",
                "date_collision": "2025-11-20T00:00:00-08:00",
                "time_collision": "08:00",
                "time_collision_unknown": False,
                "print_options": {"type": "all", "email": "officer@example.com"},
            }
        },
        "error": {"error_details": "render failed"},
    }

    monkeypatch.setattr(helper, "generate_all_PDF_attachments", lambda **kw: (False, kw))

    send_mock = MagicMock(return_value=True)
    monkeypatch.setattr(helper.rsi_email, "send_mv6020_copy", send_mock)

    success, result = helper._send_all_copy(**kwargs)

    assert success is False
    assert result["error"]["error_details"] == "render failed"
    send_mock.assert_not_called()


def test_send_all_copy_email_send_failure(monkeypatch):
    kwargs = {
        "subject": "MV6020 - Non-reportable - AB123 - VJ-9 - PF-77",
        "payload": {
            "data": {
                "collision_case_num": "AB123",
                "date_collision": "2025-11-20T00:00:00-08:00",
                "time_collision": "08:00",
                "time_collision_unknown": False,
                "print_options": {"type": "all", "email": "officer@example.com"},
            }
        },
    }

    monkeypatch.setattr(
        helper,
        "generate_all_PDF_attachments",
        lambda **kw: (
            True,
            {
                **kw,
                "attachments": [
                    {
                        "content": "cGRm",
                        "contentType": "application/pdf",
                        "encoding": "base64",
                        "filename": "MV6020_AB123_PF-77_20251120_police_Copy.pdf",
                    }
                ],
            },
        ),
    )
    monkeypatch.setattr(helper.rsi_email, "send_mv6020_copy", lambda **kw: False)

    success, result = helper._send_all_copy(**kwargs)

    assert success is False
    assert "response_dict" not in result


def test_send_mv6020_copy_unknown_type(monkeypatch):
    """Unknown type → failure with correct message."""
    payload = {
        "payload": {
            "data": {
                "collision_case_num": "12345",
                "date_collision": "2025-11-20T00:00:00-08:00",
                "print_options": {"type": "foobar", "email": "x@example.com"}
            }
        }
    }

    monkeypatch.setattr(helper.print_middleware, "set_event_type", lambda **kw: (True, kw))

    success, result = helper.send_mv6020_copy(**payload)
    assert success is False
    assert result["response_dict"]["message"] == "Failed to send email"


def test_generate_all_pdf_attachments_success(monkeypatch):
    kwargs = {
        "payload": {
            "data": {
                "collision_case_num": "AB123",
                "police_file_num": "PF-77",
                "date_collision": "2025-11-20T00:00:00-08:00",
                "print_options": {"type": "all", "email": "officer@example.com"},
                "entities": [{"entity_num": 7}, {"entity_num": 8}],
            }
        }
    }

    def fake_render(**kw):
        print_options = kw["payload"]["data"]["print_options"]
        ptype = print_options.get("type")
        entity_num = print_options.get("entity_num")

        if ptype == "police":
            return True, {"rendered_content": b"PDF-POLICE"}
        if ptype == "entity" and entity_num == 7:
            return True, {"rendered_content": b"PDF-ENTITY-7"}
        if ptype == "entity" and entity_num == 8:
            return True, {"rendered_content": "PDF-ENTITY-8"}
        return False, {"error": {"error_details": "unexpected render path"}}

    monkeypatch.setattr(helper.print_middleware, "render_document_with_playwright", fake_render)

    success, result = helper.generate_all_PDF_attachments(**kwargs)

    assert success is True
    attachments = result["attachments"]
    assert len(attachments) == 3

    assert attachments[0]["filename"] == "MV6020_AB123_PF-77_20251120_police_Copy.pdf"
    assert attachments[1]["filename"] == "MV6020_AB123_PF-77_20251120_entity_7_Copy.pdf"
    assert attachments[2]["filename"] == "MV6020_AB123_PF-77_20251120_entity_8_Copy.pdf"

    assert base64.b64decode(attachments[0]["content"]) == b"PDF-POLICE"
    assert base64.b64decode(attachments[1]["content"]) == b"PDF-ENTITY-7"
    assert base64.b64decode(attachments[2]["content"]) == b"PDF-ENTITY-8"


def test_generate_all_pdf_attachments_failure_police_render(monkeypatch):
    kwargs = {
        "payload": {
            "data": {
                "collision_case_num": "AB123",
                "police_file_num": "PF-77",
                "date_collision": "2025-11-20T00:00:00-08:00",
                "print_options": {"type": "all", "email": "officer@example.com"},
                "entities": [{"entity_num": 7}],
            }
        }
    }

    monkeypatch.setattr(
        helper.print_middleware,
        "render_document_with_playwright",
        lambda **kw: (False, {"error": {"error_details": "police render failed"}}),
    )

    success, result = helper.generate_all_PDF_attachments(**kwargs)

    assert success is False
    assert result["response_dict"]["message"] == "Failed to render document for admin copy"
    assert result["error"]["error_details"] == "police render failed"


def test_generate_all_pdf_attachments_failure_entity_render(monkeypatch):
    kwargs = {
        "payload": {
            "data": {
                "collision_case_num": "AB123",
                "police_file_num": "PF-77",
                "date_collision": "2025-11-20T00:00:00-08:00",
                "print_options": {"type": "all", "email": "officer@example.com"},
                "entities": [{"entity_num": 7}],
            }
        }
    }

    calls = {"count": 0}

    def fake_render(**kw):
        calls["count"] += 1
        if calls["count"] == 1:
            return True, {"rendered_content": b"PDF-POLICE"}
        return False, {"error": {"error_details": "entity render failed"}}

    monkeypatch.setattr(helper.print_middleware, "render_document_with_playwright", fake_render)

    success, result = helper.generate_all_PDF_attachments(**kwargs)

    assert success is False
    assert result["response_dict"]["message"] == "Failed to render document for entity 7 in admin copy"
    assert result["error"]["error_details"] == "entity render failed"




# ---------------------------
# Tests for helper: mask data
# ---------------------------
#
def test_mask_collision_sensitive_data_top_level():
    data = {
        "driver_license_num": "D1234567",
        "surname": "Smith",
        "given_name": "John",
        "contact_phone_num": "555-1234",
        "non_sensitive_field": "keep_me"
    }

    masked = helper.mask_collision_sensitive_data(data)

    assert masked["driver_license_num"] == "[REDACTED]"
    assert masked["surname"] == "[REDACTED]"
    assert masked["given_name"] == "[REDACTED]"
    assert masked["contact_phone_num"] == "[REDACTED]"
    assert masked["non_sensitive_field"] == "keep_me"


def test_mask_collision_sensitive_data_entities():
    data = {
        "entities": [
            {"vehicle_plate_num": "ABC123", "vehicle_owner_name": "Alice"},
            {"vehicle_owner_address": "123 Main St"}
        ]
    }

    masked = helper.mask_collision_sensitive_data(data)

    assert masked["entities"][0]["vehicle_plate_num"] == "[REDACTED]"
    assert masked["entities"][0]["vehicle_owner_name"] == "[REDACTED]"
    assert masked["entities"][1]["vehicle_owner_address"] == "[REDACTED]"


def test_mask_collision_sensitive_data_involved_persons():
    data = {
        "involved_persons": [
            {"surname": "Brown", "given_name": "Charlie"}
        ]
    }

    masked = helper.mask_collision_sensitive_data(data)

    assert masked["involved_persons"][0]["surname"] == "[REDACTED]"
    assert masked["involved_persons"][0]["given_name"] == "[REDACTED]"


def test_mask_collision_sensitive_data_witnesses():
    data = {
        "witnesses": [
            {"witness_name": "Tom"},
            {"contact_phn_num": "555-9876"}
        ]
    }

    masked = helper.mask_collision_sensitive_data(data)

    assert masked["witnesses"][0]["witness_name"] == "[REDACTED]"
    assert masked["witnesses"][1]["contact_phn_num"] == "[REDACTED]"


def test_mask_collision_sensitive_data_no_sensitive_fields():
    data = {"some_field": "value", "other_field": 123}
    masked = helper.mask_collision_sensitive_data(data)
    assert masked == data
