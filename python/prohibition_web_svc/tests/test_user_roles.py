import pytest
from datetime import datetime
import responses
import python.prohibition_web_svc.middleware.keycloak_middleware as middleware
from python.prohibition_web_svc.models import db, UserRole, User, Form
from python.prohibition_web_svc.app import create_app
from python.prohibition_web_svc.config import Config, TestConfig
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
            login='larry@idir')
    ]
    db.session.bulk_save_objects(users)
    db.session.commit() 
    return users

@pytest.fixture
def roles(database, clean_db, users):
    today = datetime.strptime("2021-07-21", "%Y-%m-%d")
    user_role = [
        UserRole(user_guid='john@idir', role_name='officer', submitted_dt=today),
        UserRole(user_guid='larry@idir', role_name='officer', submitted_dt=today, approved_dt=today)
    ]
    db.session.bulk_save_objects(user_role)
    db.session.commit()


@responses.activate
def test_user_without_authorization_cannot_view_their_user_roles(as_guest, monkeypatch, roles):
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    monkeypatch.setattr(middleware, "decode_keycloak_access_token", _get_keycloak_user_who_has_not_applied)
    resp = as_guest.get(Config.URL_PREFIX + "/api/v1/user_roles",
                        follow_redirects=True,
                        content_type="application/json",
                        headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    assert resp.status_code == 401
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'permission denied',
            'user_guid': 'new-officer@idir',
            'username': 'new-officer@idir'
        },
        'source': 'be78d6'
    })


@responses.activate
def test_user_with_authorization_can_view_see_their_own_user_roles(as_guest, monkeypatch, roles):
    monkeypatch.setattr(middleware, "get_keycloak_certificates", _mock_keycloak_certificates)
    monkeypatch.setattr(middleware, "decode_keycloak_access_token", _get_authorized_user)
    resp = as_guest.get(Config.URL_PREFIX + "/api/v1/user_roles",
                        follow_redirects=True,
                        content_type="application/json",
                        headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    logging.debug(json.dumps(resp.json))
    assert len(resp.json) == 1
    assert resp.json[0]['role_name'] == 'officer'
    assert resp.status_code == 200
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'get user-role',
            'user_guid': 'larry@idir',
            'username': 'larry@idir'
        },
        'source': 'be78d6'
    })


def test_get_method_not_implemented(as_guest):
    resp = as_guest.get(Config.URL_PREFIX + "/api/v1/user_roles/officer",
                        follow_redirects=True,
                        content_type="application/json",
                        headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    assert resp.status_code == 405


def test_update_method_not_implemented(as_guest):
    resp = as_guest.patch(Config.URL_PREFIX + "/api/v1/user_roles/officer",
                          follow_redirects=True,
                          content_type="application/json",
                          headers=_get_keycloak_auth_header(_get_keycloak_access_token()))
    assert resp.status_code == 405


def test_delete_method_not_implemented(as_guest):
    resp = as_guest.delete(Config.URL_PREFIX + "/api/v1/user_roles/officer",
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
                                      'identity_provider':'idir' }  # keycloak username
    return True, kwargs


def _get_keycloak_user_who_has_not_applied(**kwargs) -> tuple:
    logging.warning("inside _get_unauthorized_user()")
    kwargs['decoded_access_token'] = {'preferred_username': 'new-officer@idir','display_name':'New test',
                                      'identity_provider':'idir'}  # keycloak username
    return True, kwargs

