import json
import csv
import pytz
import logging
import logging.config
from python.form_handler.config import Config
from cerberus import Validator
import base64
from cerberus import errors
import logging
import json
from datetime import datetime
from minio import Minio
from minio.error import S3Error
from python.form_handler.models import Event,FormStorageRefs,VIForm,TwentyFourHourForm,TwelveHourForm,IRPForm,User
from python.form_handler.icbc_service import submit_to_icbc
from python.form_handler.vips_service import create_vips_doc,create_vips_imp
from python.form_handler.payloads import vips_payload,vips_document_payload
from python.form_handler.message import encode_message
from python.form_handler.helper import method2_decrypt

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
                event_type=f.form_type
                args['event_type']=event_type
                form_dict=f.__dict__
                form_dict.pop('_sa_instance_state',None)
                args['storage_ref']=form_dict
        # args['event_type']=storage_key
    except Exception as e:
        logging.error(e)
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
        logging.error(e)
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
        logging.error(e)
        return False, args
    return True,args


def validate_event_retry_count(**args)->tuple:
    logging.info("inside validate_event_retry_count()")
    logging.debug(args)
    # DONE: if event retry count is more than 10
    try:
        retry_count=0
        event_type=args.get('event_type')
        if event_type=='vi':
            retry_count=args.get('event_data').get('vi_retry_count')
        elif event_type=='irp':
            pass
        elif event_type=='24h':
            retry_count=args.get('event_data').get('icbc_retry_count')
        elif event_type=='12h':
            retry_count=args.get('event_data').get('icbc_retry_count')
        else:
            return False,args
        if retry_count >= Config.SYSTEM_RECORD_MAX_RETRIES:
            return False,args
    except Exception as e:
        logging.error(e)
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
        logging.error(e)
        return False,args
    return True,args


def get_storage_file(**args)->tuple:
    logging.debug("inside get_storage_file()")
    logging.debug(args)
    minio_host=f'{Config.STORAGE_HOST}:{Config.STORAGE_PORT}'
    storage_key=args.get('storage_ref').get('storage_key')
    encryptivkey=args.get('storage_ref').get('encryptiv')
    bucket_name=storage_key.split('/')[0]
    storage_file_name=storage_key.split('/')[1]
    try:
        client = Minio(
            minio_host,
            access_key=Config.STORAGE_ACCESS_KEY,
            secret_key=Config.STORAGE_SECRET_KEY,
            secure=False
        )
        file_data=client.get_object(bucket_name,storage_file_name)
        # convert file_data to utf-8
        # file_data=file_data.decode('utf-8')
        # print(file_data)


        file_data_content = file_data.data
        # with open("abcd12344.pdf", 'wb') as file_data1:
        #     file_data1.write(file_data_content)
        # logging.debug(file_data_content)
        # logging.debug(type(file_data_content))
        # print('encodedfile: ', base64.b64encode(file_data_content))

        # bytes to string
        # file_data_content=base64.b64encode(file_data_content).decode('utf-8')
        # logging.debug(file_data_content)
        # logging.debug(type(file_data_content))
        # logging.debug(args.get('storage_ref'))
        # logging.debug(encryptivkey)
        decrypted_data=method2_decrypt(file_data_content,encryptivkey)
        # logging.debug(decrypted_data)
        # logging.debug(type(decrypted_data))
        # with open("abcd125554.pdf", 'wb') as file_data1:
        #     file_data1.write(base64.b64decode(decrypted_data))
        

        # base64 encode string the data
        # file_data_content = base64.b64encode(file_data_content)
        # file_data_content = base64.b64encode(file_data_content).decode('utf-8')
        # args['file_data']=file_data_content
        # print(type(file_data_content))
        # print(file_data_content)
        args['file_data'] = decrypted_data
        

        # save the file_data_content to a pdf file  
        # with open('mytest.pdf', 'wb') as file_data1:
        #     file_data1.write(base64.b64decode(file_data_content))



        # You can save the content to a file or process it further
        # with open('downloaded_file.pdf', 'wb') as file:
        #     file.write(base64.b64decode(file_data_content))


        # save the data as pdf
        # with open('test.pdf', 'wb') as file_data1:
        #     for d in file_data.stream(32*1024):
        #         print(d)
        #         file_data1.write(d)
        #         # file_data.flush()
       
        logging.debug(file_data)
    except Exception as e:
        logging.error(e)
        return False,args
    finally:
        file_data.close()
        file_data.release_conn()
    return True,args


