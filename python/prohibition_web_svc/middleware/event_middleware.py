import logging
import json
import pytz
import iso8601
import os
from PIL import Image
from io import BytesIO
from minio import Minio
from datetime import datetime
from cerberus import Validator
from base64 import b64decode
from flask import jsonify, make_response
from python.prohibition_web_svc.models import db, Event, TwelveHourForm, TwentyFourHourForm, VIForm, IRPForm
from python.prohibition_web_svc.config import Config


def validate_update(**kwargs) -> tuple:
    return True, kwargs

def log_payload_to_splunk(**kwargs) -> tuple:
    request = kwargs.get('request')
    # TODO - log to Splunk
    logging.debug("payload: | {}".format(request.get_data()))
    return True, kwargs

def save_event_data(**kwargs) -> tuple:
    logging.debug('inside save_event_data()')
    data = kwargs.get('payload')
    logging.debug(type(data.get('VI_form_png')))
    try:
        date_created=datetime.now()
        event = Event(
            driver_licence_no=data.get('driver_licence_no'),
            driver_jurisdiction=data.get('drivers_licence_jurisdiction').get('value'),
            driver_last_name=data.get('driver_last_name'),
            driver_given_name=data.get('driver_given_name'),
            driver_dob=datetime.strptime(data.get('driver_dob'), "%Y-%m-%dT%H:%M:%S.%f%z"),
            driver_address=data.get('driver_address'),
            driver_city=data.get('driver_city'),
            driver_prov=data.get('driver_prov_state').get('value'),
            driver_postal=data.get('driver_postal'),
            driver_phone=data.get('driver_phone'),
            vehicle_jurisdiction=data.get('vehicle_jurisdiction').get('value'),
            vehicle_plate_no=data.get('vehicle_plate_no'),
            vehicle_registration_no=data.get('vehicle_registration_no'),
            vehicle_year=data.get('vehicle_year').get('value'),
            vehicle_mk_md=data.get('vehicle_mk_md').get('value'),
            vehicle_style=data.get('vehicle_style').get('value'),
            vehicle_colour=data.get('vehicle_colour'),
            vehicle_vin_no=data.get('vehicle_vin_no'),
            nsc_no=data.get('nsc_no'),
            owned_by_corp=data.get('owned_by_corp'),
            corporation_name=data.get('corporation_name'),
            regist_owner_last_name=data.get('regist_owner_last_name'),
            regist_owner_first_name=data.get('regist_owner_first_name'),
            regist_owner_address=data.get('regist_owner_address'),
            regist_owner_dob=datetime.strptime(data.get('driver_dob'), "%Y-%m-%dT%H:%M:%S.%f%z"),
            regist_owner_city=data.get('regist_owner_city'),
            regist_owner_prov=data.get('regist_owner_prov_state').get('value'),
            regist_owner_postal=data.get('regist_owner_postal'),
            created_dt=date_created,
            updated_dt=date_created,
        )
        if data.get('VI'):
            vi_form = VIForm(
                gender=data.get('gender'),
                driver_licence_expiry=datetime.strptime(data.get('driver_licence_expiry'), "%Y-%m-%dT%H:%M:%S.%f%z"),
                driver_licence_class=data.get('driver_licence_class'),
                unlicenced_prohibition_number=data.get('unlicenced_prohibition_number'),
                belief_driver_bc_resident=None if not data.get('belief_driver_bc_resident') else data.get('belief_driver_bc_resident'),
                out_of_province_dl=data.get('out_of_province_dl'),
                out_of_province_dl_number=data.get('out_of_province_dl_number'),
                date_of_impound=datetime.strptime(data.get('date_of_impound'), "%Y-%m-%dT%H:%M:%S.%f%z"),
                irp_impound= True if data.get('irp_impound') == 'YES' else False,
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
                linkage_location_of_keys=data.get('linkage_location_of_keys'),
                linkage_location_of_keys_explanation=data.get('linkage_location_of_keys_explanation'),
                linkage_driver_principal=data.get('linkage_driver_principal'),
                linkage_owner_in_vehicle=data.get('linkage_owner_in_vehicle'),
                linkage_owner_aware_possesion=data.get('linkage_owner_aware_possesion'),
                linkage_vehicle_transfer_notice=data.get('linkage_vehicle_transfer_notice'),
                linkage_other=data.get('linkage_other'),
                speed_limit=data.get('speed_limit'),
                vehicle_speed=data.get('vehicle_speed'),
                speed_estimation_technique=data.get('speed_estimation_technique'),
                speed_confirmation_technique=data.get('speed_confirmation_technique'),
                incident_details=data.get('incident_details'),
                incident_details_extra_page=data.get('incident_details_extra_page'),
                created_dt=date_created,
                updated_dt=date_created,
            )
            event.vi_form = vi_form   
        if data.get('TwentyFourHour'):
            return
        if data.get('TwelveHour'):
            return    
        if data.get('IRP'):
            return    
        db.session.add(event)
        db.session.commit()
    except Exception as e:
        logging.warning(str(e))
        return False, kwargs
    kwargs['response_dict'] = jsonify(event)
    return True, kwargs

