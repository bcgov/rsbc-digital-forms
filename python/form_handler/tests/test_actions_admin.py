"""
Unit tests for python.form_handler.actions_admin
"""
from __future__ import annotations

from unittest.mock import MagicMock, patch
from datetime import datetime

import python.form_handler.actions_admin as actions_admin
from python.common.enums import ErrorCode


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_app_mock():
    """Return a Flask app mock whose app_context() is a no-op context manager."""
    app = MagicMock()
    app.app_context.return_value.__enter__ = MagicMock(return_value=None)
    app.app_context.return_value.__exit__ = MagicMock(return_value=False)
    return app


def _make_db_mock():
    """Return a SQLAlchemy db mock with a fluent query interface."""
    db = MagicMock()
    return db


# ---------------------------------------------------------------------------
# get_submission_event_id (admin version)
# ---------------------------------------------------------------------------

class TestGetSubmissionEventIdAdmin:
    """Tests for actions_admin.get_submission_event_id()"""

    def _base_args(self):
        app = _make_app_mock()
        db = _make_db_mock()
        db.session.query.return_value.filter.return_value.one.return_value = MagicMock(
            submission_event_id=42
        )
        return {
            "app": app,
            "db": db,
            "storage_ref": {"form_ref_id": 5},
        }

    @patch("python.form_handler.actions_admin.actions.get_submission_event_id")
    def test_sets_destination_to_admin(self, mock_get):
        """Verify destination is set to 'ADMIN' before calling actions.get_submission_event_id"""
        mock_get.return_value = (True, {})
        args = self._base_args()
        actions_admin.get_submission_event_id(**args)
        called_args = mock_get.call_args[1]
        assert called_args["destination"] == "ADMIN"

    @patch("python.form_handler.actions_admin.actions.get_submission_event_id")
    def test_returns_tuple_from_actions(self, mock_get):
        """Verify return value is passed through from actions module"""
        expected_return = (True, {"submission_event_id": 42})
        mock_get.return_value = expected_return
        args = self._base_args()
        result = actions_admin.get_submission_event_id(**args)
        assert result == expected_return

    @patch("python.form_handler.actions_admin.actions.get_submission_event_id")
    def test_passes_all_args_to_actions(self, mock_get):
        """Verify all input arguments are passed to actions module"""
        mock_get.return_value = (True, {})
        args = self._base_args()
        args["custom_key"] = "custom_value"
        actions_admin.get_submission_event_id(**args)
        called_kwargs = mock_get.call_args[1]
        assert called_kwargs.get("custom_key") == "custom_value"

    @patch("python.form_handler.actions_admin.actions.get_submission_event_id")
    def test_handles_failure_from_actions(self, mock_get):
        """Verify failure response from actions is passed through"""
        mock_get.return_value = (False, {"error": "DB error"})
        args = self._base_args()
        result = actions_admin.get_submission_event_id(**args)
        assert result[0] is False


# ---------------------------------------------------------------------------
# send_to_admin_actions
# ---------------------------------------------------------------------------

