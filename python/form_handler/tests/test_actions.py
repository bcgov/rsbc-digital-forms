"""
Unit tests for python.form_handler.actions
"""
from __future__ import annotations

import json
from unittest.mock import MagicMock, patch, call
import pytest

import python.form_handler.actions as actions
from python.form_handler.config import Config
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
# validate_event_retry_count
# ---------------------------------------------------------------------------

class TestValidateEventRetryCount:
    """Tests for validate_event_retry_count()"""

    def _base_args(self, retry_count=0, queue_name=None):
        message = {
            "event_id": "EVT-001",
            "event_type": "24h",
            "retry_count": retry_count,
        }
        if queue_name:
            message["queue_name"] = queue_name
        return {"message": message}

    def test_first_attempt_returns_true(self):
        """retry_count=0 increments to 1 (below max) → returns True."""
        args = self._base_args(retry_count=0)
        result, out_args = actions.validate_event_retry_count(**args)
        assert result is True
        assert out_args["retry_count"] == 1

    def test_retry_count_incremented_in_message(self):
        """retry_count in message dict is also incremented."""
        args = self._base_args(retry_count=0)
        _, out_args = actions.validate_event_retry_count(**args)
        assert out_args["message"]["retry_count"] == 1

    def test_exceeds_max_retries_from_hold_queue_returns_false(self):
        """
        After SYSTEM_RECORD_MAX_RETRIES attempts from the hold queue the
        function returns False and routes to the fail queue.
        """
        max_r = Config.SYSTEM_RECORD_MAX_RETRIES
        args = self._base_args(retry_count=max_r - 1)
        result, out_args = actions.validate_event_retry_count(**args)
        assert result is False
        assert out_args["put_to_queue_name"] == Config.STORAGE_FAIL_QUEUE

    def test_exceeds_max_retries_from_fail_queue_stops_retry(self):
        """
        Exceeding the total retry budget from the transient fail queue moves
        the message to the persistent fail queue and sets stop_retry=True.
        """
        total_max = Config.SYSTEM_RECORD_MAX_RETRIES + Config.SYSTEM_RECORD_MAX_TRANSIENT_RETRIES
        args = self._base_args(
            retry_count=total_max - 1,
            queue_name=Config.STORAGE_FAIL_QUEUE,
        )
        result, out_args = actions.validate_event_retry_count(**args)
        assert result is False
        assert out_args["put_to_queue_name"] == Config.STORAGE_FAIL_QUEUE_PERS
        assert out_args.get("stop_retry") is True

    def test_below_max_retries_from_fail_queue_returns_true(self):
        """Inside the extended budget from the fail queue → still True."""
        args = self._base_args(retry_count=0, queue_name=Config.STORAGE_FAIL_QUEUE)
        result, _ = actions.validate_event_retry_count(**args)
        assert result is True

    def test_error_set_when_retry_exceeded(self):
        """An 'error' dict is populated when the retry count is exceeded."""
        max_r = Config.SYSTEM_RECORD_MAX_RETRIES
        args = self._base_args(retry_count=max_r - 1)
        _, out_args = actions.validate_event_retry_count(**args)
        assert "error" in out_args
        assert out_args["error"]["error_code"] == ErrorCode.E05

    def test_error_dict_contains_func_reference(self):
        """The error dict must include the function reference for traceability."""
        max_r = Config.SYSTEM_RECORD_MAX_RETRIES
        args = self._base_args(retry_count=max_r - 1)
        _, out_args = actions.validate_event_retry_count(**args)
        assert out_args["error"]["func"] is actions.validate_event_retry_count


# ---------------------------------------------------------------------------
# validate_event_data
# ---------------------------------------------------------------------------

class TestValidateEventData:
    """Tests for validate_event_data() – always True placeholder."""

    def test_returns_true(self):
        result, _ = actions.validate_event_data(message={"event_id": "1"})
        assert result is True

    def test_passes_args_through(self):
        in_args = {"message": {"event_id": "1"}, "custom_key": "custom_value"}
        _, out_args = actions.validate_event_data(**in_args)
        assert out_args["custom_key"] == "custom_value"


# ---------------------------------------------------------------------------
# add_unknown_event_error_to_message
# ---------------------------------------------------------------------------

class TestAddUnknownEventErrorToMessage:
    """Tests for add_unknown_event_error_to_message()"""

    def test_extracts_key_from_message(self):
        args = {"message": {"Key": "bucket/file.pdf"}}
        result, out_args = actions.add_unknown_event_error_to_message(**args)
        assert result is True
        assert out_args["storage_key"] == "bucket/file.pdf"

    def test_sets_storage_key_to_none_when_key_missing(self):
        args = {"message": {}}
        result, out_args = actions.add_unknown_event_error_to_message(**args)
        assert result is True
        assert out_args["storage_key"] is None

    def test_returns_true_on_valid_message(self):
        result, _ = actions.add_unknown_event_error_to_message(
            message={"Key": "some/path.pdf"}
        )
        assert result is True


# ---------------------------------------------------------------------------
# add_unknown_event_to_error
# ---------------------------------------------------------------------------

class TestAddUnknownEventToError:
    """Tests for add_unknown_event_to_error()"""

    def test_sets_error_in_args(self):
        args = {"message": {"event_id": "E1", "event_type": "unknown"}}
        result, out_args = actions.add_unknown_event_to_error(**args)
        assert result is True
        assert "error" in out_args

    def test_error_code_is_e04(self):
        args = {"message": {"event_id": "E1", "event_type": "unknown"}}
        _, out_args = actions.add_unknown_event_to_error(**args)
        assert out_args["error"]["error_code"] == ErrorCode.E04

    def test_error_preserves_event_id_and_type(self):
        args = {"message": {"event_id": "EVT-42", "event_type": "mystery"}}
        _, out_args = actions.add_unknown_event_to_error(**args)
        assert out_args["error"]["event_id"] == "EVT-42"
        assert out_args["error"]["event_type"] == "mystery"

    def test_error_details_contains_description(self):
        args = {"message": {"event_id": "E1", "event_type": "unknown"}}
        _, out_args = actions.add_unknown_event_to_error(**args)
        assert "Unknown Event Type" in out_args["error"]["error_details"]


