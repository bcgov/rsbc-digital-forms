from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from python.stuck_submissions_monitor_job import stuck_submissions_monitor_service as service


class TestRunStuckSubmissionsMonitor:
    def test_fetches_and_processes_stuck_submissions(self, monkeypatch):
        conn = MagicMock()
        conn.__enter__.return_value = conn
        connect_mock = MagicMock(return_value=conn)
        monkeypatch.setattr(service.psycopg2, "connect", connect_mock)

        fetch_mock = MagicMock(return_value=[])
        process_mock = MagicMock(return_value={"success": 0, "failure": 0, "not_found": 0})
        monkeypatch.setattr(service, "_fetch_stuck_submissions", fetch_mock)
        monkeypatch.setattr(service, "_process_stuck_submissions", process_mock)

        service.run_stuck_submissions_monitor()

        connect_mock.assert_called_once()
        fetch_mock.assert_called_once_with(conn)
        process_mock.assert_called_once_with([])

    def test_raises_when_connection_fails(self, monkeypatch):
        connect_mock = MagicMock(side_effect=RuntimeError("connection error"))
        monkeypatch.setattr(service.psycopg2, "connect", connect_mock)

        with pytest.raises(RuntimeError):
            service.run_stuck_submissions_monitor()


class TestFetchStuckSubmissions:
    def test_fetches_submissions_from_database(self):
        conn = MagicMock()
        cursor = conn.cursor.return_value.__enter__.return_value
        submissions = [("application-id", "draft-id", "submission-id", "form-id")]
        cursor.fetchall.return_value = submissions

        result = service._fetch_stuck_submissions(conn)

        assert result == submissions
        cursor.execute.assert_called_once()
        assert "application_status = 'New'" in cursor.execute.call_args.args[0]
        assert "INTERVAL '10 minutes'" in cursor.execute.call_args.args[0]


class TestProcessStuckSubmissions:
    def test_retries_submissions_found_in_mongo(self, monkeypatch):
        submission = ("application-id", "draft-id", "submission-id", "form-id")
        document = {"data": {"answer": "value"}}
        monkeypatch.setattr(service, "_fetch_submission_from_mongo", MagicMock(return_value=document))
        create_payload = MagicMock(return_value={"submissionId": "submission-id"})
        send_retry = MagicMock(return_value=True)
        send_summary = MagicMock()
        monkeypatch.setattr(service, "_create_retry_submission_payload", create_payload)
        monkeypatch.setattr(service, "_send_retry_submission", send_retry)
        monkeypatch.setattr(service, "_send_summary_to_splunk", send_summary)

        result = service._process_stuck_submissions([submission])

        assert result == {"success": 1, "failure": 0, "not_found": 0}
        create_payload.assert_called_once_with("form-id", "submission-id", document)
        send_retry.assert_called_once_with("application-id", {"submissionId": "submission-id"})
        send_summary.assert_called_once_with(result)

    def test_counts_missing_mongo_submissions(self, monkeypatch):
        submission = ("application-id", "draft-id", "submission-id", "form-id")
        monkeypatch.setattr(service, "_fetch_submission_from_mongo", MagicMock(return_value=None))
        send_retry = MagicMock()
        send_summary = MagicMock()
        monkeypatch.setattr(service, "_send_retry_submission", send_retry)
        monkeypatch.setattr(service, "_send_summary_to_splunk", send_summary)

        result = service._process_stuck_submissions([submission])

        assert result == {"success": 0, "failure": 0, "not_found": 1}
        send_retry.assert_not_called()
        send_summary.assert_called_once_with(result)

    def test_counts_failed_retry_submissions(self, monkeypatch):
        submission = ("application-id", "draft-id", "submission-id", "form-id")
        monkeypatch.setattr(service, "_fetch_submission_from_mongo", MagicMock(return_value={"data": {}}))
        monkeypatch.setattr(service, "_create_retry_submission_payload", MagicMock(return_value={}))
        monkeypatch.setattr(service, "_send_retry_submission", MagicMock(return_value=False))
        monkeypatch.setattr(service, "_send_summary_to_splunk", MagicMock())

        result = service._process_stuck_submissions([submission])

        assert result == {"success": 0, "failure": 1, "not_found": 0}


class TestGetAccessToken:
    def setup_method(self):
        service._access_token = None
        service._access_token_expires_at = 0.0

    def test_reuses_token_until_it_expires(self, monkeypatch):
        monkeypatch.setattr(service.time, "monotonic", lambda: 100)
        token_response = MagicMock()
        token_response.json.return_value = {"access_token": "token", "expires_in": 60}
        post_mock = MagicMock(return_value=token_response)
        monkeypatch.setattr(service.requests, "post", post_mock)

        assert service._get_access_token() == "token"
        assert service._get_access_token() == "token"

        post_mock.assert_called_once()

    def test_fetches_new_token_after_expiration(self, monkeypatch):
        current_time = [100]
        monkeypatch.setattr(service.time, "monotonic", lambda: current_time[0])
        responses = []
        for token in ("first-token", "second-token"):
            response = MagicMock()
            response.json.return_value = {"access_token": token, "expires_in": 10}
            responses.append(response)
        post_mock = MagicMock(side_effect=responses)
        monkeypatch.setattr(service.requests, "post", post_mock)

        assert service._get_access_token() == "first-token"
        current_time[0] = 110
        assert service._get_access_token() == "second-token"

        assert post_mock.call_count == 2
