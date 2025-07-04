import json
import logging
import logging.config
from python.common import form_middleware
from python.common.helper import date_time_to_local_tz_string
from python.form_handler.config import Config
import logging
import json
from minio import Minio
from python.common.models import Event,FormStorageRefs,VIForm,TwentyFourHourForm,TwelveHourForm,IRPForm,User,AgencyCrossref,CityCrossRef,JurisdictionCrossRef,ImpoundReasonCodes,IloIdCrossRef,ImpoundLotOperator
from python.form_handler.geocoding_service import get_coordinates
from python.form_handler.icbc_service import submit_to_icbc
from python.form_handler.vips_service import create_vips_doc,create_vips_imp
from python.form_handler.payloads import vips_payload,vips_document_payload
from python.form_handler.message import encode_message
from python.form_handler.helper import decryptPdf_method1,convertDateTime,convertDateTimeWithSecs
from python.common.error_middleware import record_error
from python.common.enums import ErrorCode

import fitz
import base64
import os

logging.config.dictConfig(Config.LOGGING)

def get_storage_ref_event_type(**args) -> tuple:
    """
    Get the event type from the message
    """
    logging.debug("inside actions_get_storage_ref_event_type()")
    
    try:
        
        application=args.get('app')
        db=args.get('db')
        message = args.get('message')
        event_type="unknown_event"
        tmp_key=message.get('Key',None)
        if tmp_key is None:
            return event_type    
        # storage_key=tmp_key.split('/')[1]
        storage_key = tmp_key
        # print(storage_key)
        with application.app_context():            
            form = db.session.query(FormStorageRefs) \
                .filter(FormStorageRefs.storage_key == storage_key) \
                .all()
            # db.session.commit()
            # print(form)
            if len(form) == 0 or len(form) > 1:
                return False,args
            for f in form:
                event_type=f.form_type.lower()
                args['event_type']=event_type
                form_dict=f.__dict__
                form_dict.pop('_sa_instance_state',None)
                args['storage_ref']=form_dict
        # args['event_type']=storage_key
    except Exception as e:
        logging.exception(e)
        return False,args
    return True, args


def get_event_form_data(**args) ->tuple:
    logging.debug("inside get_event_form_data()")
    try:
        application = args.get('app')
        db = args.get('db')
        message = args.get('message')
        event_type = args.get('event_type')
        storage_ref = args.get('storage_ref')
        event_id = storage_ref.get('event_id')
        form_id=''        
        with application.app_context():
            # get event data
            event_data = db.session.query(Event) \
                .filter(Event.event_id == event_id) \
                .all()
            if len(event_data) == 0 or len(event_data) > 1:
                return False, args
            for e in event_data:
                event_dict = e.__dict__
                event_dict.pop('_sa_instance_state', None)
                args['event_data'] = event_dict
            if event_type=='vi':
                form_id=storage_ref.get('form_id_vi')
                args['form_id'] = form_id
                # get form data
                form_data = db.session.query(VIForm) \
                    .filter(VIForm.form_id == form_id) \
                    .all()
                if len(form_data) == 0 or len(form_data) > 1:
                    return False, args
                for f in form_data:
                    form_dict = f.__dict__
                    form_dict.pop('_sa_instance_state', None)
                    args['form_data'] = form_dict
            elif event_type=='irp':
                form_id=storage_ref.get('form_id_irp')
                args['form_id'] = form_id
                # get form data
                form_data = db.session.query(IRPForm) \
                    .filter(IRPForm.form_id == form_id) \
                    .all()
                if len(form_data) == 0 or len(form_data) > 1:
                    return False, args
                for f in form_data:
                    form_dict = f.__dict__
                    form_dict.pop('_sa_instance_state', None)
                    args['form_data'] = form_dict
            elif event_type=='24h':
                form_id=storage_ref.get('form_id_24h')
                args['form_id'] = form_id
                # get form data
                form_data = db.session.query(TwentyFourHourForm) \
                    .filter(TwentyFourHourForm.form_id == form_id) \
                    .all()
                if len(form_data) == 0 or len(form_data) > 1:
                    return False, args
                for f in form_data:
                    form_dict = f.__dict__
                    form_dict.pop('_sa_instance_state', None)
                    args['form_data'] = form_dict
            elif event_type=='12h':
                form_id=storage_ref.get('form_id_12h')
                args['form_id'] = form_id
                # get form data
                form_data = db.session.query(TwelveHourForm) \
                    .filter(TwelveHourForm.form_id == form_id) \
                    .all()
                if len(form_data) == 0 or len(form_data) > 1:
                    return False, args
                for f in form_data:
                    form_dict = f.__dict__
                    form_dict.pop('_sa_instance_state', None)
                    args['form_data'] = form_dict
            else:
                return False,args
    except Exception as e:
        logging.exception(e)
        return False, args
    return True, args

def get_event_user_data(**args) ->tuple:
    logging.debug("inside get_form_event_data()")
    logging.debug(args)
    try:
        application = args.get('app')
        db = args.get('db')
        event_data = args.get('event_data')
        user_id = event_data.get('created_by')
        with application.app_context():
            # get user data
            user_data = db.session.query(User) \
                .filter(User.user_guid == user_id) \
                .all()
            if len(user_data) == 0 or len(user_data) > 1:
                return False, args
            for u in user_data:
                user_dict = u.__dict__
                user_dict.pop('_sa_instance_state', None)
                args['user_data'] = user_dict
    except Exception as e:
        logging.exception(e)
        return False, args
    return True,args


def validate_event_retry_count(**args)->tuple:
    logging.info("inside validate_event_retry_count()")
    logging.debug(args)
    # DONE: if event retry count is more than 10
    # DONE: Update retry count in event table
    try:
        event_type=args.get('event_type')
        message = args.get('message')
        queue_name = message.get('queue_name', None)
        retry_count=message.get('retry_count', 0)
        retry_count=retry_count+1
        args['retry_count']=retry_count
        args['message']['retry_count']=retry_count
        put_to_queue_name=Config.STORAGE_HOLD_QUEUE
        max_retries=Config.SYSTEM_RECORD_MAX_RETRIES
        if queue_name == Config.STORAGE_FAIL_QUEUE:
            max_retries=max_retries+Config.SYSTEM_RECORD_MAX_TRANSIENT_RETRIES
            put_to_queue_name=Config.STORAGE_FAIL_QUEUE
        args['put_to_queue_name']=put_to_queue_name
        if retry_count >= max_retries:
            if put_to_queue_name == Config.STORAGE_HOLD_QUEUE:
                put_to_queue_name=Config.STORAGE_FAIL_QUEUE
            elif put_to_queue_name == Config.STORAGE_FAIL_QUEUE:
                put_to_queue_name=Config.STORAGE_FAIL_QUEUE_PERS
                args['stop_retry'] = True
            args['put_to_queue_name']=put_to_queue_name
            
            # Set error in args to get consumed by the record_event_error function
            event_id = message.get('event_id', None)
            event_type = message.get('event_type', None)
            args['error'] = {
                'error_code': ErrorCode.E05,
                'error_details': f'Retry count exceeds for the event id: {event_id}, event_type: {event_type}',
                'event_id': event_id,
                'event_type': event_type,
                'func': validate_event_retry_count,
                'payload': message,
            }
            
            return False,args
    
    except Exception as e:
        logging.exception(e)
        # Set error in args to get consumed by the record_event_error function
        message = args.get('message')
        args['error'] = {
            'error_code': ErrorCode.E03,
            'error_details': e,
            'event_id': message.get('event_id'),
            'event_type': message.get('event_type'),
            'func': validate_event_retry_count,
            'payload': message,
        }
        return False,args
    return True,args


