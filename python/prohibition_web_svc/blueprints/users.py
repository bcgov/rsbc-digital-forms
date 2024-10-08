from python.prohibition_web_svc.config import Config
from python.common.helper import middle_logic
import python.prohibition_web_svc.business.keycloak_logic as keycloak_logic
import python.prohibition_web_svc.http_responses as http_responses
import python.prohibition_web_svc.middleware.splunk_middleware as splunk_middleware
import python.common.splunk as splunk
from flask import request, Blueprint, make_response, jsonify
from flask_cors import CORS
import logging.config
import python.prohibition_web_svc.middleware.user_middleware as user_middleware
import python.prohibition_web_svc.middleware.notification_middleware as notification_middleware


logging.config.dictConfig(Config.LOGGING)
logging.info('*** users blueprint loaded ***')

bp = Blueprint('users', __name__, url_prefix=Config.URL_PREFIX + '/api/v1')
CORS(bp, resources={Config.URL_PREFIX + "/api/v1/users*": {"origins": Config.ACCESS_CONTROL_ALLOW_ORIGIN}})


@bp.route('/users', methods=['GET'])
def index():
    if request.method == 'GET':
        kwargs = middle_logic(
            keycloak_logic.get_keycloak_user() + [
                {"try": splunk_middleware.get_user, "fail": []},
                {"try": splunk.log_to_splunk, "fail": []},
                {"try": user_middleware.get_user, "fail": [
                    {"try": http_responses.server_error_response, "fail": []}
                ]}
            ],
            request=request,
            config=Config)
        return kwargs.get('response')


@bp.route('/users', methods=['POST'])
def create():
    """
    New users apply by creating a user record
    """
    if request.method == 'POST':
        kwargs = middle_logic(
            keycloak_logic.get_keycloak_user() + [
                {"try": user_middleware.request_contains_a_payload, "fail": [
                    {"try": http_responses.no_payload, "fail": []}
                ]},
                {"try": user_middleware.validate_create_user_payload, "fail": [
                    {"try": http_responses.failed_validation, "fail": []}
                ]},
                {"try": user_middleware.user_has_not_applied_previously, "fail": [
                    {"try": user_middleware.update_the_user, "fail": [
                        {"try": http_responses.server_error_response, "fail": []},
                    ]},
                    {"try": user_middleware.does_role_already_exist, "fail": [
                        {"try": user_middleware.create_user_role, "fail": [
                            {"try": http_responses.server_error_response, "fail": []},
                        ]},
                        {"try": notification_middleware.send_new_user_admin_notification, "fail": [
                            {"try": logging.warning, "args": ["Failed to send admin notification email"], "fail": []}
                        ]},
                    ]},
                    {"try": http_responses.role_already_exists, "fail": []},
                ]},
                {"try": splunk_middleware.officer_has_applied, "fail": []},
                {"try": splunk.log_to_splunk, "fail": []},
                {"try": user_middleware.create_a_user, "fail": [
                    {"try": http_responses.server_error_response, "fail": []},
                ]},
                {"try": user_middleware.does_role_already_exist, "fail": [
                    {"try": user_middleware.create_user_role, "fail": [
                        {"try": http_responses.server_error_response, "fail": []},
                    ]},
                    {"try": notification_middleware.send_new_user_admin_notification, "fail": [
                            {"try": logging.warning, "args": ["Failed to send admin notification email"], "fail": []}
                        ]},
                ]},
                {"try": http_responses.role_already_exists, "fail": []},
            ],
            request=request,
            config=Config)
        return kwargs.get('response')


@bp.route('/users/<string:user_guid>', methods=['GET'])
def get(user_guid):
    if request.method == 'GET':
        kwargs = middle_logic(
            [
                {"try": splunk_middleware.get_user, "fail": []},
                {"try": splunk.log_to_splunk, "fail": []},
                {"try": user_middleware.get_user, "fail": [
                    {"try": http_responses.server_error_response, "fail": []}
                ]}
            ],
            user_guid=user_guid,
            request=request,
            config=Config)
        return kwargs.get('response')


@bp.route('/users/<string:user_guid>', methods=['PATCH'])
def update(user_guid):
    if request.method == 'PATCH':
        return make_response({"error": "method not implemented"}, 405)


@bp.route('/users/<string:user_guid>', methods=['DELETE'])
def delete(user_guid):
    if request.method == 'DELETE':
        return make_response({"error": "method not implemented"}, 405)


@bp.route('/users/<string:user_guid>/update-last-active', methods=['POST'])
def update_last_active(user_guid):
    if request.method == 'POST':
        kwargs = middle_logic(
            keycloak_logic.get_keycloak_user() + [
                {"try": user_middleware.validate_update_last_active_request, "fail": [
                    {"try": http_responses.failed_validation, "fail": []}
                ]},
                {"try": splunk_middleware.update_user_last_active_splunk, "fail": []},
                {"try": splunk.log_to_splunk, "fail": []},
                {"try": user_middleware.update_user_last_active, "fail": [
                    {"try": http_responses.server_error_response, "fail": []}
                ]},
            ],
            request=request,
            config=Config,
            user_guid=user_guid)
        return kwargs.get('response')
