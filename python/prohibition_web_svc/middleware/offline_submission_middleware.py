from datetime import datetime
import uuid

from python.common.enums import ErrorCode
from python.common.logging_utils import get_logger
from python.common.models import db, FormsflowOfflineSubmission

logger = get_logger(__name__)

def set_local_submission_id(**kwargs):
    payload = kwargs.get('payload')
    if payload:
        local_submission_id = payload.get('localSubmissionId')
        form_id = payload.get('formId')
        if local_submission_id:
            kwargs['local_submission_id'] = local_submission_id
        else:
            kwargs['local_submission_id'] = 'generated_' + uuid.uuid4().hex
        if form_id:
            kwargs['form_id'] = form_id
    return True, kwargs

def check_if_offline_submission_exists(**kwargs):
    local_submission_id = kwargs.get('local_submission_id')
    user_guid = kwargs.get('user_guid')
    logger.verbose(f"Checking if offline submission with local_submission_id {local_submission_id} exists for user_guid {user_guid}.")
    try:
      already_exists = FormsflowOfflineSubmission.query.filter_by(local_submission_id=local_submission_id, created_by=user_guid).count() > 0
      if already_exists:
          logger.info(f"Offline submission with local_submission_id {local_submission_id} already exists for user_guid {user_guid}.")
          return False, kwargs
    except Exception as e:
        logger.error(e)
        kwargs['error'] = {
            'error_code': ErrorCode.O01,
            'error_details': str(e),
            'event_id': None,
            'event_type': 'offline_submission',
            'ticket_no': local_submission_id,
            'func': check_if_offline_submission_exists,
        }
        return False, kwargs
    return True, kwargs

def create_offline_submission(**kwargs):
    local_submission_id = kwargs.get('local_submission_id')
    payload = kwargs.get('payload')
    user_guid = kwargs.get('user_guid')
    form_id = kwargs.get('form_id')
    logger.verbose(f"Creating offline submission with local_submission_id {local_submission_id} for user_guid {user_guid}.")

    try:
      offline_submission = FormsflowOfflineSubmission(
          local_submission_id=local_submission_id,
          payload=payload,
          status='pending',
          form_id=form_id,
          created_dt=datetime.now(),
          created_by=user_guid,
      )
      db.session.add(offline_submission)
      db.session.commit()
      kwargs['response_dict'] = { 'offline_submission_id': offline_submission.id }
      return True, kwargs
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        kwargs['error'] = {
            'error_code': ErrorCode.O01,
            'error_details': str(e),
            'event_id': None,
            'event_type': 'offline_submission',
            'ticket_no': local_submission_id,
            'func': create_offline_submission,
        }
        return False, kwargs