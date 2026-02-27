import base64
import requests
from python.common.icbc_common_service import get_oauth_token
from python.form_handler.config import Config
import time
from threading import Lock

_token_lock = Lock()

_contravention_token_cache = {
    "access_token": None,
    "expires_at": 0
}

def _get_contravention_oauth_token() -> str:
    """Fetch or return cached OAuth2 token."""
    global _contravention_token_cache
    
    with _token_lock:
        # Return cached token if still valid (with 60s buffer)
        if _contravention_token_cache["access_token"] and time.time() < _contravention_token_cache["expires_at"] - 60:
            return _contravention_token_cache["access_token"]
        
        # Fetch new token
        token_response = get_oauth_token(
            Config.ICBC_OAUTH_TOKEN_URL,
            Config.ICBC_OAUTH_CONTRAVENTION_CLIENT_ID,
            Config.ICBC_OAUTH_CONTRAVENTION_CLIENT_SECRET,
            Config.ICBC_OAUTH_SCOPE
        )
        _contravention_token_cache["access_token"] = token_response["access_token"]
        _contravention_token_cache["expires_at"] = time.time() + token_response.get("expires_in", 3600)
        
        return _contravention_token_cache["access_token"]

def _get_headers() -> dict:
    if Config.ICBC_USE_OAUTH:
        return {
            "Authorization": f"Bearer {_get_contravention_oauth_token()}",
            "Accept": "application/json",
            "loginUserId": "DF-Form-Handler"
        }
    else:
        auth_header = base64.b64encode("{}:{}".format(Config.ICBC_API_USERNAME, Config.ICBC_API_PASSWORD).encode('utf-8'))
        return {
            "Authorization": 'Basic {}'.format(str(auth_header, "utf-8")),
            "Accept": "application/json",
            "loginUserId": "DF-Form-Handler"
        }

def submit_to_icbc(payload,logging) -> tuple:
    contravention_endpoint = '/driverlicensing/dfft/v1/contravention' if Config.ICBC_USE_OAUTH else '/dfft/v1/contravention'
    url=f'{Config.ICBC_API_SUBMIT_ROOT}{contravention_endpoint}'
    headers = _get_headers()
    logging.debug(f"ICBC URL: {url}")
    logging.verbose(f"ICBC payload: {payload}")
    logging.verbose(f"ICBC headers: {headers}")
    icbc_response = requests.post(url, json=payload, timeout=60, headers=headers)
    
    logging.info(icbc_response.status_code)
    logging.debug(icbc_response.text)

    if(icbc_response.status_code!=200):
        return False, icbc_response.text, icbc_response.status_code

    return True, icbc_response.text, icbc_response.status_code
