import logging
from python.common.models import Event,FormStorageRefs
import logging
from python.task_scheduler.eventqueuefuncs import record_queue_error

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
                .filter(Event.task_processing_status == event_status) \
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
                    logging.error(e, exc_info=True)
                    continue
    except Exception as e:
        logging.error(e, exc_info=True)
        record_queue_error(app, None, query_pending_events, str(e) )
        errmsg=f"Error querying pending events: {e}"
        return False,errmsg, None
    logging.debug(events)
    if len(events) == 0:
        errmsg="No pending events found"
        return False,errmsg, None
    return True,None, events

def update_event_status(app,db,event_id,status):
    """Update the event status."""
    logging.debug("Update the event status.")
    try:
        application = app
        with application.app_context():
            # get event data
            event_data = db.session.query(Event) \
                .filter(Event.event_id == event_id) \
                .all()
            if len(event_data) == 0 or len(event_data) > 1:
                errmsg="No events found or multiple events found"
                return False,errmsg
            for e in event_data:
                e.task_processing_status=status
                db.session.commit()
    except Exception as e:
        logging.error(e, exc_info=True)
        record_queue_error(app, {'event_id': event_id}, update_event_status, str(e) )
        errmsg=f"Error updating processed event status: {e}"
        return False,errmsg
    return True,None




# .filter(or_(Event.icbc_sent_status == event_status, Event.vi_sent_status == event_status)) \