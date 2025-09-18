import logging
from typing import Tuple, Dict, Any
from datetime import datetime
import base64
from python.prohibition_web_svc.config import Config
import python.common.rsi_email as rsi_email
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

def send_mv6020_entity_copy(**kwargs):
    logging.verbose('inside send_mv6020_entity_copy()')

    payload = kwargs.get('payload', {}) or {}
    data = payload.get('data', {}) or {}
    collision_case_no = data.get('collision_case_num')
    date_str = data.get('date_collision')
    collision_date = None

    if date_str:
        try:
            # parse ISO 8601 string into datetime (Python 3.7+)
            dt = datetime.fromisoformat(date_str)
            collision_date = dt.strftime("%B %d, %Y")
        except ValueError:
            collision_date = date_str
    #collision_date=data.get('date_collision').strftime("%B %d, %Y %H:%M"),
    subject = "Traffic Accident Report Driver Copy - Collision Case Number {}".format(collision_case_no)
    full_name, email_address = get_entity_data(data)
    message = {
        "collision_case_number": collision_case_no,
        "collision_date": collision_date
    }

    # do the print orchestration here.
    success, print_result  = print_middleware.render_document_with_playwright(**kwargs)

    pdf_bytes = print_result.get("rendered_content")
    filename = print_result.get("filename") or "MV6020-{}.pdf".format(collision_case_no)
    content_type = print_result.get("content_type")
    
    print("filename:", filename)
    #print("pdf_bytes:", pdf_bytes)
    print("content_type:", content_type)

    #Attach PDF if provided
    if pdf_bytes and content_type == "application/pdf":
        if isinstance(pdf_bytes, str):
            pdf_bytes = pdf_bytes.encode("utf-8")

        pdf_b64 = base64.b64encode(pdf_bytes).decode("utf-8")  
        attachments = [
            {
                "content": pdf_b64,
                "contentType": "application/pdf",
                "encoding": "base64",
                "filename": filename or "MV6020.pdf",
            }
        ]  


    success = rsi_email.send_mv6020_entity_copy(
        config=Config,
        subject=subject,
        email_address=email_address,
        full_name=full_name,
        message=message,
        attachments=attachments
    )

    #,attachments=attachments

    print("response from email: ",success)

    if success:
        kwargs['response_dict'] = {
            'message': f'Successfully sent email to {full_name} at {email_address}'
        }
        return True, kwargs
    else:
        kwargs['response_dict'] = {
            'message': f'Failed to send email to {full_name} at {email_address}'
        }
        return False, kwargs


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
