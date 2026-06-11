import copy
import json
import os
from dataclasses import asdict
from minio import Minio
from datetime import datetime
from base64 import b64decode
from flask import jsonify, make_response
from sqlalchemy import exists
from python.common.logging_utils import get_logger
from python.common.models import db, Event, TwelveHourForm, TwentyFourHourForm, VIForm, FormStorageRefs, Submission, SubmissionFormRef, SubmissionEvent, IRPASDTest
from python.common.models.irp_form import IRPForm
from python.prohibition_web_svc.config import Config
from python.prohibition_web_svc.business.cryptography_logic import encryptPdf_method1
import uuid
from split_image import split_image
from python.common.enums import ErrorCode, EventType
from python.prohibition_web_svc.helpers.pdf_helpers import create_pdf_with_images
from python.prohibition_web_svc.mappers.irp_mapper import IRPMapper
from python.prohibition_web_svc.middleware.common_middleware import safe_get_value

logger = get_logger(__name__)

VI_FORM_TYPE = 'VI'
TWENTY_FOUR_HOUR_FORM_TYPE = '24h'
TWELVE_HOUR_FORM_TYPE = '12h'
IRP_FORM_TYPE = 'IRP'
VI_EXTRA_PAGE_THRESHOLD = 500


def validate_update(**kwargs) -> tuple:
    return True, kwargs

def _mask_sensitive_data(data: dict) -> dict:
    """
    Mask sensitive data in the payload before logging to Splunk.
    """
    masked_data = copy.deepcopy(data)
    sensitive_fields = [
        'driver_licence_no', 'driver_last_name', 'driver_given_name',
        'regist_owner_last_name', 'regist_owner_first_name',
        'TwelveHour_form_png', 'TwentyFourHour_form_png', 'VI_form_png', 'IRP_form_png',
    ]
    for field in sensitive_fields:
        if field in masked_data:
            masked_data[field] = '[REDACTED]'
    return masked_data

def log_payload_to_splunk(**kwargs) -> tuple:
    try:
        payload = kwargs.get('payload')
        payload_masked = _mask_sensitive_data(payload)
        kwargs['splunk_data'] = {
            'event': "create VI/24h/12h/IRP event",
            'request_id': kwargs.get('request_id', ''),
            'user_guid': kwargs.get('user_guid', ''),
            'username': kwargs.get('username'),
            'form_type': get_event_type(payload).code,
            'ticket_no': get_ticket_no(payload),
            'payload': payload_masked
        }
    except Exception as e:
        logger.error(e)
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
        submission = db.session.query(Submission).filter(
            Submission.ff_application_id == application_id).first()
        if submission is not None:
            kwargs['error'] = {
                'error_code': ErrorCode.E09,
                'error_details': 'Application ID already exists',
                'submission_id': submission.submission_id,
                'event_type': get_event_type(data),
                'ticket_no': get_ticket_no(data),
                'func': check_if_application_id_exists,
            }
            return False, kwargs
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs


