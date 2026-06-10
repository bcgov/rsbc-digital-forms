from python.common import splunk
from python.form_handler import actions, rsi_email

def get_submission_event_id(**args)->tuple:
    args['destination']='ICBC'
    return actions.get_submission_event_id(**args)

def send_to_icbc_actions() -> list:
    return [
        {"try": get_submission_event_id, "fail": [
            {"try": actions.add_to_retry_queue, "fail": []},
            {"try": actions.update_event_status_hold, "fail": []},
        ]},
        {"try": actions.get_event_status, "fail": []},
        {"try": actions.update_event_status_processing, "fail": []},
        {"try": actions.prep_icbc_payload, "fail": [
            {"try": rsi_email.rsiops_event_to_error_queue, "fail": []},
            {"try": actions.add_to_persistent_failed_queue, "fail": []},
            {"try": actions.record_event_error, "fail": []},
            {"try": actions.update_event_status_error, "fail": []},
        ]},
        {"try": actions.send_to_icbc, "fail": [
            {"try": actions.add_to_retry_queue, "fail": []},
            {"try": actions.record_event_error, "fail": []},
            {"try": actions.update_event_status_hold, "fail": []},
        ]},
        {"try": actions.update_event_status, "fail": []},
        {"try": splunk.log_to_splunk, "fail": []},
    ]