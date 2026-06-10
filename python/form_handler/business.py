# import python.common.middleware as middleware
from python.common import splunk
import python.form_handler.actions as actions
from python.form_handler.actions_icbc import send_to_icbc_actions
from python.form_handler.actions_load_event import load_event_actions
from python.form_handler.actions_odw import send_to_odw_actions
import python.form_handler.rsi_email as rsi_email
# import python.common.splunk_application_for_review as splunk
# import python.common.splunk as common_splunk
from python.form_handler.actions import get_storage_ref_event_type
import python.common.ride_actions as ride_actions
from python.form_handler.actions_vips import send_to_vips_actions


def process_incoming_form() -> dict:
    """
    This function lists the business rules required when processing
    each form.  The Orbeon form name is used as the key.  For example,
    the "send_disclosure" attributes below are used when processing the
    "send_disclosure" Orbeon form.
    """
    return {
        "unknown_event": [
            {"try": actions.add_unknown_event_error_to_message, "fail": []},
            {"try": actions.add_to_persistent_failed_queue, "fail": [
                {"try": actions.record_event_error, "fail": []}
                ]},
            {"try": rsi_email.rsiops_unknown_event_type, "fail": []},
            {"try": actions.add_unknown_event_to_error, "fail": []},
            {"try": actions.record_event_error, "fail": []}
        ],
        "vi": load_event_actions()
            + send_to_vips_actions()
            + send_to_odw_actions(),
            # {"try": actions.prep_vips_document_payload, "fail": [
            #     {"try": rsi_email.rsiops_event_to_error_queue, "fail": []},
            #     {"try": actions.add_to_persistent_failed_queue, "fail": []},
            #     {"try": actions.update_event_status_error, "fail": []},
            # ]},
            # Sending to VIPS temporarily disabled
            # {"try": actions.create_vips_document, "fail": [
            #     {"try": actions.add_to_retry_queue, "fail": []},
            #     {"try": actions.update_event_status_hold, "fail": []},
            # ]},

            # {"try": actions.prep_vips_payload, "fail": [
            #     {"try": rsi_email.rsiops_event_to_error_queue, "fail": []},
            #     {"try": actions.add_to_persistent_failed_queue, "fail": []},
            #     {"try": actions.update_event_status_error, "fail": []},
            # ]},

            # Sending to VIPS temporarily disabled
            # {"try": actions.create_vips_impoundment, "fail": [
            #     {"try": actions.add_to_retry_queue, "fail": []},
            #     {"try": actions.update_event_status_hold, "fail": []},
            # ]},
        "24h": load_event_actions()
        + send_to_icbc_actions() 
        + send_to_odw_actions(),
        "12h": load_event_actions()
        + send_to_icbc_actions()
        + send_to_odw_actions(),
        "irp": load_event_actions()
            + send_to_vips_actions()
    }
