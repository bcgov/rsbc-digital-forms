from dataclasses import asdict
from datetime import datetime
import json
import os
import uuid

from anyio import Path
from minio import Minio
from python.common.logging_utils import get_logger
from python.common.models import db, Submission, SubmissionFormRef, SubmissionEvent, TarCollision
from python.common.enums import ErrorCode
from python.prohibition_web_svc.business.cryptography_logic import encryptPdf_method1
from python.prohibition_web_svc.config import Config
from python.prohibition_web_svc.helpers import mv6020_helper
from python.prohibition_web_svc.mappers.collision_mapper import CollisionMapper
from python.prohibition_web_svc.middleware import common_middleware
from python.prohibition_web_svc.middleware.form_middleware import update_form_status
from python.prohibition_web_svc.middleware.print_middleware import render_with_playwright
from python.prohibition_web_svc.models.collision_request_payload import CollisionRequestPayload
import copy

logger = get_logger(__name__)

EVENT_TYPE = 'Collision - MV6020'
MV6020_FORM_TYPE = 'MV6020'

def set_event_type(**kwargs) -> tuple:
    """
    Set the event type for the collision event.
    """
    logger.verbose('inside set_event_type()')
    kwargs['event_type'] = EVENT_TYPE
    return True, kwargs

def set_ticket_number(**kwargs) -> tuple:
    """
    Set the ticket number for the collision event.
    """
    logger.verbose('inside set_ticket_number()')
    data = kwargs.get('payload')
    if data and 'collision_case_num' in data:
        kwargs['ticket_no'] = data['collision_case_num']
        logger.info(f"collision_case_num set to {kwargs['ticket_no']}")
    else:
        kwargs['ticket_no'] = None
    return True, kwargs

def check_if_case_number_exists(**kwargs) -> tuple:
    """
    Check if the case number exists in the database.
    """
    logger.verbose('inside check_if_case_number_exists()')
    case_number = kwargs.get('ticket_no')
    if case_number is None:
        return True, kwargs
    try:
        submission = db.session.query(TarCollision).filter(
            TarCollision.collision_case_num == case_number).first()
        if submission is not None:
            kwargs['error'] = {
                'error_code': ErrorCode.E09,
                'error_details': 'Collision case number already exists',
                'submission_id': submission.submission_id,
                'event_type': EVENT_TYPE,
                'ticket_no': case_number,
                'func': check_if_case_number_exists,
            }
            return False, kwargs
    except Exception as e:
        logger.error(e)
        kwargs['error'] = {
            'error_code': ErrorCode.G00,
            'error_details': str(e),
            'event_type': EVENT_TYPE,
            'ticket_no': case_number,
            'func': check_if_case_number_exists,
        }
        return False, kwargs
    return True, kwargs

def validate_collision_payload(**kwargs) -> tuple:
    logger.verbose("inside validate_form_payload()")

    is_valid = False
    if(kwargs.get('payload')):
        collision: CollisionRequestPayload = kwargs['payload']
        is_valid = _validate_required_fields(collision, kwargs)
    else:
        # Set error in kwargs to get consumed by the record_event_error function
        kwargs['error'] = {
            'error_code': ErrorCode.C01,
            'error_details': "Empty payload",
            'event_type': EVENT_TYPE,
            'ticket_no': None,
            'func': validate_collision_payload,
        }
    if not is_valid:
        kwargs['response_dict'] = {
            'error_details': kwargs.get('error', {}).get('error_details', None),
        }
    return is_valid, kwargs