def check_if_form_number_was_used(**kwargs) -> tuple:
    """
    Check if the form number was used in the database.
    """
    logger.verbose('inside check_if_form_number_was_used()')
    data = kwargs.get('payload')

    try:
        vi_form_number_already_exists = False
        twenty_four_hour_form_number_already_exists = False
        twelve_hour_form_number_already_exists = False
        irp_form_number_already_exists = False
        vi_form_number = data.get('VI_number')
        twenty_four_hour_form_number = data.get('twenty_four_hour_number')
        twelve_hour_form_number = data.get('twelve_hour_number')
        irp_form_number = data.get('IRP_number')
        if data.get('VI') and vi_form_number:
            vi_form_number_already_exists = db.session.query(
                exists().where(VIForm.VI_number == str(vi_form_number))
            ).scalar()
        if data.get('TwentyFourHour') and twenty_four_hour_form_number:
            twenty_four_hour_form_number_already_exists = db.session.query(
                exists().where(TwentyFourHourForm.twenty_four_hour_number == str(twenty_four_hour_form_number))
            ).scalar()
        if data.get('TwelveHour') and twelve_hour_form_number:
            twelve_hour_form_number_already_exists = db.session.query(
                exists().where(TwelveHourForm.twelve_hour_number == str(twelve_hour_form_number))
            ).scalar()
        if data.get('IRP') and irp_form_number:
            irp_form_number_already_exists = db.session.query(
                exists().where(IRPForm.irp_number == str(irp_form_number))
            ).scalar()

        if vi_form_number_already_exists or \
            twenty_four_hour_form_number_already_exists or \
            twelve_hour_form_number_already_exists or \
            irp_form_number_already_exists:
            error_details = []
            if vi_form_number_already_exists:
                error_details.append(f'VI form number already exists: {vi_form_number}')
            if twenty_four_hour_form_number_already_exists:
                error_details.append(f'24 Hour form number already exists: {twenty_four_hour_form_number}')
            if twelve_hour_form_number_already_exists:
                error_details.append(f'12 Hour form number already exists: {twelve_hour_form_number}')
            if irp_form_number_already_exists:
                error_details.append(f'IRP form number already exists: {irp_form_number}')

            kwargs['error'] = {
                'error_code': ErrorCode.E09,
                'error_details': ', '.join(error_details),
                'event_id': data.get('ff_application_id', None),
                'event_type': get_event_type(data),
                'ticket_no': get_ticket_no(data),
                'func': check_if_form_number_was_used,
            }
            return False, kwargs
    except Exception as e:
        logger.error(e)
        kwargs['error'] = {
                'error_code': ErrorCode.G00,
                'error_details': str(e),
                'event_id': data.get('ff_application_id', None),
                'event_type': get_event_type(data),
                'ticket_no': get_ticket_no(data),
                'func': check_if_form_number_was_used,
            }
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
            confirmation_of_service_date=datetime.strptime(
                data.get('confirmation_of_service_date'), "%Y-%m-%dT%H:%M:%S.%f%z") if data.get('confirmation_of_service_date') else None,
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
                irp_impound='YES' if data.get('IRP') else data.get('irp_impound'),
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
                reasonable_asd_expiry_date=_get_asd_expiry_date(data, 'resonable_test_used_alcohol', 'reasonable_asd_expiry_date', 'reasonable_asd_expiry_date_alco_6000'),
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
                requested_ASD_expiry_date=_get_asd_expiry_date(data, 'requested_test_used_alcohol', 'requested_ASD_expiry_date', 'requested_ASD_expiry_date_alco_6000'),
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
            irp_form = IRPMapper.map_to_irp_form(data, date_created)
            event.irp_form = irp_form

        submission = Submission(
            event=event,
            ff_application_id=data.get('ff_application_id'),
            submitted_offline=data.get('submitted_offline', False),
            created_dt=date_created,
            updated_dt=date_created,
            created_by=user_guid,
            updated_by=user_guid,
        )
        db.session.add(submission)

        logger.verbose('Saving Event')
        db.session.flush()
        kwargs['submission_id'] = submission.submission_id
    except Exception as e:
        logger.error(e)
        db.session.rollback()
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

def _get_asd_expiry_date(data, \
            test_used_key:str, \
            alco_sensor_asd_expiry_date_key:str, \
            alcotest_6000_asd_expiry_date_key:str):
    asd_expiry_date = None
    try:
        if data.get(test_used_key) == 'alco-sensor' and \
           data.get(alco_sensor_asd_expiry_date_key):
                asd_expiry_date = datetime.strptime(
                    data.get(alco_sensor_asd_expiry_date_key), "%Y-%m-%dT%H:%M:%S.%f%z")
        elif data.get(test_used_key) == 'alcotest-6000' and \
            data.get(alcotest_6000_asd_expiry_date_key):
                asd_expiry_date = datetime.strptime(
                    data.get(alcotest_6000_asd_expiry_date_key), "%Y-%m-%dT%H:%M:%S.%f%z")
    except Exception as e:
        logger.warning(f"Unable to parse {test_used_key} asd_expiry_date: {e}")
    return asd_expiry_date

