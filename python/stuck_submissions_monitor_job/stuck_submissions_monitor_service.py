from __future__ import annotations

import logging

import psycopg2

from python.stuck_submissions_monitor_job.config import Config

logger = logging.getLogger(__name__)


def run_stuck_submissions_monitor() -> None:
    logger.info("Running stuck submissions monitor.")

    try:
        with psycopg2.connect(
            database=Config.DB_NAME_DF,
            user=Config.DB_USER,
            password=Config.DB_PASS,
            host=Config.DB_HOST,
            port=Config.DB_PORT
        ) as conn:
            stuck_submissions = _fetch_stuck_submissions(conn)
            logger.info(f"Found {len(stuck_submissions)} stuck submissions.")
            _process_stuck_submissions(conn, stuck_submissions)

    except Exception as e:
        logger.error(f"An error occurred while running stuck submissions monitor: {e}")
        raise

    logger.info("Stuck submissions monitor completed.")


def _fetch_stuck_submissions(conn) -> list:
    # TODO: implement query to identify stuck submissions.
    raise NotImplementedError("_fetch_stuck_submissions is not yet implemented.")


def _process_stuck_submissions(conn, stuck_submissions) -> None:
    # TODO: implement processing/notification logic for stuck submissions.
    raise NotImplementedError("_process_stuck_submissions is not yet implemented.")
