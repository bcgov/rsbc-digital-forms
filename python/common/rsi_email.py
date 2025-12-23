import python.common.helper as helper
from python.common.config import Config
import python.common.common_email_services as common_email_services
from datetime import datetime
import json
import logging
import logging.config
from jinja2 import Environment, select_autoescape, FileSystemLoader
import os

logging.config.dictConfig(Config.LOGGING)


def send_email_to_admin(**args):
    subject = args.get('subject')
    config = args.get('config')
    message = args.get('message')
    body = args.get('body')
    template = get_jinja2_env().get_template('admin_notice.html')
    return common_email_services.send_email(
        [config.ADMIN_EMAIL_ADDRESS],
        subject,
        config,
        template.render(subject=subject, body=body, message=json.dumps(message)), 'admin'), args


def send_new_user_admin_notification(**args):
    subject = args.get('subject')
    config = args.get('config')
    message = args.get('message')
    body = args.get('body')
    template = get_jinja2_env().get_template('admin_notice_new_user_approval_request.html')
    return common_email_services.send_email(
        [config.ADMIN_EMAIL_ADDRESS],
        subject,
        config,
        template.render(subject=subject, body=body, message=message), 'admin'), args


def admin_unable_to_save_to_vips(**args) -> tuple:
    logging.critical('inside unable_to_save_to_vips_api()')
    config = args.get('config')
    message = args.get('message')
    subject = 'Critical Error: Unable to save to VIPS'
    body_text = 'While attempting to save an application to VIPS, an error was returned. ' + \
                'We will save the record to a failed write queue in RabbitMQ.'
    logging.critical('unable to save to VIPS: {}'.format(json.dumps(message)))
    return send_email_to_admin(config=config, subject=subject, body=body_text), args


def admin_unknown_event_type(**args) -> tuple:
    message = args.get('message')
    config = args.get('config')
    title = 'Critical Error: Unknown Event Type'
    body_text = "An unknown event has been received: " + message['event_type']
    logging.critical('unknown event type: {}'.format(message['event_type']))
    return send_email_to_admin(config=config, title=title, body=body_text), args

# Send MV6020 Entity Copy to entity email
def send_mv6020_copy(**args) -> tuple:
    config = args.get('config')
    subject = args.get('subject')
    email_address = args.get('email_address')
    full_name= args.get('full_name')
    message = args.get('message')
    attachments = args.get('attachments')
    email_type = args.get('email_type')

    # Valid email_type → template mapping
    template_map = {
        'entity': 'MV6020_send_entity_copy.html',
        'police': 'MV6020_send_police_copy.html',
        'icbc':   'MV6020_send_icbc_copy.html',
    }

    t = template_map.get(email_type)

    if not t:
        # API-safe message
        api_error = f"Unknown MV6020 email type '{email_type}'"

        args["response_dict"] = {
            "error_details": api_error
        }

        return False, args
    
    args['email_template'] = t
    template = get_jinja2_env().get_template(t)
    return common_email_services.send_email(
        [email_address],
        subject,
        config,
        template.render(subject=subject, 
        full_name=full_name, message=message),
        message.get('collision_case_number'),attachments), args


def send_admin_failure_notification(**args):
    subject = args.get('subject')
    config = args.get('config')
    message = args.get('message')
    template = get_jinja2_env().get_template('admin_notice_submission_failure.html')
    return common_email_services.send_email(
        [config.ADMIN_EMAIL_ADDRESS],
        subject,
        config,
        template.render(subject=subject, message=message), 'admin'), args



def get_jinja2_env(path="./python/common/templates"):
    template_loader = FileSystemLoader(searchpath=path)
    return Environment(
        loader=template_loader,
        autoescape=select_autoescape(['html', 'xml'])
    )


def get_email_content(template_name: str, prohibition_number: str):
    content = content_data()
    if template_name in content:
        email_content = content[template_name]
        email_content['subject'] = email_content['raw_subject'].format(_hyphenate(prohibition_number))
        logging.info(email_content)
        return email_content
    return dict({
            "raw_subject": "Unknown template requested {}",
            "subject": "Unknown template",
            "callout": "",
            "title": "Unknown Template",
            "timeline": ""
        })


def _hyphenate(prohibition_number: str) -> str:
    return "{}-{}".format(prohibition_number[0:2], prohibition_number[2:8])


def content_data() -> dict:
    return dict({
        "MV6020_send_entity_copy.html": {
            "raw_subject": "Traffic Accident Report Copy Attached - Collision Case Number {}",
            "title": "Send MV6020 Entity Copy",
        }
    })
