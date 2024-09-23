import logging
import json
import pytz
import iso8601
from datetime import datetime
from cerberus import Validator
from dataclasses import asdict
from sqlalchemy import func, case
from sqlalchemy.sql import expression
from flask import jsonify, make_response
from python.prohibition_web_svc.models import db, Form
from python.prohibition_web_svc.config import Config


def validate_update(**kwargs) -> tuple:
    return True, kwargs


def log_payload_to_splunk(**kwargs) -> tuple:
    request = kwargs.get('request')
    # TODO - log to Splunk
    logging.debug("payload: | {}".format(request.get_data()))
    return True, kwargs


def lease_a_form_id(**kwargs) -> tuple:
    logging.debug('inside lease_a_form_id()')
    data = kwargs.get('payload')
    user_guid = kwargs.get('user_guid')
    id_list = []
    for form_type in data:
        ids = db.session.query(Form) \
            .filter(Form.form_type == form_type) \
            .filter(Form.user_guid == None) \
            .limit(data.get(form_type))
        if ids is None:
            logging.warning('Insufficient unique ids available for {}'.format(form_type))
            return False, kwargs
        for id in ids:
            logging.debug(f'id: {id}')
            id.lease(user_guid)
            id_list.append(asdict(id))
    try:
        db.session.commit()
    except Exception as e:
        return False, kwargs
    kwargs['response_dict'] = jsonify({'forms':id_list})
    return True, kwargs


def renew_form_id_lease(**kwargs) -> tuple:
    logging.debug('inside renew_form_id_lease()')
    form_type = kwargs.get('form_type')
    user_guid = kwargs.get('user_guid')
    form_id = kwargs.get('form_id')
    form = db.session.query(Form) \
        .filter(Form.form_type == form_type) \
        .filter(Form.user_guid == user_guid) \
        .filter(Form.printed_timestamp == None) \
        .filter(Form.spoiled_timestamp == None) \
        .filter(Form.id == form_id) \
        .first()
    if form is None:
        logging.warning('User, {}, cannot renew the lease on {} form'.format(user_guid, form_id))
        return False, kwargs
    form.lease(user_guid)
    try:
        db.session.commit()
    except Exception as e:
        return False, kwargs
    kwargs['response_dict'] = Form.serialize(form)
    return True, kwargs


def mark_form_as_printed_or_spoiled(**kwargs) -> tuple:
    logging.debug('inside mark_form_as_printed_or_spoiled()')
    payload = kwargs.get('payload')
    forms = payload.get('forms')
    spoiled_timestamp = payload.get('spoiled_timestamp', None)
    printed_timestamp = payload.get('printed_timestamp', None)
    user_guid = kwargs.get('user_guid')
    logging.debug(payload)
    for form in forms:
        number = forms.get(form)
        if form == "VI_number" or form == "IRP_number":
            number = str(number)[:-1]
        logging.debug(f'Form Number: {number}')
        form = db.session.query(Form) \
            .filter(Form.id == number) \
            .first()
        if form is None:
            logging.warning(f'{user_guid}, cannot update {payload.get(form)} as printed or spoiled - record not found') 
            return False, kwargs
        if(spoiled_timestamp):
            form.spoiled_timestamp = payload.get('spoiled_timestamp')
        if(printed_timestamp):
            form.printed_timestamp = payload.get('printed_timestamp')
    try:
        db.session.commit()
    except Exception as e:
        return False, kwargs
    kwargs['response_dict'] = {'message': f'successfully printed or spoiled forms: {forms}'}
    return True, kwargs

# def mark_form_as_spoiled(**kwargs) -> tuple:
#     logging.debug('inside mark_form_as_spoiled()')
#     payload = kwargs.get('payload')
#     forms = payload.get('forms')
#     user_guid = kwargs.get('user_guid')
#     logging.debug(payload)
#     for form in forms:
#         number = forms.get(form)
#         if form == "VI_number" or form == "IRP_number":
#             number = str(number)[:-1]
#         logging.debug(f'Form Number: {number}')
#         form = db.session.query(Form) \
#             .filter(Form.id == number) \
#             .first()
#         if form is None:
#             logging.warning(f'{user_guid}, cannot update {payload.get(form)} as spoiled - record not found') 
#             return False, kwargs
#         form.spoiled_timestamp = payload.get('spoiled_timestamp')
#     try:
#         db.session.commit()
#     except Exception as e:
#         return False, kwargs
#     kwargs['response_dict'] = {'message': f'successfully spoiled forms: {forms}'}
#     return True, kwargs


def request_contains_a_payload(**kwargs) -> tuple:
    request = kwargs.get('request')
    try:
        payload = request.get_json()
        kwargs['payload'] = payload
        logging.debug("payload: " + json.dumps(payload))
    except Exception as e:
        return False, kwargs
    return payload is not None, kwargs


