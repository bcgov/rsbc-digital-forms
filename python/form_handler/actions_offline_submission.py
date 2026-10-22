import json
import logging

from python.common.enums import ErrorCode
from python.common.error_middleware import record_error
from python.common.models import FormsflowOfflineSubmission
from python.form_handler.rsi_email import send_error_to_rsiops
from python.form_handler.message import encode_message

def set_offline_submission_id(**args):
  logging.verbose("Setting offline submission ID")
  message = args.get('message', {})
  submission_id = message.get("id")

  if not submission_id:
    args['error'] = {
        'error_code': ErrorCode.O03,
        'error_details': ErrorCode.O03.description,
        'event_id': None,
        'event_type': 'offline_submission',
        'submission_id': submission_id,
        'payload': json.dumps(message) if message else None,
        'func': set_offline_submission_id,
    }
    return False, args

  args['offline_submission_id'] = message.get("id")
  return True, args

def get_offline_submission_data(**args):
    logging.verbose("Getting offline submission data")
    application = args.get('app')
    db = args.get('db')
    message = args.get('message', {})
    submission_id = args.get('offline_submission_id')

    try:
        with application.app_context():
            submission_data = db.session.query(FormsflowOfflineSubmission).filter_by(id=submission_id).first()
 
        args['submission_data'] = submission_data.__dict__ if submission_data else None
    except Exception:
        logging.error('Error while getting offline submission data')
        args['error'] = {
            'error_code': ErrorCode.O02,
            'error_details': ErrorCode.O02.description,
            'event_id': None,
            'event_type': 'offline_submission',
            'submission_id': submission_id,
            'payload': json.dumps(message) if message else None,
            'func': get_offline_submission_data,
        }
        return False, args
    
    return True, args

def validate_offline_submission_data(**args):
    logging.verbose("Validating offline submission data")
    submission_id = args.get('offline_submission_id')
    submission_data = args.get('submission_data')
    message = args.get('message')
    invalid_submission_error = {
        'error_code': ErrorCode.O04,
        'error_details': ErrorCode.O04.description,
        'event_id': None,
        'event_type': 'offline_submission',
        'submission_id': submission_id,
        'payload': json.dumps(message) if message else None,
        'func': validate_offline_submission_data,
    }

    if not submission_data \
        or 'form_id' not in submission_data or not submission_data['form_id'] \
        or 'payload' not in submission_data or not submission_data['payload']:
        args['error'] = invalid_submission_error
        return False, args

    payload = submission_data['payload'].get('data') if 'data' in submission_data['payload'] else None
    if not payload:
        args['error'] = invalid_submission_error
        return False, args

    return True, args

def update_status_processing(**args):
    logging.verbose("Updating status to processing")
    try:
        application = args.get('app')
        db = args.get('db')
        submission_id = args.get('offline_submission_id')
        _update_status(submission_id, 'processing', application, db)
        return True, args
    except Exception as e:
        logging.exception(e)
        args['error'] = {
            'error_code': ErrorCode.O01,
            'error_details': ErrorCode.O01.description,
            'event_id': None,
            'event_type': 'offline_submission',
            'submission_id': submission_id,
            'payload': json.dumps(args.get('message')) if args.get('message') else None,
            'func': update_status_processing,
        }
        return False, args

def update_status_completed(**args):
    logging.verbose("Updating status to completed")
    try:
        application = args.get('app')
        db = args.get('db')
        submission_id = args.get('offline_submission_id')
        _update_status(submission_id, 'completed', application, db)
        return True, args
    except Exception as e:
        logging.exception(e)
        args['error'] = {
            'error_code': ErrorCode.O01,
            'error_details': ErrorCode.O01.description,
            'event_id': None,
            'event_type': 'offline_submission',
            'submission_id': submission_id,
            'payload': json.dumps(args.get('message')) if args.get('message') else None,
            'func': update_status_completed,
        }
        return False, args        

def _update_status(submission_id, status, app, db):
    with app.app_context():
        submission_data = db.session.query(FormsflowOfflineSubmission).filter_by(id=submission_id).first()
        submission_data.status = status
        db.session.commit()

def send_to_formio(**kwargs):
    logging.verbose("Sending to Formio")
    return False, kwargs

def send_to_formsflow(**kwargs):
    logging.verbose("Sending to Formsflow")
    return False, kwargs

def add_to_hold_queue(**args)->tuple:
    logging.verbose(f"inside add_to_hold_queue() with args: {args}")
    try:
        config = args.get('config')
        message = args.get('message')
        submission_id = args.get('offline_submission_id')
        writer = args.get('writer')
        retry_count = message.get('offline_submission_retry_count', 0)
        try:
            retry_count = max(0, int(retry_count))
        except (TypeError, ValueError):
            retry_count = 0
        logging.debug('offline submission retry count: {}'.format(retry_count))

        if retry_count >= config.OFFLINE_SUBMISSION_MAX_RETRIES:
            args['error'] = {
                        'error_code': ErrorCode.O05,
                        'error_details': ErrorCode.O05.description,
                        'event_id': None,
                        'event_type': 'offline_submission',
                        'submission_id': submission_id,
                        'payload': json.dumps(message) if message else None,
                        'func': add_to_hold_queue,
                    }
            return False, args
        else:
            retry_count += 1
            message['offline_submission_retry_count'] = retry_count
            queue_name = config.OFFLINE_SUBMISSION_HOLD_QUEUE

        payload = encode_message(message, config.ENCRYPT_KEY)
        logging.verbose(f'add_to_hold_queue(): {json.dumps(message)}')

        if not writer.publish_confirmed(queue_name, payload):
            logging.critical('unable to write to RabbitMQ {} queue'.format(queue_name))
            args['error'] = {
                        'error_code': ErrorCode.O06,
                        'error_details': ErrorCode.O06.description,
                        'event_id': None,
                        'event_type': 'offline_submission',
                        'submission_id': submission_id,
                        'payload': json.dumps(message) if message else None,
                        'func': add_to_hold_queue,
                    }
            return False, args
    except Exception as e:
        logging.exception(e)
        return False, args
    return True, args

def update_status_error(**args):
    logging.verbose("Updating status to error")
    try:
        application = args.get('app')
        db = args.get('db')
        submission_id = args.get('offline_submission_id')
        _update_status(submission_id, 'error', application, db)
        return True, args
    except Exception as e:
        logging.exception(e)
        return True, args

def record_process_error(**args):
    logging.verbose("Recording error")
    try:
        error_obj = args.get('error')
        application = args.get('app')

        with application.app_context():          
            record_error(**error_obj)
            email = {
                'title': f"[DF_FORM_HANDLER] {error_obj['error_code'].code} - {error_obj['error_code'].description}",
                'config': args.get('config'),
                'body': error_obj,
            }
            send_error_to_rsiops(**email)
        return True, args
    except Exception as e:
        # If recording the error itself fails, log it
        logging.exception(f"Failed to record error: {str(e)}")
    return True, args