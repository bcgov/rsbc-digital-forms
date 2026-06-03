import json
import pytest
from flask import Flask
from python.prohibition_web_svc.blueprints import detachments as detachments_blueprint
from python.prohibition_web_svc.config import Config


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.register_blueprint(detachments_blueprint.bp)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def mock_middle_logic_returning(status_code, body):
    def _mock(*args, **kwargs):
        return {'response': (json.dumps(body), status_code, {'Content-Type': 'application/json'})}
    return _mock


class TestListDetachments:
    def test_returns_200_with_detachments(self, client, monkeypatch):
        monkeypatch.setattr(
            'python.common.helper.middle_logic',
            mock_middle_logic_returning(200, {'detachments': [{'id': 1, 'agency_name': 'Vancouver'}]}),
        )
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: []
        )
        response = client.get('/api/v1/detachments')
        assert response.status_code == 200
        assert b'detachments' in response.data

    def test_unauthorized_returns_401(self, client, monkeypatch):
        monkeypatch.setattr(
            'python.common.helper.middle_logic',
            mock_middle_logic_returning(401, {'error': 'unauthorized'}),
        )
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: []
        )
        response = client.get('/api/v1/detachments')
        assert response.status_code == 401

    def test_server_error_returns_500(self, client, monkeypatch):
        monkeypatch.setattr(
            'python.common.helper.middle_logic',
            mock_middle_logic_returning(500, {'error': 'server error'}),
        )
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: []
        )
        response = client.get('/api/v1/detachments')
        assert response.status_code == 500


class TestCreateDetachmentChangeRequest:
    def _valid_payload(self):
        return {
            'officer_id': 'officer-1',
            'new_detachment_id': 2,
            'reason': 'OVERTIME_ASSIGNMENT',
            'comments': 'Working overtime at another detachment',
        }

    def test_happy_path_returns_201(self, client, monkeypatch):
        monkeypatch.setattr(
            'python.common.helper.middle_logic',
            mock_middle_logic_returning(201, {
                'previous_detachment': {'id': 1},
                'new_detachment': {'id': 2, 'agency_name': 'Burnaby'},
                'updated_at': '2026-06-01T10:00:00',
                'session_refreshed': True,
            }),
        )
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: []
        )
        response = client.post(
            '/api/v1/detachment-change-request',
            data=json.dumps(self._valid_payload()),
            content_type='application/json',
        )
        assert response.status_code == 201
        assert b'session_refreshed' in response.data

    def test_no_payload_returns_400(self, client, monkeypatch):
        monkeypatch.setattr(
            'python.common.helper.middle_logic',
            mock_middle_logic_returning(400, {'error': 'no payload'}),
        )
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: []
        )
        response = client.post('/api/v1/detachment-change-request', content_type='application/json')
        assert response.status_code == 400

    def test_duplicate_request_returns_400(self, client, monkeypatch):
        monkeypatch.setattr(
            'python.common.helper.middle_logic',
            mock_middle_logic_returning(400, {'error': 'new detachment is same as current detachment'}),
        )
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: []
        )
        payload = self._valid_payload()
        payload['new_detachment_id'] = 1  # same as current
        response = client.post(
            '/api/v1/detachment-change-request',
            data=json.dumps(payload),
            content_type='application/json',
        )
        assert response.status_code == 400
        assert b'same as current' in response.data

    def test_unauthorized_detachment_returns_403(self, client, monkeypatch):
        monkeypatch.setattr(
            'python.common.helper.middle_logic',
            mock_middle_logic_returning(403, {'error': 'not authorized to change this officer detachment'}),
        )
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: []
        )
        payload = self._valid_payload()
        payload['officer_id'] = 'someone-else'
        response = client.post(
            '/api/v1/detachment-change-request',
            data=json.dumps(payload),
            content_type='application/json',
        )
        assert response.status_code == 403

    def test_inactive_detachment_returns_400(self, client, monkeypatch):
        monkeypatch.setattr(
            'python.common.helper.middle_logic',
            mock_middle_logic_returning(400, {'error': 'detachment not found'}),
        )
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: []
        )
        payload = self._valid_payload()
        payload['new_detachment_id'] = 9999  # non-existent
        response = client.post(
            '/api/v1/detachment-change-request',
            data=json.dumps(payload),
            content_type='application/json',
        )
        assert response.status_code == 400
        assert b'detachment not found' in response.data

    def test_concurrent_conflict_returns_409(self, client, monkeypatch):
        monkeypatch.setattr(
            'python.common.helper.middle_logic',
            mock_middle_logic_returning(409, {'error': 'detachment was changed by a concurrent request'}),
        )
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: []
        )
        response = client.post(
            '/api/v1/detachment-change-request',
            data=json.dumps(self._valid_payload()),
            content_type='application/json',
        )
        assert response.status_code == 409

    def test_invalid_reason_returns_400(self, client, monkeypatch):
        monkeypatch.setattr(
            'python.common.helper.middle_logic',
            mock_middle_logic_returning(400, {'message': 'failed validation', 'errors': {'reason': ['unallowed value']}}),
        )
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: []
        )
        payload = self._valid_payload()
        payload['reason'] = 'NOT_A_REASON'
        response = client.post(
            '/api/v1/detachment-change-request',
            data=json.dumps(payload),
            content_type='application/json',
        )
        assert response.status_code == 400

    def test_blueprint_registered(self, app):
        assert 'detachments' in app.blueprints