def list_all_users_forms(**kwargs) -> tuple:
    user_guid = kwargs.get('user_guid')
    all_ids = []
    logging.debug("inside list_all_forms() {}".format(user_guid))
    try:
        all_forms = db.session.query(Form) \
            .filter(Form.user_guid == user_guid) \
            .filter(Form.printed_timestamp == None)\
            .filter(Form.spoiled_timestamp == None)\
            .all()
        for id in all_forms:
            all_ids.append(asdict(id))
        kwargs['response'] = make_response(jsonify(all_ids))
    except Exception as e:
        logging.warning(str(e))
        return False, kwargs
    return True, kwargs


def get_a_form(**kwargs) -> tuple:
    form_type = kwargs.get('form_type')
    form_id = kwargs.get('form_id')
    try:
        form = db.session.query(Form) \
            .filter(Form.form_type == form_type) \
            .filter(Form.id == form_id) \
            .filter(Form.user_guid == kwargs['username']) \
            .first()
        kwargs['response'] = make_response(jsonify(form), 200)
    except Exception as e:
        logging.warning(str(e))
        return False, kwargs
    return True, kwargs


def admin_list_all_forms_by_type(**kwargs) -> tuple:
    logging.debug("inside admin_list_all_forms()")
    form_type = kwargs.get('form_type')
    try:
        all_forms = db.session.query(Form) \
            .filter(Form.form_type == form_type) \
            .limit(Config.MAX_RECORDS_RETURNED).all()
        kwargs['response'] = make_response(jsonify(Form.collection_to_dict(all_forms)))
    except Exception as e:
        logging.warning(str(e))
        return False, kwargs
    return True, kwargs


def get_json_payload(**kwargs) -> tuple:
    logging.debug("inside get_json_payload()")
    try:
        request = kwargs.get('request')
        kwargs['payload'] = request.json
    except Exception as e:
        logging.warning(str(e))
        return False, kwargs
    return True, kwargs


def validate_form_payload(**kwargs) -> tuple:
    logging.debug("inside validate_form_payload()")
    schema = {
        "form_id": {
            'type': 'string',
            'empty': False,
            'required': True
        },
        "form_type": {
            'type': 'string',
            'allowed': ['12Hour', '24Hour', 'IRP', 'VI'],
            'empty': False,
            'required': True
        }
    }
    v = Validator(schema)
    v.allow_unknown = False
    if v.validate(kwargs.get('payload')):
        return True, kwargs
    logging.warning("validation error: " + json.dumps(v.errors))
    kwargs['validation_errors'] = v.errors
    return False, kwargs


def admin_create_form(**kwargs) -> tuple:
    logging.debug("inside admin_create_form()")
    payload = kwargs.get('payload')
    logging.warning(str(payload))
    try:
        new_form = Form(form_id=payload.get('form_id'), form_type=payload.get('form_type'))
        db.session.add(new_form)
        db.session.commit()
        kwargs['response'] = make_response({"success": True}, 201)
    except Exception as e:
        logging.warning(str(e))
        return False, kwargs
    return True, kwargs


def convert_vancouver_to_utc(iso_datetime_string: str) -> datetime:
    """
    The datetime string we receive from the web app has a Vancouver
    timezone, but the API database field is not timezone aware. We
    convert the Vancouver timezone to UTC.
    """
    utc_timezone = pytz.timezone("UTC")
    printed = iso8601.parse_date(iso_datetime_string)
    return printed.astimezone(utc_timezone).replace(tzinfo=None)

def get_form_statistics(**kwargs) -> tuple:
    try:
        results = db.session.query(
            Form.form_type,
            func.count().label('total_forms'),
            func.sum(case(
                (expression.and_(
                    Form.printed_timestamp.is_(None),
                    Form.spoiled_timestamp.is_(None),
                    expression.or_(Form.user_guid.isnot(None), Form.lease_expiry.isnot(None))
                ), 1),
                else_=0
            )).label('leased_forms'),
            func.sum(case(
                (expression.or_(
                    Form.printed_timestamp.isnot(None),
                    Form.spoiled_timestamp.isnot(None)
                ), 1),
                else_=0
            )).label('total_used_forms'),
            func.sum(case(
                (expression.and_(
                    Form.printed_timestamp.is_(None),
                    Form.spoiled_timestamp.is_(None),
                    Form.user_guid.is_(None),
                    Form.lease_expiry.is_(None)
                ), 1),
                else_=0
            )).label('available_forms')
        ).group_by(Form.form_type).order_by(Form.form_type).all()

        stats = [
            {
                'form_type': r.form_type,
                'total_forms': r.total_forms,
                'leased_forms': r.leased_forms,
                'total_used_forms': r.total_used_forms,
                'available_forms': r.available_forms
            } for r in results
        ]

        kwargs['response_dict'] = stats
        return True, kwargs
    except Exception as e:
        logging.error(f"Error in get_form_statistics: {str(e)}")
        # kwargs['error'] = {
        #     'error_code': ErrorCode.F03,
        #     'error_details': str(e),
        #     'event_type': 'form_statistics',
        #     'func': get_form_statistics,
        # }
        return False, kwargs