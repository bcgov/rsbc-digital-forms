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


def execute_submission_report_job(number_of_days: int) -> None:
    logger.info("Starting submission report job, generating report for the last %d days.", number_of_days)
    try:
        _print_env_variables()
        if number_of_days < 0:
            raise ValueError("number_of_days must be a non-negative integer")
        final = datetime.now().date()
        initial = final - timedelta(days=number_of_days)

        generate_report_by_status(initial, final)
        logger.info("Submission reports processed successfully.")
    except Exception as e:
        logger.error(f"An error occurred during submission report job: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and send submission report by status.")
    parser.add_argument(
        "--number-of-days",
        help="Number of days back from today to generate the report for (default: 7).",
    )
    args = parser.parse_args()

    number_of_days = int(args.number_of_days) if args.number_of_days else 7
    if number_of_days < 0:
        logger.error("number-of-days must be a non-negative integer.")
        sys.exit(1)
    execute_submission_report_job(number_of_days=number_of_days)