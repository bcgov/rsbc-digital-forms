from python.form_handler import actions, rsi_email


def load_event_actions() -> list:
  return [
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
            {"try": actions.get_storage_file, "fail": [
                {"try": actions.add_to_retry_queue, "fail": []},
                {"try": actions.update_event_status_hold, "fail": []},
            ]},
        ]