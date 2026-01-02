from keycloak import KeycloakOpenID
from python.common import splunk
from python.common.config import Config
import requests
import json
from python.common.logging_utils import get_logger

logger = get_logger(__name__)


def send_email(to: list, subject: str, config, template, ticket_no=None, attachments=None) -> bool:
    """
    Send email to the applicant and bcc Appeals Registry
    """
    env = str(config.ENVIRONMENT).upper()
    subject = f'[{env}] - {subject}' if 'PROD' not in env else subject
    payload = {
        "bodyType": "html",
        "body": template,
        "from": config.REPLY_EMAIL_ADDRESS,
        "bcc": config.BCC_EMAIL_ADDRESSES.split(','),
        "encoding": "utf-8",
        "subject": subject,
        "to": to
    }
    if attachments is not None:
        payload['attachments'] = attachments
    logger.debug('{} - Sending email to: {} - {}'.format(ticket_no, to, subject))
    return _send(payload, config, ticket_no)


def _send(payload, config, ticket_no) -> bool:
    token = get_common_services_access_token(config)
    auth_header = {"Authorization": "Bearer {}".format(token)}
    try:
        response = requests.post(Config.COMM_SERV_API_ROOT_URL + '/api/v1/email', headers=auth_header, json=payload)
    except AssertionError as error:
        logger.error('No response from BC Common Services')
        logger.error(json.dumps(error))
        return False
    if response.status_code == 201:
        data = response.json()
        _log_sent_email_response(ticket_no, payload, data, config)
        return True
    logger.error('response from common services not successful: {}'.format(response.text))
    return False


def get_common_services_access_token(config):
    # Configure Keycloak client
    keycloak_openid = KeycloakOpenID(server_url=config.COMM_SERV_AUTH_URL,
                                     client_id=config.COMM_SERV_CLIENT_ID,
                                     realm_name=config.COMM_SERV_REALM,
                                     client_secret_key=config.COMM_SERV_CLIENT_SECRET)
    # Get Token
    token = keycloak_openid.token('', '', 'client_credentials')
    return token['access_token']


def _log_sent_email_response(ticket_no, payload, response, config) -> None:
    logger.verbose('response from common services successful')
    email_info = json.dumps(dict({
        "event": "email sent success",
        "to": payload.get('to'),
        "bcc": payload.get('bcc'),
        "ticket_no": ticket_no,
        "subject": payload.get('subject'),
        "response": response
    }))
    logger.info(email_info)
    args = {}
    args["splunk_data"] = email_info
    args["config"] = config
    splunk.log_to_splunk(**args)
    return
