import logging
import logging.config
import requests
import datetime
from python.common.helper import date_time_to_local_tz_string, format_date_only, yes_no_string_to_bool
from python.common.vips_api import vips_str_to_datetime
from python.common.config import Config
import pytz

from python.form_handler.models import Agency, City, ImpoundLotOperator, JurisdictionCrossRef, Province, Vehicle, VehicleColour, VehicleStyle, VehicleType

ride_url=Config.RIDE_API_URL
ride_key=Config.RIDE_API_KEY
local_tz = pytz.timezone('Canada/Pacific')

twelve_hours_submitted = "12hr_submitted"
twenty_four_hours_submitted = "24hr_submitted"
vi_submitted = "vi_submitted"

def twelve_hours_event(**args):
    try:
        logging.info("sending 12hr_submitted event to RIDE")
        logging.debug(args)
        if len(args.keys())==0:
            return True, args

        eventPayload = {}
        payloadRecord = {}
        eventPayload['typeofevent'] = twelve_hours_submitted
        eventPayload['twelveHoursPayload'] = []

        payloadRecord["eventType"] = twelve_hours_submitted
        payloadRecord["twelveHourNumber"] = args['form_data']['twelve_hour_number']
        payloadRecord["typeOfProhibition"] = args['event_data']['type_of_prohibition']
        fill_common_payload_record(args, payloadRecord)
        eventPayload['twelveHoursPayload'].append(payloadRecord)

        endpoint = f"{ride_url}/dfV2events/12hrsubmitted"
        headers = {'ride-api-key': ride_key}
        logging.info(f'calling RIDE Producer endpoint: {endpoint}')
        logging.debug(f'payload: {eventPayload}')
        logging.debug(f'headers: {headers}')
        response = requests.post(endpoint, json=eventPayload, verify=False,headers=headers)
        if response.status_code != 200:
            logging.error('error in sending 12hr_submitted event to RIDE')
            logging.error(f'error code: {response.status_code} error message: {response.json()}')
        else:
            logging.debug(response.json())
    except Exception as e:
        logging.error('error in sending 12hr_submitted event to RIDE')
        logging.error(e)  

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
        eventPayload['twentyFourHoursPayload'] = []

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

        eventPayload['twentyFourHoursPayload'].append(payloadRecord)

        endpoint = f"{ride_url}/dfV2events/24hrsubmitted"
        headers = {'ride-api-key': ride_key}
        logging.info(f'calling RIDE Producer endpoint: {endpoint}')
        logging.debug(f'payload: {eventPayload}')
        logging.debug(f'headers: {headers}')
        response = requests.post(endpoint, json=eventPayload, verify=False,headers=headers)
        if response.status_code != 200:
            logging.error('error in sending 24hr_submitted event to RIDE')
            logging.error(f'error code: {response.status_code} error message: {response.json()}')
        else:
            logging.debug(response.json())
    except Exception as e:
        logging.error('error in sending 24hr_submitted event to RIDE')
        logging.error(e)  

    return True, args


def vi_event(**args):
    try:
        logging.info("sending vi_submitted to RIDE")
        logging.debug(args)
        if len(args.keys())==0:
            return True, args

        eventPayload = {}
        payloadRecord = {}
        eventPayload['typeofevent'] = vi_submitted
        eventPayload['viPayload'] = []

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
        eventPayload['viPayload'].append(payloadRecord)

        endpoint = f"{ride_url}/dfV2events/visubmitted"
        headers = {'ride-api-key': ride_key}
        logging.info(f'calling RIDE Producer endpoint: {endpoint}')
        logging.debug(f'payload: {eventPayload}')
        logging.debug(f'headers: {headers}')
        response = requests.post(endpoint, json=eventPayload, verify=False,headers=headers)
        if response.status_code != 200:
            logging.error('error in sending vi_submitted event to RIDE')
            logging.error(f'error code: {response.status_code} error message: {response.json()}')
        else:
            logging.debug(response.json())
    except Exception as e:
        logging.error('error in sending vi_submitted event to RIDE')
        logging.error(e)  

    return True, args


