import python.form_handler.helper as helper
from python.form_handler.config import Config
import python.form_handler.common_email_services as common_email_services
from datetime import datetime
import json
import logging
import logging.config
from jinja2 import Environment, select_autoescape, FileSystemLoader

logging.config.dictConfig(Config.LOGGING)

def rsiops_unknown_event_type(**args) -> tuple:
    # message = args.get('message')
    # config = args.get('config')
    config = args.get('config')
    event_type = args.get('event_type')
    storage_key = args.get('storage_key')
    message = args.get('message')
    title = 'Critical Error: Unknown Event Type'
    body_text = f"An unknown event has been received: {event_type} for storage key: {storage_key} "
    logging.critical('unknown event type: {}'.format(event_type))
    return send_email_to_rsiops(config=config, title=title, body=body_text,eventid=storage_key,message=message), args

def rsiops_event_to_transient_error_queue(**args) -> tuple:
    # message = args.get('message')
    # config = args.get('config')
    config = args.get('config')
    event_type = args.get('event_type')
    storage_key = args.get('storage_key')
    message = args.get('message')
    title = 'Warning: Event sent to transient error queue. Will be retried soon..'
    body_text = f"An event has been sent to transient error queue. Will be retried soon..: {event_type} for storage key: {storage_key} "
    logging.critical('sent to transient error queue: {}'.format(storage_key))
    return send_email_to_rsiops(config=config, title=title, body=body_text,eventid=storage_key,message=message), args


def rsiops_event_to_error_queue(**args) -> tuple:
    # message = args.get('message')
    # config = args.get('config')
    config = args.get('config')
    event_type = args.get('event_type')
    storage_key = args.get('storage_key')
    message = args.get('message')
    title = 'Critical Error: Event sent to error queue after max retries'
    body_text = f"An event has been sent to persistent error queue after max retries: {event_type} for storage key: {storage_key} "
    logging.critical('sent to persistent error queue: {}'.format(storage_key))
    return send_email_to_rsiops(config=config, title=title, body=body_text,eventid=storage_key,message=message), args



def send_email_to_rsiops(**args):
    subject = args.get('title')
    config = args.get('config')
    message = args.get('message')
    eventid = args.get('eventid')
    body = args.get('body')
    template = get_jinja2_env().get_template('admin_notice.html')
    to_emails=config.RSIOPS_EMAIL_ADDRESS.split(',')
    return common_email_services.send_email(
        to_emails,
        subject,
        config,
        template.render(subject=subject, body=body, message=json.dumps(message)), eventid,[{
                "content": json.dumps(message),
                "contentType": "string",
                # "encoding": "base64",
                "filename": "event.json"
            }]), args

def get_jinja2_env(path="./python/form_handler/templates"):
    template_loader = FileSystemLoader(searchpath=path)
    return Environment(
        loader=template_loader,
        autoescape=select_autoescape(['html', 'xml'])
    )