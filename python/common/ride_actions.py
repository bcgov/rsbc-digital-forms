import logging
import logging.config
import requests
from python.common import form_middleware
from python.common.helper import date_time_to_local_tz_string, format_date_only, yes_no_string_to_bool
from python.common.config import Config
from python.common.enums import ErrorCode
import pytz

from python.common.models import Agency, City, ImpoundLotOperator, JurisdictionCrossRef, Province, Vehicle, VehicleColour, VehicleStyle, VehicleType

ride_url=Config.RIDE_API_URL
ride_key=Config.RIDE_API_KEY

twelve_hours_submitted = "12hr_submitted"
twenty_four_hours_submitted = "24hr_submitted"
vi_submitted = "vi_submitted"

def twelve_hours_event(**args):
    try:
        logging.info("sending 12hr_submitted event to RIDE")
        logging.debug(args)
        if len(args.keys()) == 0:
            return True, args

        eventPayload = {}
        payloadRecord = {}
        eventPayload['typeofevent'] = twelve_hours_submitted

        payloadRecord["eventType"] = twelve_hours_submitted
        payloadRecord["twelveHourNumber"] = args['form_data']['twelve_hour_number']
        payloadRecord["typeOfProhibition"] = args['event_data']['type_of_prohibition']
        fill_common_payload_record(args, payloadRecord)
        eventPayload['twelveHoursPayload'] = payloadRecord
        fill_location(args, eventPayload)

        endpoint = f"{ride_url}/dfV2events/12hrsubmitted"
        headers = {'ride-api-key': ride_key}
        logging.info(f'calling RIDE Producer endpoint: {endpoint}')
        logging.debug(f'payload: {eventPayload}')
        logging.debug(f'headers: {headers}')
        response = requests.post(endpoint, json=eventPayload, verify=False, headers=headers)
        if response.status_code != 200:
            args['error'] = {
                        'error_code': ErrorCode.R01,
                        'error_details': f'Error in sending 12hr_submitted event to RIDE, Response code: {response.status_code} response text: {response.json()}',
                        'event_type': '12hr',
                        'func': twelve_hours_event,
                        'ticket_no': args['form_data']['twelve_hour_number'] if 'twelve_hour_number' in args['form_data'] else None,
                        'event_id': args['message']['event_id']
                    }
            logging.error('error in sending 12hr_submitted event to RIDE')
            logging.error(f'error code: {response.status_code} error message: {response.json()}')
            return False, args
        else:
            logging.debug(response.json())
    except Exception as e:
        logging.error('error in sending 12hr_submitted event to RIDE')
        logging.exception(e)
        args['error'] = {
                        'error_code': ErrorCode.R01,
                        'error_details': e,
                        'event_type': '12hr',
                        'func': twelve_hours_event,
                        'ticket_no': args['form_data']['twelve_hour_number'] if 'twelve_hour_number' in args['form_data'] else None,
                        'event_id': args['message']['event_id']
                    }
        return False, args

    return True, args

