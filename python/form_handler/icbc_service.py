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

def submit_to_icbc(payload,logging) -> tuple:
    url=f'{Config.ICBC_API_SUBMIT_ROOT}/driverlicensing/dfft/v1/contravention'
    headers = {
        "Authorization": f"Bearer {_get_contravention_oauth_token()}",
        "Accept": "application/json",
        "loginUserId": "DF-Form-Handler"
    }
    logging.debug(f"ICBC URL: {url}")
    logging.verbose(f"ICBC payload: {payload}")
    logging.verbose(f"ICBC headers: {headers}")
    icbc_response = requests.post(url, json=payload, timeout=60, headers=headers)
    
    logging.info(icbc_response.status_code)
    logging.debug(icbc_response.text)

    if(icbc_response.status_code!=200):
        return False, icbc_response.text, icbc_response.status_code

    return True, icbc_response.text, icbc_response.status_code
