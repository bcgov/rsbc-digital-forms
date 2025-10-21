from flask import Blueprint, request, jsonify
from flask_cors import CORS

from python.common.logging_utils import get_logger
import python.common.helper as helper

from python.prohibition_web_svc.config import Config
from python.prohibition_web_svc.middleware import files_middleware
import python.prohibition_web_svc.business.keycloak_logic as keycloak_logic
import python.prohibition_web_svc.http_responses as http_responses

logger = get_logger(__name__)
bp = Blueprint('files', __name__, url_prefix=Config.URL_PREFIX + '/api/v1')
CORS(bp, resources={Config.URL_PREFIX + "/api/v1/files/*": {"origins": Config.ACCESS_CONTROL_ALLOW_ORIGIN}})

@bp.route('/files', methods=['POST'])
def create_file():
    kwargs = helper.middle_logic(
        keycloak_logic.get_authorized_keycloak_user() + [
            {"try": files_middleware.upload_file, "fail": [
                {"try": http_responses.server_error_response, "fail": []},
            ]},
        ],
        required_permission='admin_user_roles-create',
        request=request,
        config=Config
    )

    response = kwargs.get('response')
    status = kwargs.get('status', 200)
    return response, status


@bp.route('/files/<path:filename>', methods=['GET'])
def download_file(filename):
    kwargs = helper.middle_logic(
        keycloak_logic.get_authorized_keycloak_user() + [
            {"try": files_middleware.get_file_stream, "fail": [
                {"try": http_responses.server_error_response, "fail": []},
            ]},
        ],
        required_permission='forms-get',
        request=request,
        filename=filename,
        config=Config
    )
    response = kwargs.get('response')
    status = kwargs.get('status', 200)
    return response, status

@bp.route('/files/url/<path:filename>', methods=['GET'])
def presigned_url(filename):
    expiry = int(request.args.get('expiry', 3600))
    return files_middleware.generate_presigned_url(filename, expiry)

@bp.route('/files', methods=['GET'])
def list_all_files():
    prefix = request.args.get('prefix', '')
    return files_middleware.list_files(prefix)

@bp.route('/files/<path:filename>', methods=['DELETE'])
def remove_file(filename):
    kwargs = helper.middle_logic(
        keycloak_logic.get_authorized_keycloak_user() + [
            {"try": files_middleware.delete_file, "fail": [
                {"try": http_responses.server_error_response, "fail": []},
            ]},
        ],
        required_permission='admin_user_roles-delete',
        request=request,
        filename=filename,
        config=Config
    )
    response = kwargs.get('response')
    status = kwargs.get('status', 200)
    return response, status
