from flask import Blueprint, request
from flask_cors import CORS
from python.common import splunk
from python.common.helper import middle_logic
from python.common.logging_utils import get_logger
from python.prohibition_web_svc.config import Config
from python.prohibition_web_svc.business.keycloak_logic import get_authorized_keycloak_user
import python.prohibition_web_svc.http_responses as http_responses
from python.prohibition_web_svc.middleware import print_middleware, common_middleware
from python.prohibition_web_svc.models.print_request_payload import PrintRequestPayload

logger = get_logger(__name__)

logger.info('*** print blueprint loaded ***')

bp = Blueprint('print', __name__, url_prefix=Config.URL_PREFIX + '/api/v1')
CORS(bp, resources={Config.URL_PREFIX + "/api/v1/print/*": {"origins": Config.ACCESS_CONTROL_ALLOW_ORIGIN}})

@bp.route('/print', methods=['GET', 'POST'])
def render_document():
    logger.verbose(f"Inside render_document()")
    kwargs = middle_logic(
        get_authorized_keycloak_user() + [
            {"try": common_middleware.log_payload_to_splunk, "fail": [
                {"try": splunk.log_to_splunk, "fail": []},
                {"try": http_responses.server_error_response, "fail": []},
            ]},
            {"try": print_middleware.set_event_type, "fail": []},
            {"try": print_middleware.validate_print_payload, "fail": [
                {"try": common_middleware.record_event_error, "fail": []},
                {"try": http_responses.bad_request_response, "fail": []}
            ]},
            {"try": print_middleware.render_document_with_playwright, "fail": [
                {"try": common_middleware.record_event_error, "fail": []},
                {"try": http_responses.server_error_response, "fail": []}
            ]},
            {"try": splunk.log_to_splunk, "fail": []},
            {"try": print_middleware.return_rendered_response, "fail": []}
        ],
        required_permission='forms-print',
        request=request,
        config=Config
    )
    return kwargs.get('response')

