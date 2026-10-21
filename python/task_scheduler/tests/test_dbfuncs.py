from unittest.mock import MagicMock

import pytest

from python.common.models import Event, FormsflowOfflineSubmission, Submission, SubmissionFormRef
from python.task_scheduler import dbfuncs as service


def make_query(result=None, error=None):
    query = MagicMock()
    if error is not None:
        query.filter.side_effect = error
    else:
        query.filter.return_value.all.return_value = result
        query.filter.return_value.join.return_value.all.return_value = result
        query.filter.return_value.one.return_value = result
    return query


class TestQueryPendingEvents:
    def test_returns_events_with_form_storage_references(self):
        app = MagicMock()
        submission = MagicMock(submission_id="submission-1")
        submission.event.event_id = "event-1"
        form_ref = MagicMock(storage_key="storage-key", form_type="form-type")
        submission_query = make_query([submission])
        form_ref_query = make_query([form_ref])
        db = MagicMock()
        db.session.query.side_effect = [submission_query, form_ref_query]

        result = service.query_pending_events(app, db)

        assert result == (
            True,
            None,
            [{
                "event_id": "event-1",
                "submission_id": "submission-1",
                "Key": "storage-key",
                "FormType": "form-type",
            }],
        )
        db.session.query.assert_any_call(Submission)
        db.session.query.assert_any_call(SubmissionFormRef)
        submission_query.filter.assert_called_once()
        join_args = submission_query.filter.return_value.join.call_args.args
        assert join_args[0] is Event
        assert str(join_args[1]) == "submission.submission_id = event.submission_id"
        form_ref_query.filter.assert_called_once()

    def test_returns_no_pending_events_when_submission_query_is_empty(self):
        app = MagicMock()
        db = MagicMock()
        db.session.query.return_value = make_query([])

        result = service.query_pending_events(app, db)

        assert result == (False, "No pending events found", None)
        db.session.query.assert_called_once_with(Submission)

    def test_returns_no_pending_events_when_submissions_have_no_form_references(self):
        app = MagicMock()
        submission = MagicMock(submission_id="submission-1")
        submission_query = make_query([submission])
        form_ref_query = make_query([])
        db = MagicMock()
        db.session.query.side_effect = [submission_query, form_ref_query]

        result = service.query_pending_events(app, db)

        assert result == (False, "No pending events found", None)

    def test_records_and_returns_database_query_errors(self, monkeypatch):
        app = MagicMock()
        db = MagicMock()
        db.session.query.side_effect = RuntimeError("database unavailable")
        record_error = MagicMock()
        monkeypatch.setattr(service, "record_queue_error", record_error)

        result = service.query_pending_events(app, db)

        assert result == (False, "Error querying pending events: database unavailable", None)
        record_error.assert_called_once_with(
            app, None, service.query_pending_events, "database unavailable"
        )


class TestUpdateEventStatus:
    def test_updates_event_and_submission_and_commits(self):
        app = MagicMock()
        event = MagicMock()
        submission = MagicMock()
        event_query = make_query([event])
        submission_query = make_query(submission)
        db = MagicMock()
        db.session.query.side_effect = [event_query, submission_query]

        result = service.update_event_status(app, db, "submission-1", "event-1", "processed")

        assert result == (True, None)
        assert event.task_processing_status == "processed"
        assert submission.task_processing_status == "processed"
        db.session.commit.assert_called_once()
        db.session.query.assert_any_call(Event)
        db.session.query.assert_any_call(Submission)

    @pytest.mark.parametrize("events", [[], [MagicMock(), MagicMock()]])
    def test_returns_false_when_event_is_missing_or_ambiguous(self, events):
        app = MagicMock()
        db = MagicMock()
        db.session.query.return_value = make_query(events)

        result = service.update_event_status(app, db, "submission-1", "event-1", "processed")

        assert result == (False, "No events found or multiple events found")
        db.session.commit.assert_not_called()

    def test_records_and_returns_database_update_errors(self, monkeypatch):
        app = MagicMock()
        event_query = make_query([MagicMock()])
        submission_query = make_query(error=RuntimeError("database unavailable"))
        db = MagicMock()
        db.session.query.side_effect = [event_query, submission_query]
        record_error = MagicMock()
        monkeypatch.setattr(service, "record_queue_error", record_error)

        result = service.update_event_status(app, db, "submission-1", "event-1", "processed")

        assert result == (False, "Error updating processed event status: database unavailable")
        record_error.assert_called_once_with(
            app,
            {"event_id": "event-1"},
            service.update_event_status,
            "database unavailable",
        )


class TestQueryPendingOfflineSubmissions:
    def test_returns_ids_of_pending_offline_submissions(self):
        app = MagicMock()
        submissions = [MagicMock(id=1), MagicMock(id=2)]
        query = make_query(submissions)
        db = MagicMock()
        db.session.query.return_value = query

        result = service.query_pending_offline_submissions(app, db)

        assert result == (True, None, [{"id": 1}, {"id": 2}])
        db.session.query.assert_called_once_with(FormsflowOfflineSubmission)
        query.filter.assert_called_once()

    def test_returns_no_pending_offline_submissions_when_query_is_empty(self):
        app = MagicMock()
        db = MagicMock()
        db.session.query.return_value = make_query([])

        result = service.query_pending_offline_submissions(app, db)

        assert result == (False, "No pending offline submissions found", None)

    def test_records_and_returns_database_query_errors(self, monkeypatch):
        app = MagicMock()
        db = MagicMock()
        db.session.query.side_effect = RuntimeError("database unavailable")
        record_error = MagicMock()
        monkeypatch.setattr(service, "record_queue_error", record_error)

        result = service.query_pending_offline_submissions(app, db)

        assert result == (
            False,
            "Error querying pending offline submissions: database unavailable",
            None,
        )
        record_error.assert_called_once_with(
            app,
            None,
            service.query_pending_offline_submissions,
            "database unavailable",
        )


class TestUpdateOfflineSubmissionStatus:
    def test_updates_submission_and_commits(self):
        app = MagicMock()
        submission = MagicMock()
        query = make_query(submission)
        db = MagicMock()
        db.session.query.return_value = query

        result = service.update_offline_submission_status(app, db, 42, "processed")

        assert result == (True, None)
        assert submission.status == "processed"
        db.session.commit.assert_called_once()
        db.session.query.assert_called_once_with(FormsflowOfflineSubmission)
        query.filter.assert_called_once()

    def test_records_and_returns_database_update_errors(self, monkeypatch):
        app = MagicMock()
        db = MagicMock()
        db.session.query.return_value = make_query(error=RuntimeError("database unavailable"))
        record_error = MagicMock()
        monkeypatch.setattr(service, "record_queue_error", record_error)

        result = service.update_offline_submission_status(app, db, 42, "processed")

        assert result == (False, "Error updating offline submission status: database unavailable")
        record_error.assert_called_once_with(
            app,
            {"id": 42},
            service.update_offline_submission_status,
            "database unavailable",
        )
