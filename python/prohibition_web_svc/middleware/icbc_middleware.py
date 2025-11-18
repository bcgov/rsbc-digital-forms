import requests
from flask import make_response
import base64
from python.common.logging_utils import get_logger
from python.prohibition_web_svc.config import Config

logger = get_logger(__name__)

def get_icbc_api_authorization_header(**kwargs) -> tuple:
    username = kwargs.get('username')
    try:
        encoded_bytes = base64.b64encode("{}:{}".format(Config.ICBC_API_USERNAME, Config.ICBC_API_PASSWORD).encode('utf-8'))
        kwargs['icbc_header'] = {
            "Authorization": 'Basic {}'.format(str(encoded_bytes, "utf-8")),
            "loginUserId": username
        }
    except Exception as e:
        logger.error(f"error creating ICBC authorization header {e}")
        return False, kwargs
    return True, kwargs


def get_icbc_driver(**kwargs) -> tuple:
    url = "{}/drivers/{}".format(Config.ICBC_API_ROOT, kwargs.get('dl_number'))
    try:
        logger.debug("ICBC url:" + url)
        logger.debug("ICBC header:" + str(kwargs.get('icbc_header')))
        icbc_response = requests.get(url, headers=kwargs.get('icbc_header'))
        logger.debug(f'ICBC response status code: {icbc_response.status_code}')
        logger.verbose(icbc_response.json())
        if icbc_response.status_code == 400:
            kwargs['response'] = make_response({}, 200)
        else:
            kwargs['response'] = make_response(icbc_response.json(), icbc_response.status_code)
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs


def get_icbc_vehicle(**kwargs) -> tuple:
    url = "{}/vehicles".format(Config.ICBC_API_ROOT)
    url_parameters = {
        "plateNumber": kwargs.get('plate_number'),
        # TODO - removed effectiveDate for debugging purposes
        # "effectiveDate": datetime.now().astimezone().replace(microsecond=0).isoformat()
    }
    try:
        logger.debug("ICBC url:" + url)
        logger.debug("ICBC header:" + str(kwargs.get('icbc_header')))
        logger.debug("ICBC url parameters:" + str(url_parameters))
        icbc_response = requests.get(url, headers=kwargs.get('icbc_header'), params=url_parameters)
        logger.debug(f'ICBC response status code: {icbc_response.status_code}')
        logger.verbose(icbc_response.json())
        kwargs['response'] = make_response(icbc_response.json(), icbc_response.status_code)
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs


def splunk_get_driver(**kwargs) -> tuple:
    kwargs['splunk_data'] = {
        "event": "icbc_get_driver",
        "username": kwargs.get('username'),
        "user_guid": kwargs.get('user_guid'),
        "request_id": kwargs.get('request_id', ''),
        "queried_bcdl": kwargs.get("dl_number")
    }
    return True, kwargs


def splunk_get_vehicle(**kwargs) -> tuple:
    kwargs['splunk_data'] = {
        "event": "icbc_get_vehicle",
        "username": kwargs.get('username'),
        "user_guid": kwargs.get('user_guid'),
        "request_id": kwargs.get('request_id', ''),
        "queried_plate": kwargs.get('plate_number')
    }
    return True, kwargs
