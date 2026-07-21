from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from python.irp_rts_notification_job import irp_rts_notification_job as job


class TestExecuteIrpRtsNotificationJob:
    def test_calls_run_notification(self, monkeypatch):
        monkeypatch.setattr(job, "_print_env_variables", lambda: None)

        run_notification_mock = MagicMock()
        monkeypatch.setattr(job, "run_notification", run_notification_mock)

        job.execute_irp_rts_notification_job()

        run_notification_mock.assert_called_once()

    def test_exits_with_code_1_when_run_notification_raises(self, monkeypatch):
        monkeypatch.setattr(job, "_print_env_variables", lambda: None)

        def _boom():
            raise RuntimeError("service error")

        monkeypatch.setattr(job, "run_notification", _boom)

        def _raise_system_exit(code: int):
            raise SystemExit(code)

        monkeypatch.setattr(job.sys, "exit", _raise_system_exit)

        with pytest.raises(SystemExit) as excinfo:
            job.execute_irp_rts_notification_job()
        assert excinfo.value.code == 1