def prep_icbc_payload(**args)->tuple:
    logging.debug("inside prep_icbc_payload()")
    logging.debug(args)

    try:
        pdf_data=args.get('file_data')
        event_data=args.get('event_data')
        form_data=args.get('form_data')
        user_data=args.get('user_data')
        form_id=args.get('form_id')
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
        "section": "215.2",
        "violationLocation": "",
        "noticeNumber": form_id,
        "violationDate": "",
        "violationTime": "",
        "officerDetachment": "",        
        "officerNumber": "",
        "officerName": "",
        "pdf": pdf_data,        
        }

        # if "form_id" in form_data: tmp_payload["noticeNumber"]=event_data["form_id"]

        if "driver_licence_no" in event_data: tmp_payload["dlNumber"]=event_data["driver_licence_no"]
        if "driver_jurisdiction" in event_data:
            tmp_payload["dlJurisdiction"]=event_data["driver_jurisdiction"]
        
        if "driver_last_name" in  event_data: tmp_payload["lastName"]=event_data["driver_last_name"].upper()
        if "driver_given_name" in event_data: tmp_payload["firstName"]=event_data["driver_given_name"].upper()

        # convert birthdate to string
        birthdate=event_data.get("driver_dob")
        if birthdate is not None:
            # birthdate=datetime.strptime(birthdate, '%Y-%m-%d')
            birthdate= birthdate.strftime('%Y-%m-%d')
            # birthdate=birthdate.strftime('%Y%m%d')
            tmp_payload["birthdate"]=birthdate
            

        # if "driver_dob" in event_data: tmp_payload["birthdate"]=event_data["driver_dob"]

        if "vehicle_jurisdiction" in event_data : 
            tmp_payload["plateJurisdiction"]=event_data["vehicle_jurisdiction"]

        if "vehicle_plate_no" in event_data: tmp_payload["plateNumber"]=event_data["vehicle_plate_no"].upper()

        # if "puj_code" in data and "objectCd" in data["puj_code"]: 
        #     payload["pujCode"]=data["puj_code"]["objectCd"]  

        #Some validation required for NSC-Number. ICBC does not accept all values.
        if "nsc_no" in event_data: tmp_payload["nscNumber"]=event_data["nsc_no"]

        if "offence_city" in form_data:
            tmp_payload["violationLocation"]=form_data["offence_city"].upper()

        # if "prohibitionStartDate" in data: payload["violationDate"]=data["prohibitionStartDate"]
        # if "prohibitionStartTime" in data: payload["violationTime"]=data["prohibitionStartTime"]
        # convert date_of_driving to string
        date_of_driving=event_data.get("date_of_driving")
        if date_of_driving is not None:
            # date_of_driving=datetime.strptime(date_of_driving, '%Y-%m-%d')
            date_of_driving=date_of_driving.strftime('%Y-%m-%d')
            tmp_payload["violationDate"]=date_of_driving
        # if "date_of_driving" in event_data: tmp_payload["violationDate"]=event_data["date_of_driving"]
        if "time_of_driving" in event_data: tmp_payload["violationTime"]=event_data["time_of_driving"]

        # TODO: get agency from user table for the event
        if "agency" in user_data: tmp_payload["officerDetachment"]=user_data["agency"].upper()

        #DONE -- Need to add agency name abbr to the begining of officerNumber
        # if "badge_number" in user_data: tmp_payload["officerNumber"]="AB"+ data["badge_number"]
        if "badge_number" in user_data: tmp_payload["officerNumber"]=user_data["badge_number"]

        officer_name=f'{user_data["first_name"]} {user_data["last_name"]}'
        tmp_payload["officerName"]=officer_name.upper()
        # if "officer_name" in data: payload["officerName"]=data["officer_name"].upper()

        args['icbc_payload']=tmp_payload
    except Exception as e:
        logging.error(e)
        return False,args
    
    return True,args

def send_to_icbc(**args)->tuple:
    logging.debug("inside send_to_icbc()")
    logging.debug(args)
    try:
        logging.debug(args['icbc_payload'])
        icbc_payload=args.get('icbc_payload')
        send_status, icbc_response_txt,icbc_resp_code = submit_to_icbc(icbc_payload)
        args['icbc_response_txt']=icbc_response_txt
        args['icbc_resp_code']=icbc_resp_code
        if send_status is False:
            return False,args
    except Exception as e:
        logging.error(e)
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

        subject_cd="PERS"

        if "owned_by_corp" in event_data and event_data["owned_by_corp"] is True:
            subject_cd="CORP"
        tmp_payload["notice_subject_code"]=subject_cd

        tmp_payload["file_object"]=pdf_data

        # TODO: to confirm
        if "type_cd" in form_data: tmp_payload["type_code"]=form_data["type_cd"]

        tmp_payload["pageCount"]=1
        tmp_payload["mime_sub_type"]="pdf"
        tmp_payload["mime_type"]="application"

        # TODO: to confirm
        tmp_payload["notice_type_code"]="IMP"
        # if "notice_type_cd" in form_data: tmp_payload["notice_type_code"]=form_data["notice_type_cd"]

        args['vips_document_payload']=tmp_payload
    except Exception as e:
        logging.error(e)
        return False,args
    return True,args

