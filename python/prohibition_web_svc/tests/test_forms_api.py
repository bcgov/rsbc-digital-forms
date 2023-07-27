import pytest
from datetime import datetime
import logging
import json
import responses
import python.prohibition_web_svc.middleware.keycloak_middleware as middleware
from datetime import datetime, timedelta
from python.prohibition_web_svc.models import Form, UserRole, User
from python.prohibition_web_svc.app import db, create_app
from python.prohibition_web_svc.config import Config, TestConfig


@pytest.fixture(scope='module')
def application():
    Config.RUNNING_TESTS = True
    app = create_app()
    app.config.from_object(TestConfig)
    with app.app_context():
        yield app


@pytest.fixture
def as_guest(application):
    with application.test_client() as client:
        yield client


@pytest.fixture
def database(application):
    with application.app_context():
        db.session.begin_nested()
        yield db
        db.session.commit()
        db.session.rollback()
        db.session.close()


@pytest.fixture
def clean_db(database):
    Form.query.delete()
    UserRole.query.delete() 
    User.query.delete()
    db.session.commit()


@pytest.fixture
def users(database, clean_db):
    today = datetime.strptime("2021-07-21", "%Y-%m-%d")
    users = [
        User(
            user_guid='john@idir',
            username="aaa-bbb-ccc",
            agency='RCMP Terrace',
            badge_number="0234",
            first_name="John",
            last_name="Smith",
            login="john@idir"),
        User(
            user_guid='larry@idir',
            username="ddd-eee-fff",
            agency='RCMP Terrace',
            badge_number="8808",
            first_name="Larry",
            last_name="Smith",
            login='larry@idir'),
        User(
            user_guid='mo@idir',
            username="ggg-hhh-iii",
            agency='RCMP Terrace',
            badge_number="8805",
            first_name="Mo",
            last_name="Test",
            login='mo@idir'),
    ]
    db.session.bulk_save_objects(users)
    db.session.commit() 
    return users

@pytest.fixture
def roles(database, clean_db, users):
    today = datetime.strptime("2021-07-21", "%Y-%m-%d")
    user_role = [
        UserRole(user_guid='john@idir', role_name='officer', submitted_dt=today),
        UserRole(user_guid='larry@idir', role_name='officer', submitted_dt=today, approved_dt=today),
        UserRole(user_guid='mo@idir', role_name='administrator', submitted_dt=today, approved_dt=today)
    ]
    db.session.bulk_save_objects(user_role)
    db.session.commit()

@pytest.fixture
def forms(database, clean_db, users, roles):
    today = datetime.strptime("2021-07-21", "%Y-%m-%d")
    yesterday = today - timedelta(days=1)
    forms = [
        Form(form_id='AA123332', form_type='24Hour', user_guid='larry@idir', lease_expiry=today, printed=None),
        Form(form_id='AA-123333', form_type='24Hour', user_guid='larry@idir', lease_expiry=yesterday, printed=None),
        Form(form_id='AA-123334', form_type='12Hour', user_guid='larry@idir', lease_expiry=yesterday, printed=None),
        Form(form_id='AA-11111', form_type='24Hour', user_guid=None, lease_expiry=None, printed=None)
    ]
    db.session.bulk_save_objects(forms)
    db.session.commit()

@responses.activate
def test_authorized_user_gets_only_current_users_form_records(as_guest, monkeypatch, roles, forms):
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    monkeypatch.setattr(middleware, "decode_keycloak_access_token", _get_authorized_user)
    resp = as_guest.get(Config.URL_PREFIX + "/api/v1/forms/24Hour",
                        content_type="application/json",
                        headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    assert len(resp.json) == 2
    assert resp.json == [
        {
             'id': 'AA123332',
             'form_type': '24Hour',
             'lease_expiry': '2021-07-21',
             'printed_timestamp': None,
             'user_guid': 'larry@idir'
         },
        {
            'id': 'AA-123333',
            'form_type': '24Hour',
            'lease_expiry': '2021-07-20',
            'printed_timestamp': None,
            'user_guid': 'larry@idir'
        }
    ]
    assert resp.status_code == 200
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'get form index',
            'user_guid': 'larry@idir',
            'username': 'larry@idir'
        },
        'source': 'be78d6'
    })


def test_request_without_keycloak_user_cannot_get_forms(as_guest, monkeypatch, forms):
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    resp = as_guest.get(Config.URL_PREFIX + "/api/v1/forms/24Hour",
                        content_type="application/json",
                        headers=_get_keycloak_auth_header("invalid"))
    assert resp.status_code == 401


