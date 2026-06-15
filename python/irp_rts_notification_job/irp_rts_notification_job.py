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

    logger.info(f"KEYCLOAK_AUTH_URL: {Config.KEYCLOAK_AUTH_URL}")
    logger.info(f"KEYCLOAK_REALM: {Config.KEYCLOAK_REALM}")
    logger.info(f"KEYCLOAK_CLIENT_ID: {Config.KEYCLOAK_CLIENT_ID}")

    logger.info(f"SPLUNK_HOST: {Config.SPLUNK_HOST}")
    logger.info(f"SPLUNK_PORT: {Config.SPLUNK_PORT}")
    logger.info(f"OPENSHIFT_PLATE: {Config.OPENSHIFT_PLATE}")

    logger.info(f"COMM_SERV_AUTH_URL: {Config.COMM_SERV_AUTH_URL}")
    logger.info(f"COMM_SERV_API_ROOT_URL: {Config.COMM_SERV_API_ROOT_URL}")
    logger.info(f"COMM_SERV_REALM: {Config.COMM_SERV_REALM}")
    logger.info(f"COMM_SERV_CLIENT_ID: {Config.COMM_SERV_CLIENT_ID}")

    logger.info(f"REPLY_EMAIL_ADDRESS: {Config.REPLY_EMAIL_ADDRESS}")
    logger.info(f"BCC_EMAIL_ADDRESSES: {Config.BCC_EMAIL_ADDRESSES}")
    logger.info(f"SUPERINTENDENT_EMAIL: {Config.SUPERINTENDENT_EMAIL}")

    logger.info(f"NUMBER_OF_DAYS_TO_COMPLETE_RTS: {Config.NUMBER_OF_DAYS_TO_COMPLETE_RTS}")
    logger.info(f"NUMBER_OF_DAYS_TO_SEND_REMINDER: {Config.NUMBER_OF_DAYS_TO_SEND_REMINDER}")

    logger.info(f"JINJA2_TEMPLATE_PATH: {Config.JINJA2_TEMPLATE_PATH}")


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
