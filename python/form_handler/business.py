# import python.common.middleware as middleware
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
            {"try": actions.get_event_coordinates, "fail": []},
            {"try": ride_actions.twelve_hours_event, "fail": [
                 {"try": actions.record_event_error, "fail": []},
                ]},
            {"try": actions.update_event_status, "fail": []},
            # {"try": actions.send_email, "fail": [
            #     # {"try": actions.add_to_failed_queue, "fail": []}
            # ]},
            # {"try": actions.add_to_failed_queue, "fail": []},
        ]
        # "send_disclosure": [
        #     {"try": actions.is_not_on_hold, "fail": [
        #         {"try": actions.add_to_hold_queue, "fail": []}
        #     ]},
        #     {"try": middleware.get_data_from_disclosure_event, "fail": []},
        #     {"try": middleware.determine_current_datetime, "fail": []},
        #     {"try": middleware.get_vips_status, "fail": []},
        #     {"try": middleware.prohibition_exists_in_vips, "fail": []},
        #     {"try": middleware.is_review_in_the_future, "fail": [
        #         # No further disclosure will be sent. The review has concluded.
        #     ]},
        #     {"try": middleware.is_any_unsent_disclosure, "fail": [
        #         # No new disclosure to send at present, try again later
        #         {"try": actions.add_hold_before_sending_disclosure, "fail": []},
        #         {"try": actions.add_to_hold_queue, "fail": []}
        #     ]},
        #     {"try": middleware.retrieve_unsent_disclosure, "fail": []},
        #     {"try": middleware.if_required_add_adp_disclosure, "fail": []},
        #     {"try": rsi_email.applicant_disclosure, "fail": [
        #         # if send is not successful, add back to hold queue
        #     ]},
        #     {"try": middleware.mark_disclosure_as_sent, "fail": []},
        #     {"try": splunk.disclosure_sent, "fail": []},
        #     {"try": ride_actions.disclosure_sent, "fail": []},
        #     {"try": common_splunk.log_to_splunk, "fail": []},
        #     {"try": actions.add_hold_before_sending_disclosure, "fail": []},
        #     {"try": actions.add_to_hold_queue, "fail": []}
        #
        # ],
        # "verify_schedule": [
        #     {"try": actions.is_not_on_hold, "fail": [
        #         {"try": actions.add_to_hold_queue, "fail": []}
        #     ]},
        #     {"try": middleware.get_data_from_verify_schedule_event, "fail": []},
        #     {"try": middleware.determine_current_datetime, "fail": []},
        #     {"try": middleware.get_vips_status, "fail": []},
        #     {"try": middleware.prohibition_exists_in_vips, "fail": []},
        #     {"try": middleware.review_has_been_scheduled, "fail": [
        #         # if review has not been scheduled, notify Appeals Registry
        #         {"try": rsi_email.applicant_did_not_schedule, "fail": []},
        #     ]}
        #     # If review has been scheduled, do nothing
        # ],
        # "review_schedule_picker": [
        #     # aka: review scheduler
        #     {"try": middleware.determine_current_datetime, "fail": []},
        #     {"try": middleware.get_data_from_schedule_form, "fail": []},
        #     {"try": middleware.clean_prohibition_number, "fail": []},
        #     {"try": middleware.get_vips_status, "fail": []},
        #     {"try": middleware.prohibition_exists_in_vips, "fail": []},
        #     {"try": middleware.user_submitted_last_name_matches_vips, "fail": []},
        #     {"try": middleware.application_has_been_saved_to_vips, "fail": []},
        #
        #     {"try": middleware.get_payment_status, "fail": []},
        #     {"try": middleware.received_valid_payment_status, "fail": []},
        #     {"try": middleware.paid_not_more_than_24hrs_ago, "fail": []},
        #
        #     {"try": middleware.application_has_been_paid, "fail": []},
        #     {"try": middleware.get_application_details, "fail": []},
        #     {"try": middleware.valid_application_received_from_vips, "fail": []},
        #     {"try": middleware.get_invoice_details, "fail": []},
        #     {"try": middleware.calculate_schedule_window, "fail": []},
        #     {"try": middleware.decode_selected_timeslot, "fail": []},
        #     {"try": middleware.get_human_friendly_time_slot_string, "fail": []},
        #
        #     {"try": middleware.save_schedule_to_vips, "fail": [
        #         # Consider sending a message to the applicant in the unlikely
        #         # event that the schedule save operation is unsuccessful
        #     ]},
        #     {"try": splunk.review_scheduled, "fail": []},
        #     {"try": ride_actions.review_scheduled, "fail": []},
        #     {"try": common_splunk.log_to_splunk, "fail": []},
        #     {"try": rsi_email.applicant_schedule_confirmation, "fail": []},
        #     {"try": rsi_email.applicant_evidence_instructions, "fail": []},
        #     {"try": middleware.create_disclosure_event, "fail": []},
        #     {"try": actions.add_hold_before_sending_disclosure, "fail": []},
        #     {"try": actions.add_to_hold_queue, "fail": []}
        # ],
        # "prohibition_review": [
        #     # aka: prohibition application received
        #     {"try": actions.is_not_on_hold, "fail": [
        #         {"try": actions.add_to_hold_queue, "fail": []}
        #     ]},
        #     {"try": middleware.get_data_from_application_form, "fail": []},
        #     {"try": middleware.get_user_entered_notice_type_from_message, "fail": []},
        #     {"try": middleware.clean_prohibition_number, "fail": []},
        #     {"try": middleware.populate_driver_name_fields_if_null, "fail": []},
        #     {"try": middleware.determine_current_datetime, "fail": []},
        #     {"try": middleware.get_vips_status, "fail": [
        #         {"try": actions.add_to_hold_queue, "fail": []}
        #     ]},
        #     {"try": middleware.prohibition_exists_in_vips, "fail": [
        #         {"try": middleware.prohibition_served_within_past_week, "fail": [
        #             {"try": rsi_email.applicant_prohibition_not_found, "fail": []}
        #         ]},
        #         {"try": middleware.applicant_has_more_than_one_day_to_apply, "fail": [
        #             {"try": rsi_email.applicant_prohibition_still_not_found, "fail": []},
        #             {"try": actions.add_24_hour_hold_until, "fail": []},
        #             {"try": actions.add_to_hold_queue, "fail": []}
        #         ]},
        #         {"try": rsi_email.applicant_prohibition_not_found_yet, "fail": []},
        #         {"try": actions.add_hold_before_trying_vips_again, "fail": []},
        #         {"try": actions.add_to_hold_queue, "fail": []}
        #     ]},
        #     {"try": middleware.applicant_has_not_applied_previously, "fail": [
        #         {"try": middleware.applicant_is_eligible_to_reapply, "fail": [
        #             {"try": rsi_email.already_applied, "fail": []},
        #         ]},
        #         {"try": middleware.user_submitted_last_name_matches_vips, "fail": [
        #             {"try": rsi_email.applicant_last_name_mismatch, "fail": []}
        #         ]},
        #         {"try": middleware.is_applicant_within_window_to_apply, "fail": [
        #             {"try": rsi_email.applicant_prohibition_served_more_than_7_days_ago, "fail": []}
        #         ]},
        #         {"try": middleware.has_drivers_licence_been_seized, "fail": [
        #             {"try": rsi_email.applicant_licence_not_seized, "fail": []}
        #         ]},
        #         {"try": middleware.transform_hearing_request_type, "fail": []},
        #         {"try": middleware.force_presentation_type_to_written_if_ineligible_for_oral, "fail": []},
        #         {"try": middleware.transform_applicant_role_type, "fail": []},
        #         {"try": middleware.compress_form_data_xml, "fail": []},
        #         {"try": middleware.save_application_to_vips, "fail": [
        #             {"try": actions.add_to_failed_queue, "fail": []},
        #             {"try": rsi_email.admin_unable_to_save_to_vips, "fail": []}
        #         ]},
        #         {"try": splunk.application_accepted, "fail": []},
        #         {"try": common_splunk.log_to_splunk, "fail": []},
        #         {"try": rsi_email.application_accepted, "fail": []},
        #         {"try": ride_actions.app_accepted_event, "fail": []},
        #         {"try": middleware.is_applicant_ineligible_for_oral_review_but_requested_oral, "fail": [
        #             # end of successful application process
        #         ]},
        #         {"try": rsi_email.applicant_review_type_change, "fail": []}
        #     ]},
        #     {"try": middleware.review_has_not_been_scheduled, "fail": [
        #         {"try": rsi_email.applicant_applied_at_icbc, "fail": []},
        #     ]},
        #     {"try": middleware.user_submitted_last_name_matches_vips, "fail": [
        #         {"try": rsi_email.applicant_last_name_mismatch, "fail": []}
        #     ]},
        #     {"try": middleware.is_applicant_within_window_to_apply, "fail": [
        #         {"try": rsi_email.applicant_prohibition_served_more_than_7_days_ago, "fail": []}
        #     ]},
        #     {"try": middleware.has_drivers_licence_been_seized, "fail": [
        #         {"try": rsi_email.applicant_licence_not_seized, "fail": []}
        #     ]},
        #     {"try": middleware.transform_hearing_request_type, "fail": []},
        #     {"try": middleware.force_presentation_type_to_written_if_ineligible_for_oral, "fail": []},
        #     {"try": middleware.transform_applicant_role_type, "fail": []},
        #     {"try": middleware.compress_form_data_xml, "fail": []},
        #     {"try": middleware.save_application_to_vips, "fail": [
        #         {"try": actions.add_to_failed_queue, "fail": []},
        #         {"try": rsi_email.admin_unable_to_save_to_vips, "fail": []}
        #     ]},
        #     {"try": splunk.application_accepted, "fail": []},
        #     {"try": common_splunk.log_to_splunk, "fail": []},
        #     {"try": rsi_email.application_accepted, "fail": []},
        #     {"try": ride_actions.app_accepted_event, "fail": []},
        #     {"try": middleware.is_applicant_ineligible_for_oral_review_but_requested_oral, "fail": [
        #         # end of successful application process
        #     ]},
        #     {"try": rsi_email.applicant_review_type_change, "fail": []}
        # ],
        # "Document_submission": [
        #     # aka: evidence submission form
        #     {"try": middleware.determine_current_datetime, "fail": []},
        #     {"try": middleware.get_data_from_document_submission_form, "fail": []},
        #     {"try": middleware.clean_prohibition_number, "fail": []},
        #     {"try": middleware.get_vips_status, "fail": []},
        #     {"try": middleware.prohibition_exists_in_vips, "fail": []},
        #     {"try": middleware.user_submitted_last_name_matches_vips, "fail": []},
        #     {"try": middleware.application_has_been_saved_to_vips, "fail": []},
        #     {"try": middleware.get_application_details, "fail": []},
        #     {"try": middleware.valid_application_received_from_vips, "fail": []},
        #     {"try": rsi_email.applicant_evidence_received, "fail": []},
        #     {"try": ride_actions.evidence_submitted, "fail": []},
        #     {"try": splunk.evidence_received, "fail": []},
        #     {"try": common_splunk.log_to_splunk, "fail": []},
        # ]
    }
