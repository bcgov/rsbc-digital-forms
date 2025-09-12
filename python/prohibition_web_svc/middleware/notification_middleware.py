import logging
from typing import Tuple, Dict, Any
from datetime import datetime
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

def send_mv6020_entity_copy(**kwargs):
    logging.verbose('inside send_mv6020_entity_copy()')
    # do the print orchestration here.
    # print()
    print("Payload:", kwargs.get('payload'))
    payload = kwargs.get('payload', {}) or {}
    data = payload.get('data', {}) or {}
    collision_case_no = data.get('collision_case_num')
    date_str = data.get('date_collision')  # e.g. "2025-08-22T00:00:00-07:00"
    collision_date = None

    if date_str:
        try:
            # parse ISO 8601 string into datetime (Python 3.7+)
            dt = datetime.fromisoformat(date_str)
            collision_date = dt.strftime("%B %d, %Y %H:%M")
        except ValueError:
            collision_date = date_str
    #collision_date=data.get('date_collision').strftime("%B %d, %Y %H:%M"),
    print("Collision Num:", collision_case_no)
    subject = "Traffic Accident Report Copy Attached - Collision Case Number {}".format(collision_case_no)
    body = "Collision Report Attached"
    full_name, email_address = get_entity_data(data)
    message = {
        "collision_case_number": collision_case_no,
        "collision_date": collision_date
    }
   

    rsi_email.send_mv6020_entity_copy(
        config=Config, subject=subject, body=body, email_address=email_address, full_name=full_name,message=message)
    
    kwargs['response_dict'] = {'message': f'successfully sent email to entity'}

    return True, kwargs


def get_entity_data(data: dict) -> Tuple[str, Dict[str, Any]]:
    entities = data.get("entities", [])
    selected_num = data.get("print_options", {}).get("entity_num")

    # find entity by matching entity_num
    recipient = next(
        (e for e in entities if e.get("entity_num") == selected_num),
        None
    )

    if recipient:
        given = recipient.get("given_name", "").strip()
        surname = recipient.get("surname", "").strip()
        email_address = recipient.get("email_address", "").strip()
        return f"{given} {surname}".strip(), email_address

    return ""  # fallback if no match found
