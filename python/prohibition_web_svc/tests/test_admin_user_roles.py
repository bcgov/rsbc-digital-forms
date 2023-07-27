import pytest
from python.prohibition_web_svc.config import Config,TestConfig
import responses
from datetime import datetime
import python.prohibition_web_svc.middleware.keycloak_middleware as middleware
from python.prohibition_web_svc.models import db, UserRole, User, Form
from python.prohibition_web_svc.app import create_app
import logging
import json


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
    UserRole.query.delete()
    Form.query.delete()
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
    yield

@responses.activate
def test_administrator_can_get_all_roles_for_specific_user(as_guest, monkeypatch, roles):
    monkeypatch.setattr(Config, 'ADMIN_USERNAME', 'administrator@idir')
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    monkeypatch.setattr(middleware, "decode_keycloak_access_token", _get_administrative_user_from_database)
    resp = as_guest.get(Config.URL_PREFIX + "/api/v1/admin/users/larry%40idir/roles",
                         follow_redirects=True,
                         content_type="application/json",
                         headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    logging.debug(json.dumps(resp.json))
    assert resp.status_code == 200
    assert len(resp.json) == 1
    assert resp.json[0]['user_guid'] == 'larry@idir'
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'admin get user-role',
            'admin_user_guid': 'mo@idir',
            'admin_username': 'mo@idir',
            'requested_user_guid': 'larry@idir'
        },
        'source': 'be78d6'
    })


@responses.activate
def test_non_administrators_cannot_get_all_roles_for_specific_user(as_guest, monkeypatch, roles):
    monkeypatch.setattr(Config, 'ADMIN_USERNAME', 'administrator@idir')
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    monkeypatch.setattr(middleware, "decode_keycloak_access_token", _get_authorized_user)
    resp = as_guest.get(Config.URL_PREFIX + "/api/v1/admin/users/larry%40idir/roles",
                         follow_redirects=True,
                         content_type="application/json",
                         headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    logging.debug(json.dumps(resp.json))
    assert resp.status_code == 401
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'permission denied',
            'user_guid': 'larry@idir',
            'username': 'larry@idir'
        },
        'source': 'be78d6'
    })


@responses.activate
def test_administrator_can_approve_a_specific_user_role(as_guest, monkeypatch, roles):
    monkeypatch.setattr(Config, 'ADMIN_USERNAME', 'administrator@idir')
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    monkeypatch.setattr(middleware, "decode_keycloak_access_token", _get_administrative_user_from_database)
    resp = as_guest.patch(Config.URL_PREFIX + "/api/v1/admin/users/john%40idir/roles/officer",
                         follow_redirects=True,
                         content_type="application/json",
                         headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    logging.debug(json.dumps(resp.json))
    assert resp.status_code == 200
    assert resp.json['approved_dt'] is not None
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'admin update user-role',
            'admin_user_guid': 'mo@idir',
            'admin_username': 'mo@idir',
            'requested_user_guid': 'john@idir',
            'role_name': 'officer'
        },
        'source': 'be78d6'
    })


@responses.activate
def test_non_administrators_cannot_approve_a_user_role(as_guest, monkeypatch, roles):
    monkeypatch.setattr(Config, 'ADMIN_USERNAME', 'administrator@idir')
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    monkeypatch.setattr(middleware, "decode_keycloak_access_token", _get_authorized_user)
    resp = as_guest.patch(Config.URL_PREFIX + "/api/v1/admin/users/larry%40idir/roles/officer",
                         follow_redirects=True,
                         content_type="application/json",
                         headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    logging.debug(json.dumps(resp.json))
    assert resp.status_code == 401
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'permission denied',
            'user_guid': 'larry@idir',
            'username': 'larry@idir'
        },
        'source': 'be78d6'
    })


