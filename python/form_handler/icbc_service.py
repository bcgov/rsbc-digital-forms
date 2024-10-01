import requests
from requests.auth import HTTPBasicAuth
from python.form_handler.config import Config

def submit_to_icbc(payload,logging) -> tuple:
    url=f'{Config.ICBC_API_SUBMIT_ROOT}/dfft/v1/contravention'
   
    logging.info("_Sending to ICBC_")
    icbc_response = requests.post(url, json=payload, timeout=60, auth=HTTPBasicAuth(Config.ICBC_API_SUBMIT_USERNAME, Config.ICBC_API_SUBMIT_PASSWORD))
    
    logging.info(icbc_response.text)
    logging.info(icbc_response.status_code)

    if(icbc_response.status_code!=200):
        return False, icbc_response.text, icbc_response.status_code

    return True, icbc_response.text, icbc_response.status_code
