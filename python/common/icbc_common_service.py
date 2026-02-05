import requests
import time

from python.common.config import Config


def get_oauth_token(token_url, 
                    client_id, 
                    client_secret,
                    scope=None) -> str:     
    # Fetch new token
    token_data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }
        
    if scope:
        token_data["scope"] = scope
    
    response = requests.post(
        token_url,
        data=token_data,
        timeout=30
    )
    response.raise_for_status()
    
    token_response = response.json()
    token = {}
    token["access_token"] = token_response["access_token"]
    token["expires_at"] = time.time() + token_response.get("expires_in", 3600)
    
    return token
