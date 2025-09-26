from flask import Blueprint, request
from flask_cors import CORS
import logging.config
from python.common import splunk
from python.common.helper import middle_logic
from python.prohibition_web_svc.config import Config
from python.prohibition_web_svc.business.keycloak_logic import get_authorized_keycloak_user
import python.prohibition_web_svc.http_responses as http_responses
from python.prohibition_web_svc.middleware import print_middleware, notification_middleware, common_middleware

logging.config.dictConfig(Config.LOGGING)
logging.info('*** email blueprint loaded ***')

bp = Blueprint('email', __name__, url_prefix=Config.URL_PREFIX + '/api/v1')
CORS(bp, resources={Config.URL_PREFIX + "/api/v1/email/*": {"origins": Config.ACCESS_CONTROL_ALLOW_ORIGIN}})

@bp.route('/email', methods=['POST'])
def send_entity_copy():
    logging.info(f"Inside send_mail()")
    kwargs = middle_logic(
        get_authorized_keycloak_user() + [
            {"try": common_middleware.log_payload_to_splunk, "fail": [
                {"try": splunk.log_to_splunk, "fail": []},
                {"try": http_responses.server_error_response, "fail": []},
            ]},
            {"try": notification_middleware.validate_email_payload, "fail": [
                {"try": common_middleware.record_event_error, "fail": []},
                {"try": http_responses.bad_request_response, "fail": []}
            ]},
            {"try": notification_middleware.send_email, "fail": [
                {"try": common_middleware.record_event_error, "fail": []},
                {"try": http_responses.server_error_response, "fail": []}
            ]},
            {"try": splunk.log_to_splunk, "fail": []},
            {"try": http_responses.successful_create_response, "fail": []}
        ],
        required_permission='forms-print',
        request=request,
        config=Config
    )
    return kwargs.get('response')