def twenty_four_hours_event(**args):
    try:
        logging.info("sending 24hr_submitted event to RIDE")
        logging.debug(args)
        if len(args.keys())==0:
            return True, args

        eventPayload = {}
        payloadRecord = {}
        eventPayload['typeofevent'] = twenty_four_hours_submitted

        payloadRecord["eventType"] = twenty_four_hours_submitted
        payloadRecord["twentyFourHrNo"] = args['form_data']['twenty_four_hour_number']
        payloadRecord["typeOfProhibition"] = args['event_data']['type_of_prohibition']
        fill_common_payload_record(args, payloadRecord)
        payloadRecord["vehicleImpounded"] = yes_no_string_to_bool(args['form_data']['vehicle_impounded'])
        payloadRecord["reasonableTestAlcohol"] = args['form_data']['resonable_test_used_alcohol']
        payloadRecord["reasonForNotImpounding"] = args['form_data']['reason_for_not_impounding']
        payloadRecord["reasonableGroundOther"] = args['form_data']['reasonable_ground_other']
        payloadRecord["reasonableGroundOtherReason"] = args['form_data']['reasonable_ground_other_reason']
        payloadRecord["prescribedTestUsed"] = yes_no_string_to_bool(args['form_data']['prescribed_test_used'])
        payloadRecord["requestedPrescribedTest"] = yes_no_string_to_bool(args['form_data']['requested_prescribed_test'])
        payloadRecord["requestedAlcoholTestResult"] = args['form_data']['requested_alcohol_test_result']
        payloadRecord["requestedApprovedInstrumentUsed"] = args['form_data']['requested_approved_instrument_used']
        payloadRecord["requestedTestUsedAlcohol"] = args['form_data']['requested_test_used_alcohol']
        payloadRecord["requestedTestUsedDrug"] = args['form_data']['requested_test_used_drug']
        eventPayload['twentyFourHoursPayload'] = payloadRecord
        fill_location(args, eventPayload)

        endpoint = f"{ride_url}/dfV2events/24hrsubmitted"
        headers = {'ride-api-key': ride_key}
        logging.info(f'calling RIDE Producer endpoint: {endpoint}')
        logging.debug(f'payload: {eventPayload}')
        logging.debug(f'headers: {headers}')
        response = requests.post(endpoint, json=eventPayload, verify=False,headers=headers)
        if response.status_code != 200:
            args['error'] = {
                        'error_code': ErrorCode.R01,
                        'error_details': f'Error in sending 24hr_submitted event to RIDE, Response code: {response.status_code} response text: {response.json()}',
                        'event_type': '24hr',
                        'func': twenty_four_hours_event,
                        'ticket_no': args['form_data']['twenty_four_hour_number'] if 'twenty_four_hour_number' in args['form_data'] else None,
                        'event_id': args['message']['event_id']
                    }
            logging.error('error in sending 24hr_submitted event to RIDE')
            logging.error(f'error code: {response.status_code} error message: {response.json()}')
            return False, args
        else:
            logging.debug(response.json())
    except Exception as e:
        logging.error('error in sending 24hr_submitted event to RIDE')
        logging.exception(e)
        args['error'] = {
                        'error_code': ErrorCode.R01,
                        'error_details': e,
                        'event_type': '24hr',
                        'func': twenty_four_hours_event,
                        'ticket_no': args['form_data']['twenty_four_hour_number'] if 'twenty_four_hour_number' in args['form_data'] else None,
                        'event_id': args['message']['event_id']
                    }
        return False, args

    return True, args