def fill_common_payload_record(args, payloadRecord):
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
    payloadRecord["offenceCity"] = get_city_name(args['event_data']['offence_city'], args)

    payloadRecord["officerDisplayName"] = args['user_data']['display_name']
    payloadRecord["officerBadgeNumber"] = args['user_data']['badge_number']
    payloadRecord["enforcementAgencyName"] = args['user_data']['agency']
    payloadRecord["vjurCde"] = get_VJur_Code(args, payloadRecord)


def get_VJur_Code(args, payloadRecord) -> str:
    application = args.get('app')
    db = args.get('db')
    with application.app_context():
        agency_data = db.session.query(Agency) \
                        .filter(Agency.agency_name == payloadRecord["enforcementAgencyName"]) \
                        .all()
        if len(agency_data) == 0:
            logging.error("jurisdiction not found")
            return 'not found'
        else:
            return agency_data[0].vjur


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


def get_city_name(city_code, args) -> str:
    application = args.get('app')
    db = args.get('db')
    with application.app_context():
        city_data = db.session.query(City) \
                        .filter(City.objectCd == city_code) \
                        .all()
        if len(city_data) == 0:
            logging.error("city not found")
        else:
            return city_data[0].objectDsc
    
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

def app_accepted_event(**args):    
    try:
        logging.info("this is from ride function new app_accepted_event")
        logging.info(args)
        if len(args.keys())==0:
            return True, args
        #TODO: Call RIDE API endpoint
        eventpayload = {}
        eventpayload['typeofevent'] = 'app_accepted'
        eventpayload['appacceptedpayload'] = []
        payloadrecord = {}
        payloadrecord["eventVersion"] = 1.0

        # convert date time to string
        tvalue = args['message']['event_date_time']
        # tformat = "%Y-%m-%dT%H:%M:%S.%f"
        # tformatted = datetime.datetime.strptime(tvalue, tformat)
        # format_string = "%Y-%m-%d %H:%M:%S"
        # dtstr = tformatted.strftime(format_string)
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        tformatted = datetime.datetime.strptime(tvalue, tformat)
        tmp_formatted=tformatted.replace(tzinfo=datetime.timezone.utc).astimezone(tz=local_tz)
        format_string = "%Y-%m-%d %H:%M:%S"
        # dtstr = tformatted.strftime(format_string)
        dtstr = tmp_formatted.strftime(format_string)
        payloadrecord["eventDtm"] = dtstr

        payloadrecord["eventType"] = "app_accepted"

        # Get prohibition no
        payloadrecord["prohibitionNo"] = args['message']['prohibition_review']['form']['prohibition-information']['prohibition-number-clean']
        payloadrecord["prohibitionNoClean"] = args['message']['prohibition_review']['form']['prohibition-information']['prohibition-number-clean']

        # Get flags
        payloadrecord["isAdp"] = (lambda x: False if (x==None or x=='false') else True)(args['message']['prohibition_review']['form']['prohibition-information']['control-is-adp'])
        payloadrecord["isIrp"] = (lambda x: False if (x==None or x=='false') else True)(args['message']['prohibition_review']['form']['prohibition-information']['control-is-irp'])
        payloadrecord["isUl"] = (lambda x: False if (x==None or x=='false') else True)(args['message']['prohibition_review']['form']['prohibition-information']['control-is-ul'])
        payloadrecord["licenceNotSurrendered"] = (lambda x: False if (x == None or x == False or x=='false') else True)(args['message']['prohibition_review']['form']['prohibition-information']['licence-not-surrendered'])
        payloadrecord["licenceLostOrStolen"] = (lambda x: False if (x == None or x == False or x=='false') else True)(args['message']['prohibition_review']['form']['prohibition-information']['licence-lost-or-stolen'])
        payloadrecord["licenceNotIssued"] = (lambda x: False if (x == None or x == False or x=='false') else True)(args['message']['prohibition_review']['form']['prohibition-information']['licence-not-issued'])

        # get dt of service
        payloadrecord["dtOfService"] = args['message']['prohibition_review']['form']['prohibition-information']['date-of-service']

        # get role
        payloadrecord["applicantRole"] = args['message']['prohibition_review']['form']['identification-information']['applicant-role']

        # get applicant details
        # payloadrecord["applicantFirstNm"] = args['message']['prohibition_review']['form']['identification-information']['first-name-applicant']
        # payloadrecord["applicantLastNm"] = args['message']['prohibition_review']['form']['identification-information']['last-name-applicant']
        # payloadrecord["applicantPhoneNo"] = args['message']['prohibition_review']['form']['identification-information']['applicant-phone-number']
        # payloadrecord["applicantEmailAddr"] = args['message']['prohibition_review']['form']['identification-information']['applicant-email-address']
        # payloadrecord["applicantEmailConfirm"] = args['message']['prohibition_review']['form']['identification-information']['applicant-email-confirm']

        # Get driver deails
        # payloadrecord["driverFirstNm"] = args['message']['prohibition_review']['form']['identification-information']['driver-first-name']
        # payloadrecord["driverLastNm"] = args['message']['prohibition_review']['form']['identification-information']['driver-last-name']
        payloadrecord["driverInformationDriverDl"] = args['message']['prohibition_review']['form']['identification-information']['driver-bcdl']
        if (payloadrecord["driverInformationDriverDl"]==None or payloadrecord["driverInformationDriverDl"]=='null' or payloadrecord["driverInformationDriverDl"]=='Null' or payloadrecord["driverInformationDriverDl"]==''):
            payloadrecord["driverInformationDriverDl"]=''
        # payloadrecord["streetInformationStreetAddr"] = args['message']['prohibition_review']['form']['identification-information']['street-address']
        payloadrecord["driverCityTown"] = args['message']['prohibition_review']['form']['identification-information']['control-driver-city-town']
        payloadrecord["driverProvince"] = args['message']['prohibition_review']['form']['identification-information']['control-driver-province']
        # payloadrecord["driverPostalCde"] = args['message']['prohibition_review']['form']['identification-information']['control-driver-postal-code']

        # get applicant signatue info
        # payloadrecord["applicantSignature"] = args['message']['prohibition_review']['form']['consent-and-submission']['signature-applicant-name']
        payloadrecord["applicantDtSigned"] = args['message']['prohibition_review']['form']['consent-and-submission']['date-signed']

        eventpayload['appacceptedpayload'].append(payloadrecord)
        endpoint = f"{ride_url}/dfevents/appaccepted"
        headers = {'ride-api-key': ride_key}
        response = requests.post(endpoint, json=eventpayload, verify=False,headers=headers)
        print(response.json())
    except Exception as e:
        logging.error('error in sending app_accepted event to RIDE')
        logging.error(e)  


    


    #TODO: For errors write to RabbitMQ
    return True, args

