import json
from unittest.mock import MagicMock

import pytest

from python.common.enums import ErrorCode
from python.task_scheduler import eventqueuefuncs as service


class TestAddToEventQueue:
    @pytest.fixture(autouse=True)
    def configure_verbose_logging(self, monkeypatch):
        monkeypatch.setattr(service.logging, "verbose", MagicMock(), raising=False)

    def test_encodes_and_publishes_message(self, monkeypatch):
        app = MagicMock()
        writer = MagicMock()
        writer.publish.return_value = True
        message = {"event_id": "event-1"}
        encoded_message = b"encoded message"
        encode_mock = MagicMock(return_value=encoded_message)
        monkeypatch.setattr(service, "encode_message", encode_mock)

        result = service.add_to_event_queue(app, writer, message, "events")

        assert result == (True, "")
        encode_mock.assert_called_once_with(message, service.Config.ENCRYPT_KEY)
        writer.publish.assert_called_once_with("events", encoded_message)

    def test_records_error_when_publish_fails(self, monkeypatch):
        app = MagicMock()
        writer = MagicMock()
        writer.publish.return_value = False
        message = {"event_id": "event-1"}
        monkeypatch.setattr(service, "encode_message", MagicMock(return_value=b"payload"))
        record_error = MagicMock()
        monkeypatch.setattr(service, "record_queue_error", record_error)

        result = service.add_to_event_queue(app, writer, message, "events")

        assert result == (False, "")
        record_error.assert_called_once_with(
            app,
            message,
            service.add_to_event_queue,
            "unable to write to RabbitMQ events queue",
        )

    @pytest.mark.parametrize("failure", ["encoding", "publishing"])
    def test_records_error_when_encoding_or_publishing_raises(self, monkeypatch, failure):
        app = MagicMock()
        writer = MagicMock()
        message = {"event_id": "event-1"}
        error = RuntimeError(f"{failure} failed")
        encode_mock = MagicMock(side_effect=error if failure == "encoding" else None)
        if failure == "publishing":
            encode_mock.return_value = b"payload"
            writer.publish.side_effect = error
        monkeypatch.setattr(service, "encode_message", encode_mock)
        record_error = MagicMock()
        monkeypatch.setattr(service, "record_queue_error", record_error)

        result = service.add_to_event_queue(app, writer, message, "events")

        assert result == (False, "")
        record_error.assert_called_once_with(app, message, service.add_to_event_queue, str(error))


class TestRecordQueueError:
    def test_records_event_metadata_and_json_payload(self, monkeypatch):
        app = MagicMock()
        event = {"event_id": "event-1", "event_type": "submitted", "value": 3}
        record_error = MagicMock()
        monkeypatch.setattr(service, "record_error", record_error)

        service.record_queue_error(app, event, service.add_to_event_queue, "publish failed")

        record_error.assert_called_once_with(
            error_code=ErrorCode.E03,
            error_details="publish failed",
            event_id="event-1",
            event_type="submitted",
            payload=json.dumps(event),
            func=service.add_to_event_queue,
        )
        app.app_context.assert_called_once()

    def test_records_empty_event_as_null_metadata(self, monkeypatch):
        app = MagicMock()
        record_error = MagicMock()
        monkeypatch.setattr(service, "record_error", record_error)

        service.record_queue_error(app, None, service.add_to_event_queue)

        record_error.assert_called_once_with(
            error_code=ErrorCode.E03,
            error_details=None,
            event_id=None,
            event_type=None,
            payload=None,
            func=service.add_to_event_queue,
        )

    def test_does_not_raise_when_recording_the_error_fails(self, monkeypatch):
        app = MagicMock()
        monkeypatch.setattr(
            service, "record_error", MagicMock(side_effect=RuntimeError("error store unavailable"))
        )

        service.record_queue_error(app, {"event_id": "event-1"}, service.add_to_event_queue)
