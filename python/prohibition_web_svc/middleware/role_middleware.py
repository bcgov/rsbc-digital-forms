from flask import jsonify, make_response
import pytz
from datetime import datetime
from python.prohibition_web_svc.config import Config
from python.common.models import db, UserRole, User, Agency
from python.common.logging_utils import get_logger

logger = get_logger(__name__)

def query_current_users_roles(**kwargs) -> tuple:
    try:
        my_roles = db.session.query(UserRole) \
            .filter(UserRole.user_guid == kwargs['user_guid']) \
            .filter(UserRole.approved_dt != None) \
            .all()
        kwargs['response'] = make_response(jsonify(UserRole.collection_to_dict(my_roles, "serialize")))
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs


def query_all_users_roles(**kwargs) -> tuple:
    try:
        user_role = db.session.query(UserRole) \
            .filter(UserRole.user_guid == kwargs.get('requested_user_guid')) \
            .limit(Config.MAX_RECORDS_RETURNED).all()
        kwargs['response'] = make_response(jsonify(UserRole.collection_to_dict(user_role, "serialize")))
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs


def officer_has_not_applied_previously(**kwargs) -> tuple:
    try:
        roles = db.session.query(UserRole) \
            .filter(UserRole.role_name == 'officer') \
            .filter(UserRole.user_guid == kwargs.get('username')) \
            .count()
        logger.debug("officer_has_not_applied_previously() result: " + str(roles))
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return roles == 0, kwargs


def create_a_role(**kwargs) -> tuple:
    tz = pytz.timezone('America/Vancouver')
    try:
        role_user = UserRole("officer", kwargs.get('username'), datetime.now(tz))
        db.session.add(role_user)
        db.session.commit()
        kwargs['response'] = make_response(jsonify(UserRole.serialize(role_user)), 201)
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs


def approve_officers_role(**kwargs) -> tuple:
    try:
        user_role = db.session.query(UserRole) \
            .filter(UserRole.role_name == 'officer') \
            .filter(UserRole.user_guid == kwargs.get('requested_user_guid')) \
            .first()
        logger.info("approve_officers_role - user_guid: " + kwargs.get('requested_user_guid'))
        tz = pytz.timezone('America/Vancouver')
        user_role.approved_dt = datetime.now(tz)
        db.session.commit()
        kwargs['response'] = make_response(jsonify(UserRole.serialize(user_role)), 200)
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs


def delete_a_role(**kwargs) -> tuple:

    try:
        user_role = db.session.query(UserRole) \
            .filter(UserRole.role_name == kwargs.get('role_name')) \
            .filter(UserRole.user_guid == kwargs.get('requested_user_guid')) \
            .first()
        db.session.delete(user_role)
        db.session.commit()
        kwargs['response'] = make_response("okay", 200)
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs


def admin_create_role(**kwargs) -> tuple:
    payload = kwargs.get('payload')
    try:
        tz = pytz.timezone('America/Vancouver')
        current_dt = datetime.now(tz)
        role_user = UserRole(payload.get('role_name'),
                             kwargs.get('requested_user_guid'),
                             current_dt,
                             current_dt)
        db.session.add(role_user)
        db.session.commit()
        kwargs['response'] = make_response(jsonify(UserRole.serialize(role_user)), 201)
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs


def query_all_users(**kwargs) -> tuple:
    try:
        user_role = db.session.query(
            UserRole.user_guid,
            UserRole.role_name,
            UserRole.approved_dt,
            UserRole.submitted_dt,
            User.username,
            User.agency_id,
            Agency.agency_name,
            User.badge_number,
            User.first_name,
            User.last_name,
            User.login,
            User.last_active)\
            .join(User, User.user_guid == UserRole.user_guid) \
            .join(Agency, User.agency_id == Agency.id) \
            .limit(Config.MAX_RECORDS_RETURNED)\
            .all()
        kwargs['response'] = make_response(jsonify(UserRole.collection_to_dict(user_role, "serialize_all_users")))
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs
