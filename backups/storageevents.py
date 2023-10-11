from python.prohibition_web_svc.config import Config
from python.common.helper import middle_logic, load_json_into_dict
from python.prohibition_web_svc.business.keycloak_logic import get_authorized_keycloak_user
import python.prohibition_web_svc.http_responses as http_responses
import python.prohibition_web_svc.middleware.splunk_middleware as splunk_middleware
from flask import request, make_response, Blueprint
from python.common.splunk import log_to_splunk
from flask_cors import CORS
import json

import logging.config
from flask import jsonify

logging.config.dictConfig(Config.LOGGING)
logging.info('*** storage blueprint loaded ***')

bp = Blueprint('storageevent', __name__, url_prefix=Config.URL_PREFIX + '/api/v1')
CORS(bp, resources={Config.URL_PREFIX + "/api/v1/storageevent/*": {"origins": Config.ACCESS_CONTROL_ALLOW_ORIGIN}})


@bp.route('/storageevent', methods=['POST'])
def readevent():
    print('bbbb')
    payload = request.get_json()
    logging.info("payload: " + json.dumps(payload))
    # print(request.get_json())
    return make_response({'status': 'done'}, 200)


@bp.route('/testevent', methods=['GET'])
def readtestevent():
    print('aaaa')
    print(request.json)
    return make_response({'status': 'done'}, 200)