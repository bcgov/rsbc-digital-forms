import pytest
from unittest.mock import MagicMock, patch

from python.prohibition_web_svc.middleware import notification_middleware

class MockRequest:
    """Mock request object for testing."""
    def __init__(self, json_data=None, data=None):
        self._json = json_data
        self._data = data
        self.json = json_data
        self.is_json = True 

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

def test_validate_email_payload_no_request():
    # Arrange: kwargs without 'request'
    kwargs = {}

    # Act
    result, returned_kwargs = notification_middleware.validate_email_payload(**kwargs)

    # Assert
    assert result is False
    assert "error" in returned_kwargs
    error = returned_kwargs["error"]
    assert error["error_code"] == notification_middleware.ErrorCode.N01
    assert error["error_details"] == "No request object found"
    assert error["func"] == "validate_email_payload"
    assert error["event_type"] == notification_middleware.EVENT_TYPE 

def test_validate_email_payload_request_is_json_false():
    # Arrange
    payload = {"template": "generic.html", "data": {"field": "value"}}
    
    class MockRequest:
        def __init__(self, json_data):
            self._json = json_data
            self.is_json = False  # triggers the False branch

        def get_json(self):
            return self._json

    request = MockRequest(json_data=payload)
    kwargs = {"request": request}

    # Act
    result, returned_kwargs = notification_middleware.validate_email_payload(**kwargs)

    # Assert
    # Even though payload won't be assigned in the 'if request.is_json' block,
    # the function will eventually fail on 'if not isinstance(payload, dict):'
    # so we need to handle that.
    assert result is False
    assert "error" in returned_kwargs
    assert "Invalid JSON payload" in returned_kwargs["error"]["error_details"]

def test_validate_email_payload_payload_not_dict():
    # Arrange: MockRequest with JSON that is not a dict
    class MockRequest:
        def __init__(self):
            self.is_json = True  # triggers 'if request.is_json:'
        
        def get_json(self):
            return "this is a string, not a dict"

    request = MockRequest()
    kwargs = {"request": request}

    # Act
    result, returned_kwargs = notification_middleware.validate_email_payload(**kwargs)

    # Assert
    assert result is False
    assert "error" in returned_kwargs
    error = returned_kwargs["error"]
    assert error["error_code"] == notification_middleware.ErrorCode.N01
    assert "Payload must be a JSON object" in error["error_details"]

def test_validate_email_payload_exception_handling():
    # Arrange: MockRequest where get_json raises an exception
    class MockRequest:
        def __init__(self):
            self.is_json = True

        def get_json(self):
            raise ValueError("forced exception for testing")

    request = MockRequest()
    kwargs = {"request": request}

    # Act
    result, returned_kwargs = notification_middleware.validate_email_payload(**kwargs)

    # Assert
    assert result is False
    assert "error" in returned_kwargs
    error = returned_kwargs["error"]
    assert error["error_code"] == notification_middleware.ErrorCode.N01
    assert "Invalid JSON payload" in error["error_details"]
    assert "forced exception for testing" in error["error_details"]
    assert error["func"] == "validate_email_payload"
    assert error["event_type"] == notification_middleware.EVENT_TYPE    

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

def test_log_payload_to_splunk_mv6020():
    # Arrange
    payload = {"template": "mv6020.html", "data": {"vehicle_owner_name": "John Doe"}}
    request = MockRequest(json_data=payload)

    with patch("python.prohibition_web_svc.middleware.notification_middleware.mv6020_helper._mask_sensitive_data",
               return_value={"vehicle_owner_name": "[REDACTED]"}):
        result, kwargs = notification_middleware.log_payload_to_splunk(
            request=request, user_guid="guid123", username="tester"
        )

    # Assert
    assert result is True
    splunk_data = kwargs["splunk_data"]
    assert splunk_data["form_type"] == notification_middleware.MV6020_FORM_TYPE
    assert splunk_data["user_guid"] == "guid123"
    assert splunk_data["username"] == "tester"
    assert splunk_data["payload"]["data"] == {"vehicle_owner_name": "[REDACTED]"} 