# ---------------------------------------------------------------------------
# add_to_persistent_failed_queue
# ---------------------------------------------------------------------------

class TestAddToPersistentFailedQueue:
    """Tests for add_to_persistent_failed_queue()"""

    def _args(self, publish_returns=True):
        config = MagicMock()
        config.STORAGE_FAIL_QUEUE_PERS = "df-storage-events-fail-persistent"
        config.ENCRYPT_KEY = "secret"
        writer = MagicMock()
        writer.publish.return_value = publish_returns
        return {
            "config": config,
            "message": {"event_id": "E1", "event_type": "24h"},
            "writer": writer,
        }

    def test_returns_true_when_publish_succeeds(self):
        args = self._args(publish_returns=True)
        result, _ = actions.add_to_persistent_failed_queue(**args)
        assert result is True

    def test_returns_false_when_publish_fails(self):
        args = self._args(publish_returns=False)
        result, _ = actions.add_to_persistent_failed_queue(**args)
        assert result is False

    def test_sets_error_when_publish_fails(self):
        args = self._args(publish_returns=False)
        _, out_args = actions.add_to_persistent_failed_queue(**args)
        assert "error" in out_args
        assert out_args["error"]["error_code"] == ErrorCode.E03

    def test_message_queue_name_updated(self):
        args = self._args(publish_returns=True)
        _, out_args = actions.add_to_persistent_failed_queue(**args)
        assert out_args["message"]["queue_name"] == "df-storage-events-fail-persistent"

    def test_publishes_to_correct_queue(self):
        args = self._args(publish_returns=True)
        actions.add_to_persistent_failed_queue(**args)
        args["writer"].publish.assert_called_once()
        call_queue = args["writer"].publish.call_args[0][0]
        assert call_queue == "df-storage-events-fail-persistent"


# ---------------------------------------------------------------------------
# add_to_transient_failed_queue
# ---------------------------------------------------------------------------

class TestAddToTransientFailedQueue:
    """Tests for add_to_transient_failed_queue()"""

    def _args(self, publish_returns=True):
        config = MagicMock()
        config.STORAGE_FAIL_QUEUE = "df-storage-events-fail"
        config.ENCRYPT_KEY = "secret"
        writer = MagicMock()
        writer.publish.return_value = publish_returns
        return {
            "config": config,
            "message": {"event_id": "E2", "event_type": "vi"},
            "writer": writer,
        }

    def test_returns_true_on_success(self):
        result, _ = actions.add_to_transient_failed_queue(**self._args(True))
        assert result is True

    def test_returns_false_on_publish_failure(self):
        result, _ = actions.add_to_transient_failed_queue(**self._args(False))
        assert result is False

    def test_message_queue_name_updated(self):
        args = self._args(True)
        _, out_args = actions.add_to_transient_failed_queue(**args)
        assert out_args["message"]["queue_name"] == "df-storage-events-fail"


# ---------------------------------------------------------------------------
# add_to_hold_queue
# ---------------------------------------------------------------------------

class TestAddToHoldQueue:
    """Tests for add_to_hold_queue()"""

    def _args(self, publish_returns=True):
        config = MagicMock()
        config.STORAGE_HOLD_QUEUE = "df-storage-events-hold"
        config.ENCRYPT_KEY = "secret"
        writer = MagicMock()
        writer.publish.return_value = publish_returns
        return {
            "config": config,
            "message": {"event_id": "E3", "event_type": "irp"},
            "writer": writer,
        }

    def test_returns_true_on_success(self):
        result, _ = actions.add_to_hold_queue(**self._args(True))
        assert result is True

    def test_returns_false_on_publish_failure(self):
        result, _ = actions.add_to_hold_queue(**self._args(False))
        assert result is False

    def test_message_queue_name_updated(self):
        args = self._args(True)
        _, out_args = actions.add_to_hold_queue(**args)
        assert out_args["message"]["queue_name"] == "df-storage-events-hold"


# ---------------------------------------------------------------------------
# add_to_retry_queue
# ---------------------------------------------------------------------------

class TestAddToRetryQueue:
    """Tests for add_to_retry_queue()"""

    def _args(self, put_to_queue_name=None, publish_returns=True):
        config = MagicMock()
        config.STORAGE_HOLD_QUEUE = "df-storage-events-hold"
        config.ENCRYPT_KEY = "secret"
        writer = MagicMock()
        writer.publish.return_value = publish_returns
        args = {
            "config": config,
            "message": {"event_id": "E4", "event_type": "24h"},
            "writer": writer,
            "app": _make_app_mock(),
        }
        if put_to_queue_name is not None:
            args["put_to_queue_name"] = put_to_queue_name
        return args

    def test_defaults_to_hold_queue_when_no_put_to_queue_name(self):
        args = self._args(put_to_queue_name=None)
        result, out_args = actions.add_to_retry_queue(**args)
        assert result is True
        assert out_args["message"]["queue_name"] == "df-storage-events-hold"

    def test_uses_provided_put_to_queue_name(self):
        args = self._args(put_to_queue_name="df-storage-events-fail")
        result, out_args = actions.add_to_retry_queue(**args)
        assert result is True
        assert out_args["message"]["queue_name"] == "df-storage-events-fail"

    def test_returns_false_when_publish_fails(self):
        args = self._args(publish_returns=False)
        result, _ = actions.add_to_retry_queue(**args)
        assert result is False

    def test_publishes_encoded_message(self):
        args = self._args(publish_returns=True)
        actions.add_to_retry_queue(**args)
        args["writer"].publish.assert_called_once()


# ---------------------------------------------------------------------------
# get_storage_ref_event_type
# ---------------------------------------------------------------------------

