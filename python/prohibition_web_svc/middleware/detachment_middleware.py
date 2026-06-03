from datetime import datetime

import pytz
from cerberus import Validator
from flask import jsonify, make_response

from python.common.logging_utils import get_logger
from python.common.models import db, User, Agency
from python.common.models.detachment_change_request import DetachmentChangeRequest, VALID_CHANGE_REASONS

logger = get_logger(__name__)


def get_all_detachments(**kwargs) -> tuple:
    try:
        agencies = db.session.query(Agency).all()
        detachments = [
            {'id': a.id, 'agency_name': a.agency_name, 'vjur': a.vjur}
            for a in agencies
        ]
        kwargs['response'] = make_response(jsonify({'detachments': detachments}), 200)
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs


def get_officer_current_detachment(**kwargs) -> tuple:
    officer_id = kwargs.get('officer_id')
    try:
        user = db.session.query(User).filter(User.user_guid == officer_id).first()
        if user is None:
            return False, kwargs
        detachment = None
        if user.agency_ref:
            detachment = {
                'id': user.agency_id,
                'agency_name': user.agency_ref.agency_name,
                'vjur': user.agency_ref.vjur,
            }
        kwargs['response'] = make_response(
            jsonify({'officer_id': user.user_guid, 'detachment': detachment}), 200
        )
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs


def validate_detachment_change_request_payload(**kwargs) -> tuple:
    schema = {
        'officer_id': {'type': 'string', 'required': True},
        'new_detachment_id': {'type': 'integer', 'required': True, 'coerce': int},
        'reason': {'type': 'string', 'required': True, 'allowed': list(VALID_CHANGE_REASONS)},
        'comments': {'type': 'string', 'required': False, 'nullable': True},
    }
    v = Validator(schema)
    v.allow_unknown = False
    if v.validate(kwargs.get('payload', {})):
        return True, kwargs
    logger.warning(f"detachment change request validation error: {v.errors}")
    kwargs['validation_errors'] = v.errors
    return False, kwargs


def validate_officer_is_self(**kwargs) -> tuple:
    """Enforce that officers can only change their own detachment."""
    requesting_user_guid = kwargs.get('user_guid')
    target_officer_id = kwargs.get('payload', {}).get('officer_id')
    if requesting_user_guid != target_officer_id:
        logger.warning(
            f"officer {requesting_user_guid} attempted to change detachment for {target_officer_id}"
        )
        return False, kwargs
    return True, kwargs


def get_officer_for_change_request(**kwargs) -> tuple:
    officer_id = kwargs.get('payload', {}).get('officer_id')
    try:
        user = db.session.query(User).filter(User.user_guid == officer_id).first()
        if user is None:
            return False, kwargs
        kwargs['officer'] = user
        kwargs['previous_agency_id'] = user.agency_id
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs


def get_new_detachment(**kwargs) -> tuple:
    new_detachment_id = kwargs.get('payload', {}).get('new_detachment_id')
    try:
        agency = db.session.query(Agency).filter(Agency.id == new_detachment_id).first()
        if agency is None:
            return False, kwargs
        kwargs['new_agency'] = agency
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs


def validate_not_duplicate_request(**kwargs) -> tuple:
    previous_agency_id = kwargs.get('previous_agency_id')
    new_detachment_id = kwargs.get('payload', {}).get('new_detachment_id')
    if previous_agency_id == new_detachment_id:
        return False, kwargs
    return True, kwargs


def update_officer_detachment(**kwargs) -> tuple:
    officer = kwargs.get('officer')
    new_agency = kwargs.get('new_agency')
    try:
        officer.agency_id = new_agency.id
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs


def check_concurrent_change(**kwargs) -> tuple:
    """Detect concurrent modification via optimistic read-before-write check."""
    officer = kwargs.get('officer')
    previous_agency_id = kwargs.get('previous_agency_id')
    try:
        db.session.refresh(officer)
        if officer.agency_id != previous_agency_id:
            logger.warning(
                f"concurrent detachment change detected for officer {officer.user_guid}"
            )
            return False, kwargs
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs


def create_change_audit_record(**kwargs) -> tuple:
    tz = pytz.timezone("America/Vancouver")
    now = datetime.now(tz)
    officer = kwargs.get('officer')
    new_agency = kwargs.get('new_agency')
    payload = kwargs.get('payload', {})
    previous_agency_id = kwargs.get('previous_agency_id')

    try:
        record = DetachmentChangeRequest(
            officer_id=officer.user_guid,
            previous_agency_id=previous_agency_id,
            new_agency_id=new_agency.id,
            reason=payload.get('reason'),
            comments=payload.get('comments'),
            created_dt=now,
            created_by=kwargs.get('username'),
        )
        db.session.add(record)

        kwargs['response_dict'] = {
            'previous_detachment': {'id': previous_agency_id},
            'new_detachment': {
                'id': new_agency.id,
                'agency_name': new_agency.agency_name,
                'vjur': new_agency.vjur,
            },
            'updated_at': now.isoformat(),
            'session_refreshed': True,
        }
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs


def commit_transaction(**kwargs) -> tuple:
    try:
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return False, kwargs
    return True, kwargs
