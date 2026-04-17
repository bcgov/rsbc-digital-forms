from __future__ import annotations

from datetime import datetime, timedelta
import sys
import logging

from python.data_cleanup_job.data_cleanup_service import run_cleanup
from python.data_cleanup_job.config import Config


# Set up logging
numeric_level = getattr(logging, Config.LOG_LEVEL, 10)
logging.basicConfig(
    level=numeric_level,
    format='%(asctime)s [DATA_CLEANUP_JOB]: %(levelname)s %(module)s:%(lineno)d %(message)s'
)
logger = logging.getLogger(__name__)
# Change pymongo logging to WARNING to reduce noise
logging.getLogger("pymongo").setLevel(logging.WARNING)
logging.getLogger("pymongo.connection").setLevel(logging.ERROR)
logging.getLogger("pymongo.serverSelection").setLevel(logging.ERROR)

def _print_env_variables():
    logger.debug("Environment Variables:")
    logger.info(f"LOG_LEVEL: {Config.LOG_LEVEL}")
    logger.info(f"ENVIRONMENT: {Config.ENVIRONMENT}")
    logger.info(f"RETENTION_DAYS: {Config.RETENTION_DAYS}")
    logger.info(f"DRY_RUN: {Config.DRY_RUN}")

    logger.info(f"DB_HOST: {Config.DB_HOST}")
    logger.info(f"DB_USER: {Config.DB_USER}")
    logger.info(f"DB_NAME: {Config.DB_NAME_DF}")
    logger.info(f"DB_PORT: {Config.DB_PORT}")

    logger.info(f"MONGO_HOST: {Config.MONGO_HOST}")
    logger.info(f"MONGO_PORT: {Config.MONGO_PORT}")
    logger.info(f"MONGO_USER: {Config.MONGO_USER}")
    logger.info(f"MONGO_DB_NAME: {Config.MONGO_DB_NAME}")


def execute_data_cleanup_job() -> None:
    logger.info("Starting data cleanup job.")
    try:
        _print_env_variables()

        retention_days = Config.RETENTION_DAYS
        if retention_days < 0:
            raise ValueError("RETENTION_DAYS must be a non-negative integer")

        dry_run = Config.DRY_RUN

        cutoff_date = datetime.now() - timedelta(days=retention_days)
        logger.info("Cutoff date: %s (records older than %d days)", cutoff_date, retention_days)

        run_cleanup(cutoff_date, dry_run)

        logger.info("Data cleanup job completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred during data cleanup job: {e}")
        sys.exit(1)


if __name__ == "__main__":
    execute_data_cleanup_job()