def validate_event_data(**args)->tuple:
    logging.debug("inside validate_event_data()")
    logging.debug(args)
    # TODO: validate vips payload
    return True,args


def update_event_status_processing(**args)->tuple:
    logging.debug("inside update_event_status_processing()")
    logging.debug(args)
    try:
        application=args.get('app')
        db=args.get('db')
        event_id=args.get('event_data').get('event_id')
        event_type=args.get('event_type')
        with application.app_context():
            if event_type=='vi':
                event = db.session.query(Event) \
                    .filter(Event.event_id == event_id) \
                    .one()
                event.vi_sent_status = 'processing'
                db.session.commit()
            elif event_type=='irp':
                pass
            elif event_type=='24h' or event_type=='12h':
                event = db.session.query(Event) \
                    .filter(Event.event_id == event_id) \
                    .one()
                event.icbc_sent_status = 'processing'
                db.session.commit()
    except Exception as e:
        logging.exception(e)
        return False,args
    return True,args


def get_storage_file(**args)->tuple:
    logging.debug("inside get_storage_file()")
    logging.debug(args)
    minio_host=f'{Config.STORAGE_HOST}:{Config.STORAGE_PORT}'
    storage_key=args.get('storage_ref').get('storage_key')
    # encryptivkey=args.get('storage_ref').get('encryptiv')
    bucket_name=storage_key.split('/')[0]
    storage_file_name=storage_key.split('/')[1]
    tmp_storage_local=Config.TMP_STORAGE_LOCAL
    try:
        cert_path=Config.MINIO_CERT_FILE
        os.environ['SSL_CERT_FILE'] = cert_path
        file_data=None
        client = Minio(
            minio_host,
            access_key=Config.STORAGE_ACCESS_KEY,
            secret_key=Config.STORAGE_SECRET_KEY,
            secure=Config.MINIO_SECURE,
        )
        file_data=client.get_object(bucket_name,storage_file_name)
        file_data_content = file_data.data
        # save file to local
        with open(f'{tmp_storage_local}{storage_file_name}', 'wb') as file_data_c:
            file_data_c.write(file_data_content)
        decrypted_status,decrypted_data=decryptPdf_method1(f'{tmp_storage_local}{storage_file_name}',Config.ENCRYPT_KEY,f'{tmp_storage_local}{storage_file_name}_decrypted.pdf')
        if decrypted_status is False or decrypted_data is None:
            raise Exception("decryption failed")
        args['file_data'] = decrypted_data
        logging.debug(file_data)
        os.remove(f'{tmp_storage_local}{storage_file_name}')

        # stpre decrypted_data base64 string to local file
        # with open(f'{tmp_storage_local}{storage_file_name}_decrypted1.pdf', 'wb') as file_data_c1:
        #     file_data_c1.write(base64.b64decode(decrypted_data))

        # decrypted_data=method2_decrypt(file_data_content,encryptivkey)
    except Exception as e:
        logging.exception(e)
        if file_data is not None:
            file_data.close()
            file_data.release_conn()
        return False,args
    finally:
        if file_data is not None:
            file_data.close()
            file_data.release_conn()
    return True,args


