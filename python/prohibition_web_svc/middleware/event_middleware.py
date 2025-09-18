import json
import os
from dataclasses import asdict
from minio import Minio
from datetime import datetime
from base64 import b64decode
from flask import jsonify, make_response
from python.common.logging_utils import get_logger
from python.common.models import db, Event, TwelveHourForm, TwentyFourHourForm, VIForm, IRPForm, FormStorageRefs
from python.prohibition_web_svc.config import Config
from python.prohibition_web_svc.business.cryptography_logic import encryptPdf_method1
import uuid
from split_image import split_image
from python.common.enums import ErrorCode, EventType
from python.prohibition_web_svc.helpers.pdf_helpers import create_pdf_with_images

logger = get_logger(__name__)

def validate_update(**kwargs) -> tuple:
    return True, kwargs


def log_payload_to_splunk(**kwargs) -> tuple:
    # TODO - log to Splunk
    data = kwargs.get('payload')
    logger.debug("payload: | {}".format(data))
    kwargs['splunk_data'] = {
        'event': "create VI/24h/12h event",
        'user_guid': kwargs.get('user_guid', ''),
        'username': kwargs.get('username'),
        'form_type': get_event_type(data).code,
        'ticket_no': get_ticket_no(data),
    }
    return True, kwargs

def check_if_application_id_exists(**kwargs) -> tuple:
    """
    Check if the application id exists in the database.
    """
    logger.verbose('inside check_if_application_id_exists()')
    data = kwargs.get('payload')
    application_id = data.get('ff_application_id')
    if application_id is None:
        return True, kwargs
    try:
        event = db.session.query(Event).filter(
            Event.ff_application_id == application_id).first()
        if event is not None:
            kwargs['error'] = {
                'error_code': ErrorCode.E09,
                'error_details': 'Application ID already exists',
                'event_id': event.event_id,
                'event_type': get_event_type(data),
                'ticket_no': get_ticket_no(data),
                'func': check_if_application_id_exists,
            }
            return False, kwargs
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs

