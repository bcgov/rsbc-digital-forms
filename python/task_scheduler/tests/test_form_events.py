from unittest.mock import MagicMock

import pytest

from python.task_scheduler import form_events as service


class TestProcessPendingEvents:
    @pytest.fixture(autouse=True)
    def configure_verbose_logging(self, monkeypatch):
        monkeypatch.setattr(service.logging, "verbose", MagicMock(), raising=False)

    def test_publishes_pending_events_and_marks_them_processed(self, monkeypatch):
        app = MagicMock()
        db = MagicMock()
        events = [
            {"submission_id": "submission-1", "event_id": "event-1"},
            {"submission_id": "submission-2", "event_id": "event-2"},
        ]
        writer = MagicMock()
        rabbitmq_mock = MagicMock(return_value=writer)
        query_mock = MagicMock(return_value=(True, None, events))
        queue_mock = MagicMock(return_value=(True, ""))
        update_mock = MagicMock(return_value=(True, None))
        monkeypatch.setattr(service, "RabbitMQ", rabbitmq_mock)
        monkeypatch.setattr(service, "query_pending_events", query_mock)
        monkeypatch.setattr(service, "add_to_event_queue", queue_mock)
        monkeypatch.setattr(service, "update_event_status", update_mock)

        service.process_pending_events(app, db)

        query_mock.assert_called_once_with(app, db)
        rabbitmq_mock.assert_called_once()
        assert queue_mock.call_count == 2
        assert queue_mock.call_args_list[0].args == (
            app,
            writer,
            events[0],
            service.Config.STORAGE_WATCH_QUEUE,
        )
        update_mock.assert_any_call(app, db, "submission-1", "event-1", "processed")
        update_mock.assert_any_call(app, db, "submission-2", "event-2", "processed")
        assert update_mock.call_count == 2

    def test_does_not_update_status_when_event_cannot_be_queued(self, monkeypatch):
        app = MagicMock()
        db = MagicMock()
        event = {"submission_id": "submission-1", "event_id": "event-1"}
        monkeypatch.setattr(service, "query_pending_events", MagicMock(return_value=(True, None, [event])))
        monkeypatch.setattr(service, "RabbitMQ", MagicMock())
        queue_mock = MagicMock(return_value=(False, "queue unavailable"))
        update_mock = MagicMock()
        monkeypatch.setattr(service, "add_to_event_queue", queue_mock)
        monkeypatch.setattr(service, "update_event_status", update_mock)

        service.process_pending_events(app, db)

        queue_mock.assert_called_once()
        update_mock.assert_not_called()

    def test_returns_true_when_there_are_no_pending_events(self, monkeypatch):
        app = MagicMock()
        db = MagicMock()
        monkeypatch.setattr(
            service,
            "query_pending_events",
            MagicMock(return_value=(False, "No pending events found", None)),
        )
        rabbitmq_mock = MagicMock()
        monkeypatch.setattr(service, "RabbitMQ", rabbitmq_mock)

        result = service.process_pending_events(app, db)

        assert result is True
        rabbitmq_mock.assert_not_called()

    def test_returns_false_when_query_fails(self, monkeypatch):
        app = MagicMock()
        db = MagicMock()
        monkeypatch.setattr(
            service,
            "query_pending_events",
            MagicMock(return_value=(False, "database unavailable", None)),
        )
        rabbitmq_mock = MagicMock()
        monkeypatch.setattr(service, "RabbitMQ", rabbitmq_mock)

        result = service.process_pending_events(app, db)

        assert result is False
        rabbitmq_mock.assert_not_called()

    def test_continues_with_later_events_when_status_update_fails(self, monkeypatch):
        app = MagicMock()
        db = MagicMock()
        events = [
            {"submission_id": "submission-1", "event_id": "event-1"},
            {"submission_id": "submission-2", "event_id": "event-2"},
        ]
        monkeypatch.setattr(service, "query_pending_events", MagicMock(return_value=(True, None, events)))
        monkeypatch.setattr(service, "RabbitMQ", MagicMock())
        monkeypatch.setattr(service, "add_to_event_queue", MagicMock(return_value=(True, "")))
        update_mock = MagicMock(side_effect=[(False, "database unavailable"), (True, None)])
        monkeypatch.setattr(service, "update_event_status", update_mock)

        service.process_pending_events(app, db)

        assert update_mock.call_count == 2
        update_mock.assert_any_call(app, db, "submission-2", "event-2", "processed")

    def test_returns_false_when_rabbitmq_cannot_be_created(self, monkeypatch):
        app = MagicMock()
        db = MagicMock()
        monkeypatch.setattr(service, "query_pending_events", MagicMock(return_value=(True, None, [])))
        monkeypatch.setattr(service, "RabbitMQ", MagicMock(side_effect=RuntimeError("broker unavailable")))

        result = service.process_pending_events(app, db)

        assert result is False
