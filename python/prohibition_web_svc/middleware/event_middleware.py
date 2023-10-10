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
from base64 import b64decode, b64encode
from flask import jsonify, make_response
from python.prohibition_web_svc.models import db, Event, TwelveHourForm, TwentyFourHourForm, VIForm, IRPForm, FormStorageRefs
from python.prohibition_web_svc.config import Config
from python.prohibition_web_svc.business.cryptography_logic import encryptPdf_method1
import img2pdf
import uuid


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
    user_guid = kwargs.get('user_guid')
    try:
        logging.debug('Creating Event')
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
            created_by=user_guid,
            updated_by=user_guid,
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
        logging.debug('Saving Event')   
        db.session.add(event)
        db.session.commit()
    except Exception as e:
        logging.warning(str(e))
        return False, kwargs
    kwargs['response_dict'] = jsonify(event)
    kwargs['event'] = event
    return True, kwargs

def save_event_pdf(**kwargs) -> tuple:
    date_created=datetime.now()
    logging.debug('save event pdf')
    try:
        logging.debug('-------------------Made it to 0--------------------')
        data = kwargs.get('payload')
        event = kwargs.get('event')
        client = Minio(
            Config.MINIO_BUCKET_URL,
            access_key=Config.MINIO_AK,
            secret_key=Config.MINIO_SK,
            secure=Config.MINIO_SECURE,
        )
        logging.debug('-------------------Made it to 1--------------------')
        # Make 'asiatrip' bucket if not exist.
        found = client.bucket_exists("test")
        if not found:
            client.make_bucket("test")
        else:
            print("Bucket 'test' already exists")
        logging.debug('-------------------Made it to 2--------------------')
        if(data.get('VI')):
            filename = str(uuid.uuid4().hex)            
            pdf_filename = f"/tmp/{filename}.pdf"
            encrypted_pdf_filename = f"/tmp/{filename}_encrypted.pdf"
            b64encoded=data.get("VI_form_png").split(",")[1]
            with open(f"/tmp/{filename}.png", "wb") as fh:
                fh.write(b64decode(b64encoded))
            pdf_bytes = img2pdf.convert(f"/tmp/{filename}.png")
            with open(pdf_filename, "wb") as file:
                file.write(pdf_bytes)
            encryptPdf_method1(pdf_filename, Config.ENCRYPT_KEY, encrypted_pdf_filename)  
            logging.debug('File encrypted')
            encoded_file_name = f"{filename}_encrypted.pdf"
            encoded_pdf_filepath = f'/tmp/{encoded_file_name}'
            with open(encoded_pdf_filepath, 'rb') as file_data:
                client.fput_object(Config.STORAGE_BUCKET_NAME, encoded_file_name, encoded_pdf_filepath)
            logging.debug('File uploaded')
            
            form_storage = FormStorageRefs(
                form_id_vi=event.vi_form.form_id,
                event_id=event.event_id,
                form_type='VI',
                storage_key=f'test/{encoded_file_name}',
                created_dt=date_created,
                updated_dt=date_created,
            )
            db.session.add(form_storage)
            db.session.commit()
                    
    except Exception as e:
        logging.warning(str(e))
        return False, kwargs
    return True, kwargs

def get_events_for_user(**kwargs) -> tuple:
    user_guid = kwargs.get('user_guid')
    try:
        events = db.session.query(Event).filter(Event.created_by == user_guid).all()
        logging.debug(jsonify(events))
        kwargs['response'] = make_response(jsonify(events), 200)
    except Exception as e:
        return False, kwargs

def request_contains_a_payload(**kwargs) -> tuple:
    request = kwargs.get('request')
    try:
        payload = request.get_json()
        kwargs['payload'] = payload
        # logging.debug("payload: " + json.dumps(payload))
    except Exception as e:
        return False, kwargs
    return payload is not None, kwargs

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
    
    if(kwargs.get('payload')):
        return True, kwargs
    logging.warning("validation error: " + json.dumps(''))
    return False, kwargs