def disclosure_sent(**args):
    logging.info("this is from ride function disclosure_sent")
    logging.info(args)
    try:
        # logging.info(args)
        if len(args.keys()) == 0:
            return True, args
        # TODO: Call RIDE API endpoint
        eventpayload = {}
        eventpayload['typeofevent'] = 'disclosure_sent'
        eventpayload['disclosuresentpayload'] = []
        payloadrecord = {}
        payloadrecord["eventVersion"] = 1.0

        # convert date time to string
        dt1 = datetime.datetime.now()
        format_string = "%Y-%m-%d %H:%M:%S"
        tmp_formatted=dt1.replace(tzinfo=datetime.timezone.utc).astimezone(tz=local_tz)
        # dtstr = tformatted.strftime(format_string)
        dtstr = tmp_formatted.strftime(format_string)
        # dtstr = dt1.strftime(format_string)
        payloadrecord["eventDtm"] = dtstr

        payloadrecord["eventType"] = "disclosure_sent"

        # Get prohibition no
        payloadrecord["prohibitionNo"] = args.get('prohibition_number')
        # payloadrecord["prohibitionNo"] = args['message']['prohibition_review']['form']['prohibition-information'][
        #     'prohibition-number-clean']

        # payloadrecord["applicantNm"] = args.get('applicant_name')
        # payloadrecord["applicantEmail"] = args.get('applicant_email_address')

        message = args.get('message')
        # hold_hours = int(config.HOURS_TO_HOLD_BEFORE_DISCLOSURE)
        # message['hold_until'] = (datetime.datetime.today() + datetime.timedelta(hours=hold_hours)).isoformat()
        hold_until_val=dtstr
        if 'hold_until' not in message:
            pass
        # elif 'hold_until' not in message['send_disclosure']:
        #     pass
        else:
            # tmpval=message['send_disclosure']['hold_until']
            tmpval=message['hold_until']
            tformat="%Y-%m-%dT%H:%M:%S.%f"
            tformatted=datetime.datetime.strptime(tmpval,tformat)
            tmpdtstr=tformatted.strftime(format_string)
            hold_until_val=tmpdtstr
            # tmpval=iso8601.parse_date(message['hold_until'], "")
            # hold_until_val=tmpval.strftime(format_string)
        payloadrecord["holdUntil"] = hold_until_val

        eventpayload['disclosuresentpayload'].append(payloadrecord)        
        endpoint = f"{ride_url}/dfevents/disclosuresent"
        headers = {'ride-api-key': ride_key}
        response = requests.post(endpoint, json=eventpayload, verify=False, headers=headers)
        print(response.json())
    except Exception as e:
        logging.error('error in sending disclosure_sent event to RIDE')
        logging.error(e)
    # TODO: For errors write to RabbitMQ
    return True, args

