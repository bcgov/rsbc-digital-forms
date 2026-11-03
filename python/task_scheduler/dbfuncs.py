import logging
from python.common.models import Event,Submission,SubmissionFormRef,FormsflowOfflineSubmission
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
            event_data = db.session.query(Submission) \
                .filter(Submission.task_processing_status == event_status) \
                .join(Event, Submission.submission_id == Event.submission_id) \
                .all()
            # if len(event_data) == 0 or len(event_data) > 1:
            if len(event_data) == 0:
                errmsg="No pending events found"
                return False,errmsg, None
            for e in event_data:
                try:
                    form_storage_ref = db.session.query(SubmissionFormRef) \
                        .filter(SubmissionFormRef.submission_id == e.submission_id) \
                        .all()
                    if len(form_storage_ref) == 0:
                        continue
                    for f in form_storage_ref:
                        eventobj = {
                            'event_id': e.event.event_id,
                            'submission_id': e.submission_id,
                            'Key': f.storage_key,
                            'FormType': f.form_type
                        }
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

def update_event_status(app,db,submission_id,event_id,status):
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

            submission_data = db.session.query(Submission) \
                .filter(Submission.submission_id == submission_id) \
                .one()
            submission_data.task_processing_status=status    
            db.session.commit()
    except Exception as e:
        logging.error(e, exc_info=True)
        record_queue_error(app, {'event_id': event_id}, update_event_status, str(e) )
        errmsg=f"Error updating processed event status: {e}"
        return False,errmsg
    return True,None

def query_pending_offline_submissions(app, db):
    """Query pending offline submissions."""
    offline_submissions = []
    try:
        with app.app_context():
            query_result = db.session.query(FormsflowOfflineSubmission) \
                .filter(FormsflowOfflineSubmission.status == 'pending') \
                .all()
            if len(query_result) == 0:
                errmsg = "No pending offline submissions found"
                return False, errmsg, None

            for submission in query_result:
                offline_submissions.append({
                    'id': submission.id
                })
    except Exception as e:
        logging.error(e, exc_info=True)
        record_queue_error(app, None, query_pending_offline_submissions, str(e))
        errmsg = f"Error querying pending offline submissions: {e}"
        return False, errmsg, None
    return True, None, offline_submissions

def update_offline_submission_status(app,db,id,status):
    """Update the offline submission status."""
    try:
        application = app
        with application.app_context():
            submission_data = db.session.query(FormsflowOfflineSubmission) \
                .filter(FormsflowOfflineSubmission.id == id) \
                .one()
            submission_data.status=status    
            db.session.commit()
    except Exception as e:
        logging.error(e, exc_info=True)
        record_queue_error(app, {'id': id}, update_offline_submission_status, str(e) )
        errmsg=f"Error updating offline submission status: {e}"
        return False,errmsg
    return True,None