def test_log_payload_to_splunk_generic_template():
    # Arrange
    payload = {"template": "other_form.html", "form_id": "GENERIC123", "data": {"field": "value"}}
    request = MockRequest(json_data=payload)

    result, kwargs = notification_middleware.log_payload_to_splunk(
        request=request, user_guid="guid456", username="tester2"
    )

    # Assert
    assert result is True
    splunk_data = kwargs["splunk_data"]
    assert splunk_data["form_type"] == "GENERIC123"  # pulled from form_id
    assert splunk_data["user_guid"] == "guid456"
    assert splunk_data["username"] == "tester2"
    assert splunk_data["payload"]["data"] == {"field": "value"}      

def test_log_payload_to_splunk_fallback_template():
    payload = {"template": "no_formid.html", "data": {"field": "value"}}
    request = MockRequest(json_data=payload)

    result, kwargs = notification_middleware.log_payload_to_splunk(
        request=request, username="tester3"
    )

    splunk_data = kwargs["splunk_data"]
    assert splunk_data["form_type"] == "no_formid.html"   

def test_send_admin_submission_failure_notification_success():
    payload = {
        "application_id": "APP123",
        "form_id": "FORM456",
        "submitted_date": "2025-10-01",
        "error_details": "Some error",
        "application_url": "https://app.link",
        "camunda_incident_url": "https://camunda.link"
    }
    kwargs = {"payload": payload}

    with patch("python.prohibition_web_svc.middleware.notification_middleware.rsi_email.send_admin_failure_notification",
               return_value=True) as mock_email:
        result, returned_kwargs = notification_middleware.send_admin_submission_failure_notification(**kwargs)

    # Assertions
    assert result is True
    assert "response_dict" in returned_kwargs
    assert returned_kwargs["response_dict"]["message"] == "email sent successfully"

    # Check that email was called with correct subject and message
    expected_subject = f"Digital Forms: Application {payload['application_id']} – Submission Failed"
    expected_message = {
        "form_id": payload["form_id"],
        "application_id": payload["application_id"],
        "submitted_date": payload["submitted_date"],
        "error_details": payload["error_details"],
        "application_link": payload["application_url"],
        "camunda_incident_link": payload["camunda_incident_url"]
    }
    mock_email.assert_called_once_with(config=notification_middleware.Config,
                                       subject=expected_subject,
                                       message=expected_message)   
    
def test_send_email_admin_notice_submission_failure():
    # Arrange
    payload = {
        "template": "admin_notice_submission_failure.html",
        "application_id": "APP123",
        "form_id": "FORM456",
        "submitted_date": "2025-10-01",
        "error_details": "Some error",
        "application_url": "https://app.link",
        "camunda_incident_url": "https://camunda.link"
    }
    kwargs = {"payload": payload}

    # Patch the send_admin_submission_failure_notification function
    with patch("python.prohibition_web_svc.middleware.notification_middleware.send_admin_submission_failure_notification",
               return_value=(True, {"payload": payload, "response_dict": {"message": "email sent successfully"}})) as mock_func:
        
        # Act
        result, returned_kwargs = notification_middleware.send_email(**kwargs)

    # Assert
    assert result is True
    assert "response_dict" in returned_kwargs
    assert returned_kwargs["response_dict"]["message"] == "email sent successfully"
    
    # Ensure the patched function was called once with the same kwargs
    mock_func.assert_called_once_with(**kwargs)    

def test_send_admin_submission_failure_notification_failure():
    payload = {
        "application_id": "APP123",
        "form_id": "FORM456",
        "submitted_date": "2025-10-01",
        "error_details": "Some error",
        "application_url": "https://app.link",
        "camunda_incident_url": "https://camunda.link"
    }
    kwargs = {"payload": payload}

    with patch("python.prohibition_web_svc.middleware.notification_middleware.rsi_email.send_admin_failure_notification",
               return_value=False):
        result, returned_kwargs = notification_middleware.send_admin_submission_failure_notification(**kwargs)

    # Assertions
    assert result is False
    assert "response_dict" not in returned_kwargs      