def vi_event(**args):
    try:
        logging.verbose(f"sending vi_submitted to RIDE with args: {args}")
        if len(args.keys())==0:
            return True, args

        eventPayload = {}
        payloadRecord = {}
        eventPayload['typeofevent'] = vi_submitted
        
        payloadRecord["eventType"] = vi_submitted
        payloadRecord["viNumber"] = args['form_data']['VI_number']
        fill_common_payload_record(args, payloadRecord)
        payloadRecord["driverGender"] = args['form_data']['gender']
        payloadRecord["driverLicenceClass"] = args['form_data']['driver_licence_class']
        payloadRecord["outOfProvinceDriverLicense"] = yes_no_string_to_bool(args['form_data']['out_of_province_dl'])
        payloadRecord["impoundLotOperator"] = get_impound_lot_operator(args)
        payloadRecord["dateOfImpound"] = format_date_only(args['form_data']['date_of_impound'])
        payloadRecord["unlicencedProhibitionNumber"] = args['form_data']['unlicenced_prohibition_number']
        payloadRecord["isIrp"] = yes_no_string_to_bool(args['form_data']['irp_impound'])
        payloadRecord["irpNumber"] = args['form_data']['IRP_number']
        payloadRecord["irpDuration"] = args['form_data']['irp_impound_duration']
        payloadRecord["excessiveSpeed"] = args['form_data']['excessive_speed']
        payloadRecord["prohibited"] = args['form_data']['prohibited']
        payloadRecord["suspended"] = args['form_data']['suspended']
        payloadRecord["streetRacing"] = args['form_data']['street_racing']
        payloadRecord["stuntRacing"] = args['form_data']['stunt_driving']
        payloadRecord["motorCycleSeating"] = args['form_data']['motorcycle_seating']
        payloadRecord["motorCycleRestrictions"] = args['form_data']['motorcycle_restrictions']
        payloadRecord["unlicensed"] = args['form_data']['unlicensed']
        payloadRecord["driverIsRegistOwner"] = args['form_data']['driver_is_regist_owner'] == 'true'
        payloadRecord["speedLimit"] = args['form_data']['speed_limit']
        payloadRecord["vehicleSpeed"] = args['form_data']['vehicle_speed']
        payloadRecord["speedEstimationTechnique"] = args['form_data']['speed_estimation_technique']
        payloadRecord["speedConfirmationTechnique"] = args['form_data']['speed_confirmation_technique']
        eventPayload['viPayload'] = payloadRecord
        fill_location(args, eventPayload)

        endpoint = f"{ride_url}/dfV2events/visubmitted"
        headers = {'ride-api-key': ride_key}
        logging.info(f'calling RIDE Producer endpoint: {endpoint}')
        logging.debug(f'payload: {eventPayload}')
        logging.debug(f'headers: {headers}')
        response = requests.post(endpoint, json=eventPayload, verify=False,headers=headers)
        if response.status_code != 200:
            args['error'] = {
                        'error_code': ErrorCode.R01,
                        'error_details': f'Error in sending vi_submitted event to RIDE, Response code: {response.status_code} response text: {response.text}',
                        'event_type': 'VI',
                        'func': vi_event,
                        'ticket_no': args['form_data']['VI_number'],
                        'event_id': args['message']['event_id']
                    }
            logging.error(f'error code: {response.status_code} error message: {response.text}')
            logging.error('error in sending vi_submitted event to RIDE')
            return False, args
        else:
            logging.debug(response.text)
    except Exception as e:
        logging.error('error in sending vi_submitted event to RIDE')
        logging.exception(e)
        args['error'] = {
                        'error_code': ErrorCode.R01,
                        'error_details': e,
                        'event_type': 'VI',
                        'func': vi_event,
                        'ticket_no': args['form_data']['VI_number'] if 'VI_number' in args['form_data'] else None,
                        'event_id': args['message']['event_id']
                    }
        return False, args

    return True, args

def fill_location(args, eventPayload):
    if 'latitude' in args['event_data'] and 'longitude' in args['event_data'] and args['event_data']['latitude'] and args['event_data']['longitude']:
        eventPayload["locationRequestPayload"] = {}
        eventPayload["locationRequestPayload"]["latitude"] = args['event_data']['latitude']
        eventPayload["locationRequestPayload"]["longitude"] = args['event_data']['longitude']
        eventPayload["locationRequestPayload"]["requestedAddress"] = args['event_data']['requested_address']
        eventPayload["locationRequestPayload"]["fullAddress"] = args['event_data']['full_address'] or 'NA'


