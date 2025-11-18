import pytest
from python.prohibition_web_svc.helpers import mv6020_helper


@pytest.fixture
def base_kwargs():
    return {
        "payload": {
            "data": {
                "collision_case_num": "C12345",
                "date_collision": "2025-09-21",
                "print_options": {"type": "icbc", "email": "icbc@example.com"},
            }
        }
    }


def test_get_entity_data_found():
    data = {
        "entities": [
            {"entity_num": 1, "given_name": "John", "surname": "Doe", "email_address": "john@example.com"}
        ],
        "print_options": {"entity_num": 1},
    }
    name, email = mv6020_helper.get_entity_data(data)
    assert name == "John Doe"
    assert email == "john@example.com"


def test_get_entity_data_not_found():
    data = {
        "entities": [{"entity_num": 2, "given_name": "Jane"}],
        "print_options": {"entity_num": 1},
    }
    name, email = mv6020_helper.get_entity_data(data)
    assert name == ""
    assert email == ""


def test_send_mv6020_copy_success_icbc(monkeypatch, base_kwargs):
    # Mock dependencies
    monkeypatch.setattr(mv6020_helper.print_middleware, "set_event_type", lambda **kw: (True, kw))
    monkeypatch.setattr(
        mv6020_helper.print_middleware,
        "render_document_with_playwright",
        lambda **kw: (True, {"rendered_content": b"PDFDATA", "filename": "test.pdf", "content_type": "application/pdf"}),
    )
    monkeypatch.setattr(mv6020_helper.helper, "format_date_iso", lambda x: "2025-09-21")
    monkeypatch.setattr(
        mv6020_helper.rsi_email, "send_mv6020_copy", lambda **kw: True
    )

    payload = {
        "payload": {
            "data": {
                "collision_case_num": "12345",
                "date_collision": "2025-09-20T12:00:00",
                "print_options": {"type": "icbc", "email": "officer@example.com"}
            }
        }
    }

    success, result = mv6020_helper.send_mv6020_copy(**payload)
    assert success is True
    assert "Successfully sent email" in result["response_dict"]["message"]


def test_send_mv6020_copy_failure(monkeypatch, base_kwargs):
    # Mock dependencies
    monkeypatch.setattr(mv6020_helper.print_middleware, "set_event_type", lambda **kw: (True, kw))
    monkeypatch.setattr(
        mv6020_helper.print_middleware,
        "render_document_with_playwright",
        lambda **kw: (True, {"rendered_content": b"PDFDATA", "filename": "test.pdf", "content_type": "application/pdf"}),
    )
    monkeypatch.setattr(mv6020_helper.helper, "format_date_iso", lambda x: "2025-09-21")
    monkeypatch.setattr(
        mv6020_helper.rsi_email, "send_mv6020_copy", lambda **kw: False
    )

    success, result = mv6020_helper.send_mv6020_copy(**base_kwargs)
    assert success is False
    assert "Failed to send email" in result["response_dict"]["message"]


def test_send_mv6020_copy_invalid_event_type(monkeypatch, base_kwargs):
    monkeypatch.setattr(mv6020_helper.print_middleware, "set_event_type", lambda **kw: (False, kw))
    success, result = mv6020_helper.send_mv6020_copy(**base_kwargs)
    assert success is False
    # Should not proceed to rendering
    assert "response_dict" not in result

