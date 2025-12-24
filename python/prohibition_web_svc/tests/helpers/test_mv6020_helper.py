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
            {"entity_num": 1, "given_name": "John", "surname": "Doe", "email_address": "john@example.com"}
        ],
        "print_options": {"entity_num": 1},
    }
    name, email = helper.get_entity_data(data)
    assert name == "John Doe"
    assert email == "john@example.com"


def test_get_entity_data_not_found():
    data = {
        "entities": [{"entity_num": 2, "given_name": "Jane"}],
        "print_options": {"entity_num": 1},
    }
    name, email = helper.get_entity_data(data)
    assert name == ""
    assert email == ""



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
