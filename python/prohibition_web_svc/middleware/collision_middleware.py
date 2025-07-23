import logging
from datetime import datetime
from python.common.models import db, Submission
from python.common.enums import ErrorCode
from python.prohibition_web_svc.mappers.collision_mapper import CollisionMapper
from python.prohibition_web_svc.middleware import common_middleware
from python.prohibition_web_svc.models.collision_request_payload import CollisionRequestPayload

EVENT_TYPE = 'Collision - MV6020'

def set_event_type(**kwargs) -> tuple:
    """
    Set the event type for the collision event.
    """
    logging.debug('inside set_event_type()')
    kwargs['event_type'] = EVENT_TYPE
    return True, kwargs

def set_ticket_number(**kwargs) -> tuple:
    """
    Set the ticket number for the collision event.
    """
    logging.debug('inside set_ticket_number()')
    data = kwargs.get('payload')
    if data and 'collision_case_num' in data:
        kwargs['ticket_no'] = data['collision_case_num']
    else:
        kwargs['ticket_no'] = None
    return True, kwargs

def validate_collision_payload(**kwargs) -> tuple:
    logging.debug("inside validate_form_payload()")

    if(kwargs.get('payload')):
        collision: CollisionRequestPayload = kwargs['payload']
        is_valid = _validate_required_fields(collision, kwargs)
        return is_valid, kwargs
    logging.warning("validation error: empty payload")
    # Set error in kwargs to get consumed by the record_event_error function
    kwargs['error'] = {
        'error_code': ErrorCode.C01,
        'error_details': "Empty payload",
        'event_type': EVENT_TYPE,
        'ticket_no': None,
        'func': validate_collision_payload,
    }
    return False, kwargs

def save_collision_data(**kwargs) -> tuple:
    logging.debug('inside save_collision_data()')
    date_created = datetime.now()
    data = kwargs.get('payload')
    user_guid = common_middleware.get_user_guid(**kwargs)

    try:
        submission = Submission(
            ff_application_id=data.get('ff_application_id'),
            created_dt=date_created,
            updated_dt=date_created,
            created_by=user_guid,
            updated_by=user_guid,
        )
        collision: CollisionRequestPayload = kwargs['payload']
        # Add Collision Data to submission
        submission.collision = CollisionMapper.map_to_tar_collision(collision)

        db.session.add(submission)
        db.session.commit()

        logging.debug(f"Collision data saved with submission_id: {submission.submission_id}")
        kwargs['response_dict'] = {
            "message": "Collision created successfully",
            "submission_id": submission.submission_id
            }
    except Exception as e:
        logging.exception(e)
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
    kwargs['response_dict'] = {
        'message': 'Collision data saved successfully',
        'submission_id': submission.submission_id
    }
    kwargs['submission'] = submission
    return True, kwargs


def save_event_pdf(**kwargs) -> tuple:
    logging.debug('inside save_event_pdf()')    
    data = kwargs.get('payload')
    try:
        #TODO: generate the PDF and save it to Minio
        pass
    except Exception as e:
        logging.warning(str(e))
        # Set error in kwargs to get consumed by the record_event_error function
        kwargs['error'] = {
                'error_code': ErrorCode.E02,
                'error_details': e,
                'event_type': EVENT_TYPE,
                'ticket_no': data.get("collision_case_num"),
                'func': save_event_pdf,
            }
        return False, kwargs
    return True, kwargs


def _validate_required_fields(collision: CollisionRequestPayload, kwargs: dict) -> bool:
    is_valid = _validate_collision_required_fields(collision, kwargs) and \
        _validate_entity_required_fields(collision, kwargs) and \
        _validate_witness_required_fields(collision, kwargs)
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
        "police_agency_type_district",
        "police_agency_code",
        "primary_collision_occ_code",
        "first_contact_event",
        "first_contact_loc",
        "has_countable_fatal",
        "countable_fatal_total",
        "completed_by_name",
        "completed_by_id",
        "detachment_unit",
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
        "entities"
    ]

    missing_fields = [field for field in required_fields if field not in collision]
    if missing_fields:
        logging.info(f"Missing required fields: {missing_fields}")
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
        "damage_location_code",
        "severety_code",
    ]
    if not collision.get('entities') or len(collision.get('entities')) == 0:
        logging.info("Collision has no entities provided.")
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
            logging.info(f"Missing required fields in entity: {missing_fields}")
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

    if collision.get("has_witnesses") and (not collision.get('witnesses') or len(collision.get('witnesses')) == 0):
        logging.info("Collision has witnesses but no witness data provided.")
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
            logging.info(f"Missing required fields in witness: {missing_fields}")
            kwargs['error'] = {
                'error_code': ErrorCode.C01,
                'error_details': f"Missing required fields in witness: {missing_fields}",
                'event_type': EVENT_TYPE,
                'ticket_no': collision.get("collision_case_num"),
                'func': _validate_witness_required_fields,
            }
            return False
    return True