def save_collision_data(**kwargs) -> tuple:
    logger.verbose('inside save_collision_data()')
    date_created = datetime.now()
    data = copy.deepcopy(kwargs.get('payload'))
    user_guid = common_middleware.get_user_guid(**kwargs)

    try:
        submission = Submission(
            ff_application_id=data.get('ff_application_id'),
            submitted_offline=data.get('submitted_offline', False),
            created_dt=date_created,
            updated_dt=date_created,
            created_by=user_guid,
            updated_by=user_guid,
        )
        collision: CollisionRequestPayload = data
        # Add Collision Data to submission
        submission.collision = CollisionMapper.map_to_tar_collision(collision)
        if not update_form_status(
            form_type=MV6020_FORM_TYPE,
            form_number=data.get('collision_case_num'),
            printed_timestamp=datetime.now(),
            user_guid=user_guid
        ):
            logger.error(f"Failed to update form status for form {data.get('collision_case_num')}")

        db.session.add(submission)
        db.session.commit()

        logger.info(f"Collision data saved with submission_id: {submission.submission_id}")
        kwargs['submission_id'] = submission.submission_id
        kwargs['response_dict'] = {
            'message': 'Collision data saved successfully',
            'submission_id': submission.submission_id
        }
    except Exception as e:
        logger.error(e)
        # Set error in kwargs to get consumed by the record_event_error function
        kwargs['error'] = {
            'error_code': ErrorCode.E01,
            'error_details': e,
            'event_id': None,
            'event_type': EVENT_TYPE,
            'ticket_no': data.get("collision_case_num"),
            'func': save_collision_data,
        }
        return False, kwargs

    return True, kwargs


def save_event_pdf(**kwargs) -> tuple:
    logger.verbose('inside save_event_pdf()')
    payload = kwargs.get('payload')
    data = {}
    data = copy.deepcopy(payload)
    data["print_options"] = {
        "type": "icbc",
        "is_draft": False
    }
    submission_id = kwargs.get('submission_id')
    collision_case_num = payload.get("collision_case_num")
    try:
        pdf_bytes=None
        current_dir = Path(__file__).parent.parent  # Go up to prohibition_web_svc directory
        template_path = current_dir / "templates" / "mv6020.html"        
        rendered_success, pdf_bytes = render_with_playwright(
            template_path=str(template_path),
            data=data,
        )
        if not rendered_success or pdf_bytes is None:
            raise Exception(f"Failed to render PDF with Playwright for collision case number {collision_case_num} error: {pdf_bytes}")
        
        encoded_file_name = _save_file_to_minio(pdf_bytes)
        
        storage_key = f'{Config.STORAGE_BUCKET_NAME}/{encoded_file_name}'
        form_ref = SubmissionFormRef(
            submission_id=submission_id,
            form_type=MV6020_FORM_TYPE,
            form_id=collision_case_num,
            form_version=data.get("form_version"),
            storage_key=storage_key,
        )
        form_ref.events = []  # Initialize events as an empty list
        event = SubmissionEvent(
            destination='ICBC',
        )
        form_ref.events.append(event)
        db.session.add(form_ref)
        db.session.commit()
        logger.info(f"PDF saved for submission {submission_id} with storage key: {storage_key}")
    except Exception as e:
        logger.error(e)
        # Set error in kwargs to get consumed by the record_event_error function
        kwargs['error'] = {
                'error_code': ErrorCode.C04,
                'error_details': e,
                'event_type': EVENT_TYPE,
                'ticket_no': collision_case_num,
                'func': save_event_pdf,
            }
        common_middleware.record_event_error(**kwargs)

    return True, kwargs


def _save_file_to_minio(pdf_bytes) -> str:
    cert_path = Config.MINIO_CERT_FILE
    os.environ['SSL_CERT_FILE'] = cert_path
    client = Minio(
        Config.MINIO_BUCKET_URL,
        access_key=Config.MINIO_AK,
        secret_key=Config.MINIO_SK,
        secure=Config.MINIO_SECURE,
    )
    filename = str(uuid.uuid4().hex)
    encoded_file_name = f"{filename}_encrypted.pdf"
    pdf_filename = f"/tmp/{filename}.pdf"
    encrypted_pdf_filename = f"/tmp/{encoded_file_name}"
    with open(pdf_filename, "wb") as file:
        file.write(pdf_bytes)
    encryptPdf_method1(
        pdf_filename, Config.ENCRYPT_KEY, encrypted_pdf_filename)
    logger.verbose('File encrypted')
    with open(encrypted_pdf_filename, 'rb') as file_data:
        client.fput_object(Config.STORAGE_BUCKET_NAME,
                        encoded_file_name, encrypted_pdf_filename)
    logger.verbose('File uploaded to Minio')

    return encoded_file_name

