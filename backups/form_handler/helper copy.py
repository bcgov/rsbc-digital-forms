
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
                return "unknown_event"
            for f in form:
                event_type=f.form_type
        if event_type not in event_types:
            raise Exception("event type not found")
        # args['event_type']=storage_key
    except Exception as e:
        logging.error(e)
        return "unknown_event"
    return event_type


def method2_decrypt(ciphertext,iv):
    password = enc_password
    passwordSalt = bytes(enc_password_salt, 'utf-8')
    # print('prints')
    # print('cipher: ',ciphertext)
    key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
    iv = int.from_bytes(base64.b64decode(iv), 'big')
    # iv=base64.b64decode(iv)
    # print(f"iv- {iv}")
    # print(type(iv))
    # iv = secrets.randbits(256)
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    decrypted1 = aes.decrypt(ciphertext)
    # print('Decrypted:', decrypted1)
    # converrt bytes to string
    decrypted1 = decrypted1.decode('utf-8')
    # print(decrypted1)
    # print(sample_pdf_str)
    # print(type(decrypted1))
    # print(type(sample_pdf_str))
    # print(decrypted1==sample_pdf_str)
    # print('Decrypted:', decrypted1)
    return decrypted1


