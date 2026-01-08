from __future__ import annotations

from datetime import datetime
from unittest.mock import MagicMock

import pytest

from python.submission_report_job import submission_report_job as job


class TestExecuteSubmissionReportJob:
    def test_calls_generate_report_for_last_n_days(self, monkeypatch):
        fixed_now = datetime(2026, 1, 2, 10, 0, 0)

        class FakeDateTime(datetime):
            @classmethod
            def now(cls):
                return fixed_now

        monkeypatch.setattr(job, "datetime", FakeDateTime)
        monkeypatch.setattr(job, "_print_env_variables", lambda: None)

        generate_mock = MagicMock()
        monkeypatch.setattr(job, "generate_report_by_status", generate_mock)

        job.execute_submission_report_job(number_of_days=2)

        generate_mock.assert_called_once()
        called_initial, called_final = generate_mock.call_args.args
        assert called_final == fixed_now.date()
        assert called_initial == fixed_now.date() - job.timedelta(days=2)

    def test_exits_with_code_1_when_generate_report_raises(self, monkeypatch):
        monkeypatch.setattr(job, "_print_env_variables", lambda: None)

        def _boom(_initial, _final):
            raise RuntimeError("db down")

        monkeypatch.setattr(job, "generate_report_by_status", _boom)

        def _raise_system_exit(code: int):
            raise SystemExit(code)

        monkeypatch.setattr(job.sys, "exit", _raise_system_exit)

        with pytest.raises(SystemExit) as excinfo:
            job.execute_submission_report_job(number_of_days=7)
        assert excinfo.value.code == 1

    def test_exits_with_code_1_when_number_of_days_is_negative(self, monkeypatch):
        monkeypatch.setattr(job, "_print_env_variables", lambda: None)

        generate_mock = MagicMock()
        monkeypatch.setattr(job, "generate_report_by_status", generate_mock)

        def _raise_system_exit(code: int):
            raise SystemExit(code)

        monkeypatch.setattr(job.sys, "exit", _raise_system_exit)

        with pytest.raises(SystemExit) as excinfo:
            job.execute_submission_report_job(number_of_days=-1)

        assert excinfo.value.code == 1
        generate_mock.assert_not_called()
