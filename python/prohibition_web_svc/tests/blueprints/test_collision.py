import logging
import pytest
from flask import Flask, make_response
from python.prohibition_web_svc.blueprints import collision as collision_blueprint

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.register_blueprint(collision_blueprint.bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_collision_success(client, monkeypatch):
    # Patch middle_logic to simulate a successful flow
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response('{"message": "created"}', 201)}
    monkeypatch.setattr(collision_blueprint, 'middle_logic', fake_middle_logic)
    monkeypatch.setattr(collision_blueprint, 'get_authorized_keycloak_user', lambda: [])
    response = client.post('/api/v1/collision', json={"foo": "bar"})
    logging.debug(response)
    assert response.status_code == 201
    assert b'created' in response.data

def test_create_collision_bad_request(client, monkeypatch):
    # Patch middle_logic to simulate a bad request
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response('{"error": "bad request"}', 400)}
    monkeypatch.setattr(collision_blueprint, 'middle_logic', fake_middle_logic)
    monkeypatch.setattr(collision_blueprint, 'get_authorized_keycloak_user', lambda: [])
    response = client.post('/api/v1/collision', json={})
    assert response.status_code == 400
    assert b'bad request' in response.data

def test_create_collision_server_error(client, monkeypatch):
    # Patch middle_logic to simulate a server error
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response('{"error": "server error"}', 500)}        
    monkeypatch.setattr(collision_blueprint, 'middle_logic', fake_middle_logic)
    monkeypatch.setattr(collision_blueprint, 'get_authorized_keycloak_user', lambda: [])
    response = client.post('/api/v1/collision', json={})
    assert response.status_code == 500
    assert b'server error' in response.data

def test_create_collision_middleware_chain_execution_order(client, monkeypatch):
    call_order = []

    def fake_middle_logic(middleware_chain, **kwargs):
        for item in middleware_chain:
            if isinstance(item, dict) and 'try' in item:
                call_order.append(item['try'].__name__ if hasattr(item['try'], '__name__') else str(item['try']))
        return {'response': make_response('{"success": true}', 201)}

    monkeypatch.setattr(collision_blueprint, 'middle_logic', fake_middle_logic)
    monkeypatch.setattr(collision_blueprint, 'get_authorized_keycloak_user', lambda: [])

    response = client.post('/api/v1/collision', json={"collision_case_num": "RZ100001"})

    assert response.status_code == 201
    assert 'save_collision_data' in call_order
    assert 'save_event_pdf' in call_order
    assert 'commit_transaction' in call_order
    assert call_order.index('save_collision_data') < call_order.index('commit_transaction')
    assert call_order.index('save_event_pdf') < call_order.index('commit_transaction')

def test_get_collision_success(client, monkeypatch):
    # Patch middle_logic to simulate a successful retrieval
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response('{"message": "retrieved"}', 200)}
    monkeypatch.setattr(collision_blueprint, 'middle_logic', fake_middle_logic)
    monkeypatch.setattr(collision_blueprint, 'get_authorized_keycloak_user', lambda: [])
    response = client.get('/api/v1/collision/1')
    assert response.status_code == 200
    assert b'retrieved' in response.data
