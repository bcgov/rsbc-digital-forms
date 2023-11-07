
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
from python.form_handler.models import db, Event,FormStorageRefs
import pyaes, pbkdf2, binascii, os, secrets
import base64
import fitz

logging.config.dictConfig(Config.LOGGING)

enc_password = Config.ENCRYPT_KEY
enc_password_salt = Config.ENCRYPT_KEY_SALT


def get_listeners(listeners: dict, key: str) -> list:
    """
    Get the list of nested list of functions to invoke
    for a particular form type
    """
    if key in listeners:
        return listeners[key]
    else:
        return listeners['unknown_event']
    

def middle_logic(functions: list, **args):
    """
    Recursive function that calls each node in the list.
    Each node has a "try" function that is executed first. If the try
    function returns True, the next node in the list is returned.  If the
    try function returns False, the node's "fail" list is executed in the
    same way.

    example = dict({
            "rules": [
                {
                    "pass": success1,
                    "fail": [
                        {
                            "pass": failure1,
                            "fail": []
                        }
                    ],
                },
            ]
        })

    The middleware is called like this: middle_logic(example['rules'])
    """
    if functions:
        try_fail_node = functions.pop(0)
        logging.debug('calling try function: ' + try_fail_node['try'].__name__)
        # print(try_fail_node['try'](**args))
        flag, args = try_fail_node['try'](**args)
        logging.debug("result from {} is {}".format(try_fail_node['try'].__name__, flag))
        if flag:
            args = middle_logic(functions, **args)
        else:
            logging.debug('calling try function: ' + try_fail_node['try'].__name__)
            args = middle_logic(try_fail_node['fail'], **args)
    return args


def get_storage_ref_event_type(message,app,db,event_types) -> str:
    """
    Get the event type from the message
    """
    logging.debug("inside get_storage_ref_event_type()")
    try:
        application=app
        db=db
        # message = args.get('message')
        event_type="unknown_event"
        event_id=None
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
            print(form)
            if len(form) == 0 or len(form) > 1:
                return "unknown_event"
            for f in form:
                event_type=f.form_type
                event_id=f.event_id
        if event_type not in event_types:
            raise Exception("event type not found")
        # args['event_type']=storage_key
    except Exception as e:
        logging.error(e)
        return "unknown_event",event_id
    return event_type,event_id

def get_event_status(message,app,db,event_types,event_type,event_id) -> str:
    """
    Get the event status from the message
    """
    logging.debug("inside get_event_status()")
    try:
        application=app
        db=db
        event_status = None
        # message = args.get('message')
        # event_type="unknown_event"
        tmp_key=message.get('Key',None)
        if tmp_key is None:
            return event_type
        # storage_key=tmp_key.split('/')[1]
        storage_key = tmp_key
        # print(storage_key)
        with application.app_context():
            form = db.session.query(Event) \
                .filter(Event.event_id == event_id) \
                .all()
            # db.session.commit()
            print(form)
            if len(form) == 0 or len(form) > 1:
                return "pending"
            for f in form:
                # event_type=f.form_type
                # if event_type not in event_types:
                #     raise Exception("event type not found")
                if event_type == "unknown_event":
                    event_status='pending'
                if event_type == "vi":
                    event_status=f.vi_sent_status
                elif event_type == 'irp':
                    pass
                elif event_type == '24h' or event_type == '12h':
                    event_status=f.icbc_sent_status
        # args['event_type']=storage_key
    except Exception as e:
        logging.error(e)
        return "error"
    return event_status


def method2_decrypt(ciphertext,iv):
    password = enc_password
    passwordSalt = bytes(enc_password_salt, 'utf-8')
    key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
    iv = int.from_bytes(base64.b64decode(iv), 'big')
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    decrypted1 = aes.decrypt(ciphertext)
    # converrt bytes to string
    decrypted1 = decrypted1.decode('utf-8')
    return decrypted1


def encryptPdf_method1(pdfPath, password,outfile):
    doc = fitz.open(pdfPath)
    doc.save(outfile, encryption=fitz.PDF_ENCRYPT_AES_256, owner_pw=password, user_pw=password)
    doc.close()

def decryptPdf_method1(pdfPath, password,outfile):
    try:
        doc = fitz.open(pdfPath)
        if doc.authenticate(password):
            doc.save(outfile)
            if doc.save:
                logging.debug("PDF decrypted")
        else:
            # print('Incorrect Password')
            logging.critical("Incorrect Password")
            doc.close()
            raise Exception("Incorrect Password")
        doc.close()
        with open(outfile, "rb") as pdf_file:
            encoded_string = base64.b64encode(pdf_file.read())
        # delete the outfile
        os.remove(outfile)
        return True,encoded_string.decode('utf-8')
    except Exception as e:
        logging.error(e)
        return False,None


