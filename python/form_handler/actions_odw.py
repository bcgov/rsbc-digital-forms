from python.common import ride_actions
from python.form_handler import actions, rsi_email

def get_submission_event_id(**args)->tuple:
    args['destination']='ODW'
    return actions.get_submission_event_id(**args)

def send_to_odw(**args):
    event_type=args.get('event_type')
    if event_type == 'vi':
        return ride_actions.vi_event(**args)
    elif event_type == '12h':
        return ride_actions.twelve_hours_event(**args)
    elif event_type == '24h':
        return ride_actions.twenty_four_hours_event(**args)
    else:
        return True, args

def send_to_odw_actions() -> list:
    return [
        {"try": get_submission_event_id, "fail": [
            {"try": actions.add_to_retry_queue, "fail": []},
            {"try": actions.update_event_status_hold, "fail": []},
        ]},
        {"try": actions.get_event_status, "fail": []},
        {"try": actions.update_event_status_processing, "fail": []},
        {"try": actions.get_event_coordinates, "fail": []},
        {"try": send_to_odw, "fail": [
            {"try": actions.record_event_error, "fail": []},
        ]},
        {"try": actions.update_event_status, "fail": []},
    ]