import requests
from requests.auth import HTTPBasicAuth
from python.form_handler.config import Config
import time

def submit_to_icbc(payload) -> tuple:
    # print("___ICBC__")
    # url = "{}".format(Config.ICBC_API_ROOT)
    # url=f'{Config.ICBC_API_ROOT}/vips/icbc/dfft/contravention'
    url=f'{Config.ICBC_API_ROOT}/dfft/contravention'
    try:
        # payload = kwargs['message']['icbc_submission']
        # # TODO remove for oc
        # print("___Waiting for VPN")
        # for i in range(0,30):
        #     print(i)
        #     time.sleep(1)
        print("_Sending to ICBC_")        
        print(payload)        
        icbc_response = requests.post(url, json=payload, timeout=5, auth=HTTPBasicAuth(Config.ICBC_API_USERNAME, Config.ICBC_API_PASSWORD))
        ##kwargs['response'] = make_response(icbc_response.text, icbc_response.status_code)        
        print(icbc_response.text)
        print(icbc_response.status_code)
        if(icbc_response.status_code!=200):
            return False, icbc_response.text, icbc_response.status_code
    except Exception as e:
        # print("ERROR__in ICBC call_")
        print(e)
        return False, None, None
    return True, icbc_response.text, icbc_response.status_code
