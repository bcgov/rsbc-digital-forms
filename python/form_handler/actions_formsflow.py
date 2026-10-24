import logging
from flask import json
import requests

from python.common.enums import ErrorCode
from python.common.models import FormsflowOfflineSubmission


def send_to_formsflow(**args):
    application = args.get('app')
    db = args.get('db')
    config = args.get('config')
    message = args.get('message')
    submission_data = args.get('submission_data')
    payload_data = submission_data.get('payload', {}).get('data', {}) 

    form_id = submission_data.get('form_id')
    application_id = submission_data.get('application_id')
    offline_submission_id = args.get('offline_submission_id')
    formio_submission_id = args['formio_submission_id']
    draft_id = submission_data.get('payload', {}).get('serverDraftId')
    username = submission_data.get('username')

    formio_submission_url = f"{config.FORMIO_API_URL}/form/{form_id}/submission/{formio_submission_id}"
    web_form_url = f"{config.WEB_APP_URL}/form/{form_id}/submission/{offline_submission_id}"

    logging.verbose(f"Sending to Formsflow submission {formio_submission_id}")

    payload = {
        "formId": form_id,
        "submissionId": formio_submission_id,
        "formUrl": formio_submission_url,
        "webFormUrl": web_form_url,
        "data": payload_data,
        "createdBy": username
    }

    try:
        keycloak_token = _get_keycloak_token(config)

        if not draft_id:
            if not application_id:
                logging.debug(f"No existing application ID, creating new application")
                formsflow_create_application_url = f"{config.FORMSFLOW_API_URL}/application/create"
                logging.debug(f"Creating Formsflow application at URL: {formsflow_create_application_url}")
                logging.verbose(f"Payload for creating Formsflow application: {payload}")
                response = requests.post(formsflow_create_application_url, json=payload, headers={'Authorization': f'Bearer {keycloak_token}'})
                if response.status_code != 201:
                    logging.error(f"Failed to create application: {response.text}")
                response.raise_for_status()
                logging.verbose(f"Application created successfully: {response.json()}")

                application_id = response.json().get('id')
                with application.app_context():
                    offline_submission = db.session.query(FormsflowOfflineSubmission).filter_by(id=offline_submission_id).first()
                    offline_submission.status = 'sent_to_formsflow'
                    offline_submission.application_id = application_id
                    db.session.commit()
            else:
                logging.debug(f"Skipping Formsflow creation, existing application ID: {application_id}")
        else:
            logging.debug(f"Skipping Formsflow creation, draft ID exists: {draft_id}")
            formsflow_submit_draft_url = f"{config.FORMSFLOW_API_URL}/draft/{draft_id}/submit"
            logging.debug(f"Submitting Formsflow draft at URL: {formsflow_submit_draft_url}")
            logging.verbose(f"Payload for submitting Formsflow draft: {payload}")
            response = requests.put(formsflow_submit_draft_url, json=payload, headers={'Authorization': f'Bearer {keycloak_token}'})
            if response.status_code != 200:
                logging.error(f"Failed to submit draft: {response.text}")
            response.raise_for_status()
            logging.verbose(f"Draft submitted successfully: {response.json()}")

    except Exception as e:
        logging.exception(e)
        args['error'] = {
            'error_code': ErrorCode.O08,
            'error_details': str(e),
            'event_id': None,
            'event_type': 'offline_submission',
            'submission_id': offline_submission_id,
            'payload': json.dumps(message) if message else None,
            'func': send_to_formsflow,
        }
        return False, args

    return True, args


def _get_keycloak_token(config):
    token_url = f"{config.KEYCLOAK_URL}/auth/realms/{config.KEYCLOAK_REALM}/protocol/openid-connect/token"
    payload = {
        'grant_type': 'client_credentials',
        'client_id': config.KEYCLOAK_CLIENT_ID,
        'client_secret': config.KEYCLOAK_CLIENT_SECRET
    }
    logging.debug(f"Requesting Keycloak token from URL: {token_url}")
    response = requests.post(token_url, data=payload)
    logging.verbose(f"Keycloak token response: {response.text}")
    response.raise_for_status()
    access_token = response.json().get('access_token')
    logging.verbose(f"Obtained access token: {access_token}")
    if not access_token:
        raise Exception("Failed to obtain access token from Keycloak")

    return access_token