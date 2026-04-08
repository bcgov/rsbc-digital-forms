from __future__ import annotations

from datetime import datetime
from unittest.mock import MagicMock

import pytest

from python.data_cleanup_job import data_cleanup_job as job


class TestExecuteDataCleanupJob:
    def test_calls_run_cleanup_with_correct_cutoff_and_dry_run(self, monkeypatch):
        fixed_now = datetime(2026, 4, 1, 12, 0, 0)

        class FakeDateTime(datetime):
            @classmethod
            def now(cls):
                return fixed_now

        monkeypatch.setattr(job, "datetime", FakeDateTime)
        monkeypatch.setattr(job, "_print_env_variables", lambda: None)
        monkeypatch.setattr(job.Config, "RETENTION_DAYS", 30)
        monkeypatch.setattr(job.Config, "DRY_RUN", True)

        run_cleanup_mock = MagicMock()
        monkeypatch.setattr(job, "run_cleanup", run_cleanup_mock)

        job.execute_data_cleanup_job()

        run_cleanup_mock.assert_called_once()
        called_cutoff, called_dry_run = run_cleanup_mock.call_args.args
        assert called_cutoff == fixed_now - job.timedelta(days=30)
        assert called_dry_run is True

    def test_exits_with_code_1_when_run_cleanup_raises(self, monkeypatch):
        monkeypatch.setattr(job, "_print_env_variables", lambda: None)
        monkeypatch.setattr(job.Config, "RETENTION_DAYS", 7)
        monkeypatch.setattr(job.Config, "DRY_RUN", True)

        def _boom(_cutoff, _dry_run):
            raise RuntimeError("db down")

        monkeypatch.setattr(job, "run_cleanup", _boom)

        def _raise_system_exit(code: int):
            raise SystemExit(code)

        monkeypatch.setattr(job.sys, "exit", _raise_system_exit)

        with pytest.raises(SystemExit) as excinfo:
            job.execute_data_cleanup_job()
        assert excinfo.value.code == 1

    def test_exits_with_code_1_when_retention_days_is_negative(self, monkeypatch):
        monkeypatch.setattr(job, "_print_env_variables", lambda: None)
        monkeypatch.setattr(job.Config, "RETENTION_DAYS", -1)
        monkeypatch.setattr(job.Config, "DRY_RUN", True)

        run_cleanup_mock = MagicMock()
        monkeypatch.setattr(job, "run_cleanup", run_cleanup_mock)

        def _raise_system_exit(code: int):
            raise SystemExit(code)

        monkeypatch.setattr(job.sys, "exit", _raise_system_exit)

        with pytest.raises(SystemExit) as excinfo:
            job.execute_data_cleanup_job()

        assert excinfo.value.code == 1
        run_cleanup_mock.assert_not_called()
