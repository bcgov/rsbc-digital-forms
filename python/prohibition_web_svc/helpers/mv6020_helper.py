import logging
from typing import Tuple, Dict, Any
from datetime import datetime
import base64
import python.common.helper as helper
from python.prohibition_web_svc.config import Config
import python.common.rsi_email as rsi_email
from python.prohibition_web_svc.middleware import print_middleware


def send_mv6020_copy(**kwargs):
    logging.verbose('inside send_mv6020_copy')

    success, kwargs = print_middleware.set_event_type(**kwargs)
    if not success:
        return False, kwargs

    payload = kwargs.get('payload', {}) or {}
    data = payload.get('data', {}) or {}
    collision_case_no = data.get('collision_case_num')
    collision_date = helper.format_date_iso(data.get('date_collision'))

    print_options = data.get('print_options', {})
    ptype = print_options.get('type', '').lower()
    if ptype in ('icbc', 'police'):
        subject = f"Traffic Accident Report - Collision Case Number {collision_case_no}"
        full_name = "Officer"
        email_address = print_options.get('email', '')
    elif ptype == 'entity':
        subject = f"Traffic Accident Report Driver Copy - Collision Case Number {collision_case_no}"
        full_name, email_address = get_entity_data(data)
    else:
        subject = f"Traffic Accident Report - Collision Case Number {collision_case_no}"
  
    
    message = {
        "collision_case_number": collision_case_no,
        "collision_date": collision_date
    }

    # do the print orchestration here.
    success, print_result  = print_middleware.render_document_with_playwright(**kwargs)

    pdf_bytes = print_result.get("rendered_content")
    filename = print_result.get("filename") or "MV6020-{}.pdf".format(collision_case_no)
    content_type = print_result.get("content_type")

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


    success = rsi_email.send_mv6020_copy(
        config=Config,
        subject=subject,
        email_address=email_address,
        full_name=full_name,
        message=message,
        attachments=attachments,
        email_type=ptype
    )

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

    return "", ""  