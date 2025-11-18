
from python.task_scheduler.config import Config
from python.task_scheduler.message import encode_message
import logging
import json
from python.common.error_middleware import record_error
from python.common.enums import ErrorCode

def add_to_event_queue(app, writer, message):
    logging.debug("inside add_to_event_queue()")
    errmsg=''
    try:
        queue_name = Config.STORAGE_WATCH_QUEUE
        logging.verbose('add_to_event_queue(): {}'.format(json.dumps(message)))
        if not writer.publish(queue_name, encode_message(message, Config.ENCRYPT_KEY)):
            logging.critical('unable to write to RabbitMQ {} queue'.format(queue_name))
            record_queue_error(app, message, add_to_event_queue, 'unable to write to RabbitMQ {} queue'.format(queue_name))
            return False, errmsg
    except Exception as e:
        logging.error(e, exc_info=True)
        record_queue_error(app, message, add_to_event_queue, str(e))
        return False, errmsg
    return True, errmsg

def record_queue_error(app, event, func, error_details=None):
    try:
        
        with app.app_context():
        
            event_id = event.get('event_id') if event else None
            event_type = event.get('event_type') if event else None
            error_obj = {
                'error_code': ErrorCode.E03,
                'error_details': error_details,
                'event_id': event_id,
                'event_type': event_type,
                'payload': json.dumps(event) if event else None,
                'func': func,
            }
            
            record_error(**error_obj)
    except Exception as e:
        # Log the error that occurred during the error recording process
        logging.error(f"Error in record_queue_error: {str(e)}")
        logging.error(f"Original error details: message={event}, func={func}, error_details={error_details}")
        
   