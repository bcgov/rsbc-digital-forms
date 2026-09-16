import json

import pytest
from flask import Flask

from python.prohibition_web_svc.blueprints import admin_users as admin_users_blueprint


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.register_blueprint(admin_users_blueprint.bp)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def mock_middle_logic_returning(status_code, body):
    def _mock(*args, **kwargs):
        return {'response': (json.dumps(body), status_code, {'Content-Type': 'application/json'})}

    return _mock


class TestIndexGetAllUsers:
    """Test GET /api/v1/admin/users"""

    def test_returns_200_with_users_list(self, client, monkeypatch):
        monkeypatch.setattr(
            'python.common.helper.middle_logic',
            mock_middle_logic_returning(200, {'users': [{'username': 'user1'}, {'username': 'user2'}]}),
        )
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: []
        )
        response = client.get('/api/v1/admin/users')
        assert response.status_code == 200
        assert b'users' in response.data

    def test_unauthorized_returns_401(self, client, monkeypatch):
        monkeypatch.setattr(
            'python.common.helper.middle_logic',
            mock_middle_logic_returning(401, {'error': 'unauthorized'}),
        )
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: []
        )
        response = client.get('/api/v1/admin/users')
        assert response.status_code == 401

    def test_forbidden_returns_403(self, client, monkeypatch):
        monkeypatch.setattr(
            'python.common.helper.middle_logic',
            mock_middle_logic_returning(403, {'error': 'forbidden'}),
        )
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: []
        )
        response = client.get('/api/v1/admin/users')
        assert response.status_code == 403

    def test_server_error_returns_500(self, client, monkeypatch):
        monkeypatch.setattr(
            'python.common.helper.middle_logic',
            mock_middle_logic_returning(500, {'error': 'server error'}),
        )
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: []
        )
        response = client.get('/api/v1/admin/users')
        assert response.status_code == 500


class TestUpdateUserPatch:
    """Test PATCH /api/v1/admin/users/<username>"""

    def test_update_user_not_implemented(self, client):
        response = client.patch('/api/v1/admin/users/user1')
        assert response.status_code == 405
        body = json.loads(response.data)
        assert body['error'] == 'method not implemented'


class TestDeleteUser:
    """Test DELETE /api/v1/admin/users/<username>"""

    def test_delete_user_not_implemented(self, client):
        response = client.delete('/api/v1/admin/users/user1')
        assert response.status_code == 405
        body = json.loads(response.data)
        assert body['error'] == 'method not implemented'


class TestCreateUser:
    """Test POST /api/v1/admin/users"""

    def test_create_user_success_returns_201(self, client, monkeypatch):
        monkeypatch.setattr(
            'python.common.helper.middle_logic',
            mock_middle_logic_returning(201, {'username': 'newuser', 'roles': ['user']}),
        )
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: []
        )
        payload = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'first_name': 'New',
            'last_name': 'User',
        }
        response = client.post(
            '/api/v1/admin/users', data=json.dumps(payload), content_type='application/json'
        )
        assert response.status_code == 201
        assert b'newuser' in response.data

    def test_create_user_no_payload_returns_400(self, client, monkeypatch):
        monkeypatch.setattr(
            'python.common.helper.middle_logic',
            mock_middle_logic_returning(400, {'error': 'no payload'}),
        )
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: []
        )
        response = client.post('/api/v1/admin/users', data='', content_type='application/json')
        assert response.status_code == 400

    def test_create_user_validation_failure_returns_400(self, client, monkeypatch):
        monkeypatch.setattr(
            'python.common.helper.middle_logic',
            mock_middle_logic_returning(400, {'message': 'failed validation', 'errors': ['invalid email']}),
        )
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: []
        )
        payload = {'username': 'newuser', 'email': 'invalid-email'}
        response = client.post(
            '/api/v1/admin/users', data=json.dumps(payload), content_type='application/json'
        )
        assert response.status_code == 400
        assert b'validation' in response.data or b'errors' in response.data

    def test_create_user_unauthorized_returns_401(self, client, monkeypatch):
        monkeypatch.setattr(
            'python.common.helper.middle_logic',
            mock_middle_logic_returning(401, {'error': 'unauthorized'}),
        )
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: []
        )
        payload = {'username': 'newuser'}
        response = client.post(
            '/api/v1/admin/users', data=json.dumps(payload), content_type='application/json'
        )
        assert response.status_code == 401

    def test_create_user_server_error_returns_500(self, client, monkeypatch):
        monkeypatch.setattr(
            'python.common.helper.middle_logic',
            mock_middle_logic_returning(500, {'error': 'server error'}),
        )
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: []
        )
        payload = {'username': 'newuser'}
        response = client.post(
            '/api/v1/admin/users', data=json.dumps(payload), content_type='application/json'
        )
        assert response.status_code == 500


class TestGetUserDetails:
    """Test GET /api/v1/admin/users/<username>"""

    def test_get_user_details_not_implemented(self, client):
        response = client.get('/api/v1/admin/users/user1')
        assert response.status_code == 405
        body = json.loads(response.data)
        assert body['error'] == 'method not implemented'
