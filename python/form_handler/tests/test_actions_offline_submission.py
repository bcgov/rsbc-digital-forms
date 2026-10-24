from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest

from python.common.enums import ErrorCode
from python.form_handler import actions_offline_submission as actions


def _app_context_mock():
    app = MagicMock()
    app.app_context.return_value.__enter__ = MagicMock(return_value=None)
    app.app_context.return_value.__exit__ = MagicMock(return_value=False)
    return app


def _config(max_retries=3):
    return SimpleNamespace(
        OFFLINE_SUBMISSION_MAX_RETRIES=max_retries,
        OFFLINE_SUBMISSION_HOLD_QUEUE="offline-hold",
        ENCRYPT_KEY="secret",
    )


def test_set_offline_submission_id_accepts_message_id():
    args = {"message": {"id": 42}}

    result, out_args = actions.set_offline_submission_id(**args)

    assert result is True
    assert out_args["offline_submission_id"] == 42


def test_set_offline_submission_id_rejects_missing_id():
    result, out_args = actions.set_offline_submission_id(message={})

    assert result is False
    assert out_args["error"]["error_code"] is ErrorCode.O03


def test_get_offline_submission_data_stores_model_data(monkeypatch):
    app = _app_context_mock()
    db = MagicMock()
    model = SimpleNamespace(id=42, form_id="form-1", payload={"data": {"name": "A"}})
    db.session.query.return_value.filter_by.return_value.first.return_value = model
    monkeypatch.setattr(actions, "FormsflowOfflineSubmission", object())

    result, out_args = actions.get_offline_submission_data(
        app=app, db=db, offline_submission_id=42
    )

    assert result is True
    assert out_args["submission_data"] == model.__dict__
    db.session.query.assert_called_once()


def test_get_offline_submission_data_reports_database_error(monkeypatch):
    app = _app_context_mock()
    db = MagicMock()
    db.session.query.side_effect = RuntimeError("database unavailable")
    monkeypatch.setattr(actions, "FormsflowOfflineSubmission", object())

    result, out_args = actions.get_offline_submission_data(
        app=app, db=db, offline_submission_id=42, message={"id": 42}
    )

    assert result is False
    assert out_args["error"]["error_code"] is ErrorCode.O02


@pytest.mark.parametrize(
    "submission_data",
    [
        None,
        {"form_id": "form-1", "payload": {"data": {}}},
        {"form_id": None, "payload": {"data": {"name": "A"}}},
        {"form_id": "form-1", "payload": None},
        {"form_id": "form-1", "payload": {"other": {"name": "A"}}},
        {
            "form_id": "form-1",
            "username": "officer@example.test",
            "payload": {"data": {"name": "A"}},
        },
    ],
)
def test_validate_offline_submission_data_rejects_invalid_data(submission_data):
    result, out_args = actions.validate_offline_submission_data(
        offline_submission_id=42,
        submission_data=submission_data,
        message={"id": 42},
    )

    assert result is False
    assert out_args["error"]["error_code"] is ErrorCode.O04


def test_validate_offline_submission_data_accepts_valid_data():
    result, out_args = actions.validate_offline_submission_data(
        offline_submission_id=42,
        submission_data={
            "form_id": "form-1",
            "username": "officer@example.test",
            "payload": {"data": {"currentUser": {"id": "officer-1"}, "name": "A"}},
        },
        message={"id": 42},
    )

    assert result is True
    assert "error" not in out_args


@pytest.mark.parametrize(
    ("action", "expected_status"),
    [
        (actions.update_status_processing, "processing"),
        (actions.update_status_completed, "completed"),
    ],
)
def test_status_actions_update_submission(monkeypatch, action, expected_status):
    app = _app_context_mock()
    db = MagicMock()
    update_status = MagicMock()
    monkeypatch.setattr(actions, "_update_status", update_status)

    result, out_args = action(app=app, db=db, offline_submission_id=42)

    assert result is True
    update_status.assert_called_once_with(42, expected_status, app, db)
    assert "error" not in out_args


@pytest.mark.parametrize(
    "action", [actions.update_status_processing, actions.update_status_completed]
)
def test_status_actions_return_error_when_update_raises(monkeypatch, action):
    monkeypatch.setattr(actions, "_update_status", MagicMock(side_effect=RuntimeError("db error")))

    result, out_args = action(
        app=_app_context_mock(), db=MagicMock(), offline_submission_id=42
    )

    assert result is False
    assert out_args["error"]["error_code"] is ErrorCode.O01


