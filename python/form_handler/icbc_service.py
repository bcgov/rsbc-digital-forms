import requests
from requests.auth import HTTPBasicAuth
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
            Config.ICBC_OAUTH_CONTRAVENTION_CLIENT_ID,
            Config.ICBC_OAUTH_CONTRAVENTION_CLIENT_SECRET
        )
        _contravention_token_cache["access_token"] = token_response["access_token"]
        _contravention_token_cache["expires_at"] = time.time() + token_response.get("expires_in", 3600)
        
        return _contravention_token_cache["access_token"]

def get_oauth_token(client_id, client_secret) -> str:     
    # Fetch new token
    token_data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }
        
    if Config.ICBC_OAUTH_SCOPE:
        token_data["scope"] = Config.ICBC_OAUTH_SCOPE
    
    response = requests.post(
        Config.ICBC_OAUTH_TOKEN_URL,
        data=token_data,
        timeout=30
    )
    response.raise_for_status()
    
    token_response = response.json()
    token = {}
    token["access_token"] = token_response["access_token"]
    token["expires_at"] = time.time() + token_response.get("expires_in", 3600)
    
    return token

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
