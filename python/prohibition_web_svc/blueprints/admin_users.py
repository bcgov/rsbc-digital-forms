from python.common.logging_utils import get_logger
from python.prohibition_web_svc.config import Config
import python.prohibition_web_svc.middleware.splunk_middleware as splunk_middleware
import python.common.splunk as splunk
import python.common.helper as helper
from flask import request, Blueprint, make_response, jsonify
from flask_cors import CORS
import python.prohibition_web_svc.business.keycloak_logic as keycloak_logic
import python.prohibition_web_svc.http_responses as http_responses
import python.prohibition_web_svc.middleware.keycloak_middleware as keycloak_middleware
import python.prohibition_web_svc.middleware.role_middleware as role_middleware
import python.prohibition_web_svc.middleware.admin_user_middleware as admin_user_middleware
import python.prohibition_web_svc.middleware.notification_middleware as notification_middleware


logger = get_logger(__name__)

logger.info('*** admin/users blueprint loaded ***')

bp = Blueprint('admin_users', __name__, url_prefix=Config.URL_PREFIX + '/api/v1')
CORS(bp, resources={Config.URL_PREFIX + "/api/v1/admin/users": {"origins": Config.ACCESS_CONTROL_ALLOW_ORIGIN}})


@bp.route('/admin/users', methods=['GET'])
def index():
    """
    List all authorized users and their associated user-roles
    """
    if request.method == 'GET':
        kwargs = helper.middle_logic(
            keycloak_logic.get_authorized_keycloak_user() + [
                {"try": splunk_middleware.admin_get_users, "fail": []},
                {"try": splunk.log_to_splunk, "fail": []},
                {"try": role_middleware.query_all_users, "fail": [
                    {"try": http_responses.server_error_response, "fail": []},
                ]},
            ],
            required_permission='admin_users-index',
            request=request,
            config=Config)
        return kwargs.get('response')


@bp.route('/admin/users/<string:username>', methods=['PATCH'])
def update(username):
    if request.method == 'PATCH':
        return make_response({"error": "method not implemented"}, 405)


@bp.route('/admin/users/<string:username>', methods=['DELETE'])
def delete(username):
    if request.method == 'DELETE':
        return make_response({"error": "method not implemented"}, 405)


@bp.route('/admin/users', methods=['POST'])
def create():
    """
    New users apply by creating a user record
    """
    if request.method == 'POST':
        kwargs = helper.middle_logic(
            keycloak_logic.get_keycloak_user() + [
                {"try": admin_user_middleware.request_contains_a_payload, "fail": [
                    {"try": http_responses.no_payload, "fail": []}
                ]},
                {"try": admin_user_middleware.validate_admin_create_user_payload, "fail": [
                    {"try": http_responses.failed_validation, "fail": []}
                ]},
                {"try": admin_user_middleware.user_has_not_applied_previously, "fail": [
                    {"try": admin_user_middleware.update_the_user, "fail": [
                        {"try": http_responses.server_error_response, "fail": []},
                    ]},
                    {"try": admin_user_middleware.does_role_already_exist, "fail": [
                        {"try": admin_user_middleware.create_user_role, "fail": [
                            {"try": http_responses.server_error_response, "fail": []},
                        ]},
                        {"try": notification_middleware.send_new_user_admin_notification, "fail": [
                            {"try": logger.warning, "args": ["Failed to send admin notification email"], "fail": []}
                        ]},
                    ]},
                    {"try": http_responses.role_already_exists, "fail": []},
                ]},
                {"try": splunk_middleware.officer_has_applied, "fail": []},
                {"try": splunk.log_to_splunk, "fail": []},
                {"try": admin_user_middleware.admin_create_a_user, "fail": [
                    {"try": http_responses.server_error_response, "fail": []},
                ]},
                {"try": admin_user_middleware.does_role_already_exist, "fail": [
                    {"try": admin_user_middleware.create_user_role, "fail": [
                        {"try": http_responses.server_error_response, "fail": []},
                    ]},
                    {"try": notification_middleware.send_new_user_admin_notification, "fail": [
                            {"try": logger.warning, "args": ["Failed to send admin notification email"], "fail": []}
                        ]},
                ]},
                {"try": http_responses.role_already_exists, "fail": []},
            ],
            request=request,
            config=Config)
        return kwargs.get('response')


@bp.route('/admin/users/<string:username>', methods=['GET'])
def get(username):
    if request.method == 'GET':
        return make_response({"error": "method not implemented"}, 405)