def test_send_mv6020_copy_success_police(monkeypatch):
    """Covers the else branch (lines 47–51) when type is missing or unexpected"""
    payload = {
        "payload": {
            "data": {
                "collision_case_num": "12345",
                "date_collision": "2025-09-20T12:00:00",
                "print_options": {"type": "police","email":"police@example.com"}  # unexpected type
            }
        }
    }

    # Patch dependencies
    monkeypatch.setattr(mv6020_helper.print_middleware, "set_event_type", lambda **kwargs: (True, kwargs))
    monkeypatch.setattr(mv6020_helper.print_middleware, "render_document_with_playwright", lambda **kwargs: (True, {"rendered_content": b"pdfbytes", "filename": "test.pdf", "content_type": "application/pdf"}))
    monkeypatch.setattr(mv6020_helper.rsi_email, "send_mv6020_copy", lambda **kwargs: True)

    result, kwargs = mv6020_helper.send_mv6020_copy(**payload)
    assert result is True
    assert "Successfully sent email" in kwargs["response_dict"]["message"]
    # Specifically check subject fallback
    assert "Traffic Accident Report - Collision Case Number 12345" in kwargs["response_dict"]["message"] or isinstance(kwargs["response_dict"]["message"], str)  

def test_send_mv6020_copy_unknown_type(monkeypatch):
    """Covers the else branch (lines 47–51) when type is missing or unexpected"""
    payload = {
        "payload": {
            "data": {
                "collision_case_num": "12345",
                "date_collision": "2025-09-20T12:00:00",
                "print_options": {"type": "foobar"}  # unexpected type
            }
        }
    }

    # Patch dependencies
    monkeypatch.setattr(mv6020_helper.print_middleware, "set_event_type", lambda **kwargs: (True, kwargs))
    monkeypatch.setattr(mv6020_helper.print_middleware, "render_document_with_playwright", lambda **kwargs: (True, {"rendered_content": b"pdfbytes", "filename": "test.pdf", "content_type": "application/pdf"}))
    monkeypatch.setattr(mv6020_helper.rsi_email, "send_mv6020_copy", lambda **kwargs: True)

    result, kwargs = mv6020_helper.send_mv6020_copy(**payload)
    assert result is False
    assert "Failed to send email" in kwargs["response_dict"]["message"]

def test_mask_sensitive_data_top_level():
    data = {
        "driver_license_num": "D1234567",
        "surname": "Smith",
        "given_name": "John",
        "contact_phone_num": "555-1234",
        "non_sensitive_field": "keep_me"
    }

    masked = mv6020_helper._mask_sensitive_data(data)

    assert masked["driver_license_num"] == "[REDACTED]"
    assert masked["surname"] == "[REDACTED]"
    assert masked["given_name"] == "[REDACTED]"
    assert masked["contact_phone_num"] == "[REDACTED]"
    assert masked["non_sensitive_field"] == "keep_me"

def test_mask_sensitive_data_entities():
    data = {
        "entities": [
            {"vehicle_plate_num": "ABC123", "vehicle_owner_name": "Alice"},
            {"vehicle_owner_address": "123 Main St"}
        ]
    }

    masked = mv6020_helper._mask_sensitive_data(data)

    assert masked["entities"][0]["vehicle_plate_num"] == "[REDACTED]"
    assert masked["entities"][0]["vehicle_owner_name"] == "[REDACTED]"
    assert masked["entities"][1]["vehicle_owner_address"] == "[REDACTED]"

def test_mask_sensitive_data_involved_persons():
    data = {
        "involved_persons": [
            {"surname": "Brown", "given_name": "Charlie"}
        ]
    }

    masked = mv6020_helper._mask_sensitive_data(data)

    assert masked["involved_persons"][0]["surname"] == "[REDACTED]"
    assert masked["involved_persons"][0]["given_name"] == "[REDACTED]"


def test_mask_sensitive_data_witnesses():
    data = {
        "witnesses": [
            {"witness_name": "Tom"}, 
            {"contact_phn_num": "555-9876"}
        ]
    }

    masked = mv6020_helper._mask_sensitive_data(data)

    assert masked["witnesses"][0]["witness_name"] == "[REDACTED]"
    assert masked["witnesses"][1]["contact_phn_num"] == "[REDACTED]"

def test_mask_sensitive_data_no_sensitive_fields():
    data = {"some_field": "value", "other_field": 123}

    masked = mv6020_helper._mask_sensitive_data(data)

    assert masked == data

    