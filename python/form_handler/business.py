# import python.common.middleware as middleware
from python.common import splunk
import python.form_handler.actions as actions
import python.form_handler.rsi_email as rsi_email
# import python.common.splunk_application_for_review as splunk
# import python.common.splunk as common_splunk
from python.form_handler.actions import get_storage_ref_event_type
import python.common.ride_actions as ride_actions


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
        "vi": [
            # DONE: query form data and event data using storage key from input
            # DONE: if event retry count is more than 10, add to failed queue
            # DONE: if form data is not found, add to hold queue
            # DONE: if event data is not found, add to hold queue
            # DONE: if form data is found, but event data is not found, add to hold queue
            # DONE: if form data is found, and event data is found, continue
            # DONE: Implement add to hold queue
            # DONE: implement add to failed queue
            # DONE: Validate form and event data based on payload needed for vips
            # DONE: if form data is invalid, add to failed queue
            # DONE: if form and event data is valid update status to processin
            # DONE: Query pdf object from storage and add to args
            # DONE: Query user data for the event (comes from created by)
            # DONE: if data is valid prep payload for vips
            # DONE: if fails to send to vips, add to hold queue and add data retry_count to event table
            # DONE: if success update vips status on event row on db and retry count to 0
            {"try": actions.validate_event_retry_count, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_error_retry, "fail": []},
                {"try": actions.record_event_error, "fail": []},
                {"try": rsi_email.rsiops_event_to_retry_queue, "fail": []},
            ]},
            {"try": actions.get_storage_ref_event_type, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []}
            ]},
            {"try": actions.get_event_form_data, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []}
            ]},
            {"try": actions.get_event_user_data, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
            ]},
            {"try": actions.get_submission_event_id, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
            ]},
            {"try": actions.validate_event_data, "fail": [
                {"try": rsi_email.rsiops_event_to_error_queue, "fail": []},
                {"try": actions.add_to_persistent_failed_queue, "fail": []},
                {"try": actions.update_event_status_error, "fail": []},
            ]},
            {"try": actions.update_event_status_processing, "fail": []},
            {"try": actions.get_storage_file, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
            ]},
            {"try": rsi_email.event_to_vips_dps, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
            ]},
            {"try": splunk.log_to_splunk, "fail": []},
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
            {"try": actions.get_event_coordinates, "fail": []},
            {"try": ride_actions.vi_event, "fail": [
                 {"try": actions.record_event_error, "fail": []},
                 ]},
            {"try": actions.update_event_status, "fail": []},
        ],
        "24h": [
            {"try": actions.validate_event_retry_count, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_error_retry, "fail": []},
                {"try": actions.record_event_error, "fail": []},
                {"try": rsi_email.rsiops_event_to_retry_queue, "fail": []}
            ]},
            {"try": actions.get_storage_ref_event_type, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
            ]},
            {"try": actions.get_event_form_data, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
            ]},
            {"try": actions.get_event_user_data, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
            ]},
            {"try": actions.get_submission_event_id, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
            ]},
            {"try": actions.validate_event_data, "fail": [
                {"try": rsi_email.rsiops_event_to_error_queue, "fail": []},
                {"try": actions.add_to_persistent_failed_queue, "fail": []},
                {"try": actions.update_event_status_error, "fail": []},
            ]},
            {"try": actions.update_event_status_processing, "fail": []},
            {"try": actions.get_storage_file, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
            ]},
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
            {"try": splunk.log_to_splunk, "fail": []},
            {"try": actions.get_event_coordinates, "fail": []},
            {"try": ride_actions.twenty_four_hours_event, "fail": [
                {"try": actions.record_event_error, "fail": []},
                ]},
            {"try": actions.update_event_status, "fail": []},
            # {"try": actions.send_email, "fail": [
            #     # {"try": actions.add_to_failed_queue, "fail": []}
            # ]},
            # {"try": actions.add_to_failed_queue, "fail": []},
        ],
        "12h": [
            {"try": actions.validate_event_retry_count, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_error_retry, "fail": []},
                {"try": actions.record_event_error, "fail": []},
                {"try": rsi_email.rsiops_event_to_retry_queue, "fail": []}
            ]},
            {"try": actions.get_storage_ref_event_type, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
            ]},
            {"try": actions.get_event_form_data, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
            ]},
            {"try": actions.get_event_user_data, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
            ]},
            {"try": actions.get_submission_event_id, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
            ]},
            {"try": actions.validate_event_data, "fail": [
                {"try": rsi_email.rsiops_event_to_error_queue, "fail": []},
                {"try": actions.add_to_persistent_failed_queue, "fail": []},
                {"try": actions.update_event_status_error, "fail": []},
            ]},
            {"try": actions.update_event_status_processing, "fail": []},
            {"try": actions.get_storage_file, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
            ]},
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
            {"try": splunk.log_to_splunk, "fail": []},
            {"try": actions.get_event_coordinates, "fail": []},
            {"try": ride_actions.twelve_hours_event, "fail": [
                 {"try": actions.record_event_error, "fail": []},
                ]},
            {"try": actions.update_event_status, "fail": []},
        ],
        "irp": [
            {"try": actions.validate_event_retry_count, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_error_retry, "fail": []},
                {"try": actions.record_event_error, "fail": []},
                {"try": rsi_email.rsiops_event_to_retry_queue, "fail": []},
            ]},
            {"try": actions.get_storage_ref_event_type, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []}
            ]},
            {"try": actions.get_event_form_data, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []}
            ]},
            {"try": actions.get_event_user_data, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
            ]},
            {"try": actions.get_submission_event_id, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
            ]},
            {"try": actions.validate_event_data, "fail": [
                {"try": rsi_email.rsiops_event_to_error_queue, "fail": []},
                {"try": actions.add_to_persistent_failed_queue, "fail": []},
                {"try": actions.update_event_status_error, "fail": []},
            ]},
            {"try": actions.update_event_status_processing, "fail": []},
            {"try": actions.get_storage_file, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
            ]},
            {"try": rsi_email.event_to_vips_dps, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
            ]},
            {"try": splunk.log_to_splunk, "fail": []},
            {"try": actions.update_event_status, "fail": []},
        ]
    }
