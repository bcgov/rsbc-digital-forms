from dataclasses import is_dataclass

from python.common.logging_utils import get_logger
from python.common.models.TAR.lki_highway import TarLkiHighway
from python.common.models.TAR.lki_segment import TarLkiSegment
from python.prohibition_web_svc.config import Config
from python.common.helper import middle_logic
import python.prohibition_web_svc.http_responses as http_responses
from python.prohibition_web_svc.middleware import common_middleware
import python.prohibition_web_svc.middleware.splunk_middleware as splunk_middleware
from flask import request, make_response, Blueprint
from python.common.splunk import log_to_splunk
from flask_cors import CORS
from python.common.models import db, Agency, City, Country, ImpoundLotOperator, Jurisdiction, Permission, Province, Vehicle, VehicleStyle, VehicleType, VehicleColour, NSCPuj, JurisdictionCountry
from python.common.models.TAR.police_agency import TarPoliceAgency
from flask import jsonify
from python.prohibition_web_svc.cache import cache


logger = get_logger(__name__)

resource_map = {
    "tar_police_agencies": TarPoliceAgency,
    "agencies": Agency,
    "cities": City,
    "countries": Country,
    "impound_lot_operators": ImpoundLotOperator,
    "jurisdictions": Jurisdiction,
    "permissions": Permission,
    "provinces": Province,
    "vehicle_styles": VehicleStyle,
    "vehicle_types": VehicleType,
    "vehicle_colours": VehicleColour,
    "vehicles": Vehicle,
    "nsc_puj": NSCPuj,
    "jurisdiction_country": JurisdictionCountry,
    "lki_highway": TarLkiHighway,
    "lki_segment": TarLkiSegment
}

logger.info('*** static blueprint loaded ***')

bp = Blueprint('static', __name__, url_prefix=Config.URL_PREFIX + '/api/v1')
CORS(bp, resources={Config.URL_PREFIX + "/api/v1/static/*": {"origins": Config.ACCESS_CONTROL_ALLOW_ORIGIN}})


@bp.route('/static/<string:resource>', methods=['GET'])
def index(resource):
    """
    List all static ids
    """
    if request.method == 'GET':
        logger.verbose(f"GET /static/{resource} endpoint called")
        kwargs = middle_logic([
              {"try": common_middleware.get_request_id, "fail": []},
              {"try": _is_not_configuration, "fail": [
                  {"try": splunk_middleware.log_static_get, "fail": []},
                  {"try": _get_configuration, "fail": [
                      {"try": http_responses.server_error_response, "fail": []},
                  ]},
                  {"try": log_to_splunk, "fail": []},
              ]},
              {"try": _is_not_keycloak, "fail": [
                  {"try": splunk_middleware.log_static_get, "fail": []},
                  {"try": _get_keycloak, "fail": [
                      {"try": http_responses.server_error_response, "fail": []},
                  ]},
                  {"try": log_to_splunk, "fail": []},
              ]},
              {"try": splunk_middleware.log_static_get, "fail": []},
              {"try": _is_known_resource, "fail": [
                  {"try": http_responses.bad_request_response, "fail": []},
                  {"try": log_to_splunk, "fail": []},
              ]},
              {"try": _get_resource_cached, "fail": [
                  {"try": http_responses.server_error_response, "fail": []},
                  {"try": log_to_splunk, "fail": []},
              ]},
              {"try": log_to_splunk, "fail": []},
            ],
            resource=resource,
            required_permission='static-get',
            request=request,
            config=Config)
        logger.verbose(f"GET /static/{resource} endpoint response code: {kwargs.get('response').status_code}")
        return kwargs.get('response')


@bp.route('/static/<string:resource>/<string:static_id>', methods=['GET'])
def get(resource, static_id):
    if request.method == 'GET':
        return make_response({"error": "method not implemented"}, 405)


@bp.route('/static/<string:resource>', methods=['POST'])
def create(resource):
    if request.method == 'POST':
        return make_response({"error": "method not implemented"}, 405)


@bp.route('/static/<string:resource>/<string:static_id>', methods=['PATCH'])
def update(resource, static_id):
    if request.method == 'PATCH':
        return make_response({"error": "method not implemented"}, 405)

@bp.route('/ping', methods=['GET'])
def ping():
    if request.method == 'GET':
        logger.debug('Ping request received')
        _, response = _get_resource_cached(resource='cities')
        return response.get('response')

def _get_resource_cached(**kwargs) -> tuple:
    """Get resource data with caching"""
    resource = kwargs.get('resource')
    cache_key = f'static_resource::{resource}'

    cached_data = cache.get(cache_key)
    
    if cached_data is not None:
        logger.debug(f"Returning cached {resource} data")
        kwargs['response'] = make_response(cached_data, 200)
        return True, kwargs
    
    try:
        # Get fresh data using existing logic
        success, updated_kwargs = _get_resource(**kwargs)
        
        if success:
            # Cache the JSON response data
            response_data = updated_kwargs['response'].get_json()
            cache.set(cache_key, response_data)
        
        return success, updated_kwargs
    except Exception as e:
        logger.warning(f"error getting cached {resource} data: {e}")
        return False, kwargs


def _get_keycloak(**kwargs) -> tuple:
    config = {
        "realm": Config.KEYCLOAK_REALM,
        "url": Config.KEYCLOAK_AUTH_URL,
        "clientId": Config.KEYCLOAK_CLIENT_ID
    }
    kwargs['response'] = make_response(config, 200)
    return True, kwargs


def _is_known_resource(**kwargs) -> tuple:
    return kwargs.get('resource') in resource_map.keys(), kwargs


def _is_not_keycloak(**kwargs) -> tuple:
    return kwargs.get('resource') != 'keycloak', kwargs


def _is_not_configuration(**kwargs) -> tuple:
    return kwargs.get('resource') != 'configuration', kwargs


def _get_configuration(**kwargs) -> tuple:
    logger.verbose("inside _get_configuration()")
    config = {
        "environment": Config.ENVIRONMENT,
    }
    kwargs['response'] = make_response(config, 200)
    return True, kwargs


def _get_resource(**kwargs) -> tuple:
    resource = kwargs.get('resource')
    logger.verbose(f"{kwargs.get('request_id')} inside _get_resource() for resource: {resource}")
    try:
        if is_dataclass(resource_map[resource]):
            data = jsonify(db.session.query(resource_map[resource]).all())
            kwargs['response'] = make_response(data, 200)
            return True, kwargs
        else:
            data = jsonify(resource_map[resource]())
            kwargs['response'] = make_response(data, 200)
            return True, kwargs
    except Exception as e:
        logger.warning(f"{kwargs.get('request_id')} error getting {resource} data: {e}")
        return False, kwargs