@responses.activate
def test_administrator_can_delete_an_officer_user(as_guest, monkeypatch, roles, database):
    monkeypatch.setattr(Config, 'ADMIN_USERNAME', 'administrator@idir')
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    monkeypatch.setattr(middleware, "decode_keycloak_access_token", _get_administrative_user_from_database)
    resp = as_guest.delete(Config.URL_PREFIX + "/api/v1/admin/users/john%40idir/roles/officer",
                         follow_redirects=True,
                         content_type="application/json",
                         headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    logging.debug(json.dumps(resp.json))
    assert resp.status_code == 200
    assert database.session.query(UserRole) \
               .filter(UserRole.role_name == 'officer') \
               .filter(UserRole.user_guid == 'john@idir') \
               .count() == 0
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'admin delete user-role',
            'admin_user_guid': 'mo@idir',
            'admin_username': 'mo@idir',
            'requested_user_guid': 'john@idir',
            'role_name': 'officer'
        },
        'source': 'be78d6'
    })


def test_administrator_can_delete_another_admin_user(as_guest, monkeypatch, roles, database):
    monkeypatch.setattr(Config, 'ADMIN_USERNAME', 'administrator@idir')
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    monkeypatch.setattr(middleware, "decode_keycloak_access_token", _get_administrative_user_from_database)
    resp = as_guest.delete(Config.URL_PREFIX + "/api/v1/admin/users/mo@idir/roles/administrator",
                         follow_redirects=True,
                         content_type="application/json",
                         headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    logging.debug(json.dumps(resp.json))
    assert resp.status_code == 200
    assert database.session.query(UserRole) \
               .filter(UserRole.role_name == 'administrator') \
               .filter(UserRole.user_guid == 'mo@idir') \
               .count() == 0


@responses.activate
def test_non_administrators_cannot_delete_a_user_role(as_guest, monkeypatch, roles):
    monkeypatch.setattr(Config, 'ADMIN_USERNAME', 'administrator@idir')
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    monkeypatch.setattr(middleware, "decode_keycloak_access_token", _get_authorized_user)
    resp = as_guest.delete(Config.URL_PREFIX + "/api/v1/admin/users/larry%40idir/roles/officer",
                         follow_redirects=True,
                         content_type="application/json",
                         headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    assert resp.status_code == 401
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'permission denied',
            'user_guid': 'larry@idir',
            'username': 'larry@idir'
        },
        'source': 'be78d6'
    })


def test_administrator_can_give_another_user_administrative_permissions(as_guest, monkeypatch, roles, database):
    monkeypatch.setattr(Config, 'ADMIN_USERNAME', 'administrator@idir')
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    monkeypatch.setattr(middleware, "decode_keycloak_access_token", _get_administrative_user_from_database)
    resp = as_guest.post(Config.URL_PREFIX + "/api/v1/admin/users/john%40idir/roles",
                         json={"role_name": "administrator"},
                        follow_redirects=True,
                        content_type="application/json",
                        headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    assert resp.status_code == 201
    record = database.session.query(UserRole) \
        .filter(UserRole.role_name == 'administrator') \
        .filter(UserRole.user_guid == 'john@idir') \
        .first()
    assert record.role_name == 'administrator'
    assert record.user_guid == 'john@idir'
    

def test_administrators_have_no_user_roles_get_method(as_guest):
    resp = as_guest.get(Config.URL_PREFIX + "/api/v1/admin/users/larry%40idir/roles/officer",
                        follow_redirects=True,
                        content_type="application/json",
                        headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    assert resp.status_code == 405


def _get_keycloak_access_token() -> str:
    return 'some-secret-access-token'


def _get_keycloak_auth_header(access_token) -> dict:
    return dict({
        'Authorization': 'Bearer {}'.format(access_token)
    })


def _mock_keycloak_certificates(**kwargs) -> tuple:
    logging.warning("inside _mock_keycloak_certificates()")
    return True, kwargs


def _get_authorized_user(**kwargs) -> tuple:
    logging.warning("inside _get_authorized_user()")
    kwargs['decoded_access_token'] = {'preferred_username': 'larry@idir','display_name':'Larry test',
                                      'identity_provider':'idir'}
    return True, kwargs


def _get_administrative_user_from_database(**kwargs) -> tuple:
    kwargs['decoded_access_token'] = {'preferred_username': 'mo@idir','display_name':'Mo test',
                                      'identity_provider':'idir'}
    return True, kwargs
