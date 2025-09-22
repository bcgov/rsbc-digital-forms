import logging
from typing import Tuple, Dict, Any
from python.prohibition_web_svc.config import Config
import python.common.rsi_email as rsi_email
from python.prohibition_web_svc.helpers import mv6020_helper
from python.prohibition_web_svc.middleware import print_middleware


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

# Do data structure validation
def validate_email_payload(**kwargs) -> tuple:
    #Reuse the validation logic in print middleware for now. Change later if needed.
    success, kwargs = print_middleware.validate_print_payload(**kwargs)
    if not success:
        return False, kwargs
    return True, kwargs
    
def send_email(**kwargs):
    payload = kwargs.get('payload', {})
    template_name = payload.get('template')

    if template_name == "mv6020.html":
        result, kwargs = mv6020_helper.send_mv6020_copy(**kwargs)
    else:
        result = False
        kwargs = {"response_dict": {"message": "Unknown form type"}}
    
    return result, kwargs

