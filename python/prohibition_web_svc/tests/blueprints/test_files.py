import pytest
from flask import Flask ,make_response
from python.prohibition_web_svc.blueprints import files as files_blueprint

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(files_blueprint.bp)
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

# -------------------- CREATE FILE --------------------
def test_create_file_success(client, monkeypatch):
    # Patch middle_logic to simulate a successful flow
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response('{"message": "created"}', 201)}
    monkeypatch.setattr(files_blueprint, 'middle_logic', fake_middle_logic)
    response = client.post('/api/v1/files')
    assert response.status_code == 201
    assert b'success' in response.data

def test_create_file_failure(client, monkeypatch):
    # Patch middle_logic to simulate a server error
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response('{"error": "server error"}', 500)}    
    monkeypatch.setattr(files_blueprint, 'middle_logic', fake_middle_logic)
    response = client.post('/api/v1/files')
    assert response.status_code == 500
    assert b'server error' in response.data


# -------------------- DOWNLOAD FILE --------------------
def test_download_file_success(client, monkeypatch):
    # Patch middle_logic to simulate a successful flow
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response('{"message": "success"}', 200)}
    monkeypatch.setattr(files_blueprint, 'middle_logic', fake_middle_logic)
    response = client.get('/api/v1/files/testfile.pdf')
    assert response.status_code == 200
    assert b'success' in response.data

def test_download_file_failure(client, monkeypatch):
    # Patch middle_logic to simulate a server error
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response('{"error": "server error"}', 500)}    
    monkeypatch.setattr(files_blueprint, 'middle_logic', fake_middle_logic)
    response = client.get('/api/v1/files/testfile.pdf')
    assert response.status_code == 500
    assert b'server error' in response.data


# -------------------- PRESIGNED URL --------------------
def test_presigned_url_success(client, monkeypatch):
    # Patch middle_logic to simulate a server error
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response('{"error": "success"}', 200)}    
    monkeypatch.setattr(files_blueprint, 'middle_logic', fake_middle_logic)
    response = client.get('/api/v1/files/url/testfile.pdf?expiry=3600')
    assert response.status_code == 200
    assert b'success' in response.data

def test_presigned_url_failure(client, monkeypatch):
    # Patch middle_logic to simulate a server error
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response('{"error": "server error"}', 500)}   
    monkeypatch.setattr(files_blueprint, 'middle_logic', fake_middle_logic)
    response = client.get('/api/v1/files/url/testfile.pdf?expiry=3600')
    assert response.status_code == 500
    assert b'server error' in response.data


# -------------------- LIST FILES --------------------
def test_list_all_files_success(client, monkeypatch):
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response('{"error": "success"}', 200)} 
    monkeypatch.setattr(files_blueprint, 'middle_logic', fake_middle_logic)
    response = client.get('/api/v1/files?prefix=docs/')
    assert response.status_code == 200
    assert b'success' in response.data

def test_list_all_files_failure(client, monkeypatch):
    # Patch middle_logic to simulate a server error
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response('{"error": "server error"}', 500)}
    monkeypatch.setattr(files_blueprint, 'middle_logic', fake_middle_logic)
    response = client.get('/api/v1/files?prefix=docs/')
    assert response.status_code == 500
    assert b'server error' in response.data


# -------------------- DELETE FILE --------------------
def test_remove_file_success(client, monkeypatch):
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response('{"error": "success"}', 200)} 
    monkeypatch.setattr(files_blueprint, 'middle_logic', fake_middle_logic)
    response = client.delete('/api/v1/files/testfile.pdf')
    assert response.status_code == 200
    assert b'success' in response.data

def test_remove_file_failure(client, monkeypatch):
    # Patch middle_logic to simulate a server error
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response('{"error": "server error"}', 500)}   
    monkeypatch.setattr(files_blueprint, 'middle_logic', fake_middle_logic)
    response = client.delete('/api/v1/files/testfile.pdf')
    assert response.status_code == 500
    assert b'server error' in response.data
