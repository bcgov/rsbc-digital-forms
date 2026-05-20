from __future__ import annotations

import sys
import logging

from python.irp_rts_notification_job.irp_rts_notification_service import run_notification
from python.irp_rts_notification_job.config import Config


numeric_level = getattr(logging, Config.LOG_LEVEL, 10)
logging.basicConfig(
    level=numeric_level,
    format='%(asctime)s [IRP_RTS_NOTIFICATION_JOB]: %(levelname)s %(module)s:%(lineno)d %(message)s'
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


def execute_irp_rts_notification_job() -> None:
    logger.info("Starting IRP RTS notification job.")
    try:
        _print_env_variables()

        run_notification()

        logger.info("IRP RTS notification job completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred during IRP RTS notification job: {e}")
        sys.exit(1)


if __name__ == "__main__":
    execute_irp_rts_notification_job()
