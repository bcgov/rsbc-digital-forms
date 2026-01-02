from __future__ import annotations

from datetime import datetime
from unittest.mock import MagicMock

import pytest

from python.submission_report_job import submission_report_service as service
from python.submission_report_job.submission_report_by_status import (
	SubmissionReportByStatus,
	SubmissionReportByStatusItem,
)


class TestQuerySubmissionReportsByStatus:
	def test_groups_rows_by_form_name_and_sums_totals(self):
		initial = datetime(2025, 12, 1)
		final = datetime(2025, 12, 31)

		conn = MagicMock()
		cursor = MagicMock()
		cursor.fetchall.return_value = [
			("Form A", "SUBMITTED", False, 2),
			("Form A", "DRAFT", True, 1),
			("Form B", "SUBMITTED", False, 5),
		]

		cursor_cm = MagicMock()
		cursor_cm.__enter__.return_value = cursor
		conn.cursor.return_value = cursor_cm

		report = service._query_submission_reports_by_status(conn, initial, final)

		assert len(report) == 2
		assert report[0].form_name == "Form A"
		assert report[0].total_count == 3
		assert [(i.application_status, i.offline, i.count) for i in report[0].items] == [
			("SUBMITTED", False, 2),
			("DRAFT", True, 1),
		]
		assert report[1].form_name == "Form B"
		assert report[1].total_count == 5
		assert [(i.application_status, i.offline, i.count) for i in report[1].items] == [
			("SUBMITTED", False, 5),
		]

		(query, params), _kwargs = cursor.execute.call_args
		assert "submission_report_view" in query
		assert params == (initial, final)

	def test_empty_rows_returns_empty_report(self):
		initial = datetime(2025, 12, 1)
		final = datetime(2025, 12, 31)

		conn = MagicMock()
		cursor = MagicMock()
		cursor.fetchall.return_value = []

		cursor_cm = MagicMock()
		cursor_cm.__enter__.return_value = cursor
		conn.cursor.return_value = cursor_cm

		report = service._query_submission_reports_by_status(conn, initial, final)
		assert report == []


class TestSendReport:
	def test_send_report_builds_expected_template_and_subject(self, monkeypatch):
		initial = datetime(2025, 12, 1)
		final = datetime(2025, 12, 31)

		report_data = [SubmissionReportByStatus("Form A")]
		report_data[0].items.append(SubmissionReportByStatusItem("SUBMITTED", False, 2))
		report_data[0].total_count = 2

		send_mock = MagicMock()
		monkeypatch.setattr(service, "send_submission_report_by_status", send_mock)

		service._send_report(report_data, initial, final)

		send_mock.assert_called_once()
		kwargs = send_mock.call_args.kwargs
		assert kwargs["message"]["report_data"] == report_data
		assert kwargs["message"]["period"] == "2025-12-01 to 2025-12-31"
		assert (
			kwargs["subject"]
			== "Submission Report by Status for period of 2025-12-01 to 2025-12-31"
		)
		assert kwargs["config"] is service.Config


class TestGenerateReportByStatus:
	def test_orchestrates_db_query_and_email_send(self, monkeypatch):
		initial = datetime(2025, 12, 1)
		final = datetime(2025, 12, 31)

		conn = MagicMock()
		conn_cm = MagicMock()
		conn_cm.__enter__.return_value = conn

		connect_mock = MagicMock(return_value=conn_cm)
		monkeypatch.setattr(service.psycopg2, "connect", connect_mock)

		report = [SubmissionReportByStatus("Form A")]
		query_mock = MagicMock(return_value=report)
		send_mock = MagicMock()
		monkeypatch.setattr(service, "_query_submission_reports_by_status", query_mock)
		monkeypatch.setattr(service, "_send_report", send_mock)

		service.generate_report_by_status(initial, final)

		connect_mock.assert_called_once_with(
			database=service.Config.DB_NAME,
			user=service.Config.DB_USER,
			password=service.Config.DB_PASS,
			host=service.Config.DB_HOST,
			port=service.Config.DB_PORT,
		)
		query_mock.assert_called_once_with(conn, initial, final)
		send_mock.assert_called_once_with(report, initial, final)
