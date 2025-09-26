import logging
from typing import Tuple, Dict, Any
from python.common.enums import ErrorCode
from python.prohibition_web_svc.config import Config
import python.common.rsi_email as rsi_email
from python.prohibition_web_svc.helpers import mv6020_helper
from python.prohibition_web_svc.middleware import print_middleware

EVENT_TYPE = 'Notification Email'

def set_event_type(**kwargs) -> tuple:
    """Set the event type for the print event."""
    logging.verbose('inside set_event_type()')
    kwargs['event_type'] = EVENT_TYPE
    return True, kwargs


def send_new_user_admin_notification(**kwargs):
    subject = "Digital Forms: New User Application"
    body = "A new user has applied for access to Digital Forms:"
    message = {
        "first_name": kwargs.get('payload')['first_name'],
        "last_name": kwargs.get('payload')['last_name'],
        "badge_number": kwargs.get('payload')['badge_number'],
        "agency": kwargs.get('payload')['agency']['agency_name'],
        "admin_link": Config.REACT_APP_BASE_URL + "/admin-console",
    }

    rsi_email.send_new_user_admin_notification(config=Config, subject=subject, body=body, message=message)

    return True, kwargs

def send_admin_submission_failure_notification(**kwargs):
    application_id = kwargs.get('payload')['application_id']
    subject = f"Digital Forms: Application {application_id} – Submission Failed"
    message = {
        "form_id": kwargs.get('payload')['form_id'],
        "application_id": application_id,
        "submitted_date": kwargs.get('payload')['submitted_date'],
        "error_details": kwargs.get('payload')['error_details'],
        "application_link": kwargs.get('payload')['application_url'],
        "camunda_incident_link": kwargs.get('payload')['camunda_incident_url']
    }

    email_sent = rsi_email.send_admin_failure_notification(config=Config, subject=subject, message=message)

    if email_sent:
        kwargs['response_dict'] = {"message": "email sent successfully"}
        return True, kwargs

    return False, kwargs

def validate_email_payload(**kwargs) -> tuple:
    request = kwargs.get('request')
    if not request:
        kwargs['error'] = {
            'error_code': ErrorCode.P01,
            'error_details': "No request object found",
            'event_type': EVENT_TYPE,
            'func': validate_email_payload.__name__,
        }
        return False, kwargs
    try:
        # Get the JSON payload from the request
        if request.is_json:
            payload = request.get_json()

        # Validate required fields based on PrintRequestPayload model
        if 'template' not in payload or not payload['template']:
            logging.warning("validation error: missing or empty template")
            kwargs['error'] = {
                'error_code': ErrorCode.P01,
                'error_details': "Missing required field: template",
                'event_type': EVENT_TYPE,
                'func': validate_email_payload.__name__,
            }
            return False, kwargs
        
        # Set validate payload in kwargs
        kwargs['payload'] = payload
        template_name = payload['template']
        if template_name == "mv6020.html":
            #Reuse the validation logic in print middleware for now. Change later if needed.
            success, kwargs =  print_middleware.validate_print_payload(**kwargs)
            if not success:
                return False, kwargs
            
    except Exception as e:
        logging.warning(f"validation error: {str(e)}")
        kwargs['error'] = {
            'error_code': ErrorCode.P01,
            'error_details': f"Invalid JSON payload: {str(e)}",
            'event_type': EVENT_TYPE,
            'func': validate_email_payload.__name__,
        }
        return False, kwargs
    
    logging.debug("payload validation successful")
    return True, kwargs

# Do data structure validation

    
    
def send_email(**kwargs):
    payload = kwargs.get('payload', {})
    template_name = payload.get('template')

    if template_name == "mv6020.html":
        result, kwargs = mv6020_helper.send_mv6020_copy(**kwargs)
    elif template_name == "admin_notice_submission_failure.html":
        result, kwargs = send_admin_submission_failure_notification(**kwargs)    
    else:
        result = False
        kwargs = {"response_dict": {"message": "Unknown form type"}}
    
    return result, kwargs

