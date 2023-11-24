import json
import csv
import pytz
import logging
import logging.config
from python.task_scheduler.config import Config
from python.task_scheduler.models import Event,FormStorageRefs
import logging
import json
from datetime import datetime
from sqlalchemy import or_

def query_pending_events(app,db):
    """Query the database for pending events."""
    logging.debug("Query the database for pending events.")
    try:
        application = app
        event_status='pending'
        events=[]
        errmsg=''
        with application.app_context():
            # get event data
            event_data = db.session.query(Event) \
                .filter(or_(Event.icbc_sent_status == event_status, Event.vi_sent_status == event_status)) \
                .all()
            # if len(event_data) == 0 or len(event_data) > 1:
            if len(event_data) == 0:
                errmsg="No pending events found"
                return False,errmsg, None
            for e in event_data:
                try:
                    event_dict = e.__dict__
                    event_dict.pop('_sa_instance_state', None)
                    form_storage_ref = db.session.query(FormStorageRefs) \
                        .filter(FormStorageRefs.event_id == event_dict['event_id']) \
                        .all()
                    if len(form_storage_ref) == 0:
                        continue
                    for f in form_storage_ref:
                        eventobj = {'event_id': event_dict['event_id']}
                        form_dict = f.__dict__
                        form_dict.pop('_sa_instance_state', None)
                        eventobj['Key'] = form_dict['storage_key']
                        events.append(eventobj)
                except Exception as e:
                    logging.error('Error in processing event row')
                    logging.error(e)
                    continue
    except Exception as e:
        logging.error(e)
        errmsg=f"Error querying pending events: {e}"
        return False,errmsg, None
    logging.debug(events)
    return True,None, events