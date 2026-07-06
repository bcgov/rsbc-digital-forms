from typing import Tuple, Dict, Any
from datetime import datetime
import zoneinfo
import base64
from python.common.enums import ErrorCode
import python.common.helper as helper
from python.common.logging_utils import get_logger
from python.common.models import db, Agency,AgencyAdmin, User
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
        kwargs['ticket_no'] = collision_case_no  # for better error tracking
        raw_date = data.get("date_collision")  # ISO string
        raw_time = data.get("time_collision")  # "HH:MM"
        is_unknown = data.get("time_collision_unknown", False)
        formatted_date, formatted_time = format_collision_datetime(raw_date,raw_time,is_unknown)

        print_options = data.get('print_options', {})
        email_address = print_options.get('email', '')
        ptype = print_options.get('type', '').lower()

        if ptype != 'entity':
            # Map collision_type codes to labels
            COLLISION_TYPE_MAP = {
                "5": "Fatality",
                "3": "Personal Injury",
                "2": "Property Damage",
                "0": "Non-reportable"
            }

            collision_type_code = str(data.get("collision_type", "")).strip()
            collision_type = COLLISION_TYPE_MAP.get(collision_type_code, collision_type_code)

            prime_file_vjur = data.get("prime_file_vjur", {}).get("label", "")
            police_file_number = data.get("police_file_num", "")

            subject = (
                f"MV6020 - {collision_type} - {collision_case_no} - "
                f"{prime_file_vjur} - {police_file_number}"
            )

            if ptype == 'icbc':
                full_name = "ICBC"
            elif ptype == 'police':
                full_name = proper_case(data.get("completed_by_name"))  # defaults to "Officer"

        else:
            subject = f"Traffic Accident Report Driver Copy - Collision Case Number {collision_case_no}"
            full_name = get_entity_data(data)
  
        
        if ptype != 'admin' and ptype != 'all':
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
        elif ptype == 'admin':
            # admin copy
            kwargs['subject'] = subject
            return _send_admin_copy(**kwargs)
        elif ptype == 'all':
            kwargs['subject'] = subject
            return _send_all_copy(**kwargs)

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
    
def _send_admin_copy(**kwargs):
    logger.verbose('inside _send_admin_copy')

    success, kwargs = _get_user_data(**kwargs)
    if not success:
        return False, kwargs
    success, kwargs = _get_admin_emails(**kwargs)
    if not success:
        return False, kwargs
    email_address = kwargs.get('email_address')
    if not email_address:
        logger.info("No admin email found, skipping admin copy email sending.")
        kwargs['response_dict'] = {
            'message': 'No admin email found, skipping admin copy email sending.'
        }
        return True, kwargs  # Not a failure if there's no admin email configured
    
    success, kwargs = generate_all_PDF_attachments(**kwargs)
    if not success:
        return False, kwargs
    
    attachments = kwargs.get('attachments', [])
    payload = kwargs.get('payload', {}) or {}
    data = payload.get('data', {}) or {}
    collision_case_no = data.get('collision_case_num')
    submission_date = data.get('icbc_submission_date')
    raw_date = data.get("date_collision")  # ISO string
    raw_time = data.get("time_collision")  # "HH:MM"
    is_unknown = data.get("time_collision_unknown", False)
    formatted_date, formatted_time = format_collision_datetime(raw_date,raw_time,is_unknown)

    message = {
        "form_type": FORM_TYPE,
        "collision_case_number": collision_case_no,
        "agency_file_number": data.get("police_file_num", ""),
        "officer_name": kwargs.get('user_data', {}).get('display_name', ''),
        "officer_badge": kwargs.get('user_data', {}).get('badge_number', ''),
        "agency_name": kwargs.get('user_data', {}).get('agency_name', ''),
        "submission_date": helper.format_date_iso(submission_date, "%Y-%m-%d"),
        "collision_date": formatted_date,
        "collision_time": formatted_time,
    }
    subject = f"New {FORM_TYPE} form submitted - {collision_case_no}"

    success, kwargs = rsi_email.send_mv6020_copy(
        config=Config,
        subject=subject,
        email_address=email_address,
        message=message,
        attachments=attachments,
        email_type='admin'
    )
    if success:
        kwargs['response_dict'] = {
            'message': f'Successfully sent admin copy email to {email_address}'
        }
    return success, kwargs
    
def _send_all_copy(**kwargs):
    logger.verbose('inside _send_all_copy')

    success, kwargs = generate_all_PDF_attachments(**kwargs)
    if not success:
        return False, kwargs
    
    attachments = kwargs.get('attachments', [])
    payload = kwargs.get('payload', {}) or {}
    data = payload.get('data', {}) or {}
    collision_case_no = data.get('collision_case_num')
    raw_date = data.get("date_collision")  # ISO string
    raw_time = data.get("time_collision")  # "HH:MM"
    is_unknown = data.get("time_collision_unknown", False)
    formatted_date, formatted_time = format_collision_datetime(raw_date,raw_time,is_unknown)
    print_options = data.get('print_options', {})
    email_address = print_options.get('email', '')
    subject = kwargs.get('subject')

    message = {
        "collision_case_number": collision_case_no,
        "collision_date": formatted_date,
        "collision_time": formatted_time,
    }

    success = rsi_email.send_mv6020_copy(
        config=Config,
        subject=subject,
        email_address=email_address,
        full_name='',
        message=message,
        attachments=attachments,
        email_type='police'
    )

    if success:
        kwargs['response_dict'] = {
            'message': f'Successfully sent email to {email_address}'
        }
        return True, kwargs
    return success, kwargs

