from python.common.helper import middle_logic
from python.common.logging_utils import get_logger
from python.prohibition_web_svc.business.keycloak_logic import get_authorized_keycloak_user
from python.prohibition_web_svc.config import Config
from flask import request, Blueprint
from flask_cors import CORS
import python.prohibition_web_svc.http_responses as http_responses
import python.prohibition_web_svc.middleware.detachment_middleware as detachment_middleware
from python.prohibition_web_svc.middleware import common_middleware

logger = get_logger(__name__)
logger.info('*** detachments blueprint loaded ***')

bp = Blueprint('detachments', __name__, url_prefix=Config.URL_PREFIX + '/api/v1')
CORS(bp, resources={Config.URL_PREFIX + "/api/v1/detachment*": {"origins": Config.ACCESS_CONTROL_ALLOW_ORIGIN}})


@bp.route('/detachments', methods=['GET'])
def list_detachments():
    """Return all detachments available for selection."""
    if request.method == 'GET':
        kwargs = middle_logic(
            get_authorized_keycloak_user() + [
                {"try": detachment_middleware.get_all_detachments, "fail": [
                    {"try": http_responses.server_error_response, "fail": []}
                ]},
            ],
            required_permission='forms-get',
            request=request,
            config=Config)
        return kwargs.get('response')


@bp.route('/detachment-change-request', methods=['POST'])
def create_detachment_change_request():
    """
    Change an officer's working detachment immediately.

    Camunda integration note: the associated Camunda process is fully automated
    (no human task). Camunda calls this endpoint as an HTTP service task after
    the form submission triggers the process. Flask owns the business logic and
    DB writes; Camunda orchestrates the overall workflow.
    """
    if request.method == 'POST':
        kwargs = middle_logic(
            get_authorized_keycloak_user() + [
                {"try": common_middleware.request_contains_a_payload, "fail": [
                    {"try": http_responses.no_payload, "fail": []}
                ]},
                {"try": detachment_middleware.validate_detachment_change_request_payload, "fail": [
                    {"try": http_responses.failed_validation, "fail": []}
                ]},
                {"try": detachment_middleware.validate_officer_is_self, "fail": [
                    {"try": http_responses.forbidden_detachment, "fail": []}
                ]},
                {"try": detachment_middleware.get_officer_for_change_request, "fail": [
                    {"try": http_responses.officer_not_found, "fail": []}
                ]},
                {"try": detachment_middleware.get_new_detachment, "fail": [
                    {"try": http_responses.detachment_not_found, "fail": []}
                ]},
                {"try": detachment_middleware.validate_not_duplicate_request, "fail": [
                    {"try": http_responses.duplicate_detachment_request, "fail": []}
                ]},
                {"try": detachment_middleware.check_concurrent_change, "fail": [
                    {"try": http_responses.detachment_conflict, "fail": []}
                ]},
                {"try": detachment_middleware.update_officer_detachment, "fail": [
                    {"try": http_responses.server_error_response, "fail": []}
                ]},
                {"try": detachment_middleware.create_change_audit_record, "fail": [
                    {"try": http_responses.server_error_response, "fail": []}
                ]},
                {"try": detachment_middleware.commit_transaction, "fail": [
                    {"try": http_responses.server_error_response, "fail": []}
                ]},
                {"try": http_responses.successful_create_response, "fail": []},
            ],
            required_permission='forms-create',
            request=request,
            config=Config)
        return kwargs.get('response')
