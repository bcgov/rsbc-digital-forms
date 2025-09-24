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

def rsiops_event_to_retry_queue(**args) -> tuple:
    # message = args.get('message')
    # config = args.get('config')
    config = args.get('config')
    event_type = args.get('event_type')
    storage_key = args.get('storage_key')
    message = args.get('message')
    put_to_queue_name=args.get('put_to_queue_name',None)
    if put_to_queue_name is None:
        return False, args
    elif put_to_queue_name==Config.STORAGE_FAIL_QUEUE_PERS:
        title = 'Critical Error: Event sent to error queue after max retries'
        body_text = f"An event has been sent to persistent error queue after max retries: {event_type} for storage key: {storage_key} "
        logging.critical('sent to persistent error queue: {}'.format(storage_key))
        send_email_to_rsiops(config=config, title=title, body=body_text, eventid=storage_key,message=message)
        return False, args
    return False, args

def event_to_vips_dps(**args) -> tuple:
    # message = args.get('message')
    # config = args.get('config')
    logging.verbose(f"inside event_to_vips_dps() with args: {args}")
    config = args.get('config')
    # event_type = args.get('event_type')
    storage_key = args.get('storage_key')
    eventid = args.get('message').get('event_id')
    # put_to_queue_name=args.get('put_to_queue_name',None)
    title = 'VIPS email'
    body_text = f"Sent to vips "
    file_data=args.get('file_data',None)
    try:
        email_sent,respargs=send_email_to_vips(config=config, title=title, body=body_text, eventid=eventid,file_data=file_data)
        if email_sent:
            logging.debug("email sent to vips")
        else:
            logging.debug("email not sent to vips")
            raise Exception("email not sent to vips")
    except Exception as e:
        logging.exception("Exception in sending email to vips: {}".format(e))
        return False, args
    return True, args




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


def send_email_to_vips(**args):
    subject = args.get('title')
    config = args.get('config')
    # message = args.get('message')
    eventid = args.get('eventid')
    body = args.get('body')
    template = get_jinja2_env().get_template('vips_dps_email.html')
    vips_email=config.VIPS_DPS_EMAIL.split(',')
    # vips_email = config.VIPS_DPS_EMAIL
    file_data=args.get('file_data',None)
    # logging.debug("file_data: {}".format(file_data))
    # config['BCC_EMAIL_ADDRESSES']=config['VIPS_BCC_EMAIL_ADDRESSES'].split(',')
    config.BCC_EMAIL_ADDRESSES=config.VIPS_BCC_EMAIL_ADDRESSES
    return common_email_services.send_email(
        vips_email,
        subject,
        config,
        template.render(subject=subject, body=body, message=json.dumps("")), eventid,[{
                "content": file_data,
                "contentType": "string",
                "encoding": "base64",
                "filename": f"{eventid}.pdf"
            }]), args

def get_jinja2_env(path="./python/form_handler/templates"):
    template_loader = FileSystemLoader(searchpath=path)
    return Environment(
        loader=template_loader,
        autoescape=select_autoescape(['html', 'xml'])
    )



def send_error_to_rsiops(**args):
    if not args.get('config') or not args.get('title') or not args.get('body'):
        return False, args
    subject = args.get('title')
    config = args.get('config')
    message = args.get('message')
    eventid = args.get('eventid')
    body = args.get('body')
    template = get_jinja2_env().get_template('error_notification.html')
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