import logging
from collections import defaultdict

import psycopg2
import requests

from python.common import splunk
from python.irp_rts_notification_job.config import Config

logger = logging.getLogger(__name__)


def run_notification() -> None:
    logger.info("Running IRP RTS notification.")

    try:
        with psycopg2.connect(
            database=Config.DB_NAME_DF,
            user=Config.DB_USER,
            password=Config.DB_PASS,
            host=Config.DB_HOST,
            port=Config.DB_PORT
        ) as conn:
            pending_rts = _fetch_pending_RTS(conn)
            logger.info(f"Found {len(pending_rts)} pending RTS for notification.")
            _process_pending_RTS(conn, pending_rts)

    except Exception as e:
        logger.error(f"An error occurred while running IRP RTS notification: {e}")
        raise

    logger.info("IRP RTS notification completed.")

def _process_pending_RTS(conn, pending_rts) -> dict:
    grouped_pending_rts = defaultdict(list)

    for row in pending_rts or []:
        username = row[1]
        grouped_pending_rts[username].append(row)

    for username, rts_list in grouped_pending_rts.items():
        logger.info(f"Processing {len(rts_list)} pending RTS for user: {username}")
        try:
            _process_pending_rts_for_user(conn, username, rts_list)
        except Exception as e:
            logger.error(f"An error occurred while processing pending RTS for user {username}: {e}", exc_info=True)
            raise

    return dict(grouped_pending_rts)

def _process_pending_rts_for_user(conn, username, rts_list):
    email = _get_user_email_from_keycloak(username)
    if not email:
        logger.warning(f"Skipping notification for user {username} due to missing email.")
        return

    logger.debug(f"Sending notification to {email} for {len(rts_list)} pending RTS.")
    _send_notification_email(email, rts_list)
    _update_rts_status(conn, rts_list)
    _write_notification_report_to_splunk(email, rts_list)

def _send_notification_email(email, rts_list) -> None:
    subject = f"You have {len(rts_list)} pending Immediate Roadside Prohibitions (IRP) to complete"
    args = {
        "subject": subject,
        "email_address": email,
        "officer_name": rts_list[0][2] if rts_list else "Officer",
        "message": {
            "superintendent_email": Config.SUPERINTENDENT_EMAIL,
            "pending_rts_count": len(rts_list),
            "pending_rts": rts_list
        },
        "templates_path": Config.JINJA2_TEMPLATE_PATH,
        "config": Config
    }
    try:
        from python.common.rsi_email import send_irp_pending_rts
        send_irp_pending_rts(**args)
        logger.info(f"Notification email sent to {email} for {len(rts_list)} pending RTS.")
    except Exception as e:
        logger.error(f"An error occurred while sending notification email to {email}: {e}", exc_info=True)
        raise

def _fetch_pending_RTS(conn) -> list:
    query = """select 
                se.submission_event_id, 
                u.username, 
                u.display_name, 
                s.ff_application_id, 
                sfr.form_type, 
                sfr.form_id as form_number,
                e.driver_last_name,
                e.date_of_driving::DATE
                from submission_events se 
                inner join submission_form_refs sfr on sfr.form_ref_id = se.form_ref_id 
                inner join  submission s on s.submission_id = sfr.submission_id
                inner join "user" u on s.created_by = u.user_guid 
                inner join "event" e on s.submission_id = e.submission_id
                where se.destination = 'RTS' and se.status = 'pending'
                order by date_of_driving;"""
    with conn.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()
    
def _update_rts_status(conn, rts_list):
    rts_ids = [str(row[0]) for row in rts_list]
    logger.debug(f"Updating status to 'notified' for RTS IDs: {rts_ids}")
    update_query = f"""update submission_events set status = 'notified', updated_at = now() where submission_event_id in ({','.join(rts_ids)})"""
    with conn.cursor() as cursor:
        cursor.execute(update_query)
        conn.commit()

def _get_user_email_from_keycloak(username) -> str:
    base_url = Config.KEYCLOAK_AUTH_URL.rstrip('/')
    token_url = f"{base_url}/realms/{Config.KEYCLOAK_REALM}/protocol/openid-connect/token"

    token_response = requests.post(token_url, data={
        'grant_type': 'client_credentials',
        'client_id': Config.KEYCLOAK_CLIENT_ID,
        'client_secret': Config.KEYCLOAK_CLIENT_SECRET,
    })
    token_response.raise_for_status()
    access_token = token_response.json().get('access_token')

    users_url = f"{base_url}/admin/realms/{Config.KEYCLOAK_REALM}/users"
    users_response = requests.get(
        users_url,
        headers={'Authorization': f"Bearer {access_token}"},
        params={'username': username, 'exact': True},
    )
    users_response.raise_for_status()

    users = users_response.json()
    if not users:
        logger.warning(f"No Keycloak user found for username: {username}")
        return None

    return users[0].get('email')

def _write_notification_report_to_splunk(email, rts_list) -> None:
    logger.debug(f"Write notification report for user {email}: {len(rts_list)} pending RTS processed.")
    rts_ids = [str(row[0]) for row in rts_list]
    args = {}
    args["splunk_data"] = {
        "event": "irp_rts_notification_report",
        "email": email,
        "pending_rts_count": len(rts_list),
        "pending_rts_ids": rts_ids
    }
    args["config"] = Config
    try:
        splunk.log_to_splunk(**args)
    except Exception as e:
        logger.error(f"An error occurred while sending notification report to Splunk for user {email}: {e}")