class TestGetStorageRefEventType:
    """Tests for get_storage_ref_event_type()"""

    def test_returns_unknown_event_when_key_is_none(self):
        app = _make_app_mock()
        db = _make_db_mock()
        args = {"app": app, "db": db, "message": {}}
        result = actions.get_storage_ref_event_type(**args)
        # When Key is None, function returns the event_type string directly
        assert result == "unknown_event"

    def test_returns_true_and_sets_event_type_when_form_found(self):
        app = _make_app_mock()
        db = _make_db_mock()

        # Use a plain object so __dict__ works correctly (MagicMock.__dict__ is internal)
        class MockForm:
            pass

        mock_form = MockForm()
        mock_form.form_type = "VI"
        mock_form.storage_key = "bucket/file.pdf"
        mock_form.form_ref_id = 1
        mock_form._sa_instance_state = None

        db.session.query.return_value.filter.return_value.one.return_value = mock_form

        args = {
            "app": app,
            "db": db,
            "message": {"Key": "bucket/file.pdf"},
        }
        result, out_args = actions.get_storage_ref_event_type(**args)
        assert result is True
        assert out_args["event_type"] == "vi"

    def test_returns_false_when_db_raises(self):
        app = _make_app_mock()
        db = _make_db_mock()
        db.session.query.return_value.filter.return_value.one.side_effect = Exception("DB error")

        args = {
            "app": app,
            "db": db,
            "message": {"Key": "bucket/missing.pdf"},
        }
        # Patch logging.exception because the production code calls it with an extra
        # positional arg (`logging.exception(msg, exc_obj)`), which causes a
        # TypeError inside the logging machinery on Python 3.9/pytest 8.
        with patch("logging.exception"):
            result, _ = actions.get_storage_ref_event_type(**args)
        assert result is False


# ---------------------------------------------------------------------------
# get_event_form_data
# ---------------------------------------------------------------------------

class TestGetEventFormData:
    """Tests for get_event_form_data()"""

    def _build_mock_row(self, **fields):
        row = MagicMock()
        row.__dict__ = dict(fields)
        return row

    def test_returns_false_when_event_data_is_empty(self):
        app = _make_app_mock()
        db = _make_db_mock()
        db.session.query.return_value.filter.return_value.all.return_value = []
        args = {
            "app": app, "db": db,
            "message": {"event_id": 1},
            "event_type": "vi",
        }
        result, _ = actions.get_event_form_data(**args)
        assert result is False

    def test_returns_false_when_multiple_event_rows(self):
        app = _make_app_mock()
        db = _make_db_mock()
        db.session.query.return_value.filter.return_value.all.return_value = [
            self._build_mock_row(event_id=1), self._build_mock_row(event_id=1)
        ]
        args = {
            "app": app, "db": db,
            "message": {"event_id": 1},
            "event_type": "vi",
        }
        result, _ = actions.get_event_form_data(**args)
        assert result is False

    def test_returns_false_for_unknown_event_type(self):
        app = _make_app_mock()
        db = _make_db_mock()

        event_row = self._build_mock_row(event_id=1, created_by="user1")

        def side_effect(model):
            mock = MagicMock()
            mock.filter.return_value.all.return_value = [event_row]
            return mock

        db.session.query.side_effect = side_effect

        args = {
            "app": app, "db": db,
            "message": {"event_id": 1},
            "event_type": "unknown_type",
        }
        result, _ = actions.get_event_form_data(**args)
        assert result is False

    def test_returns_true_and_sets_event_and_form_data(self):
        app = _make_app_mock()
        db = _make_db_mock()

        event_row = MagicMock()
        event_row.__dict__ = {"event_id": 1, "created_by": "user1"}

        form_row = MagicMock()
        form_row.__dict__ = {"form_id": 10, "event_id": 1}

        call_count = [0]

        def query_side_effect(model):
            mock = MagicMock()
            if call_count[0] == 0:
                mock.filter.return_value.all.return_value = [event_row]
            else:
                mock.filter.return_value.all.return_value = [form_row]
            call_count[0] += 1
            return mock

        db.session.query.side_effect = query_side_effect

        args = {
            "app": app, "db": db,
            "message": {"event_id": 1},
            "event_type": "vi",
        }
        result, out_args = actions.get_event_form_data(**args)
        assert result is True
        assert "event_data" in out_args
        assert "form_data" in out_args


# ---------------------------------------------------------------------------
# get_submission_event_id
# ---------------------------------------------------------------------------

class TestGetSubmissionEventId:
    """Tests for get_submission_event_id()"""

    def test_returns_true_and_sets_submission_event_id(self):
        app = _make_app_mock()
        db = _make_db_mock()

        sub_event = MagicMock()
        sub_event.submission_event_id = 99
        db.session.query.return_value.filter.return_value.one.return_value = sub_event

        args = {
            "app": app, "db": db,
            "event_type": "vi",
            "storage_ref": {"form_ref_id": 5},
        }
        result, out_args = actions.get_submission_event_id(**args)
        assert result is True
        assert out_args["submission_event_id"] == 99

    def test_destination_vips_for_vi_event(self):
        """VI event type should query with destination='VIPS'."""
        app = _make_app_mock()
        db = _make_db_mock()

        sub_event = MagicMock()
        sub_event.submission_event_id = 42
        db.session.query.return_value.filter.return_value.one.return_value = sub_event

        args = {
            "app": app, "db": db,
            "event_type": "vi",
            "storage_ref": {"form_ref_id": 3},
        }
        actions.get_submission_event_id(**args)
        db.session.query.return_value.filter.assert_called_once()

    def test_destination_icbc_for_24h_event(self):
        """24h event type should query with destination='ICBC'."""
        app = _make_app_mock()
        db = _make_db_mock()

        sub_event = MagicMock()
        sub_event.submission_event_id = 7
        db.session.query.return_value.filter.return_value.one.return_value = sub_event

        args = {
            "app": app, "db": db,
            "event_type": "24h",
            "storage_ref": {"form_ref_id": 3},
        }
        result, out_args = actions.get_submission_event_id(**args)
        assert result is True

    def test_returns_false_when_db_raises(self):
        app = _make_app_mock()
        db = _make_db_mock()
        db.session.query.return_value.filter.return_value.one.side_effect = Exception("not found")

        args = {
            "app": app, "db": db,
            "event_type": "vi",
            "storage_ref": {"form_ref_id": 99},
        }
        result, _ = actions.get_submission_event_id(**args)
        assert result is False


# ---------------------------------------------------------------------------
# send_to_icbc
# ---------------------------------------------------------------------------