def create_vips_document(**args)->tuple:
    logging.debug("inside create_vips_document()")
    logging.debug(args)
    try:
        vips_document_payload=args.get('vips_document_payload')
        vips_doc_status, vips_doc_response_txt, vips_doc_resp_code = create_vips_doc(vips_document_payload)
        args['vips_doc_response_txt']=vips_doc_response_txt
        args['vips_doc_resp_code']=vips_doc_resp_code
        
        if vips_doc_status is False:
            return False,args
        else:
            # TODO: get the documentId from the response
            vips_doc_response_txt=json.loads(vips_doc_response_txt)
            vips_doc_id=vips_doc_response_txt.get('documentId')
            args['vips_doc_id']=vips_doc_id
    except Exception as e:
        logging.error(e)
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

        # vipsImpoundCreate payload
        if "driver_jurisdiction" in event_data: tmp_payload["vipsImpoundCreate"]["dlJurisdictionCd"]=event_data["driver_jurisdiction"]
        if "driver_licence_no" in event_data: tmp_payload["vipsImpoundCreate"]["driverLicenceNo"]=event_data["driver_licence_no"]
        
        # TODO: to confirm
        # if "impound_lot_operator_id" in form_data: tmp_payload["vipsImpoundCreate"]["impoundLotOperatorId"]=form_data["impound_lot_operator_id"]

        # convert impoundment_dt to string
        impoundment_dt=form_data.get("date_of_impound")
        if impoundment_dt is not None:
            # impoundment_dt=datetime.strptime(impoundment_dt, '%Y-%m-%d')
            impoundment_dt=impoundment_dt.strftime('%Y-%m-%dT%H:%M:%S')
            tmp_payload["vipsImpoundCreate"]["impoundmentDt"]=impoundment_dt
        

        if "form_id" in form_data: tmp_payload["vipsImpoundCreate"]["impoundmentNoticeNo"]=form_data["form_id"]
        
        # TODO: to confirm
        if "impoundment_release_dt" in form_data: tmp_payload["vipsImpoundCreate"]["impoundmentReleaseDt"]=form_data["impoundment_release_dt"]
        
        # TODO: to confirm
        subject_cd="PERS"

        if "owned_by_corp" in event_data and event_data["owned_by_corp"] is True:
            subject_cd="CORP"
        tmp_payload["vipsImpoundCreate"]["noticeSubjectCd"]=subject_cd
        # if "notice_subject_cd" in form_data: tmp_payload["vipsImpoundCreate"]["noticeSubjectCd"]=form_data["notice_subject_cd"]

        # TODO: to confirm
        if "notice_type_cd" in form_data: tmp_payload["vipsImpoundCreate"]["noticeTypeCd"]=form_data["notice_type_cd"]

        # TODO: to confirm (originalCauseCds)  

        # TODO: to confirm
        if "agency" in user_data: tmp_payload["vipsImpoundCreate"]["policeDetatchmentId"]=user_data["agency"].upper()


        officer_name=f'{user_data["first_name"]} {user_data["last_name"]}'
        tmp_payload["vipsImpoundCreate"]["policeOfficerNm"]=officer_name.upper()
        
        if "badge_number" in user_data: tmp_payload["vipsImpoundCreate"]["policeOfficerNo"]=user_data["badge_number"].upper()  

        # TODO: to confirm
        if "form_id" in form_data: tmp_payload["vipsImpoundCreate"]["policeFileNo"]=form_data["form_id"]  
        
        # TODO: to confirm
        if "projected_release_dt" in form_data: tmp_payload["vipsImpoundCreate"]["projectedReleaseDt"]=form_data["projected_release_dt"]

        # TODO: to confirm
        if "offence_city" in form_data: tmp_payload["vipsImpoundCreate"]["seizureLocationTxt"]=form_data["offence_city"].upper()
        
        # TODO: to confirm
        if "vehicle_returned_dt" in form_data: tmp_payload["vipsImpoundCreate"]["vehicleReturnedDt"]=form_data["vehicle_returned_dt"]



        # vipsRegistrationCreateArray payload
        vipsRegistrationCreateArray=[]
        vipsRegigCreateObj={}
        vipsRegigCreateObj["dataSourceCd"]="VIPS"

        
        if "regist_owner_first_name" in event_data: vipsRegigCreateObj["firstGivenNm"]=event_data["regist_owner_first_name"].upper()
        
        if "regist_owner_last_name" in event_data: vipsRegigCreateObj["surnameNm"]=event_data["regist_owner_last_name"].upper()
        # TODO: to confirm
        
        if "regist_owner_middle_name" in event_data: vipsRegigCreateObj["secondGivenNm"]=event_data["regist_owner_middle_name"].upper()

        # TODO: to confirm
        
        if "owned_by_corp" in event_data and event_data["owned_by_corp"] is True:
            if "corporation_name" in event_data and event_data["corporation_name"] is not None: vipsRegigCreateObj["organizationNm"]=event_data["corporation_name"].upper()

        # TODO: to confirm
        
        if "icbcEnterpriseId" in event_data: vipsRegigCreateObj["icbcEnterpriseId"]=event_data["icbcEnterpriseId"].upper()

        # TODO: to confirm
        vipsRegigCreateObj["registrationRoleCd"]="REGOWN"
        # if "regist_owner_type" in event_data: tmp_payload["vipsRegistrationCreateArray"]["registrationRoleCd"]=event_data["regist_owner_type"].upper()

        vips_address_array=[]
        vips_addr_obj={}
        vips_addr_obj["additionalDeliveryLineTxt"]=""
        if "regist_owner_address" in event_data: vips_addr_obj["addressFirstLineTxt"]=event_data["regist_owner_address"].upper()
        # if "regist_owner_address2" in event_data: vips_addr_obj["addressSecondLineTxt"]=event_data["regist_owner_address2"].upper()
        # if "regist_owner_address3" in event_data: vips_addr_obj["addressThirdLineTxt"]=event_data["regist_owner_address3"].upper()
        if "regist_owner_city" in event_data: vips_addr_obj["cityNm"]=event_data["regist_owner_city"].upper()
        vips_addr_obj["countryNm"]="CANADA"
        if "regist_owner_postal" in event_data: vips_addr_obj["postalCodeTxt"]=event_data["regist_owner_postal"].upper()
        if "regist_owner_prov" in event_data: vips_addr_obj["provinceCd"]=event_data["regist_owner_prov"].upper()
        # TODO: to confirm
        vips_addr_obj["registrationAddressTypeCd"]="MAIL"
        vips_address_array.append(vips_addr_obj)
        vipsRegigCreateObj["vipsAddressArray"]=vips_address_array

        vips_licence_create_obj={}
        # convert birthdate to string
        birthdate=event_data.get("driver_dob")
        if birthdate is not None:
            # birthdate=datetime.strptime(birthdate, '%Y-%m-%d')
            birthdate= birthdate.strftime('%Y-%m-%d')
            # birthdate=birthdate.strftime('%Y%m%d')
            vips_licence_create_obj["birthDt"]=birthdate

        if "driver_licence_no" in event_data: vips_licence_create_obj["driverLicenceNo"]=event_data["driver_licence_no"]
        if "driver_jurisdiction" in event_data: vips_licence_create_obj["dlJurisdictionCd"]=event_data["driver_jurisdiction"]
        # vipsRegigCreateObj["vipsLicenceCreateObj"]=vips_licence_create_obj

        # vipsVehicleCreate payload
        # TODO: to confirm
        if "commercial_motor_carrier_id" in event_data: tmp_payload["vipsVehicleCreate"]["commercialMotorCarrierId"]=event_data["commercial_motor_carrier_id"]
        
        if "vehicle_plate_no" in event_data: tmp_payload["vipsVehicleCreate"]["licencePlateNo"]=event_data["vehicle_plate_no"].upper()

        # TODO: to confirm
        if "vehicle_plate_expiry" in event_data: tmp_payload["vipsVehicleCreate"]["lpDecalValidYy"]=event_data["vehicle_plate_expiry"]

        if "vehicle_jurisdiction" in event_data: tmp_payload["vipsVehicleCreate"]["lpJurisdictionCd"]=event_data["vehicle_jurisdiction"]

        if "vehicle_registration_no" in event_data: tmp_payload["vipsVehicleCreate"]["registrationNo"]=event_data["vehicle_registration_no"].upper()

        if "vehicle_year" in event_data: tmp_payload["vipsVehicleCreate"]["manufacturedYy"]=event_data["vehicle_year"]

        if "nsc_prov_state" in event_data: tmp_payload["vipsVehicleCreate"]["nscJurisdictionTxt"]=event_data["nsc_prov_state"].upper()

        if "vehicle_vin_no" in event_data: tmp_payload["vipsVehicleCreate"]["vehicleIdentificationNo"]=event_data["vehicle_vin_no"].upper()  

        if "vehicle_mk_md" in event_data: tmp_payload["vipsVehicleCreate"]["vehicleMakeTxt"]=event_data["vehicle_mk_md"].upper()  

        if "vehicle_mk_md" in event_data: tmp_payload["vipsVehicleCreate"]["vehicleModelTxt"]=event_data["vehicle_mk_md"].upper()  

        if "vehicle_style" in event_data: tmp_payload["vipsVehicleCreate"]["vehicleStyleTxt"]=event_data["vehicle_style"].upper()  

        # TODO: to confirm
        if "vehicle_type" in event_data: tmp_payload["vipsVehicleCreate"]["vehicleTypeCd"]=event_data["vehicle_type"].upper()  

        # vipsDocumentIdArray payload
        vipsDocumentIdArray=[]
        if "vips_doc_id" in args: vipsDocumentIdArray.append(args["vips_doc_id"])
        tmp_payload["vipsDocumentIdArray"]=vipsDocumentIdArray


        # vipsImpoundmentArray payload
        vipsImpoundmentArray=[]
        if "VI_number" in form_data: vipsImpoundmentArray.append(form_data["VI_number"])
        tmp_payload["vipsImpoundmentArray"]=vipsImpoundmentArray

        args['vips_payload']=tmp_payload
    except Exception as e:
        logging.error(e)
        logging.error(tmp_payload)
        return False,args

    return True,args