def test_request_with_unauthorized_keycloak_user_cannot_get_forms(as_guest, monkeypatch, roles, forms):
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    monkeypatch.setattr(middleware, "decode_keycloak_access_token", _get_unauthorized_user)
    resp = as_guest.get(Config.URL_PREFIX + "/api/v1/forms/24Hour",
                        content_type="application/json",
                        headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    assert resp.status_code == 401


@responses.activate
def test_when_form_created_authorized_user_receives_unique_form_id_for_later_use(as_guest, monkeypatch, roles, forms):
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    monkeypatch.setattr(middleware, "decode_keycloak_access_token", _get_authorized_user)
    resp = as_guest.post(Config.URL_PREFIX + "/api/v1/forms/24Hour",
                         content_type="application/json",
                         headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    today = datetime.now()
    expected_lease_expiry = datetime.strftime(today + timedelta(days=30), "%Y-%m-%d")

    assert resp.status_code == 201
    assert resp.json == {
        'id': 'AA-11111',
        'form_type': '24Hour',
        'lease_expiry': expected_lease_expiry,
        'printed_timestamp': None,
        'user_guid': 'larry@idir'
    }
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'create form',
            'user_guid': 'larry@idir',
            'username': 'larry@idir',
            'form_type': '24Hour',
            'lease_expiry': expected_lease_expiry,
            'id': 'AA-11111'
        },
        'source': 'be78d6'
    })


def test_unauthorized_user_cannot_create_new_forms(as_guest, monkeypatch, roles, forms):
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    monkeypatch.setattr(middleware, "decode_keycloak_access_token", _get_unauthorized_user)
    resp = as_guest.post(Config.URL_PREFIX + "/api/v1/forms/24Hour",
                         content_type="application/json",
                         headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    today = datetime.now()
    expected_lease_expiry = datetime.strftime(today + timedelta(days=30), "%Y-%m-%d")
    assert resp.status_code == 401


def test_request_without_keycloak_user_cannot_create_forms(as_guest, monkeypatch, forms):
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    resp = as_guest.post(Config.URL_PREFIX + "/api/v1/forms/24Hour",
                         content_type="application/json",
                         headers=_get_keycloak_auth_header("invalid"))
    assert resp.status_code == 401


@responses.activate
def test_if_no_unique_ids_available_user_receives_a_500_response(as_guest, database, monkeypatch, roles):
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    monkeypatch.setattr(middleware, "decode_keycloak_access_token", _get_authorized_user)
    today = datetime.strptime("2021-07-21", "%Y-%m-%d")
    user = User(
            user_guid='other_user',
            username="aaa-bbb-ccc",
            agency='RCMP Terrace',
            badge_number="02343",
            first_name="other",
            last_name="user",
            login="other@idir")
    database.session.add(user)
    database.session.commit()
    forms = [
        Form(form_id='AA123332', form_type='24Hour', user_guid='other_user', lease_expiry=today, printed=None),
    ]
    database.session.bulk_save_objects(forms)
    database.session.commit()

    resp = as_guest.post(Config.URL_PREFIX + "/api/v1/forms/24Hour",
                         content_type="application/json",
                         headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    assert resp.status_code == 500
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'insufficient form ids',
            'user_guid': 'larry@idir',
            'username': 'larry@idir',
            'form_type': '24Hour'
        },
        'source': 'be78d6'
    })


def test_users_cannot_submit_payloads_to_the_create_endpoint(as_guest, monkeypatch, database, roles):
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    monkeypatch.setattr(middleware, "decode_keycloak_access_token", _get_authorized_user)
    resp = as_guest.post(Config.URL_PREFIX + "/api/v1/forms/24Hour",
                         content_type="application/json",
                         data=json.dumps({"attribute": "value"}),
                         headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    assert resp.status_code == 400


@responses.activate
def test_user_cannot_renew_lease_on_form_that_has_been_printed(as_guest, database, monkeypatch, roles):
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    monkeypatch.setattr(middleware, "decode_keycloak_access_token", _get_authorized_user)
    today = datetime.strptime("2021-07-21", "%Y-%m-%d")
    forms = [
        Form(form_id='AA123332', form_type='24Hour', user_guid='larry@idir', lease_expiry=today, printed=today),
    ]
    database.session.bulk_save_objects(forms)
    database.session.commit()

    resp = as_guest.patch(Config.URL_PREFIX + "/api/v1/forms/24Hour/{}".format('AA123332'),
                          content_type="application/json",
                          headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    assert resp.status_code == 400
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'unable to renew form lease',
            'user_guid': 'larry@idir',
            'username': 'larry@idir',
            'form_type': '24Hour',
            'id': 'AA123332'
        },
        'source': 'be78d6'
    })


def test_request_without_keycloak_user_cannot_update_forms_or_renew_lease_on_form(as_guest, monkeypatch, forms):
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    resp = as_guest.patch(Config.URL_PREFIX + "/api/v1/forms/24Hour/{}".format("AA123332"),
                          content_type="application/json",
                          headers=_get_keycloak_auth_header("invalid"))
    assert resp.status_code == 401