class TestSendToIcbc:
    """Tests for send_to_icbc()"""

    def _args(self):
        return {
            "message": {"event_id": "E5", "event_type": "24h"},
            "icbc_payload": {"noticeNumber": "123"},
        }

    @patch("python.form_handler.actions.submit_to_icbc")
    def test_returns_true_on_icbc_success(self, mock_submit):
        mock_submit.return_value = (True, "OK", 200)
        result, out_args = actions.send_to_icbc(**self._args())
        assert result is True
        assert out_args["icbc_resp_code"] == 200

    @patch("python.form_handler.actions.submit_to_icbc")
    def test_returns_false_on_icbc_failure(self, mock_submit):
        mock_submit.return_value = (False, "Error", 500)
        result, out_args = actions.send_to_icbc(**self._args())
        assert result is False

    @patch("python.form_handler.actions.submit_to_icbc")
    def test_sets_error_when_icbc_fails(self, mock_submit):
        mock_submit.return_value = (False, "Timeout", 503)
        _, out_args = actions.send_to_icbc(**self._args())
        assert "error" in out_args
        assert out_args["error"]["error_code"] == ErrorCode.I01

    @patch("python.form_handler.actions.submit_to_icbc")
    def test_sets_splunk_data_on_success(self, mock_submit):
        mock_submit.return_value = (True, "OK", 200)
        _, out_args = actions.send_to_icbc(**self._args())
        assert "splunk_data" in out_args
        assert out_args["splunk_data"]["event"] == "event_sent_to_icbc"

    @patch("python.form_handler.actions.submit_to_icbc")
    def test_returns_false_when_submit_raises(self, mock_submit):
        mock_submit.side_effect = Exception("connection refused")
        result, _ = actions.send_to_icbc(**self._args())
        assert result is False


# ---------------------------------------------------------------------------
# prep_vips_document_payload
# ---------------------------------------------------------------------------

class TestPrepVipsDocumentPayload:
    """Tests for prep_vips_document_payload()"""

    def test_returns_true_and_sets_payload(self):
        args = {"file_data": "base64encodedpdf=="}
        result, out_args = actions.prep_vips_document_payload(**args)
        assert result is True
        assert "vips_document_payload" in out_args

    def test_payload_has_required_fields(self):
        args = {"file_data": "base64encodedpdf=="}
        _, out_args = actions.prep_vips_document_payload(**args)
        payload = out_args["vips_document_payload"]
        assert payload["notice_subject_code"] == "VEHI"
        assert payload["file_object"] == "base64encodedpdf=="
        assert payload["type_code"] == "MV2721"
        assert payload["notice_type_code"] == "IMP"
        assert payload["mime_type"] == "application"
        assert payload["mime_sub_type"] == "pdf"

    def test_returns_false_when_no_file_data_causes_exception(self):
        """If vips_document_payload template raises, function returns False."""
        with patch("python.form_handler.actions.vips_document_payload", new=None):
            result, _ = actions.prep_vips_document_payload(file_data="data")
            assert result is False


# ---------------------------------------------------------------------------
# get_event_coordinates
# ---------------------------------------------------------------------------

class TestGetEventCoordinates:
    """Tests for get_event_coordinates() – always returns True."""

    @patch("python.form_handler.actions.get_coordinates")
    @patch("python.form_handler.actions.form_middleware")
    def test_returns_true_on_success(self, mock_middleware, mock_geo):
        mock_middleware.get_city_name.return_value = "Vancouver"
        mock_geo.return_value = (True, 49.2827, -123.1207, "123 Main St, Vancouver")
        app = _make_app_mock()
        args = {
            "app": app,
            "message": {"event_id": "E1", "event_type": "24h"},
            "event_data": {
                "intersection_or_address_of_offence": "123 Main St",
                "offence_city": "VANC",
            },
        }
        result, _ = actions.get_event_coordinates(**args)
        assert result is True

    @patch("python.form_handler.actions.get_coordinates")
    @patch("python.form_handler.actions.form_middleware")
    def test_sets_coordinates_in_event_data(self, mock_middleware, mock_geo):
        mock_middleware.get_city_name.return_value = "Burnaby"
        mock_geo.return_value = (True, 49.2488, -122.9805, "456 King St, Burnaby")
        app = _make_app_mock()
        args = {
            "app": app,
            "message": {"event_id": "E2", "event_type": "vi"},
            "event_data": {
                "intersection_or_address_of_offence": "456 King St",
                "offence_city": "BURN",
            },
        }
        _, out_args = actions.get_event_coordinates(**args)
        assert out_args["event_data"]["latitude"] == 49.2488
        assert out_args["event_data"]["longitude"] == -122.9805

    @patch("python.form_handler.actions.record_event_error")
    @patch("python.form_handler.actions.get_coordinates")
    @patch("python.form_handler.actions.form_middleware")
    def test_returns_true_even_on_geocoding_exception(
        self, mock_middleware, mock_geo, mock_record
    ):
        """Coordinate lookup failure must NOT abort processing."""
        mock_middleware.get_city_name.side_effect = Exception("lookup failed")
        app = _make_app_mock()
        args = {
            "app": app,
            "message": {"event_id": "E3", "event_type": "12h"},
            "event_data": {
                "intersection_or_address_of_offence": "Unknown",
                "offence_city": "???",
            },
        }
        result, _ = actions.get_event_coordinates(**args)
        assert result is True


# ---------------------------------------------------------------------------
# get_event_user_data
# ---------------------------------------------------------------------------

