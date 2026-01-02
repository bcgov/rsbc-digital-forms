from __future__ import annotations

from datetime import datetime, timedelta
import argparse
import sys
import logging

from python.submission_report_job.submission_report_service import generate_report_by_status
from python.submission_report_job.config import Config


# Set up logging
numeric_level = getattr(logging, Config.LOG_LEVEL, 10)
logging.basicConfig(
    level=numeric_level,
    format='%(asctime)s [SUBMISSION_REPORT_JOB]: %(levelname)s %(module)s:%(lineno)d %(message)s'
)
logger = logging.getLogger(__name__)


def _parse_iso_date_or_datetime(value: str, *, is_final: bool) -> datetime:
    """Parse an ISO 8601 date or datetime.

    Accepts:
      - YYYY-MM-DD
      - YYYY-MM-DDTHH:MM[:SS[.ffffff]][+HH:MM]

    If a date-only value is provided:
      - initial becomes start-of-day
      - final becomes end-of-day
    """
    try:
        dt = datetime.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            "Invalid date/datetime. Use ISO format like '2025-12-30' or '2025-12-30T13:45:00'."
        ) from exc

    # datetime.fromisoformat('YYYY-MM-DD') returns midnight; treat date-only specially.
    if "T" not in value and " " not in value:
        if is_final:
            return dt.replace(hour=23, minute=59, second=59, microsecond=999999)
        return dt.replace(hour=0, minute=0, second=0, microsecond=0)

    return dt

def _print_env_variables():
    logger.debug("Environment Variables:")
    logger.info(f"LOG_LEVEL: {Config.LOG_LEVEL}")
    logger.info(f"ENVIRONMENT: {Config.ENVIRONMENT}")

    logger.info(f"DB_HOST: {Config.DB_HOST}")
    logger.info(f"DB_USER: {Config.DB_USER}")
    logger.info(f"DB_NAME: {Config.DB_NAME}")
    logger.info(f"DB_PORT: {Config.DB_PORT}")

    logger.info(f"COMM_SERV_AUTH_URL: {Config.COMM_SERV_AUTH_URL}")
    logger.info(f"COMM_SERV_API_ROOT_URL: {Config.COMM_SERV_API_ROOT_URL}")
    logger.info(f"COMM_SERV_REALM: {Config.COMM_SERV_REALM}")

    logger.info(f"RSIOPS_EMAIL_ADDRESS: {Config.RSIOPS_EMAIL_ADDRESS}")
    logger.info(f"REPLY_EMAIL_ADDRESS: {Config.REPLY_EMAIL_ADDRESS}")
    logger.info(f"BCC_EMAIL_ADDRESSES: {Config.BCC_EMAIL_ADDRESSES}")


def execute_submission_report_job(initial: datetime = None, final: datetime = None) -> None:
    logger.info("Starting submission report job")
    try:
        _print_env_variables()
        if initial is None:
            final_default = datetime.now()
            initial = final_default - timedelta(days=7)
        if final is None:
            final = datetime.now()
        if initial > final:
            raise ValueError(f"initial must be <= final (got {initial.isoformat()} > {final.isoformat()})")
        generate_report_by_status(initial, final)
        logger.info("Submission reports processed successfully.")
    except Exception as e:
        logger.error(f"An error occurred during submission report job: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and send submission report by status.")
    parser.add_argument(
        "--initial",
        help="Initial date/datetime (ISO). Examples: 2025-12-01 or 2025-12-01T00:00:00",
    )
    parser.add_argument(
        "--final",
        help="Final date/datetime (ISO). Examples: 2025-12-31 or 2025-12-31T23:59:59",
    )
    args = parser.parse_args()

    if (args.initial is None) ^ (args.final is None):
        parser.error("--initial and --final must be provided together")

    initial = _parse_iso_date_or_datetime(args.initial, is_final=False) if args.initial else None
    final = _parse_iso_date_or_datetime(args.final, is_final=True) if args.final else None
    execute_submission_report_job(initial=initial, final=final)