def prep_icbc_payload(**args)->tuple:
    logging.debug("inside prep_icbc_payload()")
    logging.debug(args)
    message=args.get('message')

    try:
        application = args.get('app')
        db = args.get('db')
        pdf_data=args.get('file_data')
        event_data=args.get('event_data')
        form_data=args.get('form_data')
        user_data=args.get('user_data')
        form_id=args.get('form_id')
        event_type=args.get('event_type')
        tmp_payload= {
        "dlNumber":"",
        "dlJurisdiction": "",
        "lastName": "",
        "firstName": "",
        "birthdate": "",
        "plateJurisdiction": "",
        "plateNumber": "",
        "pujCode": "",
        "nscNumber": "",
        # TODO: get the correct section from form
        "section": "",
        "violationLocation": "",
        "noticeNumber": "",
        "violationDate": "",
        "violationTime": "",
        "officerDetachment": "",        
        "officerNumber": "",
        "officerName": "",
        "pdf": pdf_data,        
        }

        # if "form_id" in form_data: tmp_payload["noticeNumber"]=event_data["form_id"]

        if "driver_licence_no" in event_data and event_data["driver_licence_no"] is not None: 
            tmpdl=event_data["driver_licence_no"] 
            if len(tmpdl) <8:
                tmpdl="0"*(8-len(tmpdl))+tmpdl
            tmp_payload["dlNumber"]=tmpdl
        else: 
            tmp_payload["dlNumber"]=None


        if "driver_jurisdiction" in event_data and event_data["driver_jurisdiction"] is not None:
            tmp_jurisdictionvalue=event_data["driver_jurisdiction"]
            with application.app_context():
                # get jurisdiction data
                icbc_jurisdiction_code=''
                juris_data = db.session.query(JurisdictionCrossRef) \
                        .filter(JurisdictionCrossRef.jurisdiction_code == tmp_jurisdictionvalue) \
                        .all()
                if len(juris_data) == 0:
                    logging.error("jurisdiction not found")
                else:
                    for j in juris_data:
                        juris_dict = j.__dict__
                        juris_dict.pop('_sa_instance_state', None)
                        icbc_jurisdiction_code= juris_dict["icbc_jurisdiction_code"]
                        break
                tmp_payload["dlJurisdiction"]=icbc_jurisdiction_code
            
        
        if "driver_last_name" in  event_data and event_data["driver_last_name"] is not None: tmp_payload["lastName"]=event_data["driver_last_name"].upper()
        if "driver_given_name" in event_data and event_data["driver_given_name"] is not None: tmp_payload["firstName"]=event_data["driver_given_name"].upper()

        # convert birthdate to string
        birthdate=event_data.get("driver_dob")
        if birthdate is not None:
            birthdate= birthdate.strftime('%Y%m%d')
            tmp_payload["birthdate"]=birthdate

        if event_data["vehicle_jurisdiction"]:
            tmp_jurisdictionvalue=event_data["vehicle_jurisdiction"]
            with application.app_context():
                # get jurisdiction data
                juris_data = db.session.query(JurisdictionCrossRef) \
                        .filter(JurisdictionCrossRef.jurisdiction_code == tmp_jurisdictionvalue) \
                        .all()
                if len(juris_data) == 0:
                    logging.error("jurisdiction not found")
                    tmp_payload["plateJurisdiction"]= ''
                else:
                    tmp_payload["plateJurisdiction"]= juris_data[0].icbc_jurisdiction_code

        if "vehicle_plate_no" in event_data and event_data["vehicle_plate_no"] is not None: 
            tmp_plate_no=event_data["vehicle_plate_no"].upper()
            tmp_plate_no=tmp_plate_no.replace(" ", "")
            tmp_payload["plateNumber"]=tmp_plate_no

        if event_data["nsc_prov_state"] and event_data["nsc_no"]: 
            tmp_jurisdictionvalue=event_data["nsc_prov_state"]
            with application.app_context():
                # get jurisdiction data
                juris_data = db.session.query(JurisdictionCrossRef) \
                        .filter(JurisdictionCrossRef.jurisdiction_code == tmp_jurisdictionvalue) \
                        .all()
                if len(juris_data) == 0:
                    logging.error("jurisdiction not found")
                    tmp_payload["pujCode"]= ''
                else:
                    tmp_payload["pujCode"] = juris_data[0].icbc_jurisdiction_code
                    tmp_payload["nscNumber"] = event_data["nsc_no"]
            
        else:
            tmp_payload["pujCode"]=""
            tmp_payload["nscNumber"]=""

        #Some validation required for NSC-Number. ICBC does not accept all values.
        # if "nsc_no" in event_data: tmp_payload["nscNumber"]=event_data["nsc_no"]
        
        if event_data["type_of_prohibition"] == "alcohol":
            if event_type == "12h":
                tmp_payload["section"] = "90.32"
            elif event_type == "24h":
                tmp_payload["section"] = "215.2"
        
        if event_data["type_of_prohibition"] == "drugs":
            if event_type == "12h":
                tmp_payload["section"] = "90.321" 
            elif event_type == "24h":
                tmp_payload["section"] = "215.3"
        

        # get the icbc city code
        if "offence_city" in event_data and event_data["offence_city"] is not None:
            tmp_city=event_data["offence_city"]
            offence_city_value=''
            with application.app_context():
                city_data = db.session.query(CityCrossRef) \
                        .filter(CityCrossRef.city_code == tmp_city) \
                        .all()
                if len(city_data) == 0:
                    logging.error("city not found")
                else:
                    for j in city_data:
                        city_data = j.__dict__
                        city_data.pop('_sa_instance_state', None)
                        # offence_city_value= city_data["icbc_city_code"]
                        offence_city_value= city_data["icbc_city_name_legacy"]
                        break
            tmp_payload["violationLocation"]=offence_city_value
            
        if event_type == "12h":
            tmp_payload["noticeNumber"] = form_data["twelve_hour_number"]
        if event_type == "24h":
            tmp_payload["noticeNumber"] = form_data["twenty_four_hour_number"]

        # convert date_of_driving to string
        date_of_driving=event_data.get("date_of_driving")
        if date_of_driving is not None:
            date_of_driving=date_time_to_local_tz_string(date_of_driving, "%Y%m%d")
            tmp_payload["violationDate"]=date_of_driving
        if "time_of_driving" in event_data: 
            tmp_payload["violationTime"]=event_data["time_of_driving"].replace(" ", "")

        # TODO: get agency from user table for the event
        if "agency" in user_data and user_data["agency"] is not None: 
            logging.debug(user_data["agency"])
            agency_name=user_data["agency"]
            detachment_city=''
            with application.app_context():
                agency_data = db.session.query(AgencyCrossref) \
                    .filter(AgencyCrossref.agency_name == agency_name) \
                    .all()
                if len(agency_data) == 0:
                    logging.error("agency not found")
                    pass
                else:
                    for a in agency_data:
                        agency_dict = a.__dict__
                        agency_dict.pop('_sa_instance_state', None)
                        detachment_city=agency_dict["icbc_city_name"]
                        break
            tmp_payload["officerDetachment"]=detachment_city.upper()

        #DONE -- Need to add agency name abbr to the begining of officerNumber
        # if "badge_number" in user_data: tmp_payload["officerNumber"]="AB"+ data["badge_number"]
        if "badge_number" in user_data: tmp_payload["officerNumber"]=user_data["badge_number"]

        officer_name=f'{user_data["last_name"]}'
        tmp_payload["officerName"]=officer_name.upper()
        
        args['icbc_payload']=tmp_payload
    except Exception as e:
        logging.exception(e)
        args['error'] = {
            'error_code': ErrorCode.I02,
            'error_details': str(e),
            'event_id': message.get('event_id') if message else None,
            'event_type': message.get('event_type') if message else None,
            'func': prep_icbc_payload,
            'payload': event_data,
        }
        return False,args
    
    return True,args

def send_to_icbc(**args)->tuple:
    logging.debug("inside send_to_icbc()")
    logging.debug(args)
    message=args.get('message')
    try:
        logging.debug(args['icbc_payload'])
        icbc_payload=args.get('icbc_payload')
        logging.debug(icbc_payload)
        send_status, icbc_response_txt,icbc_resp_code = submit_to_icbc(icbc_payload,logging)
        args['icbc_response_txt']=icbc_response_txt
        args['icbc_resp_code']=icbc_resp_code
        if send_status is False:
            args['error'] = {
            'error_code': ErrorCode.I01,
            'error_details': f'icbc_resp_code: {icbc_resp_code} icbc_response_txt: {icbc_response_txt}',
            'event_id': message.get('event_id') if message else None,
            'event_type': message.get('event_type') if message else None,
            'func': send_to_icbc,
            'payload': icbc_payload,
        }
            return False,args
    except Exception as e:
        logging.exception(e)
        args['error'] = {
            'error_code': ErrorCode.I01,
            'error_details': e,
            'event_id': message.get('event_id') if message else None,
            'event_type': message.get('event_type') if message else None,
            'func': send_to_icbc,
            'payload': icbc_payload,
        }
        return False,args
    return True,args


# {
#   "notice_subject_code": "PERS",
#   "file_object": "",
#   "type_code": "",
#   "pageCount": 1,
#   "mime_sub_type": "pdf",
#   "mime_type": "application",
#   "notice_type_code": ""
# }



