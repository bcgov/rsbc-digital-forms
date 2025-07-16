import logging
import json
from datetime import datetime
from python.common.models import db, Submission
from python.common.enums import ErrorCode
from python.prohibition_web_svc.middleware import common_middleware

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
        #TODO: Add validation logic for the collision form payload
        return True, kwargs
    logging.warning("validation error: " + json.dumps(''))
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
        #TODO: Add Collision Data to submission
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