def save_event_pdf(**kwargs) -> tuple:
    logging.debug('save event pdf')
    try:
        data = kwargs.get('payload')
        client = Minio(
            Config.MINIO_BUCKET_URL,
            access_key=Config.MINIO_AK,
            secret_key=Config.MINIO_SK,
            secure=Config.MINIO_SECURE,
        )

        # Make 'asiatrip' bucket if not exist.
        found = client.bucket_exists("test")
        if not found:
            client.make_bucket("test")
        else:
            print("Bucket 'test' already exists")

        if(data.get('VI')):
            pdf_filename = "/tmp/VI_test_PDF.pdf"
            img = Image.open(BytesIO(b64decode(data.get("VI_form_png").split(",")[1:2][0])))
            img.save(pdf_filename, "PDF", resolution=100.0, save_all=True)
            client.fput_object("test", "VI_test_file.pdf", "/tmp/VI_test_PDF.pdf")
    except Exception as e:
        logging.warning(str(e))
        return False, kwargs
    return True, kwargs
    

def request_contains_a_payload(**kwargs) -> tuple:
    request = kwargs.get('request')
    try:
        payload = request.get_json()
        kwargs['payload'] = payload
        # logging.debug("payload: " + json.dumps(payload))
    except Exception as e:
        return False, kwargs
    return payload is not None, kwargs


def get_a_form(**kwargs) -> tuple:
    form_type = kwargs.get('form_type')
    form_id = kwargs.get('form_id')
    try:
        form = db.session.query(Form) \
            .filter(Form.form_type == form_type) \
            .filter(Form.id == form_id) \
            .filter(Form.user_guid == kwargs['username']) \
            .first()
        kwargs['response'] = make_response(jsonify(form), 200)
    except Exception as e:
        logging.warning(str(e))
        return False, kwargs
    return True, kwargs


def get_json_payload(**kwargs) -> tuple:
    logging.debug("inside get_json_payload()")
    try:
        request = kwargs.get('request')
        kwargs['payload'] = request.json
    except Exception as e:
        logging.warning(str(e))
        return False, kwargs
    return True, kwargs


def validate_form_payload(**kwargs) -> tuple:
    logging.debug("inside validate_form_payload()")
    schema = {
        "form_id": {
            'type': 'string',
            'empty': False,
            'required': True
        },
        "form_type": {
            'type': 'string',
            'allowed': ['12Hour', '24Hour', 'IRP', 'VI'],
            'empty': False,
            'required': True
        }
    }
    v = Validator(schema)
    v.allow_unknown = False
    if v.validate(kwargs.get('payload')):
        return True, kwargs
    logging.warning("validation error: " + json.dumps(v.errors))
    kwargs['validation_errors'] = v.errors
    return False, kwargs


def convert_vancouver_to_utc(iso_datetime_string: str) -> datetime:
    """
    The datetime string we receive from the web app has a Vancouver
    timezone, but the API database field is not timezone aware. We
    convert the Vancouver timezone to UTC.
    """
    utc_timezone = pytz.timezone("UTC")
    printed = iso8601.parse_date(iso_datetime_string)
    return printed.astimezone(utc_timezone).replace(tzinfo=None)
