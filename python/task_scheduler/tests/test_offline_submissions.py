from unittest.mock import MagicMock

import pytest

from python.task_scheduler import offline_submissions as service


class TestProcessOfflineSubmission:
    @pytest.fixture(autouse=True)
    def configure_verbose_logging(self, monkeypatch):
        monkeypatch.setattr(service.logging, "verbose", MagicMock(), raising=False)

    def test_publishes_submissions_and_marks_them_queued(self, monkeypatch):
        app = MagicMock()
        db = MagicMock()
        submissions = [{"id": 1}, {"id": 2}]
        writer = MagicMock()
        query_mock = MagicMock(return_value=(True, None, submissions))
        rabbitmq_mock = MagicMock(return_value=writer)
        queue_mock = MagicMock(return_value=(True, ""))
        update_mock = MagicMock(return_value=(True, None))
        monkeypatch.setattr(service, "query_pending_offline_submissions", query_mock)
        monkeypatch.setattr(service, "RabbitMQ", rabbitmq_mock)
        monkeypatch.setattr(service, "add_to_event_queue", queue_mock)
        monkeypatch.setattr(service, "update_offline_submission_status", update_mock)

        service.process_offline_submission(app, db)

        query_mock.assert_called_once_with(app, db)
        rabbitmq_mock.assert_called_once()
        assert queue_mock.call_count == 2
        queue_mock.assert_any_call(
            app, writer, submissions[0], service.Config.OFFLINE_SUBMISSION_WATCH_QUEUE
        )
        queue_mock.assert_any_call(
            app, writer, submissions[1], service.Config.OFFLINE_SUBMISSION_WATCH_QUEUE
        )
        update_mock.assert_any_call(app, db, 1, "queued")
        update_mock.assert_any_call(app, db, 2, "queued")
        assert update_mock.call_count == 2

    def test_does_not_update_status_when_submission_cannot_be_queued(self, monkeypatch):
        app = MagicMock()
        db = MagicMock()
        submission = {"id": 1}
        monkeypatch.setattr(
            service,
            "query_pending_offline_submissions",
            MagicMock(return_value=(True, None, [submission])),
        )
        monkeypatch.setattr(service, "RabbitMQ", MagicMock())
        queue_mock = MagicMock(return_value=(False, "queue unavailable"))
        update_mock = MagicMock()
        monkeypatch.setattr(service, "add_to_event_queue", queue_mock)
        monkeypatch.setattr(service, "update_offline_submission_status", update_mock)

        service.process_offline_submission(app, db)

        queue_mock.assert_called_once()
        update_mock.assert_not_called()

    def test_continues_with_later_submissions_when_status_update_fails(self, monkeypatch):
        app = MagicMock()
        db = MagicMock()
        submissions = [{"id": 1}, {"id": 2}]
        monkeypatch.setattr(
            service,
            "query_pending_offline_submissions",
            MagicMock(return_value=(True, None, submissions)),
        )
        monkeypatch.setattr(service, "RabbitMQ", MagicMock())
        monkeypatch.setattr(service, "add_to_event_queue", MagicMock(return_value=(True, "")))
        update_mock = MagicMock(side_effect=[(False, "database unavailable"), (True, None)])
        monkeypatch.setattr(service, "update_offline_submission_status", update_mock)

        service.process_offline_submission(app, db)

        assert update_mock.call_count == 2
        update_mock.assert_any_call(app, db, 2, "queued")

    def test_returns_true_when_there_are_no_pending_submissions(self, monkeypatch):
        app = MagicMock()
        db = MagicMock()
        monkeypatch.setattr(
            service,
            "query_pending_offline_submissions",
            MagicMock(return_value=(False, "No pending offline submissions found", None)),
        )
        rabbitmq_mock = MagicMock()
        monkeypatch.setattr(service, "RabbitMQ", rabbitmq_mock)

        result = service.process_offline_submission(app, db)

        assert result is True
        rabbitmq_mock.assert_not_called()

    def test_returns_false_when_query_fails(self, monkeypatch):
        app = MagicMock()
        db = MagicMock()
        monkeypatch.setattr(
            service,
            "query_pending_offline_submissions",
            MagicMock(return_value=(False, "database unavailable", None)),
        )

        result = service.process_offline_submission(app, db)

        assert result is False

    def test_returns_false_when_rabbitmq_cannot_be_created(self, monkeypatch):
        app = MagicMock()
        db = MagicMock()
        monkeypatch.setattr(
            service,
            "query_pending_offline_submissions",
            MagicMock(return_value=(True, None, [])),
        )
        monkeypatch.setattr(
            service, "RabbitMQ", MagicMock(side_effect=RuntimeError("broker unavailable"))
        )

        result = service.process_offline_submission(app, db)

        assert result is False
