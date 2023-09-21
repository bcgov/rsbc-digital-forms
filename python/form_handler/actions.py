import json
import csv
import pytz
import logging
import logging.config
from python.common.config import Config
from cerberus import Validator
from cerberus import errors
import logging
import json
from datetime import datetime
from python.prohibition_web_svc.models import Event,FormStorageRefs

logging.config.dictConfig(Config.LOGGING)

def get_storage_ref_event_type(**args) -> str:
    """
    Get the event type from the message
    """
    try:
        application=args.get('app')
        db=args.get('db')
        message = args.get('message')
        event_type="unknown_event"
        tmp_key=message.get('Key',None)
        if tmp_key is None:
            return event_type    
        storage_key=tmp_key.split('/')[1]
        print(storage_key)
        with application.app_context():            
            form = db.session.query(FormStorageRefs) \
                .filter(FormStorageRefs.storage_key == storage_key) \
                .first()
            # db.session.commit()
            print(form)
        args['event_type']=storage_key
    except Exception as e:
        logging.error(e)
        return False,args
    return True,args

