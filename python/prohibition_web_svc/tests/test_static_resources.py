import pytest
import logging
import responses
import json
from datetime import datetime
import python.prohibition_web_svc.middleware.keycloak_middleware as middleware
from python.prohibition_web_svc.models import db, UserRole, User, Form
from python.prohibition_web_svc.app import create_app
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
def test_unauthorized_can_get_agencies(as_guest, monkeypatch, roles):
    responses.add(responses.POST, "{}:{}/services/collector".format(
        Config.SPLUNK_HOST, Config.SPLUNK_PORT), status=200)

    resp = as_guest.get(Config.URL_PREFIX + "/api/v1/static/agencies",
                        follow_redirects=True,
                        content_type="application/json")
    assert resp.status_code == 200
    assert "AB" in resp.json[0]['vjur']
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'get static resource',
            'resource': 'agencies',
            'user_guid': '',
            'username': ''
        },
        'source': 'be78d6'
    })


@responses.activate
def test_unauthorized_user_gets_impound_lot_operators(as_guest, monkeypatch, roles):
    responses.add(responses.POST, "{}:{}/services/collector".format(
        Config.SPLUNK_HOST, Config.SPLUNK_PORT), status=200)

    resp = as_guest.get(Config.URL_PREFIX + "/api/v1/static/impound_lot_operators",
                        follow_redirects=True,
                        content_type="application/json")
    assert resp.status_code == 200
    assert "24 HOUR TOWING" in resp.json[0]['name']
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'get static resource',
            'resource': 'impound_lot_operators',
            'user_guid': '',
            'username': ''
        },
        'source': 'be78d6'
    })


@responses.activate
def test_unauthorized_user_gets_provinces(as_guest, monkeypatch, roles):
    responses.add(responses.POST, "{}:{}/services/collector".format(
        Config.SPLUNK_HOST, Config.SPLUNK_PORT), status=200)

    resp = as_guest.get(Config.URL_PREFIX + "/api/v1/static/provinces",
                        follow_redirects=True,
                        content_type="application/json")
    assert resp.status_code == 200
    assert 'objectCd' in resp.json[2]
    assert 'objectDsc' in resp.json[2]
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'get static resource',
            'resource': 'provinces',
            'user_guid': '',
            'username': ''
        },
        'source': 'be78d6'
    })


@responses.activate
def test_unauthorized_user_gets_jurisdictions(as_guest, monkeypatch, roles):
    responses.add(responses.POST, "{}:{}/services/collector".format(
        Config.SPLUNK_HOST, Config.SPLUNK_PORT), status=200)
    resp = as_guest.get(Config.URL_PREFIX + "/api/v1/static/jurisdictions",
                        follow_redirects=True,
                        content_type="application/json")
    assert resp.status_code == 200
    assert {'id': 7,"objectCd": "BC", "objectDsc": "BRITISH COLUMBIA"} in resp.json
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'get static resource',
            'resource': 'jurisdictions',
            'user_guid': '',
            'username': ''
        },
        'source': 'be78d6'
    })


@responses.activate
def test_unauthorized_user_can_get_countries(as_guest, monkeypatch, roles):
    responses.add(responses.POST, "{}:{}/services/collector".format(
        Config.SPLUNK_HOST, Config.SPLUNK_PORT), status=200)
    resp = as_guest.get(Config.URL_PREFIX + "/api/v1/static/countries",
                        follow_redirects=True,
                        content_type="application/json")
    assert resp.status_code == 200
    assert 'objectCd' in resp.json[2]
    assert 'objectDsc' in resp.json[2]
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'get static resource',
            'resource': 'countries',
            'user_guid': '',
            'username': ''
        },
        'source': 'be78d6'
    })


@responses.activate
def test_unauthorized_user_gets_cities(as_guest, monkeypatch, roles):
    responses.add(responses.POST, "{}:{}/services/collector".format(
        Config.SPLUNK_HOST, Config.SPLUNK_PORT), status=200)

    resp = as_guest.get(Config.URL_PREFIX + "/api/v1/static/cities",
                        follow_redirects=True,
                        content_type="application/json")
    assert resp.status_code == 200
    assert {'id': 1,'objectCd': 'OHMH', 'objectDsc': '100 MILE HOUSE'} in resp.json
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'get static resource',
            'resource': 'cities',
            'user_guid': '',
            'username': ''
        },
        'source': 'be78d6'
    })


@responses.activate
def test_unauthorized_user_can_get_vehicles(as_guest, monkeypatch, roles):
    resp = as_guest.get(Config.URL_PREFIX + "/api/v1/static/vehicles",
                        follow_redirects=True,
                        content_type="application/json")
    assert resp.status_code == 200
    assert "AC" == resp.json[0]['mk']
    assert "A C (GREAT BRITAIN)" == resp.json[0]['search']
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'get static resource',
            'resource': 'vehicles',
            'user_guid': '',
            'username': ''
        },
        'source': 'be78d6'
    })


@responses.activate
def test_unauthorized_user_can_get_vehicle_styles(as_guest, monkeypatch, roles):
    resp = as_guest.get(Config.URL_PREFIX + "/api/v1/static/vehicle_styles",
                        follow_redirects=True,
                        content_type="application/json")
    assert resp.status_code == 200
    assert {"code": "2DR", "name": "2-DOOR SEDAN"} == resp.json[0]
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'get static resource',
            'resource': 'vehicle_styles',
            'user_guid': '',
            'username': ''
        },
        'source': 'be78d6'
    })


@responses.activate
def test_unauthorized_user_can_get_keycloak_config(as_guest):
    resp = as_guest.get(Config.URL_PREFIX + "/api/v1/static/keycloak",
                        follow_redirects=True,
                        content_type="application/json")
    assert resp.status_code == 200
    assert 'realm' in resp.json
    assert 'url' in resp.json
    assert 'clientId' in resp.json
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'get static resource',
            'resource': 'keycloak',
            'user_guid': '',
            'username': ''
        },
        'source': 'be78d6'
    })


@responses.activate
def test_unauthorized_user_can_get_configuration(as_guest):
    resp = as_guest.get(Config.URL_PREFIX + "/api/v1/static/configuration",
                        follow_redirects=True,
                        content_type="application/json")
    assert resp.status_code == 200
    assert resp.json == {
        "environment": "dev"
    }
    assert responses.calls[0].request.body.decode() == json.dumps({
        'event': {
            'event': 'get static resource',
            'resource': 'configuration',
            'user_guid': '',
            'username': ''
        },
        'source': 'be78d6'
    })


def _get_unauthorized_user(**kwargs) -> tuple:
    logging.warning("inside _get_unauthorized_user()")
    kwargs['decoded_access_token'] = {'preferred_username': 'john@idir'}  # keycloak username
    return True, kwargs


def _get_authorized_user(**kwargs) -> tuple:
    logging.warning("inside _get_authorized_user()")
    kwargs['decoded_access_token'] = {'preferred_username': ''}  # keycloak username
    return True, kwargs


def _get_keycloak_access_token() -> str:
    return 'some-secret-access-token'


def _get_keycloak_auth_header(access_token) -> dict:
    return dict({
        'Authorization': 'Bearer {}'.format(access_token)
    })


def _mock_keycloak_certificates(**kwargs) -> tuple:
    logging.warning("inside _mock_keycloak_certificates()")
    return True, kwargs