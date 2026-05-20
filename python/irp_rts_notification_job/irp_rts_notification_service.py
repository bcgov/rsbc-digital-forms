import logging

import psycopg2

from python.irp_rts_notification_job.config import Config

logger = logging.getLogger(__name__)


def run_notification() -> None:
    logger.info("Running IRP RTS notification.")

    logger.info("IRP RTS notification completed.")


def _fetch_pending_notifications(conn) -> list:
    query = "SELECT * FROM irp_rts_notifications WHERE notified = FALSE"
    with conn.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()