@responses.activate
def test_when_form_updated_without_payload_user_receives_updated_lease_date(as_guest, monkeypatch, roles, forms):
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    monkeypatch.setattr(middleware, "decode_keycloak_access_token", _get_authorized_user)
    resp = as_guest.patch(Config.URL_PREFIX + "/api/v1/forms/24Hour/{}".format('AA123332'),
                          content_type="application/json",
                          headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    today = datetime.now()
    expected_lease_expiry = datetime.strftime(today + timedelta(days=30), "%Y-%m-%d")

    assert resp.status_code == 200
    assert resp.json == {
        'id': 'AA123332',
        'form_type': '24Hour',
        'lease_expiry': expected_lease_expiry,
        'printed_timestamp': None,
        'user_guid': 'larry@idir'
    }


# @responses.activate
# def test_user_can_submit_form_and_mark_form_id_as_printed(as_guest, database, monkeypatch, roles):
#     monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
#     monkeypatch.setattr(middleware, "decode_keycloak_access_token", _get_authorized_user)
#     today = datetime.now()
#     expected_lease_expiry = datetime.strftime(today + timedelta(days=30), "%Y-%m-%d")
#     forms = [
#         Form(form_id='AA123332', form_type='24Hour', user_guid='larry@idir', lease_expiry=expected_lease_expiry, printed=None),
#     ]
#     database.session.bulk_save_objects(forms)
#     database.session.commit()

#     printed_timestamp = datetime.strftime(today + timedelta(days=30), "%Y-%m-%d")

#     resp = as_guest.patch(Config.URL_PREFIX + "/api/v1/forms/24Hour/{}".format('AA123332'),
#                           content_type="application/json",
#                           headers=_get_keycloak_auth_header(_get_keycloak_access_token()),
#                           data={
#                                 "id": "AA123332",
#                                 "form_type": "24Hour",
#                                 "lease_expiry": expected_lease_expiry,
#                                 "printed_timestamp": printed_timestamp,
#                                 'user_guid': 'larry@idir'
#                             }
#                           )
    
#     assert resp.status_code == 200
#     assert database.session.query(Form.printed_timestamp) \
#                .filter(Form.id == 'AA123332') \
#                .filter(Form.form_type == '24Hour') \
#                .first()

@responses.activate
def test_user_can_submit_form_and_mark_form_id_as_printed(as_guest, database, monkeypatch, roles):
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    monkeypatch.setattr(middleware, "decode_keycloak_access_token", _get_authorized_user)
    today = datetime.now()
    expected_lease_expiry = datetime.strftime(today + timedelta(days=30), "%Y-%m-%d")
    forms = [
        Form(form_id='AA123332', form_type='24Hour', user_guid='larry@idir', lease_expiry=expected_lease_expiry, printed=None),
    ]
    database.session.bulk_save_objects(forms)
    database.session.commit()
    printed_timestamp = datetime.strftime(today + timedelta(days=30), "%Y-%m-%d")
    data={
        "form_id": "AA123332",
        "form_type": "24Hour",
        "lease_expiry": expected_lease_expiry,
        "printed_timestamp": printed_timestamp,
        "component": "TwentyFourHourProhibition",
        "label": "24-Hour",
        "description": "24-Hour Prohibition",
        "full_name": "MV2634"
    }

    resp = as_guest.patch(Config.URL_PREFIX + "/api/v1/forms/24Hour/{}".format('AA123332'),
                          content_type="application/json",
                          headers=_get_keycloak_auth_header(_get_keycloak_access_token()),
                          data=data
                          )
    assert resp.status_code == 200
 
    assert database.session.query(Form.printed_timestamp) \
               .filter(Form.id == 'AA123332') \
               .filter(Form.form_type == '24Hour') \
               .first()


def test_form_delete_method_not_implemented(as_guest):
    resp = as_guest.delete(Config.URL_PREFIX + "/api/v1/forms/24Hour/{}".format('AA123332'),
                           content_type="application/json",
                           headers=_get_keycloak_auth_header(Config))
    assert resp.status_code == 405
    assert resp.json == {"error": "method not implemented"}


def _get_keycloak_access_token() -> str:
    return 'some-secret-access-token'


def _get_keycloak_auth_header(access_token) -> dict:
    return dict({
        'Authorization': 'Bearer {}'.format(access_token)
    })


def _mock_keycloak_certificates(**kwargs) -> tuple:
    logging.warning("inside _mock_keycloak_certificates()")
    return True, kwargs


def _get_unauthorized_user(**kwargs) -> tuple:
    logging.warning("inside _get_unauthorized_user()")
    kwargs['decoded_access_token'] = {'preferred_username': 'john@idir', 'display_name':'John test',
                                      'identity_provider':'idir'}  # keycloak username
    return True, kwargs


def _get_authorized_user(**kwargs) -> tuple:
    logging.warning("inside _get_authorized_user()")
    kwargs['decoded_access_token'] = {'preferred_username': 'larry@idir','display_name':'Larry test',
                                      'identity_provider':'idir' }  # keycloak username
    return True, kwargs


def _get_administrative_user_from_database(**kwargs) -> tuple:
    kwargs['decoded_access_token'] = {'preferred_username': 'mo@idir'}
    return True, kwargs