def create_vips_impoundment(**args)->tuple:
    logging.debug("inside create_vips_impoundment()")
    logging.debug(args)
    try:
        vips_payload=args.get('vips_payload')
        vips_status, vips_response_txt, vips_resp_code = create_vips_imp(vips_payload)
        args['vips_response_txt']=vips_response_txt
        args['vips_resp_code']=vips_resp_code
        
        if vips_status is False:
            return False,args
    except Exception as e:
        logging.error(e)
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
        logging.error(e)
        return False,args
    return True,args

def update_event_status_hold(**args)->tuple:
    logging.debug("inside update_event_status_hold()")
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
    except Exception as e:
        logging.error(e)
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
    except Exception as e:
        logging.error(e)
        return False,args
    return True,args

def add_to_persistent_failed_queue(**args)->tuple:
    logging.debug("inside add_to_persistent_failed_queue()")
    logging.debug(args)
    try:
        config = args.get('config')
        message = args.get('message')
        writer = args.get('writer')
        logging.debug('add_to_hold_queue(): {}'.format(json.dumps(message)))
        if not writer.publish(config.STORAGE_FAIL_QUEUE_PERS, encode_message(message, config.ENCRYPT_KEY)):
            logging.critical('unable to write to RabbitMQ {} queue'.format(config.STORAGE_FAIL_QUEUE_PERS))
            return False, args
    except Exception as e:
        logging.error(e)
        return False, args
    return True, args