def fill_common_payload_record(args, payloadRecord):
    payloadRecord["eventID"] = args['message']['event_id']
    payloadRecord["eventVersion"] = 1.0
    payloadRecord["eventDtm"] = date_time_to_local_tz_string(args['event_data']['created_dt'])
    payloadRecord["driverLicenceNumber"] = args['event_data']['driver_licence_no']
    payloadRecord["driverCityTown"] = args['event_data']['driver_city']
    payloadRecord["driverProvince"] = get_Province(args)
    payloadRecord["driverPostalCode"] = args['event_data']['driver_postal']
    payloadRecord["driverJurisdiction"] = get_jurisdiction(args['event_data']['driver_jurisdiction'], args)
    payloadRecord["driverDateOfBirth"] = format_date_only(args['event_data']['driver_dob'])
    payloadRecord["vehicleJurisdiction"] = get_jurisdiction(args['event_data']['vehicle_jurisdiction'], args)
    payloadRecord["vehiclePlateNumber"] = args['event_data']['vehicle_plate_no']
    payloadRecord["vehicleRegistrationNumber"] = args['event_data']['vehicle_registration_no']
    payloadRecord["vehicleYear"] = args['event_data']['vehicle_year']
    payloadRecord["vehicleMakeModel"] = get_vehicle_make_model(args)
    payloadRecord["vehicleStyle"] = get_vehicle_style(args)
    payloadRecord["ownedByCorp"] = args['event_data']['owned_by_corp']
    payloadRecord["corporationName"] = args['event_data']['corporation_name']
    payloadRecord["dateOfDriving"] = format_date_only(args['event_data']['date_of_driving'])
    payloadRecord["timeOfDriving"] = args['event_data']['time_of_driving']
    payloadRecord["agencyFileNumber"] = args['event_data']['agency_file_no']
    payloadRecord["dateReleased"] = format_date_only(args['event_data']['date_released'])
    payloadRecord["timeReleased"] = args['event_data']['time_released']
    payloadRecord["vehicleTypeDesc"] = get_vehicle_type(args)
    payloadRecord["addressOfOffence"] = args['event_data']['intersection_or_address_of_offence']
    payloadRecord["offenceCity"] = form_middleware.get_city_name(args['event_data']['offence_city'], args)
    payloadRecord["officerDisplayName"] = args['user_data']['display_name']
    payloadRecord["officerBadgeNumber"] = args['user_data']['badge_number']
    payloadRecord["enforcementAgencyName"] = args['user_data']['agency_ref']['agency_name']
    payloadRecord["vjurCde"] = args['user_data']['agency_ref']['vjur']


def get_Province(args) -> str:
    if args['event_data']['driver_prov']:
        application = args.get('app')
        db = args.get('db')
        with application.app_context():
            province_data = db.session.query(Province) \
                            .filter(Province.objectCd == args['event_data']['driver_prov']) \
                            .all()
            if len(province_data) == 0:
                logging.error("Province not found")
            else:
                return province_data[0].objectDsc
    return None


def get_jurisdiction(jurisdiction, args) -> str:
    if jurisdiction:
        application = args.get('app')
        db = args.get('db')
        with application.app_context():
            juris_data = db.session.query(JurisdictionCrossRef) \
                    .filter(JurisdictionCrossRef.jurisdiction_code == jurisdiction) \
                    .all()
            if len(juris_data) == 0:
                logging.error("jurisdiction not found")
            else:
                return juris_data[0].jurisdiction_name
    return None


def get_vehicle_make_model(args) -> str:
    if args['event_data']['vehicle_mk_md']:
        application = args.get('app')
        db = args.get('db')
        with application.app_context():
            vehicle_make_model_data = db.session.query(Vehicle) \
                            .filter((Vehicle.mk + '-' + Vehicle.md) == args['event_data']['vehicle_mk_md']) \
                            .all()
            if len(vehicle_make_model_data) == 0:
                logging.error("vehicle make model not found")
            else:
                return vehicle_make_model_data[0].search
    return None

def get_vehicle_style(args) -> str:
    if args['event_data']['vehicle_style']:
        application = args.get('app')
        db = args.get('db')
        with application.app_context():
            vehicle_style_data = db.session.query(VehicleStyle) \
                            .filter(VehicleStyle.code == args['event_data']['vehicle_style']) \
                            .all()
            if len(vehicle_style_data) == 0:
                logging.error("vehicle style not found")
            else:
                return vehicle_style_data[0].name
    return None


def get_vehicle_type(args) -> str:
    if args['event_data']['vehicle_type']:
        application = args.get('app')
        db = args.get('db')
        with application.app_context():
            vehicle_type_data = db.session.query(VehicleType) \
                            .filter(VehicleType.type_cd == args['event_data']['vehicle_type']) \
                            .all()
            if len(vehicle_type_data) == 0:
                logging.error("vehicle type not found")
            else:
                return vehicle_type_data[0].description
    return None

    
def get_impound_lot_operator(args) -> str:
    if args['event_data']['impound_lot_operator']:
        application = args.get('app')
        db = args.get('db')
        with application.app_context():
            impound_operator = db.session.query(ImpoundLotOperator) \
                                .filter(ImpoundLotOperator.id == args['event_data']['impound_lot_operator']) \
                                .all()
            if len(impound_operator) == 0:
                logging.error("impound lot operator not found")
            else:
                return impound_operator[0].name
    return None