# {
#   "type_code": "MV2721",
#   "mime_sub_type": "pdf",
#   "mime_type": "application",
#   "file_object": "

#   "notice_type_code": "IMP",
#   "notice_subject_code": "VEHI",
#   "pageCount": 1
# }

# def send_to_vips_email(**args)->tuple:
#     logging.debug("inside send_to_vips_email()")
#     logging.debug(args)
#     try:
#         pdf_data = args.get('file_data')
#
#         if vips_response_txt is False:
#             return False,args
#     except Exception as e:
#         logging.exception(e)
#         return False,args
#     return True,args

def prep_vips_document_payload(**args)->tuple:
    logging.debug("inside prep_vips_document_payload()")
    logging.debug(args)

    try:
        pdf_data=args.get('file_data')
        event_data=args.get('event_data')
        form_data=args.get('form_data')
        user_data=args.get('user_data')
        form_id=args.get('form_id')
        tmp_payload=vips_document_payload.copy()

        subject_cd="VEHI"

        # if "owned_by_corp" in event_data and event_data["owned_by_corp"] is True:
        #     subject_cd="CORP"
        # tmp_payload["notice_subject_code"]=subject_cd
        tmp_payload["notice_subject_code"]=subject_cd

        tmp_payload["file_object"]=pdf_data

        # DONE: to confirm
        tmp_payload["type_code"]="MV2721"
        # if "type_cd" in form_data: tmp_payload["type_code"]=form_data["type_cd"]

        tmp_payload["pageCount"]=1
        tmp_payload["mime_sub_type"]="pdf"
        tmp_payload["mime_type"]="application"

        # TODO: to confirm
        tmp_payload["notice_type_code"]="IMP"
        # if "notice_type_cd" in form_data: tmp_payload["notice_type_code"]=form_data["notice_type_cd"]

        args['vips_document_payload']=tmp_payload
    except Exception as e:
        logging.exception(e)
        return False,args
    return True,args

def create_vips_document(**args)->tuple:
    logging.debug("inside create_vips_document()")
    logging.debug(args)
    try:
        vips_document_payload=args.get('vips_document_payload')
        logging.debug(vips_document_payload)
        vips_doc_status, vips_doc_response_txt, vips_doc_resp_code = create_vips_doc(vips_document_payload,logging)
        args['vips_doc_response_txt']=vips_doc_response_txt
        args['vips_doc_resp_code']=vips_doc_resp_code
        
        if vips_doc_status is False:
            return False,args
        else:
            # TODO: get the documentId from the response
            vips_doc_response_txt=json.loads(vips_doc_response_txt)
            vips_doc_id=vips_doc_response_txt.get('document_id')
            args['vips_doc_id']=vips_doc_id
    except Exception as e:
        logging.exception(e)
        return False,args

    return True,args

