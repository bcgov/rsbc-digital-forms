
import json
import csv
import pytz
import logging
import logging.config
from python.common.verbose_logging import VERBOSE_LEVEL_NUM, verbose
from python.form_handler.config import Config
from cerberus import Validator
from cerberus import errors
import logging
import json
from datetime import datetime
from python.common.models import db, Event,FormStorageRefs
import pyaes, pbkdf2, binascii, os, secrets
import base64
import fitz

logging.addLevelName(VERBOSE_LEVEL_NUM, 'VERBOSE')
logging.verbose = verbose
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
        if 'event' in try_fail_node and \
            args.get(try_fail_node['event'], {}).get('status') == 'sent':
            logging.info(f'Already sent to {try_fail_node["event"]}, skipping {try_fail_node["try"].__name__}')
            flag, args = True, args
        else:
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
    logging.verbose("inside get_storage_ref_event_type()")
    try:
        application=app
        db=db
        # message = args.get('message')
        logging.verbose("message received in get_storage_ref_event_type: {}".format(message))
        event_type=message.get('FormType',"unknown_event").lower()
        event_id=message.get('event_id',None)

        logging.debug("event_type: {}".format(event_type))
        logging.debug("event_id: {}".format(event_id))
        if event_type not in event_types:
            logging.error("event type not found: {}".format(event_type))
            raise Exception("event type not found")
    except Exception as e:
        logging.error(e, exc_info=True)
        return "unknown_event",event_id
    return event_type,event_id

def get_event_status(app,db,event_type,event_id) -> str:
    """
    Get the event status from the message
    """
    logging.verbose("inside get_event_status()")
    try:
        application=app
        db=db
        event_status = None

        with application.app_context():
            form = db.session.query(Event) \
                .filter(Event.event_id == event_id) \
                .all()
            # db.session.commit()
            if len(form) == 0 or len(form) > 1:
                return "pending"
            for f in form:
                if event_type == "unknown_event":
                    event_status='pending'
                if event_type == "vi":
                    event_status=f.vi_sent_status
                elif event_type == 'irp':
                    event_status='pending'
                elif event_type == '24h' or event_type == '12h':
                    event_status=f.icbc_sent_status
        # args['event_type']=storage_key
    except Exception as e:
        logging.error(e, exc_info=True)
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
    

def convertDateTime(timevalue):
    # Convert to datetime object
    date_obj = datetime.strptime(timevalue, "%Y-%m-%d")

    # Set the time to midnight
    date_obj = date_obj.replace(hour=0, minute=0, second=0, microsecond=00)

    # Specify the timezone (Pacific Time in this case)
    pacific_time = pytz.timezone("America/Los_Angeles")
    date_obj = pacific_time.localize(date_obj)

    # Convert to desired string format
    formatted_date_str = date_obj.isoformat()
    date_obj.strftime("%Y-%m-%dT%H:%M:%S.%f")

    # Reformat the datetime object to include microseconds in the specified format
    formatted_date_str_with_microseconds = date_obj.strftime('%Y-%m-%dT%H:%M:%S.000%z')
    formatted_date_str_with_correct_offset = formatted_date_str_with_microseconds[:-2] + ":" + formatted_date_str_with_microseconds[-2:]
    return formatted_date_str_with_correct_offset

def convertDateTimeWithSecs(timevalue):

    # Convert to datetime object
    new_date_obj = datetime.strptime(timevalue, "%Y-%m-%dT%H:%M:%S")

    # Specify the timezone (Pacific Time in this case)
    pacific_time = pytz.timezone("America/Los_Angeles")
    new_date_obj = pacific_time.localize(new_date_obj)

    # Reformat the datetime object to include the timezone offset in the specified format
    formatted_new_date_str_with_correct_offset = new_date_obj.strftime('%Y-%m-%dT%H:%M:%S.000%z')
    # Inserting the colon in the timezone offset
    formatted_new_date_str_with_correct_offset = formatted_new_date_str_with_correct_offset[:-2] + ":" + formatted_new_date_str_with_correct_offset[-2:]
    return formatted_new_date_str_with_correct_offset


