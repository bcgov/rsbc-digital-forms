from datetime import datetime
import logging

import psycopg2
from pymongo import MongoClient

from python.common import splunk
from python.data_cleanup_job.config import Config

logger = logging.getLogger(__name__)

POSTGRES_DF_TARGETS = [
    {"table": "df_errors", "date_column": "received_dt"},
]

POSTGRES_FF_TARGETS = [
    {"table": "draft", "date_column": "created", "parent_table": "application", "parent_join_column": "application_id"},
    {"table": "application_audit", "date_column": "created", "parent_table": "application", "parent_join_column": "application_id"},
    {"table": "application_data", "date_column": "created", "parent_table": "application", "parent_join_column": "application_id"},
    {"table": "application", "date_column": "created"},
]

MONGO_COLLECTION = "submissions"

MONGO_LIMIT_BATCH_SIZE = 200

def run_cleanup(cutoff_date: datetime, dry_run: bool) -> None:
    mode_label = "DRY RUN" if dry_run else "LIVE"
    logger.info("Running data cleanup in %s mode. Cutoff date: %s", mode_label, cutoff_date)

    results_df = cleanup_postgres_DF(cutoff_date, dry_run)
    results_ff = cleanup_postgres_FF(cutoff_date, dry_run)
    results_mongo = cleanup_mongo(cutoff_date, dry_run)

    # Combine all results
    all_results = {
        "postgres_df": results_df,
        "postgres_ff": results_ff,
        "mongo": results_mongo
    }

    _write_cleanup_report_to_splunk(cutoff_date, dry_run, all_results)

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
            count = _count_postgres_records(conn, target, cutoff_date)
            results[table] = count
            logger.info("Postgres table '%s': %d record(s) older than %s", table, count, cutoff_date)

            if not dry_run and count > 0:
                deleted = _delete_postgres_records(conn, target, cutoff_date)
                logger.info("Postgres table '%s': deleted %d record(s).", table, deleted)

    return results


def cleanup_postgres_FF(cutoff_date: datetime, dry_run: bool) -> dict:
    logger.info("Connecting to Postgres database: %s@%s:%s/%s",
                Config.DB_USER, Config.DB_HOST, Config.DB_PORT, Config.DB_NAME_FF)

    results = {}
    with psycopg2.connect(
        database=Config.DB_NAME_FF,
        user=Config.DB_USER,
        password=Config.DB_PASS,
        host=Config.DB_HOST,
        port=Config.DB_PORT
    ) as conn:
        for target in POSTGRES_FF_TARGETS:
            _execute_db_cleanup(cutoff_date, dry_run, results, conn, target)

    return results

def _execute_db_cleanup(cutoff_date, dry_run, results, conn, target):
    table = target["table"]
    count = _count_postgres_records(conn, target, cutoff_date)
    results[table] = count
    logger.info("Postgres table '%s': %d record(s) older than %s", table, count, cutoff_date)

    if not dry_run and count > 0:
        deleted = _delete_postgres_records(conn, target, cutoff_date)
        logger.info("Postgres table '%s': deleted %d record(s).", table, deleted)


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
        query = {"$and":[{"created": {"$lt": cutoff_date}}, {"metadata":{"$exists":"true"}},{"metadata":{"$ne":None}},{"metadata":{"$ne":{}}}]}

        count = collection.count_documents(query)
        logger.info("MongoDB collection '%s.%s': %d document(s) older than %s",
                     Config.MONGO_DB_NAME, MONGO_COLLECTION, count, cutoff_date)

        if not dry_run and count > 0:
            if count > MONGO_LIMIT_BATCH_SIZE:
                logger.warning("MongoDB collection '%s.%s': large number of documents to delete (%d). Deleting in batches.",
                               Config.MONGO_DB_NAME, MONGO_COLLECTION, count)
                results = collection.find(query).limit(MONGO_LIMIT_BATCH_SIZE)
                ids_to_delete = [doc["_id"] for doc in results]
                query = {"_id": {"$in": ids_to_delete}}

            result = collection.delete_many(query)
            logger.info("MongoDB collection '%s.%s': deleted %d document(s).",
                         Config.MONGO_DB_NAME, MONGO_COLLECTION, result.deleted_count)
            count = result.deleted_count
        return count
    finally:
        client.close()


def _count_postgres_records(conn, target: dict, cutoff_date: datetime) -> int:
    if ("parent_table" in target) and ("parent_join_column" in target):
        query = f"""
            SELECT COUNT(*)
            FROM {target["table"]} t
            JOIN {target["parent_table"]} p ON t.{target["parent_join_column"]} = p.id
            WHERE p.{target["date_column"]} < %s
        """
    else:
        query = f"SELECT COUNT(*) FROM {target["table"]} WHERE {target["date_column"]} < %s"

    logger.debug("Executing count query for table '%s': %s", target["table"], query.replace("%s", str(cutoff_date)))    
    with conn.cursor() as cursor:
        cursor.execute(query, (cutoff_date,))
        return cursor.fetchone()[0]


def _delete_postgres_records(conn, target: dict, cutoff_date: datetime) -> int:
    if ("parent_table" in target) and ("parent_join_column" in target):
        query = f"""
            DELETE FROM {target["table"]} t
            WHERE t.{target["parent_join_column"]} in (
             SELECT id FROM {target["parent_table"]} p 
             WHERE p.{target["date_column"]} < %s
            )
        """
    else:
        query = f"DELETE FROM {target["table"]} WHERE {target["date_column"]} < %s"

    logger.debug("Executing delete query for table '%s': %s", target["table"], query.replace("%s", str(cutoff_date)))
    with conn.cursor() as cursor:
        cursor.execute(query, (cutoff_date,))
        conn.commit()
        return cursor.rowcount

def _write_cleanup_report_to_splunk(cutoff_date, dry_run, results: dict) -> None:
    # Placeholder for writing results to Splunk
    logger.info("Cleanup report: %s", results)
    args = {}
    args["splunk_data"] = {
        "event": "data_cleanup_report",
        "cutoff_date": cutoff_date.isoformat(),
        "dry_run": dry_run,
        "results": results
    }
    args["config"] = Config
    try:
        splunk.log_to_splunk(**args)
    except Exception as e:
        logger.error("Failed to write cleanup report to Splunk: %s", e)