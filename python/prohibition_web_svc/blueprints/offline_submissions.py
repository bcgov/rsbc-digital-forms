from python.common.logging_utils import get_logger
from python.prohibition_web_svc.config import Config
from python.common.helper import middle_logic
from flask import request, Blueprint
from flask_cors import CORS
from python.prohibition_web_svc.business.keycloak_logic import get_authorized_keycloak_user
from python.prohibition_web_svc.middleware import common_middleware
import python.prohibition_web_svc.middleware.submission_middleware as submission_middleware
import python.prohibition_web_svc.middleware.offline_submission_middleware as offline_submission_middleware
import python.prohibition_web_svc.http_responses as http_responses


logger = get_logger(__name__)
logger.info('*** offline submissions blueprint loaded ***')

bp = Blueprint('offline_submission', __name__, url_prefix=Config.URL_PREFIX + '/api/v1')
CORS(bp, resources={Config.URL_PREFIX + "/api/v1/offline_submission/*": {"origins": Config.ACCESS_CONTROL_ALLOW_ORIGIN}})


@bp.route('/offline_submission', methods=['POST'])
def create_offline_submission():
    """
    Create a new offline submission.
    Payload must contain local_submission_id, payload, and status.
    """
    if request.method == 'POST':
        logger.verbose("POST /offline_submission endpoint called")
        kwargs = middle_logic(
            get_authorized_keycloak_user() + [
                {"try": submission_middleware.request_contains_a_payload, "fail": [
                    {"try": http_responses.bad_request_response, "fail": []},
                ]},
                {"try": offline_submission_middleware.set_local_submission_id, "fail": [
                    {"try": http_responses.bad_request_response, "fail": []},
                ]},
                {"try": offline_submission_middleware.check_if_offline_submission_exists, "fail": [
                    {"try": http_responses.offline_submission_already_exists, "fail": []},
                ]},
                {"try": offline_submission_middleware.create_offline_submission, "fail": [
                    {"try": common_middleware.record_event_error, "fail": []},
                    {"try": http_responses.server_error_response, "fail": []},
                ]},
                {"try": http_responses.successful_create_response, "fail": []},
            ],
            required_permission='create_submissions',
            request=request,
            config=Config)
        logger.verbose(f"POST /offline_submission endpoint response code: {kwargs.get('response').status_code}")
        return kwargs.get('response')
