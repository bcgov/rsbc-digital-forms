import copy
from python.common.enums import ErrorCode
from python.common.logging_utils import get_logger
from python.prohibition_web_svc.config import Config
import python.common.rsi_email as rsi_email
from python.prohibition_web_svc.helpers import mv6020_helper
from python.prohibition_web_svc.middleware import collision_middleware, print_middleware

logger = get_logger(__name__)

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
    data = payload.get('data', {}) or {}
    collision_case_no = data.get('collision_case_num')

    if template_name == "mv6020.html":
        try:
            result, kwargs = mv6020_helper.send_mv6020_copy(**kwargs)
        except Exception as e:
            logger.error(f"Error sending MV6020 email: {e}")
            result = False
            kwargs["error"] = {
                'error_code': ErrorCode.G01,
                'error_details': 'Error sending MV6020 email',
                'ticket_no': collision_case_no,
                'func': send_email,
            }
            kwargs["response_dict"] = {"message": "Error sending MV6020 email"}
    else:
        result = False
        kwargs["response_dict"] = {"message": "Unknown form type"}

    return result, kwargs


def log_payload_to_splunk(**kwargs) -> tuple:
    try:
        request = kwargs.get('request')
        payload = request.get_json()
        payload = copy.deepcopy(payload)
        payload_masked = collision_middleware.mask_sensitive_data(payload)
        kwargs['splunk_data'] = {
            'event': 'send email',
            'request_id': kwargs.get('request_id', ''),
            'user_guid': kwargs.get('user_guid', ''),
            'username': kwargs.get('username', ''),
            'payload': payload_masked
        }
    except Exception as e:
        logger.error(e)
    return True, kwargs