def save_event_pdf(**kwargs) -> tuple:
    date_created = datetime.now()
    logger.verbose('save event pdf')
    try:
        data = kwargs.get('payload')
        event = kwargs.get('event')
        submission_id = kwargs.get('submission_id')
        form_version = data.get("form_details", {}).get("form_version")
        form_keys = ['VI', 'TwentyFourHour', 'TwelveHour', 'IRP']

        if not any(data.get(k) for k in form_keys): # If no forms are included in the payload, skip PDF processing
            logger.verbose('No forms included in payload, skipping PDF processing')
            return True, kwargs

        cert_path = Config.MINIO_CERT_FILE
        os.environ['SSL_CERT_FILE'] = cert_path
        client = Minio(
            Config.MINIO_BUCKET_URL,
            access_key=Config.MINIO_AK,
            secret_key=Config.MINIO_SK,
            secure=Config.MINIO_SECURE,
        )
        if data.get('VI') and data.get("VI_form_png"):
            len_of_incident_details=len(data.get('incident_details') or '')
            b64encoded = data.get("VI_form_png").split(",")[1]
            storage_key = _process_and_upload_pdf(client, 
                                    b64encoded, 
                                    num_pages=3 if len_of_incident_details > VI_EXTRA_PAGE_THRESHOLD else 2)

            #TODO: this is now being stored in the SubmissionFormRef, once the dependency on this table is removed, delete this
            form_storage = FormStorageRefs(
                form_id_vi=event.vi_form.form_id,
                event_id=event.event_id,
                form_type=VI_FORM_TYPE,
                storage_key=storage_key,
                created_dt=date_created,
                updated_dt=date_created,
            )
            db.session.add(form_storage)

            _add_submission_events(
                str(data.get('VI_number')), 
                VI_FORM_TYPE,
                form_version, 
                submission_id, 
                storage_key,
                list_of_events=['VIPS', 'ADMIN', 'ODW'])

        if data.get('TwentyFourHour') and data.get("TwentyFourHour_form_png"):
            b64encoded = data.get("TwentyFourHour_form_png").split(",")[1]
            storage_key = _process_and_upload_pdf(client, 
                                    b64encoded,
                                    is_landscape=True)

            #TODO: this is now being stored in the SubmissionFormRef, once the dependency on this table is removed, delete this
            form_storage = FormStorageRefs(
                form_id_24h=event.twenty_four_hour_form.form_id,
                event_id=event.event_id,
                form_type=TWENTY_FOUR_HOUR_FORM_TYPE,
                storage_key=storage_key,
                created_dt=date_created,
                updated_dt=date_created,
            )
            db.session.add(form_storage)

            _add_submission_events(
                str(data.get('twenty_four_hour_number')), 
                TWENTY_FOUR_HOUR_FORM_TYPE,
                form_version, 
                submission_id, 
                storage_key,
                list_of_events=['ICBC', 'ADMIN', 'ODW'])            

        if data.get('TwelveHour') and data.get("TwelveHour_form_png"):
            b64encoded = data.get("TwelveHour_form_png").split(",")[1]
            storage_key = _process_and_upload_pdf(client, 
                                    b64encoded,
                                    is_landscape=True)

            #TODO: this is now being stored in the SubmissionFormRef, once the dependency on this table is removed, delete this
            form_storage = FormStorageRefs(
                form_id_12h=event.twelve_hour_form.form_id,
                event_id=event.event_id,
                form_type=TWELVE_HOUR_FORM_TYPE,
                storage_key=storage_key,
                created_dt=date_created,
                updated_dt=date_created,
            )
            db.session.add(form_storage)

            _add_submission_events(
                str(data.get('twelve_hour_number')), 
                TWELVE_HOUR_FORM_TYPE,
                form_version, 
                submission_id, 
                storage_key,
                list_of_events=['ICBC', 'ADMIN', 'ODW'])


        if data.get('IRP') and data.get("IRP_form_png"):
            b64encoded = data.get("IRP_form_png").split(",")[1]
            storage_key = _process_and_upload_pdf(client, b64encoded)

            #TODO: this is now being stored in the SubmissionFormRef, once the dependency on this table is removed, delete this
            form_storage = FormStorageRefs(
                form_id_irp=event.irp_form.form_id,
                event_id=event.event_id,
                form_type=IRP_FORM_TYPE,
                storage_key=storage_key,
                created_dt=date_created,
                updated_dt=date_created,
            )
            db.session.add(form_storage)

            _add_submission_events(
                str(data.get('IRP_number')), 
                IRP_FORM_TYPE,
                form_version, 
                submission_id, 
                storage_key,
                list_of_events=['VIPS', 'ADMIN', 'RTS'])

    except Exception as e:
        logger.error(e)
        db.session.rollback()
        # Set error in kwargs to get consumed by the record_event_error function
        kwargs['error'] = {
                'error_code': ErrorCode.E02,
                'error_details': e,
                'event_id': event.event_id if event else None,
                'event_type': get_event_type(data),
                'ticket_no': get_ticket_no(data),
                'func': save_event_pdf,
            }
        return False, kwargs
    return True, kwargs

