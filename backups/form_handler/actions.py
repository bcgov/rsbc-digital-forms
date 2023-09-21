import json
import csv
import pytz
import logging
import logging.config
from python.form_handler.config import Config
from cerberus import Validator
from cerberus import errors
import logging
import json
from datetime import datetime
from minio import Minio
from minio.error import S3Error
from python.prohibition_web_svc.models import Event,FormStorageRefs,VIForm,TwentyFourHourForm,TwelveHourForm,IRPForm

logging.config.dictConfig(Config.LOGGING)

def get_storage_ref_event_type(**args) -> tuple:
    """
    Get the event type from the message
    """
    logging.debug("inside get_storage_ref_event_type()")
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
        args['file_data']=file_data_content

        # You can save the content to a file or process it further
        # with open('downloaded_file.pdf', 'wb') as file:
        #     file.write(file_data_content)


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

def add_unknown_event_error_to_message(**args)->tuple:
    logging.debug("inside add_unknown_event_error_to_message()")



    return True,args





