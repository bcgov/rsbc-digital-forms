import os
from keycloak import KeycloakOpenID
from python.common.config import Config
import requests
import json
import logging
import logging.config

logging.config.dictConfig(Config.LOGGING)


def send_email(to: list, subject: str, config, template, eventid, attachments=None) -> bool:
    """
    Send email to the rsiops
    """
    bcc_value=config.BCC_EMAIL_ADDRESSES.split(',')
    if len(bcc_value) > 0 and bcc_value[0] != '':
        payload = {
            "bodyType": "html",
            "body": template,
            "from": config.REPLY_EMAIL_ADDRESS,
            "bcc": config.BCC_EMAIL_ADDRESSES.split(','),
            "encoding": "utf-8",
            "subject": subject,
            "to": to
        }
    else:
        payload = {
            "bodyType": "html",
            "body": template,
            "from": config.REPLY_EMAIL_ADDRESS,
            "encoding": "utf-8",
            "subject": subject,
            "to": to
        }
    if attachments is not None:
        payload['attachments'] = attachments
    logging.info('Sending email to: {} - {}'.format(to, subject))
    return _send(payload, config, eventid)





def _send(payload, config, eventid='') -> bool:
    token = get_common_services_access_token(config)
    auth_header = {"Authorization": "Bearer {}".format(token)}
    try:
        url = Config.COMM_SERV_API_ROOT_URL + '/api/v1/email'
        logging.debug(f'Email service URL: {url}')
        logging.debug(f'Email auth header: {auth_header}')
        logging.verbose(f'Email payload: {payload}')
        response = requests.post(url, headers=auth_header, json=payload)
    except AssertionError as error:
        logging.critical('No response from BC Common Services')
        logging.critical(json.dumps(error))
        return False
    if response.status_code == 201:
        data = response.json()
        _log_sent_email_response(eventid, payload, data)
        return True
    logging.error('response from common services not successful: {}'.format(response.text))
    return False


def get_common_services_access_token(config):
    os.environ['SSL_CERT_FILE'] = ''
    # Configure Keycloak client
    keycloak_openid = KeycloakOpenID(server_url=config.COMM_SERV_AUTH_URL,
                                     client_id=config.COMM_SERV_CLIENT_ID,
                                     realm_name=config.COMM_SERV_REALM,
                                     client_secret_key=config.COMM_SERV_CLIENT_SECRET,
                                     verify=False)
    # Get Token
    token = keycloak_openid.token('', '', 'client_credentials')

    os.environ['SSL_CERT_FILE'] = config.MINIO_CERT_FILE
    return token['access_token']


def _log_sent_email_response(eventid, payload, response) -> None:
    logging.debug('response from common services successful')
    logging.info(json.dumps(dict({
        "email": "success",
        "eventid": eventid,
        "to": payload.get('to'),
        "bcc": payload.get('bcc'),
        "subject": payload.get('subject'),
        "response": response
    })))
    return
