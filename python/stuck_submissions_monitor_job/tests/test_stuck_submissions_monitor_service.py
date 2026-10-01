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
        process_mock = MagicMock()
        monkeypatch.setattr(service, "_fetch_stuck_submissions", fetch_mock)
        monkeypatch.setattr(service, "_process_stuck_submissions", process_mock)

        service.run_stuck_submissions_monitor()

        connect_mock.assert_called_once()
        fetch_mock.assert_called_once_with(conn)
        process_mock.assert_called_once_with(conn, [])

    def test_raises_when_connection_fails(self, monkeypatch):
        connect_mock = MagicMock(side_effect=RuntimeError("connection error"))
        monkeypatch.setattr(service.psycopg2, "connect", connect_mock)

        with pytest.raises(RuntimeError):
            service.run_stuck_submissions_monitor()


class TestFetchStuckSubmissions:
    def test_not_yet_implemented(self):
        with pytest.raises(NotImplementedError):
            service._fetch_stuck_submissions(MagicMock())


class TestProcessStuckSubmissions:
    def test_not_yet_implemented(self):
        with pytest.raises(NotImplementedError):
            service._process_stuck_submissions(MagicMock(), [])


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