def save_event_data(**kwargs) -> tuple:
    logger.verbose('inside save_event_data()')
    data = kwargs.get('payload')
    if kwargs.get('identity_provider') == 'service_account':
       user_guid = data.get('submitted_user_guid', kwargs.get('username'))
    else:
       user_guid = kwargs.get('user_guid')

    try:
        date_created = datetime.now()
        # logger.debug(f'heres your data {data}')
        event = Event(
            icbc_sent_status='pending',
            vi_sent_status='pending',
            task_processing_status='pending',
            driver_licence_no=data.get('driver_licence_no'),
            driver_jurisdiction=safe_get_value(data.get('drivers_licence_jurisdiction', {})),
            driver_last_name=data.get('driver_last_name'),
            driver_given_name=data.get('driver_given_name'),
            driver_dob=datetime.strptime(
                data.get('driver_dob'), "%Y-%m-%dT%H:%M:%S.%f%z") if data.get('driver_dob') else None,
            driver_address=data.get('driver_address'),
            driver_city=data.get('driver_city'),
            driver_prov=safe_get_value(data.get('driver_prov_state', {})),
            driver_postal=data.get('driver_postal'),
            driver_phone=data.get('driver_phone'),
            type_of_prohibition=data.get('type_of_prohibition'),
            vehicle_jurisdiction=safe_get_value(data.get('vehicle_jurisdiction', {})),
            vehicle_plate_no=data.get('vehicle_plate_no'),
            vehicle_registration_no=safe_get_value(data.get('vehicle_registration_no', {})),
            vehicle_year=safe_get_value(data.get('vehicle_year', {})),
            vehicle_mk_md=safe_get_value(data.get('vehicle_mk_md', {})),
            vehicle_style=safe_get_value(data.get('vehicle_style', {})),
            vehicle_type=(lambda x: x.get('value') if x else None)(data.get('vehicle_type', None)),
            vehicle_colour=data.get('vehicle_colour'),
            vehicle_vin_no=data.get('vehicle_vin_no'),
            intersection_or_address_of_offence=data.get(
                'intersection_or_address_of_offence'),
            impound_lot_operator=safe_get_value(data.get('ILO-options', {})),
            offence_city=safe_get_value(data.get('offence_city', {})),
            date_of_driving=data.get('date_of_driving'),
            time_of_driving=data.get('time_of_driving'),
            nsc_no=data.get('nsc_no', None),
            # nsc_prov_state=data.get('nsc_prov_state', {
            #     'value': None, 'label': None}).get('value'),
            nsc_prov_state=(lambda x: x.get('value') if x else None)(data.get('nsc_prov_state', None)),
            owned_by_corp=data.get('owned_by_corp'),
            corporation_name=data.get('corporation_name'),
            regist_owner_last_name=data.get('regist_owner_last_name'),
            regist_owner_first_name=data.get('regist_owner_first_name'),
            regist_owner_address=data.get('regist_owner_address'),
            regist_owner_dob=datetime.strptime(
                data.get('regist_owner_dob'), "%Y-%m-%dT%H:%M:%S.%f%z") if data.get('regist_owner_dob') else None,
            regist_owner_city=data.get('regist_owner_city'),
            regist_owner_prov=safe_get_value(data.get('regist_owner_prov_state', {})),
            regist_owner_postal=data.get('regist_owner_postal'),
            regist_owner_phone=data.get('regist_owner_phone'),
            regist_owner_email=data.get('regist_owner_email'),
            vehicle_released_to=data.get("vehicle_released_to"),
            date_released=datetime.strptime(
                data.get('date_released'), "%Y-%m-%dT%H:%M:%S.%f%z") if data.get('date_released') else None,
            time_released=data.get("time_released"),
            location_of_keys=data.get('location_of_keys'),
            submitted=True,
            confirmation_of_service=data.get('confirmation_of_service'),
            confirmation_of_service_date=data.get(
                'confirmation_of_service_date'),
            agency_file_no=data.get('agency_file_no'),
            created_dt=date_created,
            updated_dt=date_created,
            created_by=user_guid,
            updated_by=user_guid,
            ff_application_id=data.get('ff_application_id'),
        )
        if data.get('VI'):
            vi_form = VIForm(
                gender=(lambda x: x.get('value') if x else None)(data.get('gender', None)),                
                # gender=data.get('gender',''),
                driver_is_regist_owner=data.get('driver_is_regist_owner'),
                driver_licence_expiry=datetime.strptime(
                    data.get('driver_licence_expiry'), "%Y-%m-%dT%H:%M:%S.%f%z") if data.get('driver_licence_expiry') else None,
                driver_licence_class=data.get('driver_licence_class'),
                unlicenced_prohibition_number=data.get(
                    'unlicenced_prohibition_number'),
                belief_driver_bc_resident=data.get(
                    'belief_driver_bc_resident'),
                out_of_province_dl=data.get('out_of_province_dl'),
                out_of_province_dl_number=data.get(
                    'out_of_province_dl_number'),
                out_of_province_dl_expiry=data.get(
                    'out_of_province_dl_expiry'),
                out_of_province_dl_jurisdiction=(lambda x: x.get('value') if x else None)(data.get('out_of_province_dl_jurisdiction', None)),
                # out_of_province_dl_jurisdiction=data.get('out_of_province_dl_jurisdiction', {
                # 'value': None, 'label': None}).get('value'),                
                date_of_impound=datetime.strptime(
                    data.get('date_of_impound'), "%Y-%m-%dT%H:%M:%S.%f%z") if data.get('date_of_impound') else None,
                irp_impound=data.get('irp_impound'),
                irp_impound_duration=data.get('irp_impound_duration'),
                IRP_number=data.get('IRP_number'),
                VI_number=data.get('VI_number'),
                excessive_speed=data.get('excessive_speed'),
                prohibited=data.get('prohibited'),
                suspended=data.get('suspended'),
                street_racing=data.get('street_racing'),
                stunt_driving=data.get('stunt_driving'),
                motorcycle_seating=data.get('motorcycle_seating'),
                motorcycle_restrictions=data.get('motorcycle_restrictions'),
                unlicensed=data.get('unlicensed'),
                linkage_location_of_keys=data.get(
                    'linkage_location_of_keys'),
                linkage_location_of_keys_explanation=data.get(
                    'linkage_location_of_keys_explanation'),
                linkage_driver_principal=data.get(
                    'linkage_driver_principal'),
                linkage_owner_in_vehicle=data.get(
                    'linkage_owner_in_vehicle'),
                linkage_owner_aware_possesion=data.get(
                    'linkage_owner_aware_possesion'),
                linkage_vehicle_transfer_notice=data.get(
                    'linkage_vehicle_transfer_notice'),
                linkage_other=data.get('linkage_other'),
                speed_limit=data.get('speed_limit'),
                vehicle_speed=data.get('vehicle_speed'),
                speed_estimation_technique=data.get(
                    'speed_estimation_technique'),
                speed_confirmation_technique=data.get(
                    'speed_confirmation_technique'),
                incident_details=data.get('incident_details'),
                incident_details_extra_page=data.get(
                    'incident_details_extra_page'),
                created_dt=date_created,
                updated_dt=date_created,
            )
            event.vi_form = vi_form
        if data.get('TwentyFourHour'):
            twenty_four_hour_form = TwentyFourHourForm(
                vehicle_impounded=data.get('vehicle_impounded'),
                reason_for_not_impounding=data.get(
                    'reason_for_not_impounding'),
                reasonable_ground_other_reason=data.get(
                    'reasonable_ground_other_reason'),
                prescribed_test_used=data.get('prescribed_test_used'),
                reasonable_date_of_test=datetime.strptime(
                    data.get('reasonable_date_of_test'), "%Y-%m-%dT%H:%M:%S.%f%z") if data.get('reasonable_date_of_test') else None,
                reasonable_time_of_test=data.get('reasonable_time_of_test'),
                reason_for_not_using_prescribed_test=data.get(
                    'reason_for_not_using_prescribed_test'),
                resonable_test_used_alcohol=data.get(
                    'resonable_test_used_alcohol'),
                reasonable_asd_expiry_date=datetime.strptime(
                    data.get('reasonable_asd_expiry_date'), "%Y-%m-%dT%H:%M:%S.%f%z") if data.get('reasonable_asd_expiry_date') else None,
                reasonable_result_alcohol=data.get(
                    'reasonable_result_alcohol'),
                reasonable_bac_result_mg=data.get('reasonable_bac_result_mg'),
                resonable_approved_instrument_used=data.get(
                    'resonable_approved_instrument_used'),
                reasonable_test_used_drugs=data.get(
                    'reasonable_test_used_drugs'),
                reasonable_can_drive_drug=data.get(
                    'reasonable_can_drive_drug'),
                reasonable_can_drive_alcohol=data.get(
                    'reasonable_can_drive_alcohol'),
                requested_can_drive_alcohol=data.get(
                    'requested_can_drive_alcohol'),
                requested_can_drive_drug=data.get('requested_can_drive_drug'),
                requested_approved_instrument_used=data.get(
                    'requested_approved_instrument_used'),
                requested_BAC_result=data.get('requested_BAC_result'),
                requested_alcohol_test_result=data.get(
                    'requested_alcohol_test_result'),
                requested_ASD_expiry_date=datetime.strptime(
                    data.get('requested_ASD_expiry_date'), "%Y-%m-%dT%H:%M:%S.%f%z") if data.get('requested_ASD_expiry_date') else None,
                time_of_requested_test=data.get('time_of_requested_test'),
                requested_test_used_alcohol=data.get(
                    'requested_test_used_alcohol'),
                requested_test_used_drug=data.get('requested_test_used_drug'),
                requested_prescribed_test=data.get(
                    'requested_prescribed_test'),
                witnessed_by_officer=data.get("witnessed_by_officer"),
                admission_by_driver=data.get("admission_by_driver"),
                independent_witness=data.get("independent_witness"),
                reasonable_ground_other=data.get("reasonable_ground_other"),
                twenty_four_hour_number=data.get("twenty_four_hour_number"),
                created_dt=date_created,
                updated_dt=date_created,

            )
            event.twenty_four_hour_form = twenty_four_hour_form
        if data.get('TwelveHour'):
            twelve_hour_form = TwelveHourForm(
                driver_phone=data.get('driver_phone'),
                twelve_hour_number=data.get("twelve_hour_number"),
                form_id=data.get('form_id'),
                event_id=data.get('event_id'),
                vehicle_location=data.get('vehicle_location', None),
                created_dt=date_created,
                updated_dt=date_created,
            )
            event.twelve_hour_form = twelve_hour_form
        if data.get('IRP'):
            return
        logger.verbose('Saving Event')

        db.session.add(event)
        db.session.commit()
    except Exception as e:
        logger.error(e, stack_info=True)
        # Set error in kwargs to get consumed by the record_event_error function
        kwargs['error'] = {
            'error_code': ErrorCode.E01,
            'error_details': str(e),
            'event_id': None,
            'event_type': get_event_type(data),
            'ticket_no': get_ticket_no(data),
            'func': save_event_data,
        }
        return False, kwargs
    kwargs['response_dict'] = jsonify(event)
    kwargs['event'] = event
    return True, kwargs