def generate_all_PDF_attachments(**kwargs):
    payload = kwargs.get('payload', {}) or {}
    data = payload.get('data', {}) or {}
    collision_case_no = data.get('collision_case_num')
    police_file_num = data.get('police_file_num')
    date_collision = helper.format_date_iso(data.get('date_collision'), '%Y%m%d')

    kwargs.get('payload', {}).get('data', {}).get('print_options', {})['type'] = 'police'
    kwargs.get('payload', {}).get('data', {}).get('print_options', {})['is_draft'] = False
    files = {}
    success, print_result  = print_middleware.render_document_with_playwright(**kwargs)
    if success:
        files['police'] = print_result
    else:
        logger.error(f"Failed to render document for admin copy: {print_result.get('error', {})}")
        kwargs['response_dict'] = {
            'message': f'Failed to render document for admin copy',
            'description': print_result.get('error', {})
        }
        kwargs["error"] = print_result.get("error", {})
        return False, kwargs

    entities = data.get("entities", [])
    kwargs.get('payload', {}).get('data', {}).get('print_options', {})['type'] = 'entity'
    for entity in entities:
        kwargs.get('payload', {}).get('data', {}).get('print_options', {})['entity_num'] = entity.get("entity_num")
        success, print_result  = print_middleware.render_document_with_playwright(**kwargs)
        if success:
            files[f"entity_{entity.get('entity_num')}"] = print_result
        else:
            logger.error(f"Failed to render document for entity {entity.get('entity_num')} in admin copy: {print_result.get('error', {})}")
            kwargs['response_dict'] = {
                'message': f'Failed to render document for entity {entity.get("entity_num")} in admin copy',
                'description': print_result.get('error', {})
            }
            kwargs["error"] = print_result.get("error", {})
            return False, kwargs
        
    attachments = []
    for key, result in files.items():
        pdf_bytes = result.get("rendered_content")
        filename = f"MV6020_{collision_case_no}_{police_file_num}_{date_collision}_{key}_Copy.pdf"

        if isinstance(pdf_bytes, str):
            pdf_bytes = pdf_bytes.encode("utf-8")

        pdf_b64 = base64.b64encode(pdf_bytes).decode("utf-8")  
        attachments.append(
            {
                "content": pdf_b64,
                "contentType": "application/pdf",
                "encoding": "base64",
                "filename": filename,
            }
        )

    kwargs['attachments'] = attachments
    return True, kwargs

def _get_user_data(**kwargs) -> tuple:
    logger.verbose('inside _get_user_data()')
    try:
        payload = kwargs.get('payload', {})
        data = payload.get('data', {})
        user_guid = data.get('completed_by_id') or payload.get('submitted_user_guid') or kwargs.get('user_guid')
        user_data = db.session.query(User) \
            .join(Agency, User.agency_id == Agency.id) \
            .filter(User.user_guid == user_guid).one()
        kwargs['user_data'] = {
            'user_guid': user_data.user_guid,
            'username': user_data.username,
            'agency_id': user_data.agency_id,
            'agency_name': user_data.agency_ref.agency_name,
            'display_name': user_data.display_name,
            'badge_number': user_data.badge_number
        }
    except Exception as e:
        logger.error(f'Error getting user data: {e}')
        kwargs['error'] = {
                'error_code': ErrorCode.G01,
                'error_details': e,
                'event_type': kwargs['event_type'],
                'func': _get_user_data,
                'ticket_no': kwargs.get('ticket_no')
            }
        return False, kwargs

    return True, kwargs

def _get_admin_emails(**kwargs) -> tuple:
    logger.verbose('inside _get_admin_email()')
    try:
        user_data = kwargs.get('user_data', {})
        agency_id = user_data.get('agency_id')
        agency_admins = db.session.query(AgencyAdmin) \
            .filter(AgencyAdmin.agency_id == agency_id) \
            .all()
        if len(agency_admins) == 0:
            logger.debug("No agency admin found for agency_id: {}".format(agency_id))
            kwargs['email_address'] = None
        else:
            emails = [admin.email for admin in agency_admins]
            kwargs['email_address'] = emails
    except Exception as e:
        logger.error(f'Error getting admin email: {e}')
        kwargs['error'] = {
                'error_code': ErrorCode.G01,
                'error_details': e,
                'event_type': kwargs['event_type'],
                'func': _get_admin_emails,
                'ticket_no': kwargs.get('ticket_no')
            }
        return False, kwargs

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
        return f"{given} {surname}".strip()

    return ""

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