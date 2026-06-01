"""
Unit tests for python.form_handler.helper
"""
from __future__ import annotations

import base64
from unittest.mock import MagicMock, patch, mock_open
import pytest

from python.form_handler.helper import (
    get_listeners,
    middle_logic,
    get_storage_ref_event_type,
    get_event_status,
    convertDateTime,
    convertDateTimeWithSecs,
    decryptPdf_method1,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_app_mock():
    app = MagicMock()
    app.app_context.return_value.__enter__ = MagicMock(return_value=None)
    app.app_context.return_value.__exit__ = MagicMock(return_value=False)
    return app


# ---------------------------------------------------------------------------
# get_listeners
# ---------------------------------------------------------------------------

class TestGetListeners:
    """Tests for get_listeners()"""

    def _listeners(self):
        return {
            "unknown_event": ["fallback_fn"],
            "vi": ["vi_fn1", "vi_fn2"],
            "24h": ["twenty_four_fn"],
        }

    def test_returns_pipeline_for_known_key(self):
        result = get_listeners(self._listeners(), "vi")
        assert result == ["vi_fn1", "vi_fn2"]

    def test_returns_unknown_event_pipeline_for_missing_key(self):
        result = get_listeners(self._listeners(), "nonexistent")
        assert result == ["fallback_fn"]

    def test_returns_unknown_event_pipeline_for_empty_string_key(self):
        result = get_listeners(self._listeners(), "")
        assert result == ["fallback_fn"]

    def test_returns_correct_pipeline_for_24h(self):
        result = get_listeners(self._listeners(), "24h")
        assert result == ["twenty_four_fn"]

    def test_returns_same_object_not_copy(self):
        """get_listeners returns the actual list, not a copy."""
        listeners = self._listeners()
        result = get_listeners(listeners, "vi")
        assert result is listeners["vi"]


# ---------------------------------------------------------------------------
# middle_logic
# ---------------------------------------------------------------------------

class TestMiddleLogic:
    """Tests for middle_logic()"""

    def _step(self, fn, fail=None):
        return {"try": fn, "fail": fail or []}

    def test_empty_pipeline_returns_args(self):
        args = {"key": "value"}
        result = middle_logic([], **args)
        assert result["key"] == "value"

    def test_single_passing_step_returns_updated_args(self):
        def add_flag(**kwargs):
            kwargs["flag"] = True
            return True, kwargs

        result = middle_logic([self._step(add_flag)], key="start")
        assert result["flag"] is True

    def test_single_failing_step_calls_fail_branch(self):
        def failing_step(**kwargs):
            return False, kwargs

        def fail_handler(**kwargs):
            kwargs["handled"] = True
            return True, kwargs

        pipeline = [self._step(failing_step, fail=[self._step(fail_handler)])]
        result = middle_logic(pipeline, key="start")
        assert result["handled"] is True

    def test_args_are_passed_through_across_steps(self):
        def step_a(**kwargs):
            kwargs["a"] = 1
            return True, kwargs

        def step_b(**kwargs):
            kwargs["b"] = 2
            return True, kwargs

        result = middle_logic([self._step(step_a), self._step(step_b)])
        assert result["a"] == 1
        assert result["b"] == 2

    def test_failing_step_does_not_execute_remaining_pipeline(self):
        executed = []

        def failing_step(**kwargs):
            executed.append("fail")
            return False, kwargs

        def should_not_run(**kwargs):
            executed.append("skipped")
            return True, kwargs

        middle_logic([self._step(failing_step), self._step(should_not_run)])
        assert "skipped" not in executed

    def test_passing_step_does_not_execute_fail_branch(self):
        executed = []

        def passing_step(**kwargs):
            executed.append("pass")
            return True, kwargs

        def fail_handler(**kwargs):
            executed.append("fail_handler")
            return True, kwargs

        middle_logic([self._step(passing_step, fail=[self._step(fail_handler)])])
        assert "fail_handler" not in executed

    def test_nested_fail_branch_is_fully_traversed(self):
        """A fail handler that also fails executes its own fail branch."""
        executed = []

        def outer_fail(**kwargs):
            executed.append("outer")
            return False, kwargs

        def inner_fail(**kwargs):
            executed.append("inner")
            return False, kwargs

        def deepest_handler(**kwargs):
            executed.append("deepest")
            return True, kwargs

        pipeline = [
            self._step(
                outer_fail,
                fail=[
                    self._step(inner_fail, fail=[self._step(deepest_handler)])
                ],
            )
        ]
        middle_logic(pipeline)
        assert executed == ["outer", "inner", "deepest"]

    def test_empty_fail_list_does_not_crash(self):
        def failing_step(**kwargs):
            return False, kwargs

        result = middle_logic([self._step(failing_step, fail=[])], key="v")
        assert result["key"] == "v"

    def test_multiple_steps_all_passing(self):
        results = []

        def make_step(label):
            def step(**kwargs):
                results.append(label)
                return True, kwargs
            step.__name__ = label
            return step

        pipeline = [self._step(make_step(f"step{i}")) for i in range(5)]
        middle_logic(pipeline)
        assert results == ["step0", "step1", "step2", "step3", "step4"]


# ---------------------------------------------------------------------------
# get_storage_ref_event_type
# ---------------------------------------------------------------------------

class TestGetStorageRefEventType:
    """Tests for get_storage_ref_event_type()"""

    _EVENT_TYPES = ["vi", "24h", "12h", "irp"]

    def test_returns_event_type_and_event_id_for_known_type(self):
        message = {"FormType": "vi", "event_id": "EVT-1"}
        event_type, event_id = get_storage_ref_event_type(
            message, app=None, db=None, event_types=self._EVENT_TYPES
        )
        assert event_type == "vi"
        assert event_id == "EVT-1"

    def test_form_type_is_lowercased(self):
        message = {"FormType": "VI", "event_id": "E2"}
        event_type, _ = get_storage_ref_event_type(
            message, app=None, db=None, event_types=self._EVENT_TYPES
        )
        assert event_type == "vi"

    def test_returns_unknown_event_for_unrecognised_form_type(self):
        message = {"FormType": "mystery", "event_id": "E3"}
        event_type, event_id = get_storage_ref_event_type(
            message, app=None, db=None, event_types=self._EVENT_TYPES
        )
        assert event_type == "unknown_event"
        assert event_id == "E3"

    def test_returns_unknown_event_when_form_type_absent(self):
        message = {"event_id": "E4"}
        event_type, _ = get_storage_ref_event_type(
            message, app=None, db=None, event_types=self._EVENT_TYPES
        )
        assert event_type == "unknown_event"

    def test_event_id_defaults_to_none_when_absent(self):
        message = {"FormType": "vi"}
        _, event_id = get_storage_ref_event_type(
            message, app=None, db=None, event_types=self._EVENT_TYPES
        )
        assert event_id is None

    def test_all_known_event_types_are_accepted(self):
        for et in self._EVENT_TYPES:
            message = {"FormType": et, "event_id": "X"}
            event_type, _ = get_storage_ref_event_type(
                message, app=None, db=None, event_types=self._EVENT_TYPES
            )
            assert event_type == et

    def test_returns_unknown_event_for_empty_form_type(self):
        message = {"FormType": "", "event_id": "E5"}
        event_type, _ = get_storage_ref_event_type(
            message, app=None, db=None, event_types=self._EVENT_TYPES
        )
        assert event_type == "unknown_event"


# ---------------------------------------------------------------------------
# get_event_status
# ---------------------------------------------------------------------------

class TestGetEventStatus:
    """Tests for get_event_status()"""

    def _mock_event(self, vi_status="pending", icbc_status="pending"):
        e = MagicMock()
        e.vi_sent_status = vi_status
        e.icbc_sent_status = icbc_status
        return e

    def test_returns_vi_sent_status_for_vi_type(self):
        app = _make_app_mock()
        db = MagicMock()
        event = self._mock_event(vi_status="sent")
        db.session.query.return_value.filter.return_value.all.return_value = [event]

        status = get_event_status(app, db, "vi", 1)
        assert status == "sent"

    def test_returns_icbc_sent_status_for_24h_type(self):
        app = _make_app_mock()
        db = MagicMock()
        event = self._mock_event(icbc_status="processing")
        db.session.query.return_value.filter.return_value.all.return_value = [event]

        status = get_event_status(app, db, "24h", 2)
        assert status == "processing"

    def test_returns_icbc_sent_status_for_12h_type(self):
        app = _make_app_mock()
        db = MagicMock()
        event = self._mock_event(icbc_status="retrying")
        db.session.query.return_value.filter.return_value.all.return_value = [event]

        status = get_event_status(app, db, "12h", 3)
        assert status == "retrying"

    def test_returns_pending_for_unknown_event_type(self):
        app = _make_app_mock()
        db = MagicMock()
        event = self._mock_event()
        db.session.query.return_value.filter.return_value.all.return_value = [event]

        status = get_event_status(app, db, "unknown_event", 4)
        assert status == "pending"

    def test_returns_pending_when_no_rows_found(self):
        app = _make_app_mock()
        db = MagicMock()
        db.session.query.return_value.filter.return_value.all.return_value = []

        status = get_event_status(app, db, "vi", 99)
        assert status == "pending"

    def test_returns_pending_when_multiple_rows_found(self):
        app = _make_app_mock()
        db = MagicMock()
        db.session.query.return_value.filter.return_value.all.return_value = [
            self._mock_event(), self._mock_event()
        ]

        status = get_event_status(app, db, "vi", 5)
        assert status == "pending"

    def test_returns_error_when_exception_raised(self):
        app = _make_app_mock()
        db = MagicMock()
        db.session.query.side_effect = Exception("DB down")

        status = get_event_status(app, db, "vi", 6)
        assert status == "error"

    def test_returns_pending_for_irp_type(self):
        app = _make_app_mock()
        db = MagicMock()
        event = self._mock_event()
        db.session.query.return_value.filter.return_value.all.return_value = [event]

        status = get_event_status(app, db, "irp", 7)
        assert status == "pending"


# ---------------------------------------------------------------------------
# convertDateTime
# ---------------------------------------------------------------------------

class TestConvertDateTime:
    """Tests for convertDateTime() – converts YYYY-MM-DD → ISO 8601 with Pacific TZ."""

    def test_output_format_contains_date(self):
        result = convertDateTime("2024-07-15")
        assert "2024-07-15" in result

    def test_time_part_is_midnight(self):
        result = convertDateTime("2024-07-15")
        assert "T00:00:00.000" in result

    def test_dst_offset_is_minus_seven(self):
        """During Pacific Daylight Time (summer) offset should be -07:00."""
        result = convertDateTime("2024-07-15")
        assert result.endswith("-07:00")

    def test_non_dst_offset_is_minus_eight(self):
        """During Pacific Standard Time (winter) offset should be -08:00."""
        result = convertDateTime("2024-01-15")
        assert result.endswith("-08:00")

    def test_returns_string(self):
        assert isinstance(convertDateTime("2024-06-01"), str)

    def test_full_expected_output_dst(self):
        assert convertDateTime("2024-07-15") == "2024-07-15T00:00:00.000-07:00"

    def test_full_expected_output_non_dst(self):
        assert convertDateTime("2024-01-15") == "2024-01-15T00:00:00.000-08:00"

    def test_invalid_format_raises(self):
        with pytest.raises(ValueError):
            convertDateTime("15-07-2024")

    def test_invalid_string_raises(self):
        with pytest.raises(ValueError):
            convertDateTime("not-a-date")

    @pytest.mark.parametrize("date_str,expected", [
        # Midnight on DST-start day is still in PST (clocks spring forward at 2am)
        ("2024-03-10", "2024-03-10T00:00:00.000-08:00"),
        # Midnight on DST-end day is still in PDT (clocks fall back at 2am)
        ("2024-11-03", "2024-11-03T00:00:00.000-07:00"),
        ("2023-12-31", "2023-12-31T00:00:00.000-08:00"),
        ("2023-06-21", "2023-06-21T00:00:00.000-07:00"),
    ])
    def test_parametrized_dates(self, date_str, expected):
        assert convertDateTime(date_str) == expected


# ---------------------------------------------------------------------------
# convertDateTimeWithSecs
# ---------------------------------------------------------------------------

class TestConvertDateTimeWithSecs:
    """Tests for convertDateTimeWithSecs() – converts YYYY-MM-DDTHH:MM:SS → ISO 8601."""

    def test_returns_string(self):
        assert isinstance(convertDateTimeWithSecs("2024-07-15T14:30:00"), str)

    def test_dst_offset_is_minus_seven(self):
        result = convertDateTimeWithSecs("2024-07-15T14:30:00")
        assert result.endswith("-07:00")

    def test_non_dst_offset_is_minus_eight(self):
        result = convertDateTimeWithSecs("2024-01-15T09:00:00")
        assert result.endswith("-08:00")

    def test_full_expected_output_dst(self):
        assert convertDateTimeWithSecs("2024-07-15T14:30:00") == "2024-07-15T14:30:00.000-07:00"

    def test_full_expected_output_non_dst(self):
        assert convertDateTimeWithSecs("2024-01-15T14:30:00") == "2024-01-15T14:30:00.000-08:00"

    def test_midnight_time(self):
        result = convertDateTimeWithSecs("2024-07-15T00:00:00")
        assert "T00:00:00.000" in result

    def test_preserves_seconds(self):
        result = convertDateTimeWithSecs("2024-07-15T14:30:59")
        assert "T14:30:59.000" in result

    def test_invalid_format_raises(self):
        with pytest.raises(ValueError):
            convertDateTimeWithSecs("2024-07-15")

    def test_invalid_string_raises(self):
        with pytest.raises(ValueError):
            convertDateTimeWithSecs("not-a-datetime")

    @pytest.mark.parametrize("dt_str,expected", [
        ("2024-07-15T14:30:00", "2024-07-15T14:30:00.000-07:00"),
        ("2024-01-15T14:30:00", "2024-01-15T14:30:00.000-08:00"),
        ("2023-12-31T23:59:59", "2023-12-31T23:59:59.000-08:00"),
        ("2023-06-21T08:00:00", "2023-06-21T08:00:00.000-07:00"),
    ])
    def test_parametrized_datetimes(self, dt_str, expected):
        assert convertDateTimeWithSecs(dt_str) == expected


# ---------------------------------------------------------------------------
# decryptPdf_method1
# ---------------------------------------------------------------------------

class TestDecryptPdfMethod1:
    """Tests for decryptPdf_method1() – patches fitz and filesystem I/O."""

    def test_returns_true_and_base64_on_success(self):
        pdf_bytes = b"%PDF-1.4 fake content"
        encoded = base64.b64encode(pdf_bytes).decode("utf-8")

        mock_doc = MagicMock()
        mock_doc.authenticate.return_value = True
        mock_doc.save = MagicMock()

        with patch("python.form_handler.helper.fitz.open", return_value=mock_doc), \
             patch("builtins.open", mock_open(read_data=pdf_bytes)), \
             patch("python.form_handler.helper.os.remove"):
            status, data = decryptPdf_method1("/fake/input.pdf", "password", "/fake/out.pdf")

        assert status is True
        assert data == encoded

    def test_returns_false_none_when_authentication_fails(self):
        mock_doc = MagicMock()
        mock_doc.authenticate.return_value = False

        with patch("python.form_handler.helper.fitz.open", return_value=mock_doc):
            status, data = decryptPdf_method1("/fake/input.pdf", "wrong_pw", "/fake/out.pdf")

        assert status is False
        assert data is None

    def test_returns_false_none_when_fitz_raises(self):
        with patch("python.form_handler.helper.fitz.open", side_effect=Exception("corrupt PDF")):
            status, data = decryptPdf_method1("/fake/bad.pdf", "pw", "/fake/out.pdf")

        assert status is False
        assert data is None

    def test_output_file_is_removed_after_success(self):
        pdf_bytes = b"dummy"
        mock_doc = MagicMock()
        mock_doc.authenticate.return_value = True

        remove_mock = MagicMock()
        with patch("python.form_handler.helper.fitz.open", return_value=mock_doc), \
             patch("builtins.open", mock_open(read_data=pdf_bytes)), \
             patch("python.form_handler.helper.os.remove", remove_mock):
            decryptPdf_method1("/in.pdf", "pw", "/out.pdf")

        remove_mock.assert_called_once_with("/out.pdf")

    def test_doc_is_closed_on_success(self):
        pdf_bytes = b"data"
        mock_doc = MagicMock()
        mock_doc.authenticate.return_value = True

        with patch("python.form_handler.helper.fitz.open", return_value=mock_doc), \
             patch("builtins.open", mock_open(read_data=pdf_bytes)), \
             patch("python.form_handler.helper.os.remove"):
            decryptPdf_method1("/in.pdf", "pw", "/out.pdf")

        mock_doc.close.assert_called()

    def test_doc_is_closed_on_authentication_failure(self):
        mock_doc = MagicMock()
        mock_doc.authenticate.return_value = False

        with patch("python.form_handler.helper.fitz.open", return_value=mock_doc):
            decryptPdf_method1("/in.pdf", "wrong", "/out.pdf")

        mock_doc.close.assert_called()