def add_to_transient_failed_queue(**args)->tuple:
    logging.debug("inside add_to_transient_failed_queue()")
    logging.debug(args)
    try:
        config = args.get('config')
        message = args.get('message')
        writer = args.get('writer')
        logging.debug('add_to_transient_failed_queue(): {}'.format(json.dumps(message)))
        if not writer.publish(config.STORAGE_FAIL_QUEUE, encode_message(message, config.ENCRYPT_KEY)):
            logging.critical('unable to write to RabbitMQ {} queue'.format(config.STORAGE_FAIL_QUEUE))
            return False, args
    except Exception as e:
        logging.error(e)
        return False, args
    return True, args

def add_to_hold_queue(**args)->tuple:
    logging.debug("inside add_to_hold_queue()")
    logging.debug(args)
    try:
        config = args.get('config')
        message = args.get('message')
        writer = args.get('writer')
        logging.debug('add_to_hold_queue(): {}'.format(json.dumps(message)))
        if not writer.publish(config.STORAGE_HOLD_QUEUE, encode_message(message, config.ENCRYPT_KEY)):
            logging.critical('unable to write to RabbitMQ {} queue'.format(config.STORAGE_HOLD_QUEUE))
            return False, args
    except Exception as e:
        logging.error(e)
        return False, args
    return True, args



def add_unknown_event_error_to_message(**args)->tuple:
    logging.debug("inside add_unknown_event_error_to_message()")



    return True,args