def save_event_pdf(**kwargs) -> tuple:
    date_created = datetime.now()
    logger.verbose('save event pdf')
    try:
        data = kwargs.get('payload')
        event = kwargs.get('event')
        cert_path = Config.MINIO_CERT_FILE
        os.environ['SSL_CERT_FILE'] = cert_path
        client = Minio(
            Config.MINIO_BUCKET_URL,
            access_key=Config.MINIO_AK,
            secret_key=Config.MINIO_SK,
            secure=Config.MINIO_SECURE,
        )
        if(data.get('VI')):
            len_of_incident_details=len(data.get('incident_details', '')) if (data.get('incident_details')) else 0
            filename = str(uuid.uuid4().hex)
            pdf_filename = f"/tmp/{filename}.pdf"
            encrypted_pdf_filename = f"/tmp/{filename}_encrypted.pdf"
            b64encoded = data.get("VI_form_png").split(",")[1]
            extra_page_flag=len_of_incident_details>500
            page_num=3 if extra_page_flag else 2
            with open(f"/tmp/{filename}.png", "wb") as fh:
                fh.write(b64decode(b64encoded))
            split_image(f"/tmp/{filename}.png", page_num, 1, False, True,output_dir="/tmp")
            
            if extra_page_flag:
                list_of_images=[f"/tmp/{filename}_0.png", f"/tmp/{filename}_1.png", f"/tmp/{filename}_2.png"]
            else:
                list_of_images=[f"/tmp/{filename}_0.png", f"/tmp/{filename}_1.png"]

            pdf_bytes=None
            pdf_bytes = create_pdf_with_images(*list_of_images)
            with open(pdf_filename, "wb") as file:
                file.write(pdf_bytes)
            encryptPdf_method1(
                pdf_filename, Config.ENCRYPT_KEY, encrypted_pdf_filename)
            logger.debug('File encrypted')
            encoded_file_name = f"{filename}_encrypted.pdf"
            encoded_pdf_filepath = f'/tmp/{encoded_file_name}'
            with open(encoded_pdf_filepath, 'rb') as file_data:
                client.fput_object(Config.STORAGE_BUCKET_NAME,
                                   encoded_file_name, encoded_pdf_filepath)
            logger.debug('File uploaded')

            form_storage = FormStorageRefs(
                form_id_vi=event.vi_form.form_id,
                event_id=event.event_id,
                form_type='VI',
                storage_key=f'{Config.STORAGE_BUCKET_NAME}/{encoded_file_name}',
                created_dt=date_created,
                updated_dt=date_created,
            )
            db.session.add(form_storage)
            db.session.commit()
        if(data.get('TwentyFourHour')):
            filename = str(uuid.uuid4().hex)
            pdf_filename = f"/tmp/{filename}.pdf"
            encrypted_pdf_filename = f"/tmp/{filename}_encrypted.pdf"
            b64encoded = data.get("TwentyFourHour_form_png").split(",")[1]
            with open(f"/tmp/{filename}.png", "wb") as fh:
                fh.write(b64decode(b64encoded))
            pdf_bytes = create_pdf_with_images(f"/tmp/{filename}.png", is_landscape=True)
            with open(pdf_filename, "wb") as file:
                file.write(pdf_bytes)
            encryptPdf_method1(
                pdf_filename, Config.ENCRYPT_KEY, encrypted_pdf_filename)
            logger.debug('File encrypted')
            encoded_file_name = f"{filename}_encrypted.pdf"
            encoded_pdf_filepath = f'/tmp/{encoded_file_name}'
            with open(encoded_pdf_filepath, 'rb') as file_data:
                client.fput_object(Config.STORAGE_BUCKET_NAME,
                                   encoded_file_name, encoded_pdf_filepath)
            logger.debug('File uploaded')

            form_storage = FormStorageRefs(
                form_id_24h=event.twenty_four_hour_form.form_id,
                event_id=event.event_id,
                form_type='24h',
                storage_key=f'{Config.STORAGE_BUCKET_NAME}/{encoded_file_name}',
                created_dt=date_created,
                updated_dt=date_created,
            )
            db.session.add(form_storage)
            db.session.commit()

        if(data.get('TwelveHour')):
            filename = str(uuid.uuid4().hex)
            pdf_filename = f"/tmp/{filename}.pdf"
            encrypted_pdf_filename = f"/tmp/{filename}_encrypted.pdf"
            b64encoded = data.get("TwelveHour_form_png").split(",")[1]
            with open(f"/tmp/{filename}.png", "wb") as fh:
                fh.write(b64decode(b64encoded))
            pdf_bytes = create_pdf_with_images(f"/tmp/{filename}.png", is_landscape=True)
            with open(pdf_filename, "wb") as file:
                file.write(pdf_bytes)
            encryptPdf_method1(
                pdf_filename, Config.ENCRYPT_KEY, encrypted_pdf_filename)
            logger.debug('File encrypted')
            encoded_file_name = f"{filename}_encrypted.pdf"
            encoded_pdf_filepath = f'/tmp/{encoded_file_name}'
            with open(encoded_pdf_filepath, 'rb') as file_data:
                client.fput_object(Config.STORAGE_BUCKET_NAME,
                                   encoded_file_name, encoded_pdf_filepath)
            logger.debug('File uploaded')
            

            form_storage = FormStorageRefs(
                form_id_12h=event.twelve_hour_form.form_id,
                event_id=event.event_id,
                form_type='12h',
                storage_key=f'{Config.STORAGE_BUCKET_NAME}/{encoded_file_name}',
                created_dt=date_created,
                updated_dt=date_created,
            )
            db.session.add(form_storage)
            db.session.commit()

    except Exception as e:
        logger.warning(str(e))
        # Set error in kwargs to get consumed by the record_event_error function
        kwargs['error'] = {
                'error_code': ErrorCode.E02,
                'error_details': e,
                'event_id': event.event_id,
                'event_type': get_event_type(data),
                'ticket_no': get_ticket_no(data),
                'func': save_event_pdf,
            }
        return False, kwargs
    return True, kwargs


