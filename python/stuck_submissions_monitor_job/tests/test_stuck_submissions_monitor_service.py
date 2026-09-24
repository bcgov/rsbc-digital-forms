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