def _validate_required_fields(collision: CollisionRequestPayload, kwargs: dict) -> bool:
    is_valid = _validate_collision_required_fields(collision, kwargs) and \
        _validate_entity_required_fields(collision, kwargs) and \
        _validate_witness_required_fields(collision, kwargs) and \
        _validate_lki_fields(collision, kwargs)
    return is_valid

def _validate_collision_required_fields(collision: CollisionRequestPayload, kwargs: dict) -> bool:
    required_fields = [
        # Collision required fields
        "collision_case_num",
        "collision_scenario",
        "police_file_num",
        "prime_file_vjur",
        "date_collision",
        "time_collision",
        "reported_same_day",
        "time_collision_unknown",
        "date_reported",
        "hit_and_run",
        "police_attended",
        "police_agency_code",
        "primary_collision_occ_code",
        "first_contact_event",
        "first_contact_loc",
        "has_countable_fatal",
        "countable_fatal_total",
        "completed_by_name",
        "completed_by_id",
        "investigated_by_traffic_analyst",
        # Location required fields (from location.py)
        "hwy_code",
        "city_name",
        "lat_decim_degrees",
        "long_decim_degrees",
        "road_class",
        "traffic_flow",
        "collision_loc",
        "primary_speed_zone",
        "land_usage",
        "road_type",
        "roadway_character",
        "roadway_surface_cond",
        "weather_cond",
        "lighting_cond",
        # AdditionalCollisionDetails required fields (from additional_collision_details.py)
        "has_other_prop_damage",
        "has_witnesses",
        "collision_type",
        "total_est_damage",
        "total_injured",
        "total_killed",
        "total_vehicles",
        "summary_was_verified",
        # Entities and witnesses are handled separately
        "entities",
        "form_version"
    ]

    missing_fields = [field for field in required_fields if field not in collision]
    if missing_fields:
        logger.debug(f"Missing required fields: {missing_fields}")
        kwargs['error'] = {
            'error_code': ErrorCode.C01,
            'error_details': f"Missing required fields: {missing_fields}",
            'event_type': EVENT_TYPE,
            'ticket_no': collision.get("collision_case_num"),
            'func': _validate_required_fields,
        }
        return False
    return True

def _validate_entity_required_fields(collision: CollisionRequestPayload, kwargs: dict) -> bool:
    required_entity_fields = [
        "entity_type",
        "entity_num",
        "possible_offender",
        "contributing_factor_1",
        "contributing_factor_2",
        "contributing_factor_3",
        "contributing_factor_4",
    ]
    if not collision.get('entities') or len(collision.get('entities')) == 0:
        logger.debug("Collision has no entities provided.")
        kwargs['error'] = {
            'error_code': ErrorCode.C01,
            'error_details': "Collision has no entities provided.",
            'event_type': EVENT_TYPE,
            'ticket_no': collision.get("collision_case_num"),
            'func': _validate_entity_required_fields,
        }
        return False
    for entity in collision.get('entities', []):
        missing_fields = [field for field in required_entity_fields if not entity.get(field)]
        if missing_fields:
            logger.debug(f"Missing required fields in entity: {missing_fields}")
            kwargs['error'] = {
                'error_code': ErrorCode.C01,
                'error_details': f"Missing required fields in entity: {missing_fields}",
                'event_type': EVENT_TYPE,
                'ticket_no': collision.get("collision_case_num"),
                'func': _validate_entity_required_fields,
            }
            return False
    return True

def _validate_witness_required_fields(collision: CollisionRequestPayload, kwargs: dict) -> bool:
    required_witness_fields = [
        "witness_name",
        "address",
        "contact_phn_num"
    ]

    if collision.get("has_witnesses") and collision.get("has_witnesses").upper() == 'Y' and (not collision.get('witnesses') or len(collision.get('witnesses')) == 0):
        logger.debug("Collision has witnesses but no witness data provided.")
        kwargs['error'] = {
            'error_code': ErrorCode.C01,
            'error_details': "Collision has witnesses but no witness data provided.",
            'event_type': EVENT_TYPE,
            'ticket_no': collision.get("collision_case_num"),
            'func': _validate_witness_required_fields,
        }
        return False

    for witness in collision.get('witnesses', []):
        missing_fields = [field for field in required_witness_fields if not witness.get(field)]
        if missing_fields:
            logger.debug(f"Missing required fields in witness: {missing_fields}")
            kwargs['error'] = {
                'error_code': ErrorCode.C01,
                'error_details': f"Missing required fields in witness: {missing_fields}",
                'event_type': EVENT_TYPE,
                'ticket_no': collision.get("collision_case_num"),
                'func': _validate_witness_required_fields,
            }
            return False
    return True