def get_events_for_user(**kwargs) -> tuple:
    user_guid = kwargs.get('user_guid')
    try:
        events = db.session.query(Event).filter(
            Event.created_by == user_guid).all()
        event_dict = []
        for event in events:
            event_obj = asdict(event)
            event_obj['vi_form'] = asdict(
                event.vi_form) if event.vi_form else {}
            event_obj['twelve_hour_form'] = asdict(
                event.twelve_hour_form) if event.twelve_hour_form else {}
            event_obj['irp_form'] = asdict(
                event.irp_form) if event.irp_form else {}
            event_obj['twenty_four_hour_form'] = asdict(
                event.twenty_four_hour_form) if event.twenty_four_hour_form else {}
            event_dict.append(event_obj)
        kwargs['response'] = make_response(jsonify(event_dict), 200)
    except Exception as e:
        return False, kwargs
    return True, kwargs


def request_contains_a_payload(**kwargs) -> tuple:
    request = kwargs.get('request')
    try:
        payload = request.get_json()
        kwargs['payload'] = payload
        # logger.debug("payload: " + json.dumps(payload))
    except Exception as e:
        return False, kwargs
    return payload is not None, kwargs


def get_json_payload(**kwargs) -> tuple:
    logger.debug("inside get_json_payload()")
    try:
        request = kwargs.get('request')
        kwargs['payload'] = request.json
    except Exception as e:
        logger.warning(str(e))
        return False, kwargs
    return True, kwargs


