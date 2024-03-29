import requests
from requests.auth import HTTPBasicAuth
from python.form_handler.config import Config
import time
import uuid
import json

def create_vips_doc(payload,logging) -> tuple:
    correlation_id = str(uuid.uuid4())
    # url=f'{Config.VIPS_ROOT}/digitalforms-viirp/v1/documents/CreateDocument'
    url=f'{Config.VIPS_ROOT}/digitalforms-viirp/v1/documents/{correlation_id}'
    try:
        # print("_Creating VIPS doc_")        
        # print(payload)        
        logging.info("_Creating VIPS doc_")
        vips_doc_response = requests.post(url, json=payload, timeout=60, auth=HTTPBasicAuth(Config.VIPS_API_USERNAME, Config.VIPS_API_PASSWORD))
        logging.info(vips_doc_response.text)
        logging.info(vips_doc_response.status_code)
        # print(vips_doc_response.text)
        # print(vips_doc_response.status_code)
        if(vips_doc_response.status_code!=200):
            return False, vips_doc_response.text, vips_doc_response.status_code
    except Exception as e:
        # print(e)
        logging.error(e)
        return False, None, None
    return True, vips_doc_response.text, vips_doc_response.status_code


def create_vips_imp(payload,logging) -> tuple:
    correlation_id = str(uuid.uuid4())
    # url=f'{Config.VIPS_ROOT}/digitalforms-viirp/v1/impoundments/CreateImpoundment'
    # url=f'{Config.VIPS_ROOT}/digitalforms-viirp/v1/prohibitions/CreateProhibition'
    url=f'{Config.VIPS_ROOT}/digitalforms-viirp/v1/impoundments/{correlation_id}'
    try:
        logging.info("_Creating VIPS impoundment_")
        # print("_Creating VIPS impoundment_")        
        # print(payload)        
        vips_doc_response = requests.post(url, json=payload, timeout=60, auth=HTTPBasicAuth(Config.VIPS_API_USERNAME, Config.VIPS_API_PASSWORD))
        logging.info(vips_doc_response.text)
        logging.info(vips_doc_response.status_code)
        # print(vips_doc_response.text)
        # print(vips_doc_response.status_code)
        if(vips_doc_response.status_code!=200):
            return False, vips_doc_response.text, vips_doc_response.status_code
    except Exception as e:
        # print(e)
        logging.error(e)
        return False, None, None
    return True, vips_doc_response.text, vips_doc_response.status_code