def prep_vips_payload(**args)->tuple:
    logging.debug("inside prep_vips_payload()")
    logging.debug(args)
    try:
        event_data=args.get('event_data')
        form_data=args.get('form_data')
        user_data=args.get('user_data')
        form_id=args.get('form_id')
        # copy a dict
        tmp_payload=vips_payload.copy()
        logging.debug(tmp_payload)

        # get data from db
        application = args.get('app')
        db = args.get('db')
        with application.app_context():
            # get detachment data
            policeDetatchmentId=''
            agency_name=''
            if "agency" in user_data: 
                logging.debug(user_data["agency"])
                agency_name=user_data["agency"]
                agency_data = db.session.query(AgencyCrossref) \
                    .filter(AgencyCrossref.agency_name == agency_name) \
                    .all()
                logging.debug(agency_data)
                if len(agency_data) == 0:
                    logging.error("agency not found")
                    pass
                else:
                    for a in agency_data:
                        agency_dict = a.__dict__
                        agency_dict.pop('_sa_instance_state', None)
                        logging.debug(agency_dict)
                        policeDetatchmentId=int(agency_dict["vips_policedetachments_agency_id"])
                        break
            tmp_payload["vipsImpoundCreate"]["policeDetatchmentId"]=policeDetatchmentId

        # vipsImpoundCreate payload
        # get jursdiction value
        tmp_jursdiction_val=None
        if "driver_jurisdiction" in event_data:
            application = args.get('app')
            db = args.get('db')
            tmp_jurisdictionvalue=event_data["driver_jurisdiction"]
            with application.app_context():
                # get jurisdiction data
                vips_jurisdiction_code=''
                juris_data = db.session.query(JurisdictionCrossRef) \
                        .filter(JurisdictionCrossRef.jurisdiction_code == tmp_jurisdictionvalue) \
                        .all()
                if len(juris_data) == 0:
                    logging.error("jurisdiction not found")
                else:
                    for j in juris_data:
                        juris_dict = j.__dict__
                        juris_dict.pop('_sa_instance_state', None)
                        vips_jurisdiction_code= juris_dict["vips_jurisdictions_objectCd"]
                        break
                tmp_jursdiction_val=vips_jurisdiction_code
        tmp_payload["vipsImpoundCreate"]["dlJurisdictionCd"]=tmp_jursdiction_val
        # if "driver_jurisdiction" in event_data: tmp_payload["vipsImpoundCreate"]["dlJurisdictionCd"]=event_data["driver_jurisdiction"]

        if "driver_licence_no" in event_data: tmp_payload["vipsImpoundCreate"]["driverLicenceNo"]=event_data["driver_licence_no"]


        # get ilo id from db
        tmp_ilo_id=None
        ilo_id_from_db=event_data.get("impound_lot_operator",None)
        if ilo_id_from_db:
            with application.app_context():
                ilo_data_db = db.session.query(ImpoundLotOperator) \
                    .filter(ImpoundLotOperator.id == ilo_id_from_db) \
                    .all()
                if len(ilo_data_db) == 0:
                    logging.error("ilo db data not found")
                else:
                    for i in ilo_data_db:
                        ilo_dict = i.__dict__
                        ilo_dict.pop('_sa_instance_state', None)
                        tmp_ilo_name=ilo_dict["name"]
                        ilo_cross_ref = db.session.query(IloIdCrossRef) \
                            .filter(IloIdCrossRef.ilo_name == tmp_ilo_name) \
                            .all()
                        if len(ilo_cross_ref) == 0:
                            logging.error("ilo cross ref data not found")
                        else:
                            for c in ilo_cross_ref:
                                ilo_cross_ref_dict = c.__dict__
                                ilo_cross_ref_dict.pop('_sa_instance_state', None)
                                tmp_ilo_id=ilo_cross_ref_dict["vips_impound_lot_operator_id"]
                                break
                        break
        tmp_payload["vipsImpoundCreate"]["impoundLotOperatorId"]=tmp_ilo_id

        # convert impoundment_dt to string
        impoundment_dt=form_data.get("date_of_impound")
        if impoundment_dt is not None:
            impoundment_dt=impoundment_dt.strftime('%Y-%m-%dT%H:%M:%S')
            impoundment_dt=convertDateTimeWithSecs(impoundment_dt)
            tmp_payload["vipsImpoundCreate"]["impoundmentDt"]=impoundment_dt
        
        if "VI_number" in form_data: 
            tmp_vi_number=form_data["VI_number"]
            tmp_vi_number=tmp_vi_number[:-1]
            tmp_payload["vipsImpoundCreate"]["impoundmentNoticeNo"]=tmp_vi_number
        else:
            tmp_payload["vipsImpoundCreate"]["impoundmentNoticeNo"]=""
        
        tmp_payload["vipsImpoundCreate"]["noticeSubjectCd"]="VEHI"

        # get reason codes from DB
        # DONE: Check the reason list
        reason_list=[]
        payload_reason_list=[]
        excessive_speeding=form_data.get("excessive_speed",False)
        street_racing=form_data.get("street_racing",False)
        stunt_driving=form_data.get("stunt_driving",False)
        motor_seating=form_data.get("motorcycle_seating",False)
        motor_restriction=form_data.get("motorcycle_restrictions",False)
        unlicensed=form_data.get("unlicensed",False)
        irp_impound_dur=form_data.get("irp_impound_duration",False)
        prohibited_val=form_data.get("prohibited",False)
        suspended_val=form_data.get("suspended",False)
        if prohibited_val or suspended_val:
            reason_list.append("IDEPPROHIB")
        if excessive_speeding:
            reason_list.append("EXSPEED")
        if street_racing:
            reason_list.append("RACE")
        if stunt_driving:
            reason_list.append("STUNT")
        if motor_seating:
            reason_list.append("SITTING")
        if motor_restriction:
            reason_list.append("MCUNLIC")
        if unlicensed:
            reason_list.append("IDEPUNLIC")
        if irp_impound_dur:
            reason_list.append(irp_impound_dur)
        with application.app_context():
            # get reason data
            for v in reason_list:
                reason_data = db.session.query(ImpoundReasonCodes) \
                    .filter(ImpoundReasonCodes.df_unique_code == v) \
                    .all()
                if len(reason_data) == 0:
                    logging.error("reason not found")
                else:
                    for r in reason_data:
                        reason_dict = r.__dict__
                        reason_dict.pop('_sa_instance_state', None)
                        payload_reason_list.append(reason_dict["vips_value_cd"])
                        break
        tmp_payload["vipsImpoundCreate"]["originalCauseCds"]=payload_reason_list

        # if "notice_type_cd" in form_data: tmp_payload["vipsImpoundCreate"]["noticeTypeCd"]="IMP"
        tmp_payload["vipsImpoundCreate"]["noticeTypeCd"]="IMP"
        # tmp_payload["vipsImpoundCreate"]["policeDetatchmentId"]=policeDetatchmentId
        # if "agency" in user_data: tmp_payload["vipsImpoundCreate"]["policeDetatchmentId"]=user_data["agency"].upper()


        officer_name=f'{user_data["first_name"]} {user_data["last_name"]}'
        tmp_payload["vipsImpoundCreate"]["policeOfficerNm"]=officer_name.upper()
        
        if "badge_number" in user_data: tmp_payload["vipsImpoundCreate"]["policeOfficerNo"]=user_data["badge_number"].upper()  
        if "agency_file_no" in event_data: tmp_payload["vipsImpoundCreate"]["policeFileNo"]=event_data["agency_file_no"]  
        # if "projected_release_dt" in form_data: tmp_payload["vipsImpoundCreate"]["projectedReleaseDt"]=None
        tmp_payload["vipsImpoundCreate"]["projectedReleaseDt"]=None

        # TODO: to confirm
        tmp_payload["vipsImpoundCreate"]["seizureLocationTxt"]=""
        if "offence_city" in form_data: tmp_payload["vipsImpoundCreate"]["seizureLocationTxt"]=form_data["offence_city"].upper()
        
        # vipsRegistrationCreateArray payload
        vipsRegistrationCreateArray=[]
        vipsRegigCreateObj={}
        vips_addr_obj={}
        vipsRegigCreateObj["dataSourceCd"]="VIPS"
        vips_addr_obj["registrationAddressTypeCd"]="RES"

        
        if "regist_owner_first_name" in event_data: vipsRegigCreateObj["firstGivenNm"]=event_data["regist_owner_first_name"].upper()
        if "icbcEnterpriseId" in event_data: vipsRegigCreateObj["icbcEnterpriseId"]=event_data["icbcEnterpriseId"]
        if "regist_owner_last_name" in event_data: vipsRegigCreateObj["surnameNm"]=event_data["regist_owner_last_name"].upper()
        # TODO: to confirm
        if "regist_owner_middle_name" in event_data: vipsRegigCreateObj["secondGivenNm"]=event_data["regist_owner_middle_name"].upper()
        # TODO: to confirm
        if "owned_by_corp" in event_data and event_data["owned_by_corp"] is True:
            if "corporation_name" in event_data and event_data["corporation_name"] is not None: vipsRegigCreateObj["organizationNm"]=event_data["corporation_name"].upper()
            vips_addr_obj["registrationAddressTypeCd"]="BUSI"
        vipsRegigCreateObj["registrationRoleCd"]="REGOWN"
        # if "regist_owner_type" in event_data: tmp_payload["vipsRegistrationCreateArray"]["registrationRoleCd"]=event_data["regist_owner_type"].upper()

        vips_address_array=[]
        
        vips_addr_obj["additionalDeliveryLineTxt"]=""
        if "regist_owner_address" in event_data: vips_addr_obj["addressFirstLineTxt"]=event_data["regist_owner_address"].upper()
        # if "regist_owner_address2" in event_data: vips_addr_obj["addressSecondLineTxt"]=event_data["regist_owner_address2"].upper()
        # if "regist_owner_address3" in event_data: vips_addr_obj["addressThirdLineTxt"]=event_data["regist_owner_address3"].upper()
        if "regist_owner_city" in event_data: vips_addr_obj["cityNm"]=event_data["regist_owner_city"].upper()
        if "regist_owner_postal" in event_data: vips_addr_obj["postalCodeTxt"]=event_data["regist_owner_postal"].upper()
        if "regist_owner_prov" in event_data:
            application = args.get('app')
            db = args.get('db')
            tmp_jurisdictionvalue=event_data["regist_owner_prov"]
            with application.app_context():
                # get jurisdiction data
                juris_data = db.session.query(JurisdictionCrossRef) \
                        .filter(JurisdictionCrossRef.jurisdiction_code == tmp_jurisdictionvalue) \
                        .all()
                if len(juris_data) == 0:
                    logging.error("jurisdiction not found")
                    vips_addr_obj["provinceCd"] = ''
                else:
                    vips_addr_obj["provinceCd"] = juris_data[0].vips_jurisdictions_objectCd
        vips_address_array.append(vips_addr_obj)
        vipsRegigCreateObj["vipsAddressArray"]=vips_address_array

        vips_licence_create_obj={}
        # convert birthdate to string
        birthdate=event_data.get("driver_dob")
        if birthdate is not None:
            # birthdate=datetime.strptime(birthdate, '%Y-%m-%d')
            birthdate= birthdate.strftime('%Y-%m-%d')
            birthdate= convertDateTime(birthdate)
            # birthdate=birthdate.strftime('%Y%m%d')
            vips_licence_create_obj["birthDt"]=birthdate
        # TODO: Confirm this fixes DF-2870 (2023-12-13)
        # if "driver_licence_no" in event_data: vips_licence_create_obj["driverLicenceNo"]=event_data["driver_licence_no"]
        vips_licence_create_obj["driverLicenceNo"]=""
        vips_licence_create_obj["dlJurisdictionCd"]=tmp_jursdiction_val
        # if "driver_jurisdiction" in event_data: vips_licence_create_obj["dlJurisdictionCd"]=event_data["driver_jurisdiction"]
        # vipsRegigCreateObj["vipsLicenceCreateObj"]=vips_licence_create_obj
        
        vipsRegistrationCreateArray.append(vipsRegigCreateObj)
        tmp_payload["vipsRegistrationCreateArray"]=vipsRegistrationCreateArray

        # vipsVehicleCreate payload
        # TODO: to confirm
        # if "nsc_no" in event_data: tmp_payload["vipsVehicleCreate"]["commercialMotorCarrierId"]=event_data["nsc_no"]
        tmp_payload["vipsVehicleCreate"]["commercialMotorCarrierId"]=""
        
        if "vehicle_plate_no" in event_data: tmp_payload["vipsVehicleCreate"]["licencePlateNo"]=event_data["vehicle_plate_no"].upper()
        tmp_payload["vipsVehicleCreate"]["lpDecalValidYy"]=None


        # get vehicle jurisdiction value
        tmp_vehicle_jursdiction_val=None
        if "vehicle_jurisdiction" in event_data:
            application = args.get('app')
            db = args.get('db')
            tmp_vehi_jurisdictionvalue=event_data["vehicle_jurisdiction"]
            with application.app_context():
                # get jurisdiction data
                vips_jurisdiction_code=''
                juris_data = db.session.query(JurisdictionCrossRef) \
                        .filter(JurisdictionCrossRef.jurisdiction_code == tmp_vehi_jurisdictionvalue) \
                        .all()
                if len(juris_data) == 0:
                    logging.error("jurisdiction not found")
                else:
                    for j in juris_data:
                        juris_dict = j.__dict__
                        juris_dict.pop('_sa_instance_state', None)
                        vips_jurisdiction_code= juris_dict["vips_jurisdictions_objectCd"]
                        break
                tmp_vehicle_jursdiction_val=vips_jurisdiction_code
        tmp_payload["vipsVehicleCreate"]["lpJurisdictionCd"]=tmp_vehicle_jursdiction_val

        # if "vehicle_jurisdiction" in event_data: tmp_payload["vipsVehicleCreate"]["lpJurisdictionCd"]=event_data["vehicle_jurisdiction"]




        if "vehicle_registration_no" in event_data: tmp_payload["vipsVehicleCreate"]["registrationNo"]=event_data["vehicle_registration_no"].upper()

        if "vehicle_year" in event_data: tmp_payload["vipsVehicleCreate"]["manufacturedYy"]=event_data["vehicle_year"]

        # get nsc jurisdiction value
        tmp_nsc_jursdiction_val=None
        if "nsc_prov_state" in event_data:
            application = args.get('app')
            db = args.get('db')
            tmp_nsc_jurisdictionvalue=event_data["nsc_prov_state"]
            with application.app_context():
                # get jurisdiction data
                vips_jurisdiction_code=''
                juris_data = db.session.query(JurisdictionCrossRef) \
                        .filter(JurisdictionCrossRef.jurisdiction_code == tmp_nsc_jurisdictionvalue) \
                        .all()
                if len(juris_data) == 0:
                    logging.error("jurisdiction not found")
                else:
                    for j in juris_data:
                        juris_dict = j.__dict__
                        juris_dict.pop('_sa_instance_state', None)
                        vips_jurisdiction_code= juris_dict["vips_jurisdictions_objectCd"]
                        break
                tmp_nsc_jursdiction_val=vips_jurisdiction_code
        tmp_payload["vipsVehicleCreate"]["nscJurisdictionTxt"]=tmp_nsc_jursdiction_val

        # if "nsc_prov_state" in event_data: tmp_payload["vipsVehicleCreate"]["nscJurisdictionTxt"]=event_data["nsc_prov_state"].upper()
        # tmp_payload["vipsVehicleCreate"]["nscJurisdictionTxt"]=None
        if "vehicle_colour" in event_data: 
            tmp_vehicle_color=event_data["vehicle_colour"].upper()
            tmp_vehicle_color=tmp_vehicle_color.replace("{","")
            tmp_vehicle_color=tmp_vehicle_color.replace("}","")
            tmp_payload["vipsVehicleCreate"]["vehicleColourTxt"]=tmp_vehicle_color

        if "vehicle_vin_no" in event_data: tmp_payload["vipsVehicleCreate"]["vehicleIdentificationNo"]=event_data["vehicle_vin_no"].upper()  
        

        if "vehicle_mk_md" in event_data: 
            mk, md = event_data["vehicle_mk_md"].split("-")
            tmp_payload["vipsVehicleCreate"]["vehicleModelTxt"]=md.upper()
            tmp_payload["vipsVehicleCreate"]["vehicleMakeTxt"]=mk.upper()  

        if "vehicle_style" in event_data: tmp_payload["vipsVehicleCreate"]["vehicleStyleTxt"]=event_data["vehicle_style"].upper()  
        if "vehicle_type" in event_data: 
            if event_data["vehicle_type"] == None:
                tmp_payload["vipsVehicleCreate"]["vehicleTypeCd"]=""
            else:
                tmp_payload["vipsVehicleCreate"]["vehicleTypeCd"]=event_data["vehicle_type"]
                # tmp_payload["vipsVehicleCreate"]["vehicleTypeCd"]=str(event_data["vehicle_type"])

        # vipsDocumentIdArray payload
        vipsDocumentIdArray=[]
        if "vips_doc_id" in args: vipsDocumentIdArray.append(args["vips_doc_id"])
        tmp_payload["vipsDocumentIdArray"]=vipsDocumentIdArray


        # vipsImpoundmentArray payload
        vipsImpoundmentArray=[]
        # if "VI_number" in form_data: vipsImpoundmentArray.append(form_data["VI_number"])
        tmp_payload["vipsImpoundmentArray"]=vipsImpoundmentArray

        args['vips_payload']=tmp_payload
        logging.debug(tmp_payload)
    except Exception as e:
        logging.exception(e)
        logging.error(tmp_payload)
        return False,args

    return True,args

