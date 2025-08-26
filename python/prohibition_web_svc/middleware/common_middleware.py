import logging
from python.common.enums import ErrorCode
from python.common.error_middleware import record_error
from python.common.models import db, Submission

def log_payload_to_splunk(**kwargs) -> tuple:
    logging.debug('inside log_payload_to_splunk()')
    request = kwargs.get('request')
    # TODO - log to Splunk
    logging.debug(f"payload: | {request.get_data()}")
    return True, kwargs


def request_contains_a_payload(**kwargs) -> tuple:
    logging.debug("inside request_contains_a_payload()")
    request = kwargs.get('request')
    try:
        payload = request.get_json()
        kwargs['payload'] = payload
        logging.debug(f"payload: {payload}")
    except Exception as e:
        kwargs['error'] = {
            'error_code': ErrorCode.E01,
            'error_details': 'Invalid JSON payload',
            'ticket_no': None,
            'func': request_contains_a_payload,
        }
        kwargs['response_dict'] = {
            'error': 'bad request',
            'error_details': 'Invalid JSON payload'
        }
        return False, kwargs
    return payload is not None, kwargs


def check_if_application_id_exists(**kwargs) -> tuple:
    """
    Check if the application id exists in the database.
    """
    logging.debug('inside check_if_application_id_exists()')
    data = kwargs.get('payload')
    application_id = data.get('ff_application_id')
    event_type = kwargs.get('event_type', 'Unknown Event Type')
    ticket_no = kwargs.get('ticket_no', None)
    if application_id is None:
        return True, kwargs
    try:
        submission = db.session.query(Submission).filter(
            Submission.ff_application_id == application_id).first()
        if submission is not None:
            kwargs['error'] = {
                'error_code': ErrorCode.E09,
                'error_details': 'Application ID already exists',
                'submission_id': submission.submission_id,
                'event_type': event_type,
                'ticket_no': ticket_no,
                'func': check_if_application_id_exists,
            }
            return False, kwargs
    except Exception as e:
        logging.exception(e)
        kwargs['error'] = {
            'error_code': ErrorCode.G00,
            'error_details': str(e),
            'event_type': event_type,
            'ticket_no': ticket_no,
            'func': check_if_application_id_exists,
        }
        return False, kwargs
    return True, kwargs

def safe_get_value(data, default=None):
    """
    Safely extract the 'value' from a dictionary or handle other input types.
    
    Args:
        data (dict or str or None): Input data to extract value from
        default (Any, optional): Default value to return if no value found
    
    Returns:
        The extracted value or default
    """
    # If data is a dictionary, try to get the 'value' key
    if isinstance(data, dict):
        return data.get('value', default)
    
    # If data is an empty string, return default
    if data == "":
        return default
    
    # For None or other types, return default
    return data if data is not None else default    

def get_user_guid(**kwargs) -> tuple:
    logging.debug('inside get_user_guid()')
    data = kwargs.get('payload')
    if kwargs.get('identity_provider') == 'service_account':
       user_guid = data.get('submitted_user_guid', kwargs.get('username'))
    else:
       user_guid = kwargs.get('user_guid')
    logging.debug(f"user_guid: {user_guid}")
    return user_guid

def record_event_error(**kwargs):
    """
    Record an error that occurred during event processing.
    
    Args:
        **kwargs: Additional keyword arguments, including event_id and event_type.
    """   

    try:
        error = kwargs.get('error')

        if error is None:
            logging.warning("Error object is None")
            return
        record_error(**error)

    except Exception as e:
        # If recording the error itself fails, log it
        logging.error(f"Failed to record error: {str(e)}")
        return True, kwargs
    
    return True, kwargs