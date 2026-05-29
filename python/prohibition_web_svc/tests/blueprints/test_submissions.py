import pytest
import json
from flask import Flask
from python.prohibition_web_svc.blueprints import submissions as submissions_blueprint
from python.prohibition_web_svc.config import Config


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['URL_PREFIX'] = '/api/v1'
    app.register_blueprint(submissions_blueprint.bp)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


class TestSubmissionsBlueprint:

    def test_update_event_status_success(self, client, monkeypatch):
        """Test successful PATCH /submission/event/status request."""
        def mock_middle_logic(*args, **kwargs):
            from flask import make_response
            mock_response = make_response(
                '{"submission_event_id": 1, "destination": "VIPS", "status": "sent"}', 200
            )
            mock_response.headers['Content-Type'] = 'application/json'
            return {'response': mock_response}

        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user',
            lambda: [],
        )

        payload = {'ff_application_id': 'app-001', 'form_id': 'VI123', 'destination': 'VIPS', 'status': 'sent'}
        response = client.patch(
            '/api/v1/submission/event/status',
            data=json.dumps(payload),
            content_type='application/json',
        )
        assert response.status_code == 200
        assert b'submission_event_id' in response.data
        assert b'sent' in response.data

    def test_update_event_status_missing_payload(self, client, monkeypatch):
        """Test PATCH /submission/event/status returns 400 when payload is missing required fields."""
        def mock_middle_logic(*args, **kwargs):
            from flask import make_response
            mock_response = make_response('{"error": "bad request"}', 400)
            mock_response.headers['Content-Type'] = 'application/json'
            return {'response': mock_response}

        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user',
            lambda: [],
        )

        response = client.patch(
            '/api/v1/submission/event/status',
            data=json.dumps({'ff_application_id': 'app-001'}),
            content_type='application/json',
        )
        assert response.status_code == 400

    def test_update_event_status_not_found(self, client, monkeypatch):
        """Test PATCH /submission/event/status returns 400 when submission or event is not found."""
        def mock_middle_logic(*args, **kwargs):
            from flask import make_response
            mock_response = make_response('{"error": "record not found"}', 400)
            mock_response.headers['Content-Type'] = 'application/json'
            return {'response': mock_response}

        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user',
            lambda: [],
        )

        payload = {'ff_application_id': 'nonexistent', 'form_id': 'VI123', 'destination': 'VIPS', 'status': 'sent'}
        response = client.patch(
            '/api/v1/submission/event/status',
            data=json.dumps(payload),
            content_type='application/json',
        )
        assert response.status_code == 400
        assert b'record not found' in response.data

    def test_update_event_status_server_error(self, client, monkeypatch):
        """Test PATCH /submission/event/status returns 500 on commit failure."""
        def mock_middle_logic(*args, **kwargs):
            from flask import make_response
            mock_response = make_response('{"error": "server error"}', 500)
            mock_response.headers['Content-Type'] = 'application/json'
            return {'response': mock_response}

        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user',
            lambda: [],
        )

        payload = {'ff_application_id': 'app-001', 'form_id': 'VI123', 'destination': 'VIPS', 'status': 'sent'}
        response = client.patch(
            '/api/v1/submission/event/status',
            data=json.dumps(payload),
            content_type='application/json',
        )
        assert response.status_code == 500

    def test_update_event_status_middleware_chain(self, client, monkeypatch):
        """Test that PATCH /submission/event/status triggers the expected middleware chain."""
        call_order = []

        def mock_middle_logic(middleware_chain, **kwargs):
            for item in middleware_chain:
                if isinstance(item, dict) and 'try' in item:
                    name = item['try'].__name__ if hasattr(item['try'], '__name__') else str(item['try'])
                    call_order.append(name)
            from flask import make_response
            mock_response = make_response('{"status": "sent"}', 200)
            mock_response.headers['Content-Type'] = 'application/json'
            return {'response': mock_response}

        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr(
            'python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user',
            lambda: [],
        )

        payload = {'ff_application_id': 'app-001', 'form_id': 'VI123', 'destination': 'VIPS', 'status': 'sent'}
        response = client.patch(
            '/api/v1/submission/event/status',
            data=json.dumps(payload),
            content_type='application/json',
        )
        assert response.status_code == 200
        assert 'validate_update_event_status_payload' in call_order
        assert 'update_submission_event_status' in call_order
        assert 'commit_transaction' in call_order
        assert call_order.index('validate_update_event_status_payload') < call_order.index('update_submission_event_status')
        assert call_order.index('update_submission_event_status') < call_order.index('commit_transaction')

    def test_blueprint_registration(self, app):
        """Test that the submissions blueprint is properly registered."""
        assert 'submission' in app.blueprints
        blueprint = app.blueprints['submission']
        assert blueprint.url_prefix == '/api/v1'
        assert blueprint.name == 'submission'
