from python.common import splunk
from python.form_handler import actions, rsi_email

VIPS = 'VIPS'

def get_submission_event_id(**args)->tuple:
    args['destination']=VIPS
    return actions.get_submission_event_id(**args)

def send_to_vips_actions() -> list:
    return [ 
        {"try": get_submission_event_id, "event": VIPS, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
        ]},
        {"try": actions.update_event_status_processing, "event": VIPS, "fail": []},
        {"try": rsi_email.event_to_vips_dps, "event": VIPS, "fail": [
            {"try": actions.add_to_retry_queue, "fail": []},
            {"try": actions.update_event_status_hold, "fail": []},
        ]},
        {"try": actions.update_event_status, "event": VIPS, "fail": []},
        {"try": splunk.log_to_splunk, "event": VIPS, "fail": []},
    ]