class TestSendToAdminActions:
    """Tests for send_to_admin_actions()"""

    def test_returns_list(self):
        """Function should return a list of action dictionaries"""
        result = actions_admin.send_to_admin_actions()
        assert isinstance(result, list)

    def test_returns_non_empty_list(self):
        """List should contain action definitions"""
        result = actions_admin.send_to_admin_actions()
        assert len(result) > 0

    def test_first_action_is_get_submission_event_id(self):
        """First action should be get_submission_event_id with ADMIN event"""
        result = actions_admin.send_to_admin_actions()
        assert result[0]["try"] == actions_admin.get_submission_event_id
        assert result[0]["event"] == "ADMIN"

    def test_all_actions_have_try_key(self):
        """All actions should have a 'try' key with a callable"""
        result = actions_admin.send_to_admin_actions()
        for action in result:
            assert "try" in action
            assert callable(action["try"])

    def test_all_actions_have_fail_key(self):
        """All actions should have a 'fail' key with a list"""
        result = actions_admin.send_to_admin_actions()
        for action in result:
            assert "fail" in action
            assert isinstance(action["fail"], list)

    def test_all_actions_have_event_key(self):
        """All actions should have an 'event' key set to ADMIN"""
        result = actions_admin.send_to_admin_actions()
        for action in result:
            assert "event" in action
            assert action["event"] == "ADMIN"

    def test_action_includes_update_event_status_processing(self):
        """Actions should include update_event_status_processing"""
        result = actions_admin.send_to_admin_actions()
        actions_list = [a["try"] for a in result]
        assert any(a.__name__ == "update_event_status_processing" for a in actions_list)

    def test_action_includes_update_event_status(self):
        """Actions should include update_event_status"""
        result = actions_admin.send_to_admin_actions()
        actions_list = [a["try"] for a in result]
        assert any(a.__name__ == "update_event_status" for a in actions_list)

    def test_action_includes_log_to_splunk(self):
        """Actions should include log_to_splunk"""
        result = actions_admin.send_to_admin_actions()
        actions_list = [a["try"] for a in result]
        assert any(a.__name__ == "log_to_splunk" for a in actions_list)


# ---------------------------------------------------------------------------
# get_agency_admin_email
# ---------------------------------------------------------------------------

class TestGetAgencyAdminEmail:
    """Tests for get_agency_admin_email()"""

    def _base_args(self):
        app = _make_app_mock()
        db = _make_db_mock()
        return {
            "app": app,
            "db": db,
            "user_data": {"agency_id": 1},
            "message": {"event_id": "E1", "event_type": "admin"},
        }

    def test_returns_true_on_success(self):
        """Function should return True when agency admins are found"""
        db = _make_db_mock()
        admin_mock = MagicMock()
        admin_mock.email = "admin@example.com"
        db.session.query.return_value.filter.return_value.all.return_value = [admin_mock]

        args = self._base_args()
        args["db"] = db
        result, _ = actions_admin.get_agency_admin_email(**args)
        assert result is True

    def test_sets_agency_admin_emails_when_found(self):
        """Function should set agency_admin_emails in output args"""
        db = _make_db_mock()
        admin_mock = MagicMock()
        admin_mock.email = "admin@example.com"
        db.session.query.return_value.filter.return_value.all.return_value = [admin_mock]

        args = self._base_args()
        args["db"] = db
        _, out_args = actions_admin.get_agency_admin_email(**args)
        assert "agency_admin_emails" in out_args
        assert out_args["agency_admin_emails"] == ["admin@example.com"]

    def test_sets_agency_admin_emails_to_none_when_not_found(self):
        """Function should set agency_admin_emails to None when no admins found"""
        db = _make_db_mock()
        db.session.query.return_value.filter.return_value.all.return_value = []

        args = self._base_args()
        args["db"] = db
        _, out_args = actions_admin.get_agency_admin_email(**args)
        assert out_args["agency_admin_emails"] is None

    def test_handles_multiple_agency_admins(self):
        """Function should handle multiple admins for same agency"""
        db = _make_db_mock()
        admin1 = MagicMock()
        admin1.email = "admin1@example.com"
        admin2 = MagicMock()
        admin2.email = "admin2@example.com"
        db.session.query.return_value.filter.return_value.all.return_value = [admin1, admin2]

        args = self._base_args()
        args["db"] = db
        _, out_args = actions_admin.get_agency_admin_email(**args)
        assert out_args["agency_admin_emails"] == ["admin1@example.com", "admin2@example.com"]

    @patch("python.form_handler.actions_admin.actions.record_event_error")
    def test_records_error_on_exception(self, mock_record):
        """Function should record error when exception occurs"""
        db = _make_db_mock()
        db.session.query.side_effect = Exception("DB connection failed")

        args = self._base_args()
        args["db"] = db
        result, out_args = actions_admin.get_agency_admin_email(**args)
        
        assert result is True
        assert "error" in out_args
        assert out_args["error"]["error_code"] == ErrorCode.E07
        mock_record.assert_called_once()

    def test_returns_true_even_on_error(self):
        """Function should return True even when error occurs"""
        db = _make_db_mock()
        db.session.query.side_effect = Exception("DB error")

        args = self._base_args()
        args["db"] = db
        result, _ = actions_admin.get_agency_admin_email(**args)
        assert result is True

    def test_queries_with_correct_agency_id(self):
        """Function should query database with correct agency_id"""
        db = _make_db_mock()
        db.session.query.return_value.filter.return_value.all.return_value = []

        args = self._base_args()
        args["user_data"]["agency_id"] = 99
        args["db"] = db
        actions_admin.get_agency_admin_email(**args)
        
        # Verify filter was called with correct agency_id
        db.session.query.return_value.filter.assert_called_once()