def test_add_to_hold_queue_increments_retry_and_publishes(monkeypatch):
    encoded = MagicMock(return_value=b"encoded")
    monkeypatch.setattr(actions, "encode_message", encoded)
    message = {"id": 42}
    writer = MagicMock()
    writer.publish_confirmed.return_value = True

    result, out_args = actions.add_to_hold_queue(
        config=_config(),
        message=message,
        offline_submission_id=42,
        writer=writer,
    )

    assert result is True
    assert message["offline_submission_retry_count"] == 1
    encoded.assert_called_once_with(message, "secret")
    writer.publish_confirmed.assert_called_once_with("offline-hold", b"encoded")
    assert out_args["message"] is message


def test_add_to_hold_queue_normalizes_invalid_retry_count(monkeypatch):
    monkeypatch.setattr(actions, "encode_message", MagicMock(return_value=b"encoded"))
    message = {"id": 42, "offline_submission_retry_count": "invalid"}
    writer = MagicMock()
    writer.publish_confirmed.return_value = True

    result, _ = actions.add_to_hold_queue(
        config=_config(), message=message, offline_submission_id=42, writer=writer
    )

    assert result is True
    assert message["offline_submission_retry_count"] == 1


def test_add_to_hold_queue_does_not_publish_after_retry_limit():
    writer = MagicMock()
    message = {"id": 42, "offline_submission_retry_count": 3}

    result, out_args = actions.add_to_hold_queue(
        config=_config(max_retries=3),
        message=message,
        offline_submission_id=42,
        writer=writer,
    )

    assert result is False
    assert out_args["error"]["error_code"] is ErrorCode.O05
    writer.publish_confirmed.assert_not_called()


def test_add_to_hold_queue_reports_publish_failure(monkeypatch):
    monkeypatch.setattr(actions, "encode_message", MagicMock(return_value=b"encoded"))
    writer = MagicMock()
    writer.publish_confirmed.return_value = False

    result, out_args = actions.add_to_hold_queue(
        config=_config(),
        message={"id": 42},
        offline_submission_id=42,
        writer=writer,
    )

    assert result is False
    assert out_args["error"]["error_code"] is ErrorCode.O06


def test_add_to_hold_queue_handles_publish_exception(monkeypatch):
    monkeypatch.setattr(actions, "encode_message", MagicMock(return_value=b"encoded"))
    writer = MagicMock()
    writer.publish_confirmed.side_effect = RuntimeError("broker unavailable")

    result, out_args = actions.add_to_hold_queue(
        config=_config(),
        message={"id": 42},
        offline_submission_id=42,
        writer=writer,
    )

    assert result is False
    assert "error" not in out_args


def test_update_status_error_marks_submission_error(monkeypatch):
    update_status = MagicMock()
    monkeypatch.setattr(actions, "_update_status", update_status)
    app = _app_context_mock()
    db = MagicMock()

    result, out_args = actions.update_status_error(
        app=app, db=db, offline_submission_id=42
    )

    assert result is True
    update_status.assert_called_once_with(42, "error", app, db)
    assert "error" not in out_args


def test_update_status_error_swallows_database_exception(monkeypatch):
    monkeypatch.setattr(
        actions, "_update_status", MagicMock(side_effect=RuntimeError("db error"))
    )

    result, out_args = actions.update_status_error(
        app=_app_context_mock(), db=MagicMock(), offline_submission_id=42
    )

    assert result is True
    assert "error" not in out_args


def test_record_process_error_records_and_notifies(monkeypatch):
    app = _app_context_mock()
    record_error = MagicMock()
    send_email = MagicMock()
    monkeypatch.setattr(actions, "record_error", record_error)
    monkeypatch.setattr(actions, "send_error_to_rsiops", send_email)
    error = {"error_code": ErrorCode.O03}
    config = MagicMock()

    result, out_args = actions.record_process_error(
        app=app, error=error, config=config
    )

    assert result is True
    record_error.assert_called_once_with(**error)
    send_email.assert_called_once_with(
        title="[DF_FORM_HANDLER] O03 - " + ErrorCode.O03.description,
        config=config,
        body=error,
    )
    assert out_args["error"] is error

