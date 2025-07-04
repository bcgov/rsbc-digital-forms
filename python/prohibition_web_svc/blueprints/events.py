from python.prohibition_web_svc.config import Config
from python.common.helper import middle_logic
from flask import request, Blueprint, make_response, jsonify
from flask_cors import CORS
import logging.config
import python.common.splunk as splunk
import python.prohibition_web_svc.middleware.splunk_middleware as splunk_middleware
import python.prohibition_web_svc.middleware.event_middleware as event_middleware
import python.prohibition_web_svc.http_responses as http_responses
from python.prohibition_web_svc.business.keycloak_logic import get_authorized_keycloak_user


logging.config.dictConfig(Config.LOGGING)
logging.info('*** forms blueprint loaded ***')

bp = Blueprint('event', __name__, url_prefix=Config.URL_PREFIX + '/api/v1')
CORS(bp, resources={Config.URL_PREFIX + "/api/v1/event/*": {"origins": Config.ACCESS_CONTROL_ALLOW_ORIGIN}})


@bp.route('/event', methods=['GET'])
def index():
    if request.method == 'GET':
        kwargs = middle_logic(
            get_authorized_keycloak_user() + [
                {"try": splunk.log_to_splunk, "fail": []},
                {"try": event_middleware.get_events_for_user, "fail": [
                    {"try": http_responses.server_error_response, "fail": []}
                ]}
            ],
            required_permission='forms-get',
            request=request,
            config=Config)
        return kwargs.get('response')


@bp.route('', methods=['GET'])
def get(form_type, form_id):
    """
    Get a specific form
    """
    if request.method == 'GET':
        return make_response({'error': 'method not implemented'}, 405)


@bp.route('/event', methods=['POST'])
def create():
    """
    Save a new form.  The web_app uses this endpoint to lease a unique form_id
    for 30 days and save the user's name in the form table. This endpoint is not
    used to submit a new form.  All payloads to this endpoint are ignored.
    """
    # logging.debug("new event post: {}".format(request.data))
    if request.method == 'POST':
        kwargs = middle_logic(
            get_authorized_keycloak_user() + [
                {"try": event_middleware.request_contains_a_payload, "fail": [
                    {"try": splunk.log_to_splunk, "fail": []},
                    {"try": http_responses.server_error_response, "fail": []},
                ]},
                {"try": event_middleware.check_if_application_id_exists, "fail": [
                    {"try": event_middleware.record_event_error, "fail": []},
                    {"try": http_responses.application_already_exists, "fail": []},
                ]},
                {"try": event_middleware.save_event_data, "fail": [ 
                    {"try": event_middleware.record_event_error, "fail": []},
                    {"try": http_responses.bad_request_response, "fail": []}
                ]},
                {"try": event_middleware.save_event_pdf, "fail": [
                     {"try": event_middleware.record_event_error, "fail": []},
                     {"try": http_responses.server_error_response, "fail": []},
                ]},
                {"try": splunk.log_to_splunk, "fail": []},
                {"try": http_responses.successful_create_response, "fail": []},
            ],
            required_permission='forms-create',
            request=request,
            config=Config)
        return kwargs.get('response')


@bp.route('', methods=['PATCH'])
def update(form_type, form_id):
    """
    Update an existing form is used when either a) submitting a form using an previously
    leased form_id; or, b) renewing the lease of a form_id.  If a patch request is
    received without a payload, this endpoint assumes the form lease should be renewed;
    otherwise, the payload is received as a form submission.
    """
    # if request.method == 'PATCH':
    #     kwargs = helper.middle_logic(
    #         get_authorized_keycloak_user() + [
    #             {"try": form_middleware.request_contains_a_payload, "fail": [
    #                 # Request contains no payload - renew form lease
    #                 {"try": form_middleware.renew_form_id_lease, "fail": [
    #                     {"try": splunk_middleware.unable_to_renew_lease, "fail": []},
    #                     {"try": splunk.log_to_splunk, "fail": []},
    #                     {"try": http_responses.bad_request_response, "fail": []},
    #                 ]},
    #                 {"try": splunk_middleware.form_lease_renewed, "fail": []},
    #                 {"try": splunk.log_to_splunk, "fail": []},
    #                 {"try": http_responses.successful_update_response, "fail": []},
    #             ]},
    #             # Request contains a payload - process submitted form
    #             {"try": splunk_middleware.form_submitted, "fail": []},
    #             {"try": splunk.log_to_splunk, "fail": []},
    #             {"try": form_middleware.mark_form_as_printed, "fail": [
    #                 # TODO - Write to RabbitMQ fail queue
    #                 {"try": http_responses.record_not_found, "fail": []},
    #             ]},
    #             # TODO - Write to RabbitMQ ingested queue
    #             {"try": http_responses.successful_update_response, "fail": []}
    #         ],
    #         required_permission='forms-update',
    #         form_type=form_type,
    #         form_id=form_id,
    #         request=request,
    #         config=Config)
    #     return kwargs.get('response')


@bp.route("", methods=['DELETE'])
def delete(form_type, form_id):
    """
    Delete a specific form
    """
    if request.method == 'DELETE':
        return make_response({'error': 'method not implemented'}, 405)

