import json
import logging
import time

import psycopg2
from bson import ObjectId
from pymongo import MongoClient
import requests

from python.common import splunk
from python.stuck_submissions_monitor_job.config import Config

logger = logging.getLogger(__name__)

_access_token: str | None = None
_access_token_expires_at = 0.0


def run_stuck_submissions_monitor() -> None:
    logger.info("Running stuck submissions monitor.")

    try:
        with psycopg2.connect(
            database=Config.DB_NAME_FF_API,
            user=Config.DB_USER,
            password=Config.DB_PASS,
            host=Config.DB_HOST,
            port=Config.DB_PORT
        ) as conn:
            stuck_submissions = _fetch_stuck_submissions(conn)
            logger.info(f"Found {len(stuck_submissions)} stuck submissions.")

        result = _process_stuck_submissions(stuck_submissions)

    except Exception as e:
        logger.error(f"An error occurred while running stuck submissions monitor: {e}", exc_info=True, stack_info=True)
        raise

    if result and (result["failure"] > 0 or result["not_found"] > 0):
        raise Exception(f"There were {result['failure']} failed retry submissions and {result['not_found']} submissions not found in MongoDB.")

    logger.info("Stuck submissions monitor completed.")


def _fetch_stuck_submissions(conn) -> list:
    with conn.cursor() as cursor:
        cursor.execute( \
            "select a.id as application_id, d.id as draft_id, a.submission_id, a.latest_form_id as form_id " \
            "from application a " \
            "inner join draft d on a.id = d.application_id " \
            "where a.application_status = 'New' and a.process_instance_id is null and a.created < NOW() - INTERVAL '10 minutes';")

        stuck_submissions = cursor.fetchall()
        return stuck_submissions


def _process_stuck_submissions(stuck_submissions) -> dict:
    retry_status_count = {
        "success": 0,
        "failure": 0,
        "not_found": 0,
    }
    for submission in stuck_submissions:
        application_id = submission[0]
        draft_id = submission[1]
        submission_id = submission[2]
        form_id = submission[3]
        logger.debug(f"Stuck submission detected: application_id={application_id}, draft_id={draft_id}, submission_id={submission_id}, form_id={form_id}")

        submission_document = _fetch_submission_from_mongo(submission_id)
        if not submission_document:
            logger.error(f"Submission document not found in MongoDB for submissionId={submission_id}")
            retry_status_count["not_found"] += 1
            continue
        
        retry_payload = _create_retry_submission_payload(form_id, submission_id, submission_document)
        logger.debug(f"Created retry submission payload for submissionId={submission_id}")
        success = _send_retry_submission(application_id, retry_payload)
        if success:
            retry_status_count["success"] += 1
        else:
            retry_status_count["failure"] += 1

    logger.info(f"Retry submission summary: {retry_status_count}")

    _send_summary_to_splunk(retry_status_count)
    return retry_status_count


def _send_retry_submission(application_id, retry_payload) -> bool:
    try:
        url = Config.RETRY_SUBMISSION_URL.rstrip('/')
        url = f"{url}/application/{application_id}/retry"
        logger.debug(f"Sending retry submission to URL: {url}")

        access_token = _get_access_token()
        headers = {"Content-Type": "application/json"}
        if access_token:
            headers["Authorization"] = f"Bearer {access_token}"
        payload = json.dumps(retry_payload, default=str)
        response = requests.put(url, data=payload, headers=headers)
        response.raise_for_status()
        logger.info(f"Successfully sent retry submission for submissionId={retry_payload['submissionId']}")
        return True
    except Exception as e:
        logger.error(f"Failed to send retry submission for submissionId={retry_payload['submissionId']}: {e}")
        return False


def _fetch_submission_from_mongo(submission_id) -> dict | None:
    with MongoClient(
        host=Config.MONGO_HOST,
        port=Config.MONGO_PORT,
        username=Config.MONGO_USER or None,
        password=Config.MONGO_PASS or None,
    ) as client:
        db = client[Config.MONGO_DB_NAME]
        submissions_collection = db["submissions"]
        return submissions_collection.find_one({"_id": ObjectId(submission_id)})


def _create_retry_submission_payload(form_id, submission_id, submission_document) -> dict:
    return {
        "formId": form_id,
        "submissionId": submission_id,
        "formUrl": f"{Config.FORMIO_BASE_URL}/form/{form_id}/submission/{submission_id}",
        "webFormUrl": f"{Config.WEB_FORM_BASE_URL}/form/{form_id}/submission/{submission_id}",
        "data": submission_document.get("data") if submission_document else {}
    }


def _send_summary_to_splunk(retry_status_count) -> None:
    args = {}
    args["splunk_data"] = {
        "event": "stuck_submissions_retry_summary",
        "retry_status_count": retry_status_count
    }
    args["config"] = Config
    try:
        splunk.log_to_splunk(**args)
    except Exception as e:
        logger.error("Failed to write retry summary to Splunk: %s", e)


def _get_access_token() -> str | None:
    global _access_token, _access_token_expires_at

    if _access_token and time.monotonic() < _access_token_expires_at:
        return _access_token

    base_url = Config.KEYCLOAK_AUTH_URL.rstrip('/')
    token_url = f"{base_url}/realms/{Config.KEYCLOAK_REALM}/protocol/openid-connect/token"

    token_response = requests.post(token_url, data={
        'grant_type': 'client_credentials',
        'client_id': Config.KEYCLOAK_CLIENT_ID,
        'client_secret': Config.KEYCLOAK_CLIENT_SECRET,
    })
    token_response.raise_for_status()
    token_data = token_response.json()
    _access_token = token_data.get('access_token')
    expires_in = token_data.get('expires_in', 0)
    _access_token_expires_at = time.monotonic() + expires_in if _access_token else 0.0
    return _access_token