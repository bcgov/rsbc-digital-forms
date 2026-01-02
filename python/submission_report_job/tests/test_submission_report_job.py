from __future__ import annotations

from datetime import datetime
import argparse

from unittest.mock import MagicMock

import pytest

from python.submission_report_job import submission_report_job as job


class TestParseIsoDateOrDatetime:
	def test_parses_date_only_initial_as_start_of_day(self):
		dt = job._parse_iso_date_or_datetime("2025-12-01", is_final=False)
		assert dt == datetime(2025, 12, 1, 0, 0, 0, 0)

	def test_parses_date_only_final_as_end_of_day(self):
		dt = job._parse_iso_date_or_datetime("2025-12-31", is_final=True)
		assert dt == datetime(2025, 12, 31, 23, 59, 59, 999999)

	def test_parses_datetime_preserving_time(self):
		dt = job._parse_iso_date_or_datetime("2025-12-31T13:45:00", is_final=True)
		assert dt == datetime(2025, 12, 31, 13, 45, 0)

	def test_invalid_value_raises_argument_type_error(self):
		with pytest.raises(argparse.ArgumentTypeError):
			job._parse_iso_date_or_datetime("not-a-date", is_final=False)


class TestExecuteSubmissionReportJob:
	def test_uses_defaults_when_initial_and_final_missing(self, monkeypatch):
		fixed_now = datetime(2026, 1, 2, 10, 0, 0)

		class FakeDateTime(datetime):
			@classmethod
			def now(cls):
				return fixed_now

		monkeypatch.setattr(job, "datetime", FakeDateTime)
		monkeypatch.setattr(job, "_print_env_variables", lambda: None)

		generate_mock = MagicMock()
		monkeypatch.setattr(job, "generate_report_by_status", generate_mock)

		job.execute_submission_report_job(initial=None, final=None)

		generate_mock.assert_called_once()
		called_initial, called_final = generate_mock.call_args.args
		assert called_final == fixed_now
		assert called_initial == fixed_now - job.timedelta(days=7)

	def test_exits_with_code_1_when_initial_greater_than_final(self, monkeypatch):
		monkeypatch.setattr(job, "_print_env_variables", lambda: None)

		generate_mock = MagicMock()
		monkeypatch.setattr(job, "generate_report_by_status", generate_mock)

		def _raise_system_exit(code: int):
			raise SystemExit(code)

		monkeypatch.setattr(job.sys, "exit", _raise_system_exit)

		with pytest.raises(SystemExit) as excinfo:
			job.execute_submission_report_job(
				initial=datetime(2026, 1, 2, 0, 0, 1),
				final=datetime(2026, 1, 2, 0, 0, 0),
			)

		assert excinfo.value.code == 1
		generate_mock.assert_not_called()

	def test_exits_with_code_1_when_generate_report_raises(self, monkeypatch):
		monkeypatch.setattr(job, "_print_env_variables", lambda: None)

		def _boom(_initial, _final):
			raise RuntimeError("db down")

		monkeypatch.setattr(job, "generate_report_by_status", _boom)

		def _raise_system_exit(code: int):
			raise SystemExit(code)

		monkeypatch.setattr(job.sys, "exit", _raise_system_exit)

		with pytest.raises(SystemExit) as excinfo:
			job.execute_submission_report_job(
				initial=datetime(2025, 12, 1),
				final=datetime(2025, 12, 31),
			)
		assert excinfo.value.code == 1
