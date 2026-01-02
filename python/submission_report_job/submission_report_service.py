from datetime import datetime
import logging
import psycopg2

from python.common.rsi_email import send_submission_report_by_status
from python.submission_report_job.config import Config
from python.submission_report_job.submission_report_by_status import SubmissionReportByStatus, SubmissionReportByStatusItem

logger = logging.getLogger(__name__)

def generate_report_by_status(initial: datetime, final: datetime) -> None:
    logger.info("Generating submission report by status for period: %s to %s", initial, final)
    with psycopg2.connect(
      database=Config.DB_NAME,
      user=Config.DB_USER,
      password=Config.DB_PASS,
      host=Config.DB_HOST,
      port=Config.DB_PORT
    ) as conn:
        report = _query_submission_reports_by_status(conn, initial, final)
    
    _send_report(report, initial, final)
    logger.info("Submission report by status generated and sent successfully.")


def _query_submission_reports_by_status(conn, initial: datetime, final: datetime) -> list['SubmissionReportByStatus']:
    query = """
      SELECT form_name, application_status, offline, count(1)
      FROM submission_report_view
      WHERE created_dt BETWEEN %s AND %s
      GROUP BY form_name, application_status, offline
      ORDER BY form_name, application_status;
    """
    with conn.cursor() as cursor:
        cursor.execute(query, (initial, final))
        rows = cursor.fetchall()

    current_form_name = None
    report_data: list['SubmissionReportByStatus'] = []
    for row in rows:
        form_name, application_status, offline, count = row
        if current_form_name != form_name:
            current_form_name = form_name
            report_data.append(SubmissionReportByStatus(
                form_name=form_name
            ))
        report_data[-1].items.append(SubmissionReportByStatusItem(
            application_status=application_status,
            offline=offline,
            count=count
        ))
        report_data[-1].total_count += count
    return report_data

def _send_report(report_data: list['SubmissionReportByStatus'], initial: datetime, final: datetime) -> str:
    template_data = {
        "report_data": report_data,
        "period": f"{initial.strftime('%Y-%m-%d')} to {final.strftime('%Y-%m-%d')}"
    }
    send_submission_report_by_status(message=template_data,
                                     subject=f"Submission Report by Status for period of {initial.strftime('%Y-%m-%d')} to {final.strftime('%Y-%m-%d')}",
                                     config=Config)