def _validate_lki_fields(collision: CollisionRequestPayload, kwargs: dict) -> bool:
    if (collision.get('hwy_code') and str(collision['hwy_code']) == '1' and
        (not collision.get('hwy_route_num') or not collision.get('segment_num'))):
        logger.debug("For Hwy Code '1', both hwy_route_num and segment_num are required.")
        kwargs['error'] = {
            'error_code': ErrorCode.C01,
            'error_details': "For Hwy Code '1', both hwy_route_num and segment_num are required.",
            'event_type': EVENT_TYPE,
            'ticket_no': collision.get("collision_case_num"),
            'func': _validate_lki_fields,
        }
        return False
    return True

def get_collision_data(**kwargs) -> tuple:
    collision_case_num = kwargs.get('collision_case_num')
    logger.debug(f"Retrieving collision data for collision: {collision_case_num}")
    try:
        collision_data = db.session.query(TarCollision)\
                        .filter(TarCollision.collision_case_num == collision_case_num)\
                        .first()
        if not collision_data:
            kwargs['error'] = {
                'error_code': ErrorCode.C03,
                'error_details': f"Collision not found for case number: {collision_case_num}",
                'event_type': EVENT_TYPE,
                'ticket_no': collision_case_num,
                'func': get_collision_data,
            }
            return False, kwargs
        
        kwargs['response_dict'] = asdict(collision_data)
        location = asdict(collision_data.location) if collision_data.location else None
        kwargs['response_dict']['location'] = location
        additional_details = asdict(collision_data.additional_details) if collision_data.additional_details else None
        kwargs['response_dict']['additional_details'] = additional_details
        entities = [_load_entity(entity) for entity in collision_data.entities]
        kwargs['response_dict']['entities'] = entities
        witnesses = [asdict(witness) for witness in collision_data.witnesses]
        kwargs['response_dict']['witnesses'] = witnesses
        return True, kwargs
    except Exception as e:
        logger.error(e)
        kwargs['error'] = {
            'error_code': ErrorCode.C02,
            'error_details': str(e),
            'event_type': EVENT_TYPE,
            'ticket_no': collision_case_num,
            'func': get_collision_data,
        }
        return False, kwargs

def _load_entity(entity):
    entity_dict = asdict(entity)
    charges = entity.charges if entity.charges else []
    entity_dict['charges'] = [asdict(charge) for charge in charges]
    involved_persons = entity.involved_persons if entity.involved_persons else []
    entity_dict['involved_persons'] = [asdict(person) for person in involved_persons]
    return entity_dict

def log_payload_to_splunk(**kwargs) -> tuple:
    try:
        request = kwargs.get('request')
        payload = request.get_json()
        payload = copy.deepcopy(payload)
        payload_masked = mv6020_helper.mask_collision_sensitive_data(payload)
        kwargs['splunk_data'] = {
            'event': "create collision",
            'request_id': kwargs.get('request_id', ''),
            'user_guid': kwargs.get('user_guid', ''),
            'username': kwargs.get('username'),
            'form_type': MV6020_FORM_TYPE,
            'payload': payload_masked
        }
    except Exception as e:
        logger.error(e)
    return True, kwargs

def log_get_collision_to_splunk(**kwargs) -> tuple:
    kwargs['splunk_data'] = {
        'event': "get collision",
        'request_id': kwargs.get('request_id', ''),
        'user_guid': kwargs.get('user_guid'),
        'username': kwargs.get('username'),
        'form_type': MV6020_FORM_TYPE,
        'collision_case_number': kwargs.get('collision_case_num')
    }
    return True, kwargs