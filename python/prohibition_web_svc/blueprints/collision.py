from flask import Blueprint, request
from flask_cors import CORS
import logging.config
from python.common import splunk
from python.common.helper import middle_logic
from python.prohibition_web_svc.config import Config
from python.prohibition_web_svc.business.keycloak_logic import get_authorized_keycloak_user
import python.prohibition_web_svc.http_responses as http_responses
from python.prohibition_web_svc.middleware import collision_middleware, common_middleware
from python.prohibition_web_svc.models.collision_request_payload import CollisionRequestPayload

logging.config.dictConfig(Config.LOGGING)
logging.info('*** collision blueprint loaded ***')

bp = Blueprint('collision', __name__, url_prefix=Config.URL_PREFIX + '/api/v1')
CORS(bp, resources={Config.URL_PREFIX + "/api/v1/collision/*": {"origins": Config.ACCESS_CONTROL_ALLOW_ORIGIN}})

@bp.route('/collision', methods=['POST'])
def create_collision():
    logging.info(f"POST /collision endpoint called")
    kwargs = middle_logic(
        get_authorized_keycloak_user() + [
            {"try": collision_middleware.log_payload_to_splunk, "fail": [
                {"try": splunk.log_to_splunk, "fail": []},
                {"try": http_responses.server_error_response, "fail": []},
            ]},
            {"try": splunk.log_to_splunk, "fail": []},
            {"try": common_middleware.request_contains_a_payload, "fail": [
                {"try": common_middleware.record_event_error, "fail": []},
                {"try": http_responses.bad_request_response, "fail": []}
            ]},
            {"try": collision_middleware.set_event_type, "fail": []},
            {"try": collision_middleware.set_ticket_number, "fail": []},
            {"try": common_middleware.check_if_application_id_exists, "fail": [
                  {"try": common_middleware.record_event_error, "fail": []},
                  {"try": http_responses.application_already_exists, "fail": []},
            ]},
            {"try": collision_middleware.check_if_case_number_exists, "fail": [
                  {"try": common_middleware.record_event_error, "fail": []},
                  {"try": http_responses.application_already_exists, "fail": []},
            ]},
            {"try": collision_middleware.validate_collision_payload, "fail": [
                {"try": common_middleware.record_event_error, "fail": []},
                {"try": http_responses.bad_request_response, "fail": []}
            ]},
            {"try": collision_middleware.save_collision_data, "fail": [
                {"try": common_middleware.record_event_error, "fail": []},
                {"try": http_responses.bad_request_response, "fail": []}
            ]},
            {"try": collision_middleware.save_event_pdf, "fail": [
                  {"try": common_middleware.record_event_error, "fail": []},
                  {"try": http_responses.server_error_response, "fail": []},
            ]},
            {"try": splunk.log_to_splunk, "fail": []},
            {"try": http_responses.successful_create_response, "fail": []}
        ],
        required_permission='forms-create',
        request=request,
        config=Config
    )
    return kwargs.get('response')

@bp.route('/collision/<collision_case_num>', methods=['GET'])
def get_collision(collision_case_num):
    logging.info(f"Inside get_collision() for collision_case_num: {collision_case_num}")    
    kwargs = middle_logic(
        get_authorized_keycloak_user() + [
            {"try": collision_middleware.get_collision_data, "fail": [
                {"try": common_middleware.record_event_error, "fail": []},
                {"try": http_responses.not_found_response, "fail": []}
            ]},
            {"try": splunk.log_to_splunk, "fail": []},
            {"try": http_responses.successful_get_response, "fail": []}
        ],
        required_permission='forms-get',
        request=request,
        config=Config,
        collision_case_num=collision_case_num
    )
    return kwargs.get('response')