from __future__ import annotations

import sys
import logging

from python.stuck_submissions_monitor_job.stuck_submissions_monitor_service import run_stuck_submissions_monitor
from python.stuck_submissions_monitor_job.config import Config


numeric_level = getattr(logging, Config.LOG_LEVEL, 10)
logging.basicConfig(
    level=numeric_level,
    format='%(asctime)s [STUCK_SUBMISSIONS_MONITOR_JOB]: %(levelname)s %(module)s:%(lineno)d %(message)s'
)
logger = logging.getLogger(__name__)
logging.getLogger("pymongo").setLevel(logging.WARNING)
logging.getLogger("pymongo.connection").setLevel(logging.ERROR)
logging.getLogger("pymongo.serverSelection").setLevel(logging.ERROR)


def _print_env_variables():
    logger.debug("Environment Variables:")
    logger.info(f"LOG_LEVEL: {Config.LOG_LEVEL}")
    logger.info(f"ENVIRONMENT: {Config.ENVIRONMENT}")

    logger.info(f"DB_HOST: {Config.DB_HOST}")
    logger.info(f"DB_USER: {Config.DB_USER}")
    logger.info(f"DB_NAME: {Config.DB_NAME_DF}")
    logger.info(f"DB_PORT: {Config.DB_PORT}")

    logger.info(f"SPLUNK_HOST: {Config.SPLUNK_HOST}")
    logger.info(f"SPLUNK_PORT: {Config.SPLUNK_PORT}")
    logger.info(f"OPENSHIFT_PLATE: {Config.OPENSHIFT_PLATE}")


def execute_stuck_submissions_monitor_job() -> None:
    logger.info("Starting stuck submissions monitor job.")
    try:
        _print_env_variables()

        run_stuck_submissions_monitor()

        logger.info("Stuck submissions monitor job completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred during stuck submissions monitor job: {e}")
        sys.exit(1)


if __name__ == "__main__":
    execute_stuck_submissions_monitor_job()