def evidence_submitted(**args):
    logging.info("this is from ride function evidence_submitted")
    logging.info(args)
    try:
        # logging.info("this is from ride function new evidence_submitted")
        # logging.info(args)
        if len(args.keys()) == 0:
            return True, args
        # TODO: Call RIDE API endpoint
        eventpayload = {}
        eventpayload['typeofevent'] = 'evidence_submitted'
        eventpayload['evidencesubmittedpayload'] = []
        payloadrecord = {}
        payloadrecord["eventVersion"] = 1.0

        # convert date time to string
        # tvalue = args['message']['event_date_time']
        # tformat = "%Y-%m-%dT%H:%M:%S.%f"
        # tformatted = datetime.datetime.strptime(tvalue, tformat)
        # format_string = "%Y-%m-%d %H:%M:%S"
        # dtstr = tformatted.strftime(format_string)
        # payloadrecord["eventDtm"] = dtstr
        dt1 = datetime.datetime.now()
        # format_string = "%Y-%m-%d %H:%M:%S"
        # dtstr = dt1.strftime(format_string)

        format_string = "%Y-%m-%d %H:%M:%S"
        tmp_formatted=dt1.replace(tzinfo=datetime.timezone.utc).astimezone(tz=local_tz)
        # dtstr = tformatted.strftime(format_string)
        dtstr = tmp_formatted.strftime(format_string)
        payloadrecord["eventDtm"] = dtstr

        payloadrecord["eventType"] = "evidence_submitted"

        # Get prohibition no
        payloadrecord["prohibitionNo"]=args.get('prohibition_number')
        # payloadrecord["prohibitionNo"] = args['message']['prohibition_review']['form']['prohibition-information'][
        #     'prohibition-number-clean']

        eventpayload['evidencesubmittedpayload'].append(payloadrecord)
        endpoint = f"{ride_url}/dfevents/evidencesubmitted"
        headers = {'ride-api-key': ride_key}
        response = requests.post(endpoint, json=eventpayload, verify=False, headers=headers)
        print(response.json())
    except Exception as e:
        logging.error('error in sending evidence_submitted event to RIDE')
        logging.error(e)
    # TODO: For errors write to RabbitMQ
    return True, args