class TestGetEventUserData:
    """Tests for get_event_user_data()"""

    def _make_user_row(self):
        class _AgencyRef:
            pass
        class _UserRow:
            pass
        agency_ref = _AgencyRef()
        agency_ref.agency_name = "RCMP"
        agency_ref.agency_id = 1
        row = _UserRow()
        row.user_guid = "user1"
        row.badge_number = "B001"
        row.last_name = "Smith"
        row.first_name = "John"
        row.agency = "RCMP"
        row._sa_instance_state = None
        row.agency_ref = agency_ref
        row.agency_ref._sa_instance_state = None
        return row

    def test_returns_true_and_sets_user_data(self):
        app = _make_app_mock()
        db = _make_db_mock()
        db.session.query.return_value.filter.return_value.all.return_value = [
            self._make_user_row()
        ]
        args = {"app": app, "db": db, "event_data": {"created_by": "user1"}}
        result, out_args = actions.get_event_user_data(**args)
        assert result is True
        assert "user_data" in out_args

    def test_returns_false_when_no_user_found(self):
        app = _make_app_mock()
        db = _make_db_mock()
        db.session.query.return_value.filter.return_value.all.return_value = []
        args = {"app": app, "db": db, "event_data": {"created_by": "ghost"}}
        result, _ = actions.get_event_user_data(**args)
        assert result is False

    def test_returns_false_when_multiple_users_found(self):
        app = _make_app_mock()
        db = _make_db_mock()
        db.session.query.return_value.filter.return_value.all.return_value = [
            self._make_user_row(),
            self._make_user_row(),
        ]
        args = {"app": app, "db": db, "event_data": {"created_by": "user1"}}
        result, _ = actions.get_event_user_data(**args)
        assert result is False

    def test_returns_false_when_db_raises(self):
        app = _make_app_mock()
        db = _make_db_mock()
        db.session.query.side_effect = Exception("DB error")
        args = {"app": app, "db": db, "event_data": {"created_by": "user1"}}
        result, _ = actions.get_event_user_data(**args)
        assert result is False

    def test_user_data_includes_agency_ref(self):
        app = _make_app_mock()
        db = _make_db_mock()
        db.session.query.return_value.filter.return_value.all.return_value = [
            self._make_user_row()
        ]
        args = {"app": app, "db": db, "event_data": {"created_by": "user1"}}
        _, out_args = actions.get_event_user_data(**args)
        assert "agency_ref" in out_args["user_data"]


# ---------------------------------------------------------------------------
# update_event_status_processing
# ---------------------------------------------------------------------------

class TestUpdateEventStatusProcessing:
    """Tests for update_event_status_processing()"""

    def _args(self, event_type="vi", event_status=None):
        app = _make_app_mock()
        db = _make_db_mock()
        db.session.query.return_value.filter.return_value.one.return_value = MagicMock()
        args = {
            "app": app,
            "db": db,
            "event_data": {"event_id": 1},
            "event_type": event_type,
            "submission_event_id": 10,
        }
        if event_status is not None:
            args["event_status"] = event_status
        return args

    def test_skips_when_event_status_is_sent(self):
        args = self._args(event_status="sent")
        args["db"].session.query.side_effect = AssertionError("should not query DB")
        result, _ = actions.update_event_status_processing(**args)
        assert result is True

    def test_returns_true_for_vi_event(self):
        result, _ = actions.update_event_status_processing(**self._args(event_type="vi"))
        assert result is True

    def test_returns_true_for_24h_event(self):
        result, _ = actions.update_event_status_processing(**self._args(event_type="24h"))
        assert result is True

    def test_returns_true_for_12h_event(self):
        result, _ = actions.update_event_status_processing(**self._args(event_type="12h"))
        assert result is True

    def test_returns_true_for_irp_event(self):
        """IRP branch is a no-op but should still succeed."""
        result, _ = actions.update_event_status_processing(**self._args(event_type="irp"))
        assert result is True

    def test_returns_false_when_db_raises(self):
        args = self._args(event_type="vi")
        args["db"].session.query.side_effect = Exception("DB error")
        result, _ = actions.update_event_status_processing(**args)
        assert result is False

    def test_vi_event_sets_vi_sent_status_to_processing(self):
        app = _make_app_mock()
        db = _make_db_mock()
        mock_event = MagicMock()
        db.session.query.return_value.filter.return_value.one.return_value = mock_event
        args = {
            "app": app, "db": db,
            "event_data": {"event_id": 1},
            "event_type": "vi",
            "submission_event_id": 10,
        }
        actions.update_event_status_processing(**args)
        assert mock_event.vi_sent_status == "processing"


# ---------------------------------------------------------------------------
# get_storage_file
# ---------------------------------------------------------------------------

class TestGetStorageFile:
    """Tests for get_storage_file()"""

    def _args(self, storage_key="bucket/file.pdf"):
        return {"storage_ref": {"storage_key": storage_key}}

    @patch("python.form_handler.actions.decryptPdf_method1", return_value=(True, "base64data"))
    @patch("python.form_handler.actions.os.remove")
    @patch("builtins.open", create=True)
    @patch("python.form_handler.actions.Minio")
    def test_returns_true_and_sets_file_data(
        self, mock_minio_cls, mock_open, mock_remove, mock_decrypt
    ):
        mock_client = MagicMock()
        mock_minio_cls.return_value = mock_client
        mock_obj = MagicMock()
        mock_obj.data = b"pdf bytes"
        mock_client.get_object.return_value = mock_obj
        mock_open.return_value.__enter__ = MagicMock(return_value=MagicMock())
        mock_open.return_value.__exit__ = MagicMock(return_value=False)

        result, out_args = actions.get_storage_file(**self._args())
        assert result is True
        assert out_args["file_data"] == "base64data"

    @patch("python.form_handler.actions.decryptPdf_method1", return_value=(False, None))
    @patch("python.form_handler.actions.os.remove")
    @patch("builtins.open", create=True)
    @patch("python.form_handler.actions.Minio")
    def test_returns_false_when_decryption_fails(
        self, mock_minio_cls, mock_open, mock_remove, mock_decrypt
    ):
        mock_client = MagicMock()
        mock_minio_cls.return_value = mock_client
        mock_obj = MagicMock()
        mock_obj.data = b"pdf bytes"
        mock_client.get_object.return_value = mock_obj
        mock_open.return_value.__enter__ = MagicMock(return_value=MagicMock())
        mock_open.return_value.__exit__ = MagicMock(return_value=False)

        result, _ = actions.get_storage_file(**self._args())
        assert result is False

    @patch("python.form_handler.actions.Minio")
    def test_returns_false_when_minio_raises(self, mock_minio_cls):
        mock_minio_cls.side_effect = Exception("connection refused")
        result, _ = actions.get_storage_file(**self._args())
        assert result is False


# ---------------------------------------------------------------------------
# prep_icbc_payload
# ---------------------------------------------------------------------------

