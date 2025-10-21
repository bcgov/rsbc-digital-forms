import pytest
from flask import Flask, jsonify
from python.prohibition_web_svc.blueprints import files

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(files.bp)
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()


# -------------------- Helper functions for monkeypatch --------------------
def fake_middle_logic_success(*args, **kwargs):
    return True, {'response': jsonify({'message': 'success'}), 'status': 200}

def fake_middle_logic_failure(*args, **kwargs):
    return False, {'response': jsonify({'error': 'failure'}), 'status': 500}


# -------------------- CREATE FILE --------------------
def test_create_file_success(client, monkeypatch):
    monkeypatch.setattr(files.helper, 'middle_logic', fake_middle_logic_success)
    response = client.post('/api/v1/files')
    assert response.status_code == 200
    assert b'success' in response.data

def test_create_file_failure(client, monkeypatch):
    monkeypatch.setattr(files.helper, 'middle_logic', fake_middle_logic_failure)
    response = client.post('/api/v1/files')
    assert response.status_code == 500
    assert b'failure' in response.data


# -------------------- DOWNLOAD FILE --------------------
def test_download_file_success(client, monkeypatch):
    monkeypatch.setattr(files.helper, 'middle_logic', fake_middle_logic_success)
    response = client.get('/api/v1/files/testfile.pdf')
    assert response.status_code == 200
    assert b'success' in response.data

def test_download_file_failure(client, monkeypatch):
    monkeypatch.setattr(files.helper, 'middle_logic', fake_middle_logic_failure)
    response = client.get('/api/v1/files/testfile.pdf')
    assert response.status_code == 500
    assert b'failure' in response.data


# -------------------- PRESIGNED URL --------------------
def test_presigned_url_success(client, monkeypatch):
    monkeypatch.setattr(files.helper, 'middle_logic', fake_middle_logic_success)
    response = client.get('/api/v1/files/url/testfile.pdf?expiry=3600')
    assert response.status_code == 200
    assert b'success' in response.data

def test_presigned_url_failure(client, monkeypatch):
    monkeypatch.setattr(files.helper, 'middle_logic', fake_middle_logic_failure)
    response = client.get('/api/v1/files/url/testfile.pdf?expiry=3600')
    assert response.status_code == 500
    assert b'failure' in response.data


# -------------------- LIST FILES --------------------
def test_list_all_files_success(client, monkeypatch):
    monkeypatch.setattr(files.helper, 'middle_logic', fake_middle_logic_success)
    response = client.get('/api/v1/files?prefix=docs/')
    assert response.status_code == 200
    assert b'success' in response.data

def test_list_all_files_failure(client, monkeypatch):
    monkeypatch.setattr(files.helper, 'middle_logic', fake_middle_logic_failure)
    response = client.get('/api/v1/files?prefix=docs/')
    assert response.status_code == 500
    assert b'failure' in response.data


# -------------------- DELETE FILE --------------------
def test_remove_file_success(client, monkeypatch):
    monkeypatch.setattr(files.helper, 'middle_logic', fake_middle_logic_success)
    response = client.delete('/api/v1/files/testfile.pdf')
    assert response.status_code == 200
    assert b'success' in response.data

def test_remove_file_failure(client, monkeypatch):
    monkeypatch.setattr(files.helper, 'middle_logic', fake_middle_logic_failure)
    response = client.delete('/api/v1/files/testfile.pdf')
    assert response.status_code == 500
    assert b'failure' in response.data