def _add_submission_events(form_number:str, form_type:str, form_version:str, submission_id:int, storage_key:str, list_of_events:list=None):
    list_of_events = list_of_events or []
    form_ref = SubmissionFormRef(
                submission_id=submission_id,
                form_type=form_type,
                form_id=form_number,
                form_version=form_version if form_version else "unknown",
                storage_key=storage_key,
            )
    form_ref.events = [SubmissionEvent(destination=d) for d in list_of_events]
    db.session.add(form_ref)


def commit_transaction(**kwargs) -> tuple:
    """Commit the shared DB transaction that spans save_event_data and save_event_pdf."""
    try:
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        data = kwargs.get('payload', {})
        kwargs['error'] = {
            'error_code': ErrorCode.E01,
            'error_details': str(e),
            'event_id': None,
            'event_type': get_event_type(data),
            'ticket_no': get_ticket_no(data),
            'func': commit_transaction,
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
        logger.error(e)
        return False, kwargs
    return True, kwargs


def request_contains_a_payload(**kwargs) -> tuple:
    request = kwargs.get('request')
    try:
        payload = request.get_json()
        kwargs['payload'] = payload
        logger.verbose("payload: " + json.dumps(payload))
    except Exception as e:
        return False, kwargs
    return payload is not None, kwargs


def get_json_payload(**kwargs) -> tuple:
    logger.verbose("inside get_json_payload()")
    try:
        request = kwargs.get('request')
        kwargs['payload'] = request.json
    except Exception as e:
        logger.warning(str(e))
        return False, kwargs
    return True, kwargs


def validate_form_payload(**kwargs) -> tuple:
    logger.verbose("inside validate_form_payload()")

    if (not kwargs.get('payload')):
        error_message = 'No payload provided'
        logger.warning(error_message)
        kwargs['error'] = {
            'error_code': ErrorCode.E10,
            'error_details': error_message,
            'func': validate_form_payload,
        }
        return False, kwargs
    
    payload = kwargs.get('payload')
    if (payload.get('TwelveHour') and not payload.get('twelve_hour_number')) or \
       (payload.get('TwentyFourHour') and not payload.get('twenty_four_hour_number')) or \
         (payload.get('IRP') and not payload.get('IRP_number')) or \
           (payload.get('VI') and not payload.get('VI_number')):
        error_message = "Invalid payload provided: missing form number for the indicated form type"
        logger.warning(error_message)
        kwargs['error'] = {
            'error_code': ErrorCode.E10,
            'error_details': error_message,
            'func': validate_form_payload,
        }
        kwargs['response_dict'] = {
            'error_details': error_message
        }
        return False, kwargs
    
    if (not payload.get('TwelveHour')) and (not payload.get('TwentyFourHour')) and (not payload.get('IRP')) and (not payload.get('VI')):
        error_message = "Invalid payload provided: no form type indicated"
        logger.warning(error_message)
        kwargs['error'] = {
            'error_code': ErrorCode.E10,
            'error_details': error_message,
            'func': validate_form_payload,
        }
        kwargs['response_dict'] = {
            'error_details': error_message
        }
        return False, kwargs
    
    if (not payload.get('ff_application_id')):
        error_message = 'Invalid payload provided: missing ff_application_id'
        logger.warning(error_message)
        kwargs['error'] = {
            'error_code': ErrorCode.E10,
            'error_details': error_message,
            'func': validate_form_payload,
        }
        kwargs['response_dict'] = {
            'error_details': error_message
        }
        return False, kwargs

    return True, kwargs

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

def _process_and_upload_pdf(client, b64encoded, num_pages=1, is_landscape=False) -> str:
    """Process the base64 encoded image, convert to PDF, encrypt and upload to MinIO. Returns the storage key of the uploaded file."""

    filename = uuid.uuid4().hex
    pdf_path = f"/tmp/{filename}.pdf"
    png_path = f"/tmp/{filename}.png"
    encrypted_pdf = f"{filename}_encrypted.pdf"
    encrypted_pdf_path = f'/tmp/{encrypted_pdf}'

    try:        
        with open(png_path, "wb") as fh:
            fh.write(b64decode(b64encoded))

        if num_pages > 1:            
            split_image(png_path, num_pages, 1, False, True, output_dir="/tmp")

            list_of_images = [f"/tmp/{filename}_{i}.png" for i in range(num_pages)]            
        else:
            list_of_images=[png_path]

        pdf_bytes = create_pdf_with_images(*list_of_images, is_landscape=is_landscape)
        with open(pdf_path, "wb") as file:
            file.write(pdf_bytes)
        encryptPdf_method1(
            pdf_path, Config.ENCRYPT_KEY, encrypted_pdf_path)
        logger.verbose('File encrypted')
        
        client.fput_object(Config.STORAGE_BUCKET_NAME,
            encrypted_pdf, encrypted_pdf_path)
        logger.verbose('File uploaded')

        return f"{Config.STORAGE_BUCKET_NAME}/{encrypted_pdf}"
    finally:
        for path in [*list_of_images, pdf_path, encrypted_pdf_path]:  # cleanup temp files
            if os.path.exists(path):
                os.remove(path)


def get_irp_form_by_event_id(**kwargs) -> tuple:
    """Fetch an IRPForm by its parent event_id; stores it in kwargs['irp_form']."""
    logger.verbose('inside get_irp_form_by_event_id()')
    event_id = kwargs.get('event_id')
    try:
        irp_form = db.session.query(IRPForm).filter(IRPForm.event_id == event_id).first()
        if irp_form is None:
            logger.warning(f'IRP form for event {event_id} not found')
            return False, kwargs
        kwargs['irp_form'] = irp_form
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs


def log_irp_update_to_splunk(**kwargs) -> tuple:
    try:
        payload = kwargs.get('payload')
        irp_form = kwargs.get('irp_form')
        payload_masked = _mask_sensitive_data(payload)
        kwargs['splunk_data'] = {
            'event': 'update IRP RTS event',
            'event_id': irp_form.event_id if irp_form else None,
            'irp_number': irp_form.irp_number if irp_form else None,
            'payload': payload_masked,
        }
    except Exception as e:
        logger.error(e)
    return True, kwargs

def update_irp_form_data(**kwargs) -> tuple:
    """Apply patch fields from the request payload onto the fetched IRPForm, including ASD tests."""
    logger.verbose('inside update_irp_form_data()')
    irp_form = kwargs.get('irp_form')
    original_payload = kwargs.get('payload')
    try:
        IRPMapper.map_update_irp_form(irp_form, original_payload)

        kwargs['response_dict'] = {'event_id': irp_form.event_id}
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        kwargs['response_dict'] = {'error_details': str(e)}
        kwargs['error'] = {
            'error_code': ErrorCode.E01,
            'error_details': str(e),
            'event_id': irp_form.event_id if irp_form else None,
            'event_type': EventType.IRP,
            'ticket_no': irp_form.irp_number if irp_form else None,
            'func': update_irp_form_data,
        }
        return False, kwargs
    return True, kwargs