def validate_form_payload(**kwargs) -> tuple:
    logger.debug("inside validate_form_payload()")

    if(kwargs.get('payload')):
        return True, kwargs
    logger.warning("validation error: " + json.dumps(''))
    return False, kwargs

def get_event_type(data):
    event_type = None
    if data.get('TwelveHour'):
        event_type = EventType.TWELVE_HOUR
    elif data.get('TwentyFourHour'):
        event_type = EventType.TWENTY_FOUR_HOUR
    elif data.get('IRP'):
        event_type = EventType.IRP
    elif data.get('VI'):
        event_type = EventType.VI
    else:
        event_type = None
    return event_type

def get_ticket_no(data):
    if data.get('TwelveHour'):
        return data.get("twelve_hour_number")
    elif data.get('TwentyFourHour'):
        return data.get("twenty_four_hour_number")
    elif data.get('IRP'):
        return data.get('IRP_number')
    elif data.get('VI'):
        return data.get('VI_number')
    else:
        return None
    
def safe_get_value(data, default=None):
    """
    Safely extract the 'value' from a dictionary or handle other input types.
    
    Args:
        data (dict or str or None): Input data to extract value from
        default (Any, optional): Default value to return if no value found
    
    Returns:
        The extracted value or default
    """
    # If data is a dictionary, try to get the 'value' key
    if isinstance(data, dict):
        return data.get('value', default)
    
    # If data is an empty string, return default
    if data == "":
        return default
    
    # For None or other types, return default
    return data if data is not None else default    