def payment_received(**args):
    logging.info("this is from ride function payment_received")
    logging.info(args)
    try:
        # logging.info(args)
        if len(args.keys()) == 0:
            return True, args
        else:
            tmpPayload=args.get('payload')
            tmpRecpt=tmpPayload['receipt_number']
            if tmpRecpt=='ABCD-1234':
                return True, args
        payload = args.get('payload')
        # TODO: Call RIDE API endpoint
        eventpayload = {}
        eventpayload['typeofevent'] = 'payment_received'
        eventpayload['payrecvdpayload'] = []
        payloadrecord = {}
        payloadrecord["eventVersion"] = 1.0

        # convert date time to string
        # "eventDtm":"2021-12-27 15:40:45",
        dt1 = datetime.datetime.now()
        # format_string = "%Y-%m-%d %H:%M:%S"
        # dtstr = dt1.strftime(format_string)
        format_string = "%Y-%m-%d %H:%M:%S"
        tmp_formatted=dt1.replace(tzinfo=datetime.timezone.utc).astimezone(tz=local_tz)
        # dtstr = tformatted.strftime(format_string)
        dtstr = tmp_formatted.strftime(format_string)
        payloadrecord["eventDtm"] = dtstr

        payloadrecord["eventType"] = "payment_received"

        # Get prohibition no
        payloadrecord["prohibitionNo"] = args.get('prohibition_number')

        # payloadrecord["recieptNo"] = payload['receipt_number']

        payloadrecord["receiptAmt"] = payload['receipt_amount']

        # payloadrecord["transactionId"] = payload.get('transaction_id')

        payloadrecord["paymentMethod"] = payload.get('payment_method')

        payloadrecord["cardType"] = payload.get('cardtype')

        receipt_datetime_object = args.get('receipt_date')
        # change timezone
        tmp_formatted=receipt_datetime_object.replace(tzinfo=datetime.timezone.utc).astimezone(tz=local_tz)
        # dtstr = tformatted.strftime(format_string)
        dtstr = tmp_formatted.strftime(format_string)

        # payloadrecord["receiptDtm"] = receipt_datetime_object.strftime(format_string)
        payloadrecord["receiptDtm"] = dtstr

        eventpayload['payrecvdpayload'].append(payloadrecord)
        endpoint = f"{ride_url}/dfevents/paymentreceived"
        headers = {'ride-api-key': ride_key}
        response = requests.post(endpoint, json=eventpayload, verify=False, headers=headers)
        print(response.json())
    except Exception as e:
        logging.error('error in sending payment_received event to RIDE')
        logging.error(e)
    # TODO: For errors write to RabbitMQ
    return True, args

def review_scheduled(**args):
    logging.info("this is from ride function review_scheduled")
    logging.info(args)
    try:
        # logging.info(args)
        if len(args.keys()) == 0:
            return True, args
        else:
            tmpTimeslot=args.get('requested_time_slot')
            if tmpTimeslot['reviewStartDtm']=='2020-12-09 11:00:00 -08:00' and args.get('prohibition_number')=='21900040':
                return True, args
        # TODO: Call RIDE API endpoint
        eventpayload = {}
        eventpayload['typeofevent'] = 'review_scheduled'
        eventpayload['reviewscheduledpayload'] = []
        payloadrecord = {}
        payloadrecord["eventVersion"] = 1.0

        # convert date time to string
        # "eventDtm":"2021-12-27 15:40:45",
        dt1 = datetime.datetime.now()
        # format_string = "%Y-%m-%d %H:%M:%S"
        # dtstr = dt1.strftime(format_string)
        format_string = "%Y-%m-%d %H:%M:%S"
        tmp_formatted=dt1.replace(tzinfo=datetime.timezone.utc).astimezone(tz=local_tz)
        # dtstr = tformatted.strftime(format_string)
        dtstr = tmp_formatted.strftime(format_string)
        payloadrecord["eventDtm"] = dtstr

        payloadrecord["eventType"] = "review_scheduled"

        # Get prohibition no
        payloadrecord["prohibitionNo"] = args.get('prohibition_number')

        timeslotvalue=args.get('requested_time_slot')
        start_time = timeslotvalue['reviewStartDtm']
        end_time = timeslotvalue['reviewEndDtm']
        # {"reviewStartDtm":"2020-09-30 13:00:00 -07:00","reviewEndDtm":"2020-09-30 13:30:00 -07:00"}
        start_str=vips_str_to_datetime(start_time).strftime(format_string)
        end_str = vips_str_to_datetime(end_time).strftime(format_string)


        payloadrecord["reviewStartDtm"] = start_str

        payloadrecord["reviewEndDtm"] = end_str

        eventpayload['reviewscheduledpayload'].append(payloadrecord)
        endpoint = f"{ride_url}/dfevents/reviewscheduled"
        headers = {'ride-api-key': ride_key}
        response = requests.post(endpoint, json=eventpayload, verify=False, headers=headers)
        print(response.json())
    except Exception as e:
        logging.error('error in sending review_scheduled event to RIDE')
        logging.error(e)
    # TODO: For errors write to RabbitMQ
    return True, args




