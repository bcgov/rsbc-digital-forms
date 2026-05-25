from flask import make_response
from python.common.logging_utils import get_logger
from python.common.models import db, Submission, SubmissionFormRef, SubmissionEvent

logger = get_logger(__name__)


def request_contains_a_payload(**kwargs) -> tuple:
    logger.verbose("inside request_contains_a_payload()")
    request = kwargs.get('request')
    try:
        payload = request.get_json()
        kwargs['payload'] = payload
    except Exception:
        return False, kwargs
    return payload is not None, kwargs


def log_status_update_payload_to_splunk(**kwargs) -> tuple:
    try:
        payload = kwargs.get('payload')
        kwargs['splunk_data'] = {
            'event': "update_submission_event_status",
            'payload': payload
        }
    except Exception as e:
        logger.error(e)
    return True, kwargs

def validate_update_event_status_payload(**kwargs) -> tuple:
    """Validate that the payload contains ff_application_id, destination, and status."""
    logger.verbose("inside validate_update_event_status_payload()")
    payload = kwargs.get('payload')
    if not payload:
        kwargs['response_dict'] = {'error_details': 'No payload provided'}
        return False, kwargs
    missing = [f for f in ('ff_application_id', 'destination', 'status', 'form_id') if not payload.get(f)]
    if missing:
        error_message = f"Invalid payload: missing required field(s): {', '.join(missing)}"
        logger.warning(error_message)
        kwargs['response_dict'] = {'error_details': error_message}
        return False, kwargs
    return True, kwargs


def update_submission_event_status(**kwargs) -> tuple:
    """
    Find the SubmissionEvent matching ff_application_id + form_id + destination and update its status.
    Lookup chain: Submission -> SubmissionFormRef -> SubmissionEvent.
    """
    logger.verbose("inside update_submission_event_status()")
    payload = kwargs.get('payload')
    ff_application_id = payload.get('ff_application_id')
    form_id = payload.get('form_id')
    destination = payload.get('destination')
    new_status = payload.get('status')
    try:
        submission = db.session.query(Submission).filter(
            Submission.ff_application_id == ff_application_id
        ).first()
        if submission is None:
            logger.warning(f"No submission found for ff_application_id: {ff_application_id}")
            return False, kwargs

        submission_event = (
            db.session.query(SubmissionEvent)
            .join(SubmissionFormRef, SubmissionEvent.form_ref_id == SubmissionFormRef.form_ref_id)
            .filter(
                SubmissionFormRef.submission_id == submission.submission_id,
                SubmissionFormRef.form_id == form_id,
                SubmissionEvent.destination == destination,
            )
            .first()
        )
        if submission_event is None:
            logger.warning(
                f"No submission event found for submission_id: {submission.submission_id}, "
                f"form_id: {form_id}, destination: {destination}"
            )
            return False, kwargs

        submission_event.status = new_status
        db.session.flush()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return False, kwargs
    kwargs['response_dict'] = {
        'submission_event_id': submission_event.submission_event_id,
        'destination': submission_event.destination,
        'status': submission_event.status,
    }
    return True, kwargs


def commit_transaction(**kwargs) -> tuple:
    """Commit the current DB transaction."""
    try:
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return False, kwargs
    return True, kwargs
