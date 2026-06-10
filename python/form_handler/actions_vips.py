from python.common import splunk
from python.form_handler import actions, rsi_email

def get_submission_event_id(**args)->tuple:
    args['destination']='VIPS'
    return actions.get_submission_event_id(**args)

def send_to_vips_actions() -> list:
    return [ 
        {"try": get_submission_event_id, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
        ]},
        {"try": actions.update_event_status_processing, "fail": []},
        {"try": rsi_email.event_to_vips_dps, "fail": [
            {"try": actions.add_to_retry_queue, "fail": []},
            {"try": actions.update_event_status_hold, "fail": []},
        ]},
        {"try": actions.update_event_status, "fail": []},
        {"try": splunk.log_to_splunk, "fail": []},
    ]