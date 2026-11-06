
import logging
import requests
import json

from python.common.enums import ErrorCode
from python.common.models import FormsflowOfflineSubmission

def send_to_formio(**args):
    logging.verbose("Sending to Formio")
    application = args.get('app')
    db = args.get('db')
    config = args.get('config')
    message = args.get('message')
    submission_data = args.get('submission_data')
    form_id = submission_data.get('form_id')
    submission_id = args.get('offline_submission_id')
    formio_token_url = f"{config.FORMIO_API_URL}/user/login"
    formio_url = f"{config.FORMIO_API_URL}/form/{form_id}/submission"
    formio_token_header = config.FORMIO_TOKEN_HEADER

    args['formio_submission_id'] = submission_data.get('submission_id')

    if not args['formio_submission_id']:
        try:
            formio_token = requests.post(
                formio_token_url,
                json={
                    'data': {
                        'email': config.FORMIO_ROOT_EMAIL,
                        'password': config.FORMIO_ROOT_PASSWORD
                    }
                }
            ).headers.get(formio_token_header)

            headers = {
                formio_token_header: formio_token
            }
            payload = {
                **submission_data.get('payload', {}).get('data', {}),
                'submitted_offline': True
            }
            response = requests.post(
                formio_url,
                json={
                    'data': {
                        **payload
                    },
                    'metadata': submission_data.get('payload', {}).get('metadata'),
                    'state': submission_data.get('payload', {}).get('state'),
                    '_vnote': submission_data.get('payload', {}).get('_vnote')
                },
                headers=headers
            )

            if response.status_code != 201:
                logging.error(f"Failed to create Formio submission: {response.text}")
            response.raise_for_status()
            new_submission = response.json()
            args['formio_submission_id'] = new_submission.get('_id')

            with application.app_context():
                offline_submission = db.session.query(FormsflowOfflineSubmission).filter_by(id=submission_id).first()
                offline_submission.status = 'sent_to_formio'
                offline_submission.submission_id = new_submission.get('_id')
                db.session.commit()

        except Exception as e:
            logging.exception(e)
            args['error'] = {
                'error_code': ErrorCode.O07,
                'error_details': str(e),
                'event_id': None,
                'event_type': 'offline_submission',
                'submission_id': submission_id,
                'payload': json.dumps(message) if message else None,
                'func': send_to_formio,
            }
            return False, args
    else:
        logging.debug('Skipping send to Formio as formio_submission_id is already set')

    return True, args