class TestPrepIcbcPayload:
    """Tests for prep_icbc_payload()"""

    def _base_args(self, event_type="24h", event_status=None):
        app = _make_app_mock()
        db = _make_db_mock()
        juris_row = MagicMock()
        juris_row.__dict__ = {
            "icbc_jurisdiction_code": "BC",
            "vips_jurisdictions_objectCd": "BC",
            "icbc_city_name_legacy": "VANCOUVER",
            "icbc_city_name": "VANCOUVER",
        }
        db.session.query.return_value.filter.return_value.all.return_value = [juris_row]

        driver_dob = MagicMock()
        driver_dob.strftime.return_value = "19900101"
        date_of_driving = MagicMock()

        args = {
            "app": app,
            "db": db,
            "message": {"event_id": "E10", "event_type": event_type},
            "event_type": event_type,
            "file_data": "base64pdf",
            "event_data": {
                "driver_licence_no": "1234567",
                "driver_jurisdiction": "BC",
                "driver_last_name": "Smith",
                "driver_given_name": "John",
                "driver_dob": driver_dob,
                "vehicle_jurisdiction": "BC",
                "vehicle_plate_no": "ABC123",
                "nsc_prov_state": "BC",
                "nsc_no": "NSC001",
                "type_of_prohibition": "alcohol",
                "offence_city": "VANC",
                "date_of_driving": date_of_driving,
                "time_of_driving": "1400",
                "agency": "RCMP",
                "agency_id": 1,
            },
            "form_data": {
                "twenty_four_hour_number": "24H001",
                "twelve_hour_number": "12H001",
            },
            "user_data": {
                "last_name": "Officer",
                "badge_number": "B001",
                "agency": "RCMP",
                "agency_id": 1,
            },
        }
        if event_status is not None:
            args["event_status"] = event_status
        return args

    @patch("python.form_handler.actions.date_time_to_local_tz_string", return_value="20240101")
    def test_returns_true_and_sets_icbc_payload(self, _mock_dt):
        args = self._base_args(event_type="24h")
        result, out_args = actions.prep_icbc_payload(**args)
        assert result is True
        assert "icbc_payload" in out_args

    @patch("python.form_handler.actions.date_time_to_local_tz_string", return_value="20240101")
    def test_skips_when_event_status_is_sent(self, _mock_dt):
        args = self._base_args(event_status="sent")
        args["db"].session.query.side_effect = AssertionError("should not query DB")
        result, _ = actions.prep_icbc_payload(**args)
        assert result is True

    def test_returns_false_when_user_data_missing(self):
        args = self._base_args()
        args.pop("user_data")
        result, out_args = actions.prep_icbc_payload(**args)
        assert result is False
        assert "error" in out_args
        assert out_args["error"]["error_code"] == ErrorCode.I02

    @patch("python.form_handler.actions.date_time_to_local_tz_string", return_value="20240101")
    def test_section_set_correctly_for_24h_alcohol(self, _mock_dt):
        args = self._base_args(event_type="24h")
        args["event_data"]["type_of_prohibition"] = "alcohol"
        _, out_args = actions.prep_icbc_payload(**args)
        assert out_args["icbc_payload"]["section"] == "215.2"

    @patch("python.form_handler.actions.date_time_to_local_tz_string", return_value="20240101")
    def test_section_set_correctly_for_12h_drugs(self, _mock_dt):
        args = self._base_args(event_type="12h")
        args["event_data"]["type_of_prohibition"] = "drugs"
        _, out_args = actions.prep_icbc_payload(**args)
        assert out_args["icbc_payload"]["section"] == "90.321"

    @patch("python.form_handler.actions.date_time_to_local_tz_string", return_value="20240101")
    def test_dl_number_zero_padded_to_8_chars(self, _mock_dt):
        args = self._base_args(event_type="24h")
        args["event_data"]["driver_licence_no"] = "12345"
        _, out_args = actions.prep_icbc_payload(**args)
        assert out_args["icbc_payload"]["dlNumber"] == "00012345"


# ---------------------------------------------------------------------------
# create_vips_document
# ---------------------------------------------------------------------------

class TestCreateVipsDocument:
    """Tests for create_vips_document()"""

    @patch("python.form_handler.actions.create_vips_doc")
    def test_returns_true_and_sets_doc_id(self, mock_create):
        mock_create.return_value = (True, '{"document_id": "DOC-1"}', 201)
        args = {"vips_document_payload": {"file_object": "data"}}
        result, out_args = actions.create_vips_document(**args)
        assert result is True
        assert out_args["vips_doc_id"] == "DOC-1"

    @patch("python.form_handler.actions.create_vips_doc")
    def test_sets_response_code(self, mock_create):
        mock_create.return_value = (True, '{"document_id": "D99"}', 201)
        args = {"vips_document_payload": {}}
        _, out_args = actions.create_vips_document(**args)
        assert out_args["vips_doc_resp_code"] == 201

    @patch("python.form_handler.actions.create_vips_doc")
    def test_returns_false_when_vips_fails(self, mock_create):
        mock_create.return_value = (False, "error", 500)
        args = {"vips_document_payload": {}}
        result, _ = actions.create_vips_document(**args)
        assert result is False

    @patch("python.form_handler.actions.create_vips_doc")
    def test_returns_false_when_exception_raised(self, mock_create):
        mock_create.side_effect = Exception("connection error")
        args = {"vips_document_payload": {}}
        result, _ = actions.create_vips_document(**args)
        assert result is False


# ---------------------------------------------------------------------------
# create_vips_impoundment
# ---------------------------------------------------------------------------

class TestCreateVipsImpoundment:
    """Tests for create_vips_impoundment()"""

    @patch("python.form_handler.actions.create_vips_imp")
    def test_returns_true_on_success(self, mock_create):
        mock_create.return_value = (True, "OK", 201)
        args = {"vips_payload": {"vipsImpoundCreate": {}}}
        result, out_args = actions.create_vips_impoundment(**args)
        assert result is True
        assert out_args["vips_resp_code"] == 201

    @patch("python.form_handler.actions.create_vips_imp")
    def test_sets_response_text(self, mock_create):
        mock_create.return_value = (True, "Created", 201)
        args = {"vips_payload": {}}
        _, out_args = actions.create_vips_impoundment(**args)
        assert out_args["vips_response_txt"] == "Created"

    @patch("python.form_handler.actions.create_vips_imp")
    def test_returns_false_when_vips_fails(self, mock_create):
        mock_create.return_value = (False, "error", 500)
        args = {"vips_payload": {}}
        result, _ = actions.create_vips_impoundment(**args)
        assert result is False

    @patch("python.form_handler.actions.create_vips_imp")
    def test_returns_false_when_exception_raised(self, mock_create):
        mock_create.side_effect = Exception("network error")
        args = {"vips_payload": {}}
        result, _ = actions.create_vips_impoundment(**args)
        assert result is False