def create_vips_impoundment(**args)->tuple:
    logging.debug("inside create_vips_impoundment()")
    logging.debug(args)
    try:
        vips_payload=args.get('vips_payload')
        logging.debug('This is the payload sent to VIPS')
        logging.debug(json.dumps(vips_payload))
        vips_status, vips_response_txt, vips_resp_code = create_vips_imp(vips_payload,logging)
        args['vips_response_txt']=vips_response_txt
        args['vips_resp_code']=vips_resp_code
        
        if vips_status is False:
            return False,args
    except Exception as e:
        logging.exception(e)
        return False,args

    return True,args

def update_event_status(**args)->tuple:
    logging.debug("inside update_event_status()")
    logging.debug(args)
    try:
        application=args.get('app')
        db=args.get('db')
        event_id=args.get('event_data').get('event_id')
        event_type=args.get('event_type')
        with application.app_context():
            if event_type=='vi':
                event = db.session.query(Event) \
                    .filter(Event.event_id == event_id) \
                    .one()
                event.vi_sent_status = 'sent'
                db.session.commit()
            elif event_type=='irp':
                pass
            elif event_type=='24h' or event_type=='12h':
                event = db.session.query(Event) \
                    .filter(Event.event_id == event_id) \
                    .one()
                event.icbc_sent_status = 'sent'
                db.session.commit()
    except Exception as e:
        logging.exception(e)
        return False,args
    return True,args

