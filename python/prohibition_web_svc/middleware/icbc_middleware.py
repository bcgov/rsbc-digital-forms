import logging
import requests
from datetime import datetime
from flask import make_response
import base64
from python.prohibition_web_svc.config import Config


def get_icbc_api_authorization_header(**kwargs) -> tuple:
    username = kwargs.get('username')
    try:
        encoded_bytes = base64.b64encode("{}:{}".format(Config.ICBC_API_USERNAME, Config.ICBC_API_PASSWORD).encode('utf-8'))
        kwargs['icbc_header'] = {
            "Authorization": 'Basic {}'.format(str(encoded_bytes, "utf-8")),
            "loginUserId": username
        }
    except Exception as e:
        logging.warning("error creating ICBC authorization header")
        return False, kwargs
    return True, kwargs


def get_icbc_driver(**kwargs) -> tuple:
    url = "{}/drivers/{}".format(Config.ICBC_API_ROOT, kwargs.get('dl_number'))
    try:
        logging.debug("icbc url:" + url)
        logging.debug("icbc header:" + str(kwargs.get('icbc_header')))
        icbc_response = requests.get(url, headers=kwargs.get('icbc_header'))
        logging.debug(icbc_response.status_code)
        logging.debug(icbc_response.json())
        logging.debug(icbc_response.reason)
        if icbc_response.status_code == 400:
            kwargs['response'] = make_response({}, 200)
        else:
            kwargs['response'] = make_response(icbc_response.json(), icbc_response.status_code)
    except Exception as e:
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
        icbc_response = requests.get(url, headers=kwargs.get('icbc_header'), params=url_parameters)
        logging.warning("icbc url:" + icbc_response.url)
        logging.debug("---------------------------Made it here---------------------------")
        logging.debug(icbc_response.json())
        logging.debug("------------------------------------------------------------------")
        kwargs['response'] = make_response(icbc_response.json(), icbc_response.status_code)
    except Exception as e:
        return False, kwargs
    return True, kwargs


def splunk_get_driver(**kwargs) -> tuple:
    kwargs['splunk_data'] = {
        "event": "icbc_get_driver",
        "username": kwargs.get('username'),
        "user_guid": kwargs.get('user_guid'),
        "queried_bcdl": kwargs.get("dl_number")
    }
    return True, kwargs


def splunk_get_vehicle(**kwargs) -> tuple:
    kwargs['splunk_data'] = {
        "event": "icbc_get_vehicle",
        "username": kwargs.get('username'),
        "user_guid": kwargs.get('user_guid'),
        "queried_plate": kwargs.get('plate_number')
    }
    return True, kwargs
