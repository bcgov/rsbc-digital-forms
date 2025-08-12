from python.prohibition_web_svc.config import Config
import python.common.rsi_email as rsi_email


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