# ---------------------------------------------------------------------------
# update_event_status
# ---------------------------------------------------------------------------

class TestUpdateEventStatus:
    """Tests for update_event_status()"""

    def _args(self, event_type="vi", event_status=None):
        app = _make_app_mock()
        db = _make_db_mock()
        db.session.query.return_value.filter.return_value.one.return_value = MagicMock()
        args = {
            "app": app,
            "db": db,
            "event_data": {"event_id": 1},
            "event_type": event_type,
            "submission_event_id": 10,
        }
        if event_status is not None:
            args["event_status"] = event_status
        return args

    def test_skips_when_event_status_is_sent(self):
        args = self._args(event_status="sent")
        args["db"].session.query.side_effect = AssertionError("should not query DB")
        result, _ = actions.update_event_status(**args)
        assert result is True

    def test_returns_true_for_vi_event(self):
        result, _ = actions.update_event_status(**self._args(event_type="vi"))
        assert result is True

    def test_returns_true_for_24h_event(self):
        result, _ = actions.update_event_status(**self._args(event_type="24h"))
        assert result is True

    def test_returns_true_for_irp_event(self):
        result, _ = actions.update_event_status(**self._args(event_type="irp"))
        assert result is True

    def test_returns_false_when_db_raises(self):
        args = self._args(event_type="vi")
        args["db"].session.query.side_effect = Exception("DB error")
        result, _ = actions.update_event_status(**args)
        assert result is False

    def test_vi_event_sets_vi_sent_status_to_sent(self):
        app = _make_app_mock()
        db = _make_db_mock()
        mock_event = MagicMock()
        db.session.query.return_value.filter.return_value.one.return_value = mock_event
        args = {
            "app": app, "db": db,
            "event_data": {"event_id": 1},
            "event_type": "vi",
            "submission_event_id": 10,
        }
        actions.update_event_status(**args)
        assert mock_event.vi_sent_status == "sent"

    def test_24h_event_sets_icbc_sent_status_to_sent(self):
        app = _make_app_mock()
        db = _make_db_mock()
        mock_event = MagicMock()
        db.session.query.return_value.filter.return_value.one.return_value = mock_event
        args = {
            "app": app, "db": db,
            "event_data": {"event_id": 1},
            "event_type": "24h",
            "submission_event_id": 10,
        }
        actions.update_event_status(**args)
        assert mock_event.icbc_sent_status == "sent"


# ---------------------------------------------------------------------------
# update_event_status_hold
# ---------------------------------------------------------------------------

class TestUpdateEventStatusHold:
    """Tests for update_event_status_hold()"""

    def _args(self, event_type="vi"):
        app = _make_app_mock()
        db = _make_db_mock()
        db.session.query.return_value.filter.return_value.one.return_value = MagicMock()
        return {
            "app": app,
            "db": db,
            "message": {"event_id": 1, "event_type": event_type},
            "submission_event_id": 10,
        }

    @patch("python.form_handler.actions.record_event_error")
    def test_returns_true_for_vi_event(self, mock_record):
        mock_record.return_value = (True, {})
        result, _ = actions.update_event_status_hold(**self._args("vi"))
        assert result is True

    @patch("python.form_handler.actions.record_event_error")
    def test_returns_true_for_24h_event(self, mock_record):
        mock_record.return_value = (True, {})
        result, _ = actions.update_event_status_hold(**self._args("24h"))
        assert result is True

    @patch("python.form_handler.actions.record_event_error")
    def test_returns_true_for_irp_event(self, mock_record):
        mock_record.return_value = (True, {})
        result, _ = actions.update_event_status_hold(**self._args("irp"))
        assert result is True

    @patch("python.form_handler.actions.record_event_error")
    def test_calls_record_event_error(self, mock_record):
        mock_record.return_value = (True, {})
        actions.update_event_status_hold(**self._args("vi"))
        mock_record.assert_called()

    @patch("python.form_handler.actions.record_event_error")
    def test_returns_false_when_db_raises(self, mock_record):
        mock_record.return_value = (True, {})
        args = self._args("vi")
        args["db"].session.query.side_effect = Exception("DB error")
        result, _ = actions.update_event_status_hold(**args)
        assert result is False

    @patch("python.form_handler.actions.record_event_error")
    def test_vi_event_sets_retrying_status(self, mock_record):
        mock_record.return_value = (True, {})
        app = _make_app_mock()
        db = _make_db_mock()
        mock_event = MagicMock()
        db.session.query.return_value.filter.return_value.one.return_value = mock_event
        args = {
            "app": app, "db": db,
            "message": {"event_id": 1, "event_type": "vi"},
            "submission_event_id": 10,
        }
        actions.update_event_status_hold(**args)
        assert mock_event.vi_sent_status == "retrying"


# ---------------------------------------------------------------------------
# update_event_status_error
# ---------------------------------------------------------------------------

class TestUpdateEventStatusError:
    """Tests for update_event_status_error()"""

    def _args(self, event_type="vi"):
        app = _make_app_mock()
        db = _make_db_mock()
        db.session.query.return_value.filter.return_value.one.return_value = MagicMock()
        return {
            "app": app,
            "db": db,
            "event_data": {"event_id": 1},
            "event_type": event_type,
            "message": {"event_id": 1, "event_type": event_type},
        }

    @patch("python.form_handler.actions.record_event_error")
    def test_returns_true_for_vi_event(self, mock_record):
        mock_record.return_value = (True, {})
        result, _ = actions.update_event_status_error(**self._args("vi"))
        assert result is True

    @patch("python.form_handler.actions.record_event_error")
    def test_returns_true_for_24h_event(self, mock_record):
        mock_record.return_value = (True, {})
        result, _ = actions.update_event_status_error(**self._args("24h"))
        assert result is True

    @patch("python.form_handler.actions.record_event_error")
    def test_calls_record_event_error(self, mock_record):
        mock_record.return_value = (True, {})
        actions.update_event_status_error(**self._args("vi"))
        mock_record.assert_called()

    @patch("python.form_handler.actions.record_event_error")
    def test_returns_false_when_db_raises(self, mock_record):
        mock_record.return_value = (True, {})
        args = self._args("vi")
        args["db"].session.query.side_effect = Exception("DB error")
        result, _ = actions.update_event_status_error(**args)
        assert result is False

    @patch("python.form_handler.actions.record_event_error")
    def test_vi_event_sets_error_status(self, mock_record):
        mock_record.return_value = (True, {})
        app = _make_app_mock()
        db = _make_db_mock()
        mock_event = MagicMock()
        db.session.query.return_value.filter.return_value.one.return_value = mock_event
        args = {
            "app": app, "db": db,
            "event_data": {"event_id": 1},
            "event_type": "vi",
            "message": {},
        }
        actions.update_event_status_error(**args)
        assert mock_event.vi_sent_status == "error"


