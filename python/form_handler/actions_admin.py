
import logging

from python.common import splunk
from python.common.enums import ErrorCode
from python.common.helper import date_time_to_local_tz_string
from python.common.models import AgencyAdmin
from python.form_handler import actions, rsi_email

ADMIN = 'ADMIN'

def get_submission_event_id(**args)->tuple:
    args['destination']=ADMIN
    return actions.get_submission_event_id(**args)

def send_to_admin_actions() -> list:
    return [
        {"try": get_submission_event_id, "event": ADMIN, "fail": [
            {"try": actions.add_to_retry_queue, "fail": []},
            {"try": actions.update_event_status_hold, "fail": []},
        ]},
        {"try": actions.update_event_status_processing, "event": ADMIN, "fail": []},
        {"try": get_agency_admin_email, "event": ADMIN, "fail": [
            {"try": actions.add_to_retry_queue, "fail": []},
            {"try": actions.update_event_status_hold, "fail": []},
        ]},
        {"try": set_admin_email_content, "event": ADMIN, "fail": [
            {"try": actions.add_to_retry_queue, "fail": []},
            {"try": actions.update_event_status_hold, "fail": []},
        ]},
        {"try": rsi_email.send_email_to_agency_admins, "event": ADMIN, "fail": [
            {"try": actions.add_to_retry_queue, "fail": []},
            {"try": actions.update_event_status_hold, "fail": []},
        ]},
        {"try": actions.update_event_status, "event": ADMIN, "fail": []},
        {"try": splunk.log_to_splunk, "event": ADMIN, "fail": []},
    ]


def get_agency_admin_email(**args)->tuple:
    logging.verbose(f"inside get_agency_admin_email() with args: {args}")
    try:
        user_data = args.get('user_data', {})
        application = args.get('app')
        db = args.get('db')
        agency_id = user_data.get('agency_id')
        with application.app_context():
            agency_admins = db.session.query(AgencyAdmin) \
                .filter(AgencyAdmin.agency_id == agency_id) \
                .all()
            if len(agency_admins) == 0:
                logging.debug("No agency admin found for agency_id: {}".format(agency_id))
                args['agency_admin_emails'] = None
            else:
                emails = [admin.email for admin in agency_admins]
                args['agency_admin_emails'] = emails
    except Exception as e:
        logging.error(f'Error getting agency admin email: {e}')
        args['error'] = {
                'error_code': ErrorCode.E07,
                'error_details': e,
                'event_type': args['message']['event_type'],
                'func': get_agency_admin_email,
                'event_id': args['message']['event_id']
            }
        actions.record_event_error(**args)

    return True, args

def set_admin_email_content(**args)->tuple:
    logging.verbose(f"inside set_admin_email_content() with args: {args}")
    try:
        submission_date = args.get('event_data', {}).get('created_dt')
        body = {
            'form_type': args.get('storage_ref', {}).get('form_type'),
            'form_number': args.get('storage_ref', {}).get('form_id'),
            'agency_file_number': args.get('event_data', {}).get('agency_file_no'),
            'submission_date': date_time_to_local_tz_string(submission_date),
            'officer_badge': args.get('user_data', {}).get('badge_number'),
            'officer_name': f"{args.get('user_data', {}).get('display_name')}",
            'agency_name': args.get('user_data', {}).get('agency_ref', {}).get('agency_name'),
        }
        args['body'] = body
        args['title'] = f"New {body['form_type']} form submitted - {body['form_number']}"
    except Exception as e:
        logging.error(f'Error setting admin email content: {e}')
        args['error'] = {
                'error_code': ErrorCode.E07,
                'error_details': e,
                'event_type': args['message']['event_type'],
                'func': set_admin_email_content,
                'event_id': args['message']['event_id']
            }
        actions.record_event_error(**args)

    return True, args