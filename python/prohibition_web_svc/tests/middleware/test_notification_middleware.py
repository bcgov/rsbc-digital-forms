import pytest
from unittest.mock import MagicMock, patch

from python.prohibition_web_svc.middleware import notification_middleware

class MockRequest:
    """Mock request object for testing."""
    def __init__(self, json_data=None, data=None):
        self._json = json_data
        self._data = data
        self.json = json_data

    def get_json(self):
        if isinstance(self._json, Exception):
            raise self._json
        return self._json

    def get_data(self):
        return self._data

def test_set_event_type():
    result, kwargs = notification_middleware.set_event_type()
    assert result is True
    assert kwargs['event_type'] == notification_middleware.EVENT_TYPE


def test_send_new_user_admin_notification_calls_rsi_email():
    kwargs = {
        "payload": {
            "first_name": "John",
            "last_name": "Doe",
            "badge_number": "123",
            "agency": {"agency_name": "RCMP"},
        }
    }

    with patch("python.prohibition_web_svc.middleware.notification_middleware.rsi_email.send_new_user_admin_notification") as mock_send:
        result, updated_kwargs = notification_middleware.send_new_user_admin_notification(**kwargs)

    # Assertions
    assert result is True
    assert updated_kwargs == kwargs
    mock_send.assert_called_once()
    called_args, called_kwargs = mock_send.call_args
    assert called_kwargs["config"] == notification_middleware.Config
    assert "Digital Forms: New User Application" in called_kwargs["subject"]
    assert "A new user has applied" in called_kwargs["body"]
    assert called_kwargs["message"]["first_name"] == "John"
    assert "admin-console" in called_kwargs["message"]["admin_link"]


def test_validate_mv6020_email_payload_success():
    request = MockRequest(json_data={"template": "mv6020.html","data": {}})
    patched_kwargs = {"request": request} 
    with patch("python.prohibition_web_svc.middleware.notification_middleware.print_middleware.validate_print_payload", return_value=(True, patched_kwargs)):
        result, kwargs = notification_middleware.validate_email_payload(request=request)
    assert result is True
    assert kwargs['request'] == request


def test_validate_email_payload_failure():
    request = MockRequest(json_data={})
    patched_kwargs = {"request": request} 
    with patch("python.prohibition_web_svc.middleware.notification_middleware.print_middleware.validate_print_payload", return_value=(False, patched_kwargs)):
        result, kwargs  = notification_middleware.validate_email_payload(request=request)
    assert result is False
    assert kwargs['request'] == request


def test_send_email_with_mv6020_template():
    kwargs = {"payload": {"template": "mv6020.html"}}
    with patch("python.prohibition_web_svc.middleware.notification_middleware.mv6020_helper.send_mv6020_copy", return_value=(True, kwargs)) as mock_send:
        result, updated_kwargs = notification_middleware.send_email(**kwargs)

    assert result is True
    assert updated_kwargs == kwargs
    mock_send.assert_called_once_with(**kwargs)


def test_send_email_with_unknown_template():
    kwargs = {"payload": {"template": "unknown.html"}}
    result, updated_kwargs = notification_middleware.send_email(**kwargs)
    assert result is False
    assert "Unknown form type" in updated_kwargs["response_dict"]["message"]
