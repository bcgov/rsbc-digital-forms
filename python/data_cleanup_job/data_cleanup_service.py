from datetime import datetime
import logging

import psycopg2
from pymongo import MongoClient

from python.data_cleanup_job.config import Config

logger = logging.getLogger(__name__)

POSTGRES_DF_TARGETS = [
    {"table": "df_errors", "date_column": "received_dt"},
]

MONGO_COLLECTION = "submissions"


def run_cleanup(cutoff_date: datetime, dry_run: bool) -> None:
    mode_label = "DRY RUN" if dry_run else "LIVE"
    logger.info("Running data cleanup in %s mode. Cutoff date: %s", mode_label, cutoff_date)

    cleanup_postgres_DF(cutoff_date, dry_run)
    cleanup_mongo(cutoff_date, dry_run)

    logger.info("Data cleanup completed.")


def cleanup_postgres_DF(cutoff_date: datetime, dry_run: bool) -> dict:
    logger.info("Connecting to Postgres database: %s@%s:%s/%s",
                Config.DB_USER, Config.DB_HOST, Config.DB_PORT, Config.DB_NAME_DF)

    results = {}
    with psycopg2.connect(
        database=Config.DB_NAME_DF,
        user=Config.DB_USER,
        password=Config.DB_PASS,
        host=Config.DB_HOST,
        port=Config.DB_PORT
    ) as conn:
        for target in POSTGRES_DF_TARGETS:
            table = target["table"]
            date_column = target["date_column"]
            count = _count_postgres_records(conn, table, date_column, cutoff_date)
            results[table] = count
            logger.info("Postgres table '%s': %d record(s) older than %s", table, count, cutoff_date)

            if not dry_run and count > 0:
                deleted = _delete_postgres_records(conn, table, date_column, cutoff_date)
                logger.info("Postgres table '%s': deleted %d record(s).", table, deleted)

    return results


def cleanup_mongo(cutoff_date: datetime, dry_run: bool) -> int:
    logger.info("Connecting to MongoDB: %s:%s, database: %s",
                Config.MONGO_HOST, Config.MONGO_PORT, Config.MONGO_DB_NAME)

    client = MongoClient(
        host=Config.MONGO_HOST,
        port=Config.MONGO_PORT,
        username=Config.MONGO_USER or None,
        password=Config.MONGO_PASS or None,
    )
    try:
        db = client[Config.MONGO_DB_NAME]
        collection = db[MONGO_COLLECTION]
        query = {"created": {"$lt": cutoff_date}}

        count = collection.count_documents(query)
        logger.info("MongoDB collection '%s.%s': %d document(s) older than %s",
                     Config.MONGO_DB_NAME, MONGO_COLLECTION, count, cutoff_date)

        if not dry_run and count > 0:
            result = collection.delete_many(query)
            logger.info("MongoDB collection '%s.%s': deleted %d document(s).",
                         Config.MONGO_DB_NAME, MONGO_COLLECTION, result.deleted_count)
        return count
    finally:
        client.close()


def _count_postgres_records(conn, table: str, date_column: str, cutoff_date: datetime) -> int:
    query = f"SELECT COUNT(*) FROM {table} WHERE {date_column} < %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (cutoff_date,))
        return cursor.fetchone()[0]


def _delete_postgres_records(conn, table: str, date_column: str, cutoff_date: datetime) -> int:
    query = f"DELETE FROM {table} WHERE {date_column} < %s"
    with conn.cursor() as cursor:
        cursor.execute(query, (cutoff_date,))
        conn.commit()
        return cursor.rowcount