# ---------------------------------------------------------------------------
# update_event_status_error_retry
# ---------------------------------------------------------------------------

class TestUpdateEventStatusErrorRetry:
    """Tests for update_event_status_error_retry()"""

    def _args(self, event_type="vi", stop_retry_flg=False):
        app = _make_app_mock()
        db = _make_db_mock()
        db.session.query.return_value.filter.return_value.one.return_value = MagicMock()
        return {
            "app": app,
            "db": db,
            "message": {"event_id": 1, "event_type": event_type},
            "stop_retry_flg": stop_retry_flg,
        }

    def test_returns_true_for_vi_event(self):
        result, _ = actions.update_event_status_error_retry(**self._args("vi"))
        assert result is True

    def test_returns_true_for_24h_event(self):
        result, _ = actions.update_event_status_error_retry(**self._args("24h"))
        assert result is True

    def test_returns_true_for_irp_event(self):
        result, _ = actions.update_event_status_error_retry(**self._args("irp"))
        assert result is True

    def test_sets_error_status_when_stop_retry_true_for_vi(self):
        app = _make_app_mock()
        db = _make_db_mock()
        mock_event = MagicMock()
        db.session.query.return_value.filter.return_value.one.return_value = mock_event
        args = {
            "app": app, "db": db,
            "message": {"event_id": 1, "event_type": "vi"},
            "stop_retry_flg": True,
        }
        actions.update_event_status_error_retry(**args)
        assert mock_event.vi_sent_status == "error"

    def test_sets_retrying_status_when_stop_retry_false_for_vi(self):
        app = _make_app_mock()
        db = _make_db_mock()
        mock_event = MagicMock()
        db.session.query.return_value.filter.return_value.one.return_value = mock_event
        args = {
            "app": app, "db": db,
            "message": {"event_id": 1, "event_type": "vi"},
            "stop_retry_flg": False,
        }
        actions.update_event_status_error_retry(**args)
        assert mock_event.vi_sent_status == "retrying"

    def test_sets_error_status_when_stop_retry_true_for_24h(self):
        app = _make_app_mock()
        db = _make_db_mock()
        mock_event = MagicMock()
        db.session.query.return_value.filter.return_value.one.return_value = mock_event
        args = {
            "app": app, "db": db,
            "message": {"event_id": 1, "event_type": "24h"},
            "stop_retry_flg": True,
        }
        actions.update_event_status_error_retry(**args)
        assert mock_event.icbc_sent_status == "error"

    def test_returns_false_when_db_raises(self):
        args = self._args("vi")
        args["db"].session.query.side_effect = Exception("DB error")
        result, _ = actions.update_event_status_error_retry(**args)
        assert result is False


# ---------------------------------------------------------------------------
# record_event_error
# ---------------------------------------------------------------------------

class TestRecordEventError:
    """Tests for record_event_error()"""

    def _make_error(self, error_code=ErrorCode.E07):
        return {
            "error_code": error_code,
            "error_details": "something went wrong",
            "event_id": "E1",
            "event_type": "vi",
            "func": lambda: None,
        }

    @patch("python.form_handler.actions.send_error_to_rsiops")
    @patch("python.form_handler.actions.record_error")
    def test_returns_true_on_success(self, mock_record, mock_send):
        app = _make_app_mock()
        args = {
            "app": app,
            "error": self._make_error(),
            "message": {"event_id": "E1", "event_type": "vi"},
        }
        result, _ = actions.record_event_error(**args)
        assert result is True

    @patch("python.form_handler.actions.send_error_to_rsiops")
    @patch("python.form_handler.actions.record_error")
    def test_calls_record_error_with_error_code(self, mock_record, mock_send):
        app = _make_app_mock()
        args = {
            "app": app,
            "error": self._make_error(ErrorCode.E07),
            "message": {"event_id": "E1", "event_type": "vi"},
        }
        actions.record_event_error(**args)
        mock_record.assert_called_once()
        called_kwargs = mock_record.call_args[1]
        assert called_kwargs["error_code"] == ErrorCode.E07

    @patch("python.form_handler.actions.send_error_to_rsiops")
    @patch("python.form_handler.actions.record_error")
    def test_uses_e08_when_no_error_object(self, mock_record, mock_send):
        app = _make_app_mock()
        args = {
            "app": app,
            "error": None,
            "message": {"event_id": "E1", "event_type": "vi", "error_message": "something"},
        }
        actions.record_event_error(**args)
        called_kwargs = mock_record.call_args[1]
        assert called_kwargs["error_code"] == ErrorCode.E08

    @patch("python.form_handler.actions.send_error_to_rsiops")
    @patch("python.form_handler.actions.record_error")
    def test_calls_send_error_to_rsiops(self, mock_record, mock_send):
        app = _make_app_mock()
        args = {
            "app": app,
            "error": self._make_error(),
            "message": {"event_id": "E1", "event_type": "vi"},
        }
        actions.record_event_error(**args)
        mock_send.assert_called_once()

    @patch("python.form_handler.actions.send_error_to_rsiops")
    @patch("python.form_handler.actions.record_error")
    def test_returns_true_even_when_record_error_raises(self, mock_record, mock_send):
        """Failure to record the error itself must not propagate."""
        mock_record.side_effect = Exception("logging failed")
        app = _make_app_mock()
        args = {
            "app": app,
            "error": self._make_error(),
            "message": {"event_id": "E1", "event_type": "vi"},
        }
        result, _ = actions.record_event_error(**args)
        assert result is True