def update_event_status_hold(**args)->tuple:
    logging.debug("inside update_event_status_hold()")
    logging.debug(args)
    try:
        application=args.get('app')
        db=args.get('db')
        message=args.get('message')
        event_id=message.get('event_id') if message else args.get('event_id')
        event_type=message.get('event_type') if message else args.get('event_type')
        with application.app_context():
            if event_type=='vi':
                event = db.session.query(Event) \
                    .filter(Event.event_id == event_id) \
                    .one()
                event.vi_sent_status = 'retrying'
                db.session.commit()
            elif event_type=='irp':
                pass
            elif event_type=='24h' or event_type=='12h':
                event = db.session.query(Event) \
                    .filter(Event.event_id == event_id) \
                    .one()
                event.icbc_sent_status = 'retrying'
                db.session.commit()
            # Directly call record_event_error
            error_args = {
                'error': {
                    'error_code': ErrorCode.E06,
                    'error_details': f'Holding a event_id: {event_id}, event_type:{event_type}',
                    'event_id': event_id,
                    'event_type': event_type,
                    'func': update_event_status_hold,
                },
                'message': args.get('message', {}),
                'app': application
            }
            record_event_error(**error_args)
    except Exception as e:
        logging.exception(e)
        # Directly call record_event_error
        error_args = {
            'error': {
                'error_code': ErrorCode.E06,
                'error_details': e,
                'event_id': event_id,
                'event_type': event_type,
                'func': update_event_status_hold,
            },
            'message': args.get('message', {}),
            'app': application
        }
        record_event_error(**error_args)
        return False,args
    return True,args

def update_event_status_error(**args)->tuple:
    logging.debug("inside update_event_status_error()")
    logging.debug(args)
    try:
        application=args.get('app')
        db=args.get('db')
        event_id=args.get('event_data').get('event_id')
        event_type=args.get('event_type')
        with application.app_context():
            if event_type=='vi':
                event = db.session.query(Event) \
                    .filter(Event.event_id == event_id) \
                    .one()
                event.vi_sent_status = 'error'
                db.session.commit()
            elif event_type=='irp':
                pass
            elif event_type=='24h' or event_type=='12h':
                event = db.session.query(Event) \
                    .filter(Event.event_id == event_id) \
                    .one()
                event.icbc_sent_status = 'error'
                db.session.commit()
                
            # Directly call record_event_error
            error_args = {
                'error': {
                    'error_code': ErrorCode.E07,
                    'error_details': f'Failed to process {event_type} event',
                    'event_id': event_id,
                    'event_type': event_type,
                    'func': update_event_status_error,
                },
                'message': args.get('message', {}),
                'app': application
            }
            record_event_error(**error_args)
    except Exception as e:
        logging.exception(e)
        # If an exception occurs, record it as an error
        error_args = {
            'error': {
                'error_code': ErrorCode.E07,
                'error_details': e,
                'event_id': event_id,
                'event_type': event_type,
                'func': update_event_status_error,
            },
            'message': args.get('message', {}),
            'app': application
        }
        record_event_error(**error_args)
        return False,args
    return True,args


def update_event_status_error_retry(**args)->tuple:
    logging.debug("inside update_event_status_error_retry()")
    logging.debug(args)
    try:
        application=args.get('app')
        db=args.get('db')
        message = args.get('message')
        event_id=message.get('event_id')
        event_type=message.get('event_type')
        stop_retry_flg=args.get('stop_retry_flg',False)
        with application.app_context():
            if event_type=='vi':
                event = db.session.query(Event) \
                    .filter(Event.event_id == event_id) \
                    .one()
                if stop_retry_flg is True:
                    event.vi_sent_status = 'error'
                else:
                    event.vi_sent_status = 'retrying'
                db.session.commit()
            elif event_type=='irp':
                pass
            elif event_type=='24h' or event_type=='12h':
                event = db.session.query(Event) \
                    .filter(Event.event_id == event_id) \
                    .one()
                if stop_retry_flg is True:
                    event.icbc_sent_status = 'error'
                else:
                    event.icbc_sent_status = 'retrying'
                db.session.commit()
    except Exception as e:
        logging.exception(e)
        return False,args
    return True,args

