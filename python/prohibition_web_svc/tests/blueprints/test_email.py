import logging
import pytest
from flask import Flask, make_response
from python.prohibition_web_svc.blueprints import email as email_blueprint

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.register_blueprint(email_blueprint.bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_send_email_success(client, monkeypatch):
    # Patch middle_logic to simulate a successful flow
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response('{"message": "created"}', 201)}
    monkeypatch.setattr(email_blueprint, 'middle_logic', fake_middle_logic)
    monkeypatch.setattr(email_blueprint, 'get_authorized_keycloak_user', lambda: [])
    response = client.post('/api/v1/email', json={"foo": "bar"})
    logging.debug(response)
    assert response.status_code == 201
    assert b'created' in response.data

def test_send_email_bad_request(client, monkeypatch):
    # Patch middle_logic to simulate a bad request
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response('{"error": "bad request"}', 400)}
    monkeypatch.setattr(email_blueprint, 'middle_logic', fake_middle_logic)
    monkeypatch.setattr(email_blueprint, 'get_authorized_keycloak_user', lambda: [])
    response = client.post('/api/v1/email', json={})
    assert response.status_code == 400
    assert b'bad request' in response.data

def test_send_email_server_error(client, monkeypatch):
    # Patch middle_logic to simulate a server error
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response('{"error": "server error"}', 500)}        
    monkeypatch.setattr(email_blueprint, 'middle_logic', fake_middle_logic)
    monkeypatch.setattr(email_blueprint, 'get_authorized_keycloak_user', lambda: [])
    response = client.post('/api/v1/email', json={})
    assert response.status_code == 500
    assert b'server error' in response.data


