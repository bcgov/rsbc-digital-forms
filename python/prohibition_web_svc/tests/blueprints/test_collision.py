import pytest
from flask import Flask
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
        return {'response': ('{"message": "created"}', 201, {'Content-Type': 'application/json'})}
    monkeypatch.setattr(collision_blueprint, 'middle_logic', fake_middle_logic)
    monkeypatch.setattr(collision_blueprint, 'get_authorized_keycloak_user', lambda: [])
    response = client.post('/api/v1/collision', json={"foo": "bar"})
    assert response.status_code == 201
    assert b'created' in response.data

def test_create_collision_bad_request(client, monkeypatch):
    # Patch middle_logic to simulate a bad request
    def fake_middle_logic(*args, **kwargs):
        return {'response': ('{"error": "bad request"}', 400, {'Content-Type': 'application/json'})}
    monkeypatch.setattr(collision_blueprint, 'middle_logic', fake_middle_logic)
    monkeypatch.setattr(collision_blueprint, 'get_authorized_keycloak_user', lambda: [])
    response = client.post('/api/v1/collision', json={})
    assert response.status_code == 400
    assert b'bad request' in response.data

def test_create_collision_server_error(client, monkeypatch):
    # Patch middle_logic to simulate a server error
    def fake_middle_logic(*args, **kwargs):
        return {'response': ('{"error": "server error"}', 500, {'Content-Type': 'application/json'})}
    monkeypatch.setattr(collision_blueprint, 'middle_logic', fake_middle_logic)
    monkeypatch.setattr(collision_blueprint, 'get_authorized_keycloak_user', lambda: [])
    response = client.post('/api/v1/collision', json={})
    assert response.status_code == 500
    assert b'server error' in response.data

def test_get_collision_success(client, monkeypatch):
    # Patch middle_logic to simulate a successful retrieval
    def fake_middle_logic(*args, **kwargs):
        return {'response': ('{"message": "retrieved"}', 200, {'Content-Type': 'application/json'})}
    monkeypatch.setattr(collision_blueprint, 'middle_logic', fake_middle_logic)
    monkeypatch.setattr(collision_blueprint, 'get_authorized_keycloak_user', lambda: [])
    response = client.get('/api/v1/collision/1')
    assert response.status_code == 200
    assert b'retrieved' in response.data
