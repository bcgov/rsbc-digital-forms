
import logging.config
from python.task_scheduler.config import Config
from python.task_scheduler.message import encode_message
import logging
import json


def add_to_event_queue(writer,message):
    logging.debug("inside add_to_event_queue()")
    errmsg=''
    try:
        queue_name = Config.STORAGE_WATCH_QUEUE
        logging.debug('add_to_event_queue(): {}'.format(json.dumps(message)))
        if not writer.publish(queue_name, encode_message(message, Config.ENCRYPT_KEY)):
            logging.critical('unable to write to RabbitMQ {} queue'.format(queue_name))
            return False, errmsg
    except Exception as e:
        logging.error(e)
        return False, errmsg
    return True, errmsg