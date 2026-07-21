from python.common import splunk
from python.common.logging_utils import get_logger
from python.prohibition_web_svc.config import Config
from python.common.helper import middle_logic
from flask import request, Blueprint
from flask_cors import CORS
from python.prohibition_web_svc.business.keycloak_logic import get_authorized_keycloak_user
import python.prohibition_web_svc.middleware.submission_middleware as submission_middleware
import python.prohibition_web_svc.http_responses as http_responses


logger = get_logger(__name__)
logger.info('*** submissions blueprint loaded ***')

bp = Blueprint('submission', __name__, url_prefix=Config.URL_PREFIX + '/api/v1')
CORS(bp, resources={Config.URL_PREFIX + "/api/v1/submission/*": {"origins": Config.ACCESS_CONTROL_ALLOW_ORIGIN}})


@bp.route('/submission/event/status', methods=['PATCH'])
def update_event_status():
    """
    Update the status of a submission event identified by ff_application_id.
    Payload must contain ff_application_id, destination, and status.
    """
    if request.method == 'PATCH':
        logger.verbose("PATCH /submission/event/status endpoint called")
        kwargs = middle_logic(
            get_authorized_keycloak_user() + [
                {"try": submission_middleware.request_contains_a_payload, "fail": [
                    {"try": http_responses.bad_request_response, "fail": []},
                ]},
                {"try": submission_middleware.validate_update_event_status_payload, "fail": [
                    {"try": http_responses.bad_request_response, "fail": []},
                ]},
                {"try": submission_middleware.log_status_update_payload_to_splunk, "fail": []},
                {"try": splunk.log_to_splunk, "fail": []},                
                {"try": submission_middleware.update_submission_event_status, "fail": [
                    {"try": http_responses.record_not_found, "fail": []},
                ]},
                {"try": submission_middleware.commit_transaction, "fail": [
                    {"try": http_responses.server_error_response, "fail": []},
                ]},
                {"try": http_responses.successful_update_response, "fail": []},
            ],
            required_permission='forms-update',
            request=request,
            config=Config)
        logger.verbose(f"PATCH /submission/event/status endpoint response code: {kwargs.get('response').status_code}")
        return kwargs.get('response')
