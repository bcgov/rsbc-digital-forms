from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from python.stuck_submissions_monitor_job import stuck_submissions_monitor_job as job


class TestExecuteStuckSubmissionsMonitorJob:
    def test_calls_run_stuck_submissions_monitor(self, monkeypatch):
        monkeypatch.setattr(job, "_print_env_variables", lambda: None)

        run_monitor_mock = MagicMock()
        monkeypatch.setattr(job, "run_stuck_submissions_monitor", run_monitor_mock)

        job.execute_stuck_submissions_monitor_job()

        run_monitor_mock.assert_called_once()

    def test_exits_with_code_1_when_run_stuck_submissions_monitor_raises(self, monkeypatch):
        monkeypatch.setattr(job, "_print_env_variables", lambda: None)

        def _boom():
            raise RuntimeError("service error")

        monkeypatch.setattr(job, "run_stuck_submissions_monitor", _boom)

        def _raise_system_exit(code: int):
            raise SystemExit(code)

        monkeypatch.setattr(job.sys, "exit", _raise_system_exit)

        with pytest.raises(SystemExit) as excinfo:
            job.execute_stuck_submissions_monitor_job()
        assert excinfo.value.code == 1
