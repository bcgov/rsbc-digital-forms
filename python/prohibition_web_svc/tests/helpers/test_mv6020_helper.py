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

    success, result = mv6020_helper.send_mv6020_copy(**base_kwargs)
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