def add_to_persistent_failed_queue(**args)->tuple:
    logging.debug("inside add_to_persistent_failed_queue()")
    logging.debug(args)
    try:
        config = args.get('config')
        message = args.get('message')
        message['queue_name'] = config.STORAGE_FAIL_QUEUE_PERS
        writer = args.get('writer')
        logging.debug('add_to_hold_queue(): {}'.format(json.dumps(message)))
        if not writer.publish(config.STORAGE_FAIL_QUEUE_PERS, encode_message(message, config.ENCRYPT_KEY)):
            # Set error in args to get consumed by the record_event_error function
            args['error'] = {
                'error_code': ErrorCode.E03,
                'error_details': 'unable to write to RabbitMQ {} queue'.format(config.STORAGE_FAIL_QUEUE_PERS),
                'event_id': message.get('event_id'),
                'event_type': message.get('event_type'),
                'func': add_to_persistent_failed_queue,
                'payload': message,
            }
            logging.critical('unable to write to RabbitMQ {} queue'.format(config.STORAGE_FAIL_QUEUE_PERS))
            return False, args
    except Exception as e:
        logging.exception(e)
        # Set error in args to get consumed by the record_event_error function
        message = args.get('message')
        args['error'] = {
            'error_code': ErrorCode.E03,
            'error_details': e,
            'event_id': message.get('event_id'),
            'event_type': message.get('event_type'),
            'func': add_to_persistent_failed_queue,
            'payload': message,
        }
        return False, args
    return True, args

def add_to_transient_failed_queue(**args)->tuple:
    logging.debug("inside add_to_transient_failed_queue()")
    logging.debug(args)
    try:
        config = args.get('config')
        message = args.get('message')
        message['queue_name'] = config.STORAGE_FAIL_QUEUE
        writer = args.get('writer')
        logging.debug('add_to_transient_failed_queue(): {}'.format(json.dumps(message)))
        if not writer.publish(config.STORAGE_FAIL_QUEUE, encode_message(message, config.ENCRYPT_KEY)):
            logging.critical('unable to write to RabbitMQ {} queue'.format(config.STORAGE_FAIL_QUEUE))
            return False, args
    except Exception as e:
        logging.exception(e)
        return False, args
    return True, args

def add_to_hold_queue(**args)->tuple:
    logging.debug("inside add_to_hold_queue()")
    logging.debug(args)
    try:
        config = args.get('config')
        message = args.get('message')
        message['queue_name'] = config.STORAGE_HOLD_QUEUE
        writer = args.get('writer')
        logging.debug('add_to_hold_queue(): {}'.format(json.dumps(message)))
        if not writer.publish(config.STORAGE_HOLD_QUEUE, encode_message(message, config.ENCRYPT_KEY)):
            logging.critical('unable to write to RabbitMQ {} queue'.format(config.STORAGE_HOLD_QUEUE))
            return False, args
    except Exception as e:
        logging.exception(e)
        return False, args
    return True, args


def add_to_retry_queue(**args)->tuple:
    logging.debug("inside add_to_retry_queue()")
    logging.debug(args)
    try:    
        config = args.get('config')
        message = args.get('message')
        put_to_queue_name=args.get('put_to_queue_name',None)
        writer = args.get('writer')
        logging.debug('add_to_retry_queue(): {}'.format(json.dumps(message)))
        if put_to_queue_name is None:
            put_to_queue_name=config.STORAGE_HOLD_QUEUE
            args['message']['queue_name']=config.STORAGE_HOLD_QUEUE
        else:
            args['message']['queue_name']=put_to_queue_name         
        if not writer.publish(put_to_queue_name, encode_message(message, config.ENCRYPT_KEY)):
            logging.critical('unable to write to RabbitMQ {} queue'.format(put_to_queue_name))
            # If an exception occurs, record it as an error
            error_args = {
                'error': {
                    'error_code': ErrorCode.E03,
                    'error_details': 'unable to write to RabbitMQ {} queue'.format(put_to_queue_name),
                    'event_id': message.get('event_id'),
                    'event_type': message.get('event_type'),
                    'func': add_to_retry_queue,
                },
                'message': args.get('message', {}),
                'app': args.get('app')
            }
            record_event_error(**error_args)
            return False, args
    except Exception as e:
        logging.exception(e)
        return False, args
    return True, args



def add_unknown_event_error_to_message(**args)->tuple:
    logging.debug("inside add_unknown_event_error_to_message()")
    logging.debug(args)
    try:
        message = args.get('message')
        tmp_key = message.get('Key', None)
        args['storage_key'] = tmp_key
    except Exception as e:
        logging.exception(e)
        return False, args
    return True,args

def add_unknown_event_to_error(**args)->tuple:
    logging.debug("inside add_unknown_event_error()")
    logging.debug(args)
    try:
        message = args.get('message')
        args['error'] = {
            'error_code': ErrorCode.E04,
            'error_details': 'Critical Error: Unknown Event Type',
            'event_id': message.get('event_id'),
            'event_type': message.get('event_type'),
            'func': add_unknown_event_to_error,
            'payload': message,
        }
    except Exception as e:
        logging.exception(e)
        return False, args
    return True,args

def record_event_error(**args):
    """
    Record an error that occurred during event processing.
    
    Args:
        **args: Additional keyword arguments, including event_id and event_type.
    """
    

    try:
        error = args.get('error')
        message = args.get('message')
        
        application = args.get('app')
        with application.app_context():
            if error is None:
                error_obj = {
                    'error_code': ErrorCode.E08,
                    'error_details': message.get('error_message',  'Unknown error'),
                    'event_id': message.get('event_id'),
                    'event_type': message.get('event_type'),
                    'payload': json.dumps(message) if message else None,
                    'func': record_event_error,
                }
            else:
                error_obj = {
                    'error_code': error.get('error_code'),
                    'error_details': error.get('error_details'),
                    'event_id': error.get('event_id'),
                    'event_type': error.get('event_type'),
                    'payload': json.dumps(message) if message else None,
                    'ticket_no': error.get('ticket_no'),
                    'func': error.get('func'),
                }
            
            record_error(**error_obj)
        return True, args
    except Exception as e:
        # If recording the error itself fails, log it
        logging.error(f"Failed to record error: {str(e)}")
    return True, args


def get_event_coordinates(**args)->tuple:
    logging.debug("inside get_event_coordinates()")
    try:
        address = args['event_data']['intersection_or_address_of_offence']
        city = form_middleware.get_city_name(args['event_data']['offence_city'], args)

        geocoding_status, latitude, longitude, full_address = get_coordinates(address, city)
        args['event_data']['latitude'] = latitude
        args['event_data']['longitude'] = longitude
        args['event_data']['full_address'] = full_address
        args['event_data']['requested_address'] = f'{address}, {city}'

    except Exception as e:
        logging.error(f'Error getting coordinates: {e}')
        args['error'] = {
                'error_code': ErrorCode.L01,
                'error_details': e,
                'event_type': args['message']['event_type'],
                'func': get_event_coordinates,
                'event_id': args['message']['event_id']
            }
        record_event_error(**args)

    # Always return True to continue processing even if not able to get coordinates
    return True, args