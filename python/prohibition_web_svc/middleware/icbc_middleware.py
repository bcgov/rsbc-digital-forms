import requests
from flask import make_response
from python.common.logging_utils import get_logger
from python.common.icbc_common_service import get_oauth_token
from python.prohibition_web_svc.config import Config
import time
from threading import Lock

logger = get_logger(__name__)

# Token cache with thread safety
_drivers_token_cache = {
    "access_token": None,
    "expires_at": 0
}
_vehicles_token_cache = {
    "access_token": None,
    "expires_at": 0
}
_token_lock = Lock()

def _get_drivers_oauth_token() -> str:
    """Fetch or return cached OAuth2 token."""
    global _drivers_token_cache
    
    with _token_lock:
        # Return cached token if still valid (with 60s buffer)
        if _drivers_token_cache["access_token"] and time.time() < _drivers_token_cache["expires_at"] - 60:
            return _drivers_token_cache["access_token"]
        
        # Fetch new token
        token_response = get_oauth_token(
            Config.ICBC_OAUTH_TOKEN_URL,
            Config.ICBC_OAUTH_DRIVERS_CLIENT_ID,
            Config.ICBC_OAUTH_DRIVERS_CLIENT_SECRET,
            Config.ICBC_OAUTH_SCOPE 
        )
        _drivers_token_cache["access_token"] = token_response["access_token"]
        _drivers_token_cache["expires_at"] = time.time() + token_response.get("expires_in", 3600)
        
        return _drivers_token_cache["access_token"]
    
def _get_vehicles_oauth_token() -> str:
    """Fetch or return cached OAuth2 token."""
    global _vehicles_token_cache
    
    with _token_lock:
        # Return cached token if still valid (with 60s buffer)
        if _vehicles_token_cache["access_token"] and time.time() < _vehicles_token_cache["expires_at"] - 60:
            return _vehicles_token_cache["access_token"]
        
        # Fetch new token
        token_response = get_oauth_token(
            Config.ICBC_OAUTH_TOKEN_URL,
            Config.ICBC_OAUTH_VEHICLES_CLIENT_ID,
            Config.ICBC_OAUTH_VEHICLES_CLIENT_SECRET,
            Config.ICBC_OAUTH_SCOPE
        )
        _vehicles_token_cache["access_token"] = token_response["access_token"]
        _vehicles_token_cache["expires_at"] = time.time() + token_response.get("expires_in", 3600)
        
        return _vehicles_token_cache["access_token"]    


def get_icbc_drivers_api_authorization_header(**kwargs) -> tuple:
    """Build OAuth2 authorization header."""
    username = kwargs.get('username')
    try:
        access_token = _get_drivers_oauth_token()
        kwargs['icbc_header'] = {
            "Authorization": f"Bearer {access_token}",
            "loginUserId": username,
            "Accept": "*/*"
        }
    except Exception as e:
        logger.error(f"Error obtaining ICBC OAuth token: {e}")
        return False, kwargs
    return True, kwargs


def get_icbc_vehicles_api_authorization_header(**kwargs) -> tuple:
    """Build OAuth2 authorization header."""
    username = kwargs.get('username')
    try:
        access_token = _get_vehicles_oauth_token()
        kwargs['icbc_header'] = {
            "Authorization": f"Bearer {access_token}",
            "loginUserId": username
        }
    except Exception as e:
        logger.error(f"Error obtaining ICBC OAuth token: {e}")
        return False, kwargs
    return True, kwargs


def get_icbc_driver(**kwargs) -> tuple:
    url = "{}/integration/rsbc-driver-api/v1/drivers/{}".format(Config.ICBC_API_ROOT, kwargs.get('dl_number'))
    try:
        logger.debug("ICBC url:" + url)
        logger.verbose("ICBC header:" + str(kwargs.get('icbc_header')))
        headers = kwargs.get('icbc_header')
        icbc_response = requests.get(url, headers=headers)
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
    url = "{}/integration/vips-vehicle-api/v1/vehicles".format(Config.ICBC_API_ROOT)
    url_parameters = {
        "plateNumber": kwargs.get('plate_number'),
        # TODO - removed effectiveDate for debugging purposes
        # "effectiveDate": datetime.now().astimezone().replace(microsecond=0).isoformat()
    }
    try:
        logger.debug("ICBC url:" + url)
        logger.verbose("ICBC header:" + str(kwargs.get('icbc_header')))
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
