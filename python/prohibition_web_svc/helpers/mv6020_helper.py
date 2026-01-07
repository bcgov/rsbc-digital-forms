from typing import Tuple, Dict, Any
from datetime import datetime
import zoneinfo
import base64
from python.common.enums import ErrorCode
import python.common.helper as helper
from python.common.logging_utils import get_logger
from python.prohibition_web_svc.config import Config
import python.common.rsi_email as rsi_email
from python.prohibition_web_svc.middleware import print_middleware

logger = get_logger(__name__)

# constants for mv6020. move to enums.
FORM_TYPE = 'MV6020'
EMAIL_TEMPLATE = 'mv6020.html'
PACIFIC = zoneinfo.ZoneInfo("America/Vancouver")

def send_mv6020_copy(**kwargs):
    logger.verbose('inside send_mv6020_copy')

    try:
        success, kwargs = print_middleware.set_event_type(**kwargs)
        if not success:
            return False, kwargs

        payload = kwargs.get('payload', {}) or {}
        data = payload.get('data', {}) or {}
        collision_case_no = data.get('collision_case_num')
        #collision_date = helper.format_date_iso(data.get('date_collision'))
        raw_date = data.get("date_collision")  # ISO string
        raw_time = data.get("time_collision")  # "HH:MM"
        is_unknown = data.get("time_collision_unknown", False)
        formatted_date, formatted_time = format_collision_datetime(raw_date,raw_time,is_unknown)

        print_options = data.get('print_options', {})
        ptype = print_options.get('type', '').lower()
        if ptype == 'icbc' or ptype == 'police':

            # Map collision_type codes to labels
            COLLISION_TYPE_MAP = {
                "5": "Fatality",
                "3": "Personal Injury",
                "2": "Property Damage",
            }

            collision_type_code = str(data.get("collision_type", "")).strip()
            collision_type = COLLISION_TYPE_MAP.get(collision_type_code, collision_type_code)

            prime_file_vjur = data.get("prime_file_vjur", {}).get("label", "")
            police_file_number = data.get("police_file_num", "")

            subject = (
                f"MV6020 - {collision_type} - {collision_case_no} - "
                f"{prime_file_vjur} - {police_file_number}"
            )

            
            email_address = print_options.get('email', '')

            if ptype == 'icbc':
                full_name = "ICBC"
            else:
                full_name = proper_case(data.get("completed_by_name"))  # defaults to "Officer"

        elif ptype == 'entity':
            subject = f"Traffic Accident Report Driver Copy - Collision Case Number {collision_case_no}"
            full_name, email_address = get_entity_data(data)
            # Fallback: use email from print_options if entity email is missing or empty
            if not email_address:
                email_address = print_options.get('email', '')
        else:
            kwargs['error'] = {
                'error_code': ErrorCode.G01,
                'error_details': 'Unknown message type found in print options',
                'ticket_no': collision_case_no,
                'func': send_mv6020_copy,
            }
            kwargs['response_dict'] = {
                'message': 'Failed to send email',
                'description': 'Unknown message type found in print options' 
            }
            return False, kwargs
    
        
        message = {
            "collision_case_number": collision_case_no,
            "collision_date": formatted_date,
            "collision_time": formatted_time,
        }

        # do the print orchestration here.
        success, print_result  = print_middleware.render_document_with_playwright(**kwargs)

        if success:
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
        
        kwargs['response_dict'] = {
            'message': f'Failed to send email to {full_name} at {email_address}'
        }
        kwargs["error"] = print_result.get("error", {})
        return False, kwargs
    except Exception as e:
        logger.error(f"Exception in send_mv6020_copy: {e}")
        kwargs['error'] = {
            'error_code': ErrorCode.G01,
            'error_details': str(e),
            'ticket_no': collision_case_no,
            'func': send_mv6020_copy,
        }
        kwargs['response_dict'] = {
            'message': 'Failed to send email',
            'description': str(e)
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

def mask_collision_sensitive_data(data):
    sensitive_fields = [
        'driver_license_num',
        'surname',
        'given_name',
        'contact_phone_num',
        'vehicle_plate_num',
        'vehicle_owner_name',
        'vehicle_owner_address',
        'nsc_num',
        'other_insurance_policy_num',
        'witness_name',
        'address',
        'contact_phn_num'
    ]
    for field in sensitive_fields:
        if field in data:
            data[field] = "[REDACTED]"
        if 'entities' in data:
            data['entities'] = [
                mask_collision_sensitive_data(entity) for entity in data['entities']
            ]
        if 'involved_persons' in data:
            data['involved_persons'] = [
                mask_collision_sensitive_data(person) for person in data['involved_persons']
            ]
        if 'witnesses' in data:
            data['witnesses'] = [
                mask_collision_sensitive_data(witness) for witness in data['witnesses']
            ]
        if 'data' in data and isinstance(data['data'], dict):
            data['data'] = mask_collision_sensitive_data(data['data'])            
    return data

def proper_case(name: str, default="Officer") -> str:
    """
    Converts ALL CAPS or mixed-case names to Proper Case.
    Example: 'JOHN DOE' → 'John Doe'
    """
    if not name or not name.strip():
        return default

    return name.strip().title()



def format_collision_datetime(date_str: str, time_str: str, is_unknown: bool):
    """
    Safely reconstructs collision datetime in BC local time (PST/PDT).
    Handles:
      - Split date/time inputs
      - Unknown time (27:00)
      - Avoids UTC rollover bugs
      - Works on Windows + Linux/OSX
    """
    # Extract date portion only → "YYYY-MM-DD"
    date_only = date_str[:10]

    # Parse as date, then assign Pacific timezone
    date_obj = datetime.strptime(date_only, "%Y-%m-%d").replace(tzinfo=PACIFIC)

    # Format date safely (“November 19, 2025”)
    date_fmt = date_obj.strftime("%B %d, %Y").replace(" 0", " ")

    # If time is unknown, stop here
    if is_unknown:
        return date_fmt, "(Time Unknown)"

    try:
        hour, minute = map(int, time_str.split(":"))
        dt = date_obj.replace(hour=hour, minute=minute)

        time_fmt = dt.strftime("%I:%M %p").lstrip("0")
        return date_fmt, time_fmt

    except Exception:
        # If something is malformed
        return date_fmt, time_str