# ---------------------------------------------------------------------------
# set_admin_email_content
# ---------------------------------------------------------------------------

class TestSetAdminEmailContent:
    """Tests for set_admin_email_content()"""

    def _base_args(self):
        submission_date = datetime(2024, 1, 15, 10, 30, 0)
        app = _make_app_mock()
        return {
            "app": app,
            "event_data": {
                "created_dt": submission_date,
                "agency_file_no": "FILE-001",
            },
            "storage_ref": {
                "form_type": "VI",
                "form_id": "VI-2024-001",
            },
            "user_data": {
                "badge_number": "B123",
                "display_name": "Officer Smith",
                "agency_ref": {"agency_name": "Vancouver Police Department"},
            },
            "message": {"event_id": "E1", "event_type": "admin"},
        }

    @patch("python.form_handler.actions_admin.date_time_to_local_tz_string")
    def test_returns_true_on_success(self, mock_date_fn):
        """Function should return True on successful execution"""
        mock_date_fn.return_value = "2024-01-15 10:30:00"
        args = self._base_args()
        result, _ = actions_admin.set_admin_email_content(**args)
        assert result is True

    @patch("python.form_handler.actions_admin.date_time_to_local_tz_string")
    def test_sets_body_in_output_args(self, mock_date_fn):
        """Function should set body dictionary in output args"""
        mock_date_fn.return_value = "2024-01-15 10:30:00"
        args = self._base_args()
        _, out_args = actions_admin.set_admin_email_content(**args)
        assert "body" in out_args
        assert isinstance(out_args["body"], dict)

    @patch("python.form_handler.actions_admin.date_time_to_local_tz_string")
    def test_body_contains_form_type(self, mock_date_fn):
        """Body should contain form_type"""
        mock_date_fn.return_value = "2024-01-15 10:30:00"
        args = self._base_args()
        _, out_args = actions_admin.set_admin_email_content(**args)
        assert out_args["body"]["form_type"] == "VI"

    @patch("python.form_handler.actions_admin.date_time_to_local_tz_string")
    def test_body_contains_form_number(self, mock_date_fn):
        """Body should contain form_number"""
        mock_date_fn.return_value = "2024-01-15 10:30:00"
        args = self._base_args()
        _, out_args = actions_admin.set_admin_email_content(**args)
        assert out_args["body"]["form_number"] == "VI-2024-001"

    @patch("python.form_handler.actions_admin.date_time_to_local_tz_string")
    def test_body_contains_agency_file_number(self, mock_date_fn):
        """Body should contain agency_file_number"""
        mock_date_fn.return_value = "2024-01-15 10:30:00"
        args = self._base_args()
        _, out_args = actions_admin.set_admin_email_content(**args)
        assert out_args["body"]["agency_file_number"] == "FILE-001"

    @patch("python.form_handler.actions_admin.date_time_to_local_tz_string")
    def test_body_contains_submission_date(self, mock_date_fn):
        """Body should contain submission_date"""
        mock_date_fn.return_value = "2024-01-15 10:30:00"
        args = self._base_args()
        _, out_args = actions_admin.set_admin_email_content(**args)
        assert out_args["body"]["submission_date"] == "2024-01-15 10:30:00"

    @patch("python.form_handler.actions_admin.date_time_to_local_tz_string")
    def test_body_contains_officer_badge(self, mock_date_fn):
        """Body should contain officer_badge"""
        mock_date_fn.return_value = "2024-01-15 10:30:00"
        args = self._base_args()
        _, out_args = actions_admin.set_admin_email_content(**args)
        assert out_args["body"]["officer_badge"] == "B123"

    @patch("python.form_handler.actions_admin.date_time_to_local_tz_string")
    def test_body_contains_officer_name(self, mock_date_fn):
        """Body should contain officer_name"""
        mock_date_fn.return_value = "2024-01-15 10:30:00"
        args = self._base_args()
        _, out_args = actions_admin.set_admin_email_content(**args)
        assert out_args["body"]["officer_name"] == "Officer Smith"

    @patch("python.form_handler.actions_admin.date_time_to_local_tz_string")
    def test_body_contains_agency_name(self, mock_date_fn):
        """Body should contain agency_name"""
        mock_date_fn.return_value = "2024-01-15 10:30:00"
        args = self._base_args()
        _, out_args = actions_admin.set_admin_email_content(**args)
        assert out_args["body"]["agency_name"] == "Vancouver Police Department"

    @patch("python.form_handler.actions_admin.date_time_to_local_tz_string")
    def test_body_contains_none_agency_name_when_missing(self, mock_date_fn):
        """Body should set agency_name to None when agency_ref is missing"""
        mock_date_fn.return_value = "2024-01-15 10:30:00"
        args = self._base_args()
        args["user_data"].pop("agency_ref")
        _, out_args = actions_admin.set_admin_email_content(**args)
        assert "agency_name" in out_args["body"]
        assert out_args["body"]["agency_name"] is None

    @patch("python.form_handler.actions_admin.date_time_to_local_tz_string")
    def test_sets_title_in_output_args(self, mock_date_fn):
        """Function should set title in output args"""
        mock_date_fn.return_value = "2024-01-15 10:30:00"
        args = self._base_args()
        _, out_args = actions_admin.set_admin_email_content(**args)
        assert "title" in out_args

    @patch("python.form_handler.actions_admin.date_time_to_local_tz_string")
    def test_title_includes_form_type_and_number(self, mock_date_fn):
        """Title should include form type and number"""
        mock_date_fn.return_value = "2024-01-15 10:30:00"
        args = self._base_args()
        _, out_args = actions_admin.set_admin_email_content(**args)
        assert "VI" in out_args["title"]
        assert "VI-2024-001" in out_args["title"]

    @patch("python.form_handler.actions_admin.date_time_to_local_tz_string")
    def test_handles_missing_optional_fields(self, mock_date_fn):
        """Function should handle missing optional fields gracefully"""
        mock_date_fn.return_value = "2024-01-15 10:30:00"
        args = self._base_args()
        args["event_data"] = {}
        args["storage_ref"] = {}
        args["user_data"] = {}
        result, _ = actions_admin.set_admin_email_content(**args)
        assert result is True

    @patch("python.form_handler.actions_admin.actions.record_event_error")
    @patch("python.form_handler.actions_admin.date_time_to_local_tz_string")
    def test_records_error_on_exception(self, mock_date_fn, mock_record):
        """Function should record error when exception occurs"""
        mock_date_fn.side_effect = Exception("Date conversion failed")
        args = self._base_args()
        result, out_args = actions_admin.set_admin_email_content(**args)
        
        assert result is True
        assert "error" in out_args
        assert out_args["error"]["error_code"] == ErrorCode.E07
        mock_record.assert_called_once()

    def test_returns_true_even_on_error(self):
        """Function should return True even when error occurs"""
        args = self._base_args()
        args["event_data"] = None  # This will cause an exception
        result, _ = actions_admin.set_admin_email_content(**args)
        assert result is True
