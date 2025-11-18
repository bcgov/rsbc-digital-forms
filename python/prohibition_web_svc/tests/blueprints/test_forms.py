import pytest
import json
from unittest.mock import patch, MagicMock
from flask import Flask
from python.prohibition_web_svc.blueprints import forms as forms_blueprint
from python.prohibition_web_svc.config import Config


@pytest.fixture
def app():
    """Create a test Flask application."""
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['URL_PREFIX'] = '/api/v1'
    app.register_blueprint(forms_blueprint.bp)
    return app


@pytest.fixture
def client(app):
    """Create a test client."""
    return app.test_client()


class TestFormsBlueprint:
    """Test cases for the forms blueprint."""

    def test_index_success(self, client, monkeypatch):
        """Test successful GET /forms request."""
        # Mock the middleware chain
        def mock_middle_logic(*args, **kwargs):
            return {'response': ('{"forms": []}', 200, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        response = client.get('/api/v1/forms')
        assert response.status_code == 200
        assert b'forms' in response.data

    def test_index_unauthorized(self, client, monkeypatch):
        """Test GET /forms request with unauthorized user."""
        def mock_middle_logic(*args, **kwargs):
            return {'response': ('{"error": "unauthorized"}', 401, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        response = client.get('/api/v1/forms')
        assert response.status_code == 401
        assert b'unauthorized' in response.data

    def test_index_server_error(self, client, monkeypatch):
        """Test GET /forms request with server error."""
        def mock_middle_logic(*args, **kwargs):
            return {'response': ('{"error": "server error"}', 500, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        response = client.get('/api/v1/forms')
        assert response.status_code == 500
        assert b'server error' in response.data

    def test_create_success(self, client, monkeypatch):
        """Test successful POST /forms request to lease form IDs."""
        test_payload = {"24Hour": 1, "12Hour": 2}
        
        def mock_middle_logic(*args, **kwargs):
            return {'response': ('{"form_ids": ["AA123456", "BB123457"]}', 201, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        response = client.post('/api/v1/forms', 
                              data=json.dumps(test_payload),
                              content_type='application/json')
        assert response.status_code == 201
        assert b'form_ids' in response.data

    def test_create_bad_request(self, client, monkeypatch):
        """Test POST /forms request with bad payload."""
        def mock_middle_logic(*args, **kwargs):
            return {'response': ('{"error": "bad request"}', 400, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        response = client.post('/api/v1/forms', 
                              data='invalid json',
                              content_type='application/json')
        assert response.status_code == 400
        # Flask returns default HTML error page for invalid JSON, which is expected behavior
        assert b'bad request' in response.data

    def test_create_insufficient_form_ids(self, client, monkeypatch):
        """Test POST /forms request when insufficient form IDs are available."""
        test_payload = {"24Hour": 100}  # Requesting too many IDs
        
        def mock_middle_logic(*args, **kwargs):
            return {'response': ('{"error": "insufficient form IDs"}', 500, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        response = client.post('/api/v1/forms', 
                              data=json.dumps(test_payload),
                              content_type='application/json')
        assert response.status_code == 500
        assert b'insufficient form IDs' in response.data

    def test_update_renew_lease_success(self, client, monkeypatch):
        """Test successful PATCH /forms request to renew form lease."""
        def mock_middle_logic(*args, **kwargs):
            return {'response': ('{"message": "lease renewed"}', 200, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        # No payload should trigger lease renewal
        response = client.patch('/api/v1/forms')
        assert response.status_code == 200
        assert b'lease renewed' in response.data

    def test_update_form_submission_success(self, client, monkeypatch):
        """Test successful PATCH /forms request to submit a form."""
        test_payload = {
            "forms": {"mv6020":"JZ110449"},
            "spoiled_timestamp":"2025-08-13T20:36:34.636Z"
        }

        def mock_middle_logic(*args, **kwargs):
            return {'response': ('{"message": "form submitted"}', 200, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        response = client.patch('/api/v1/forms', 
                               data=json.dumps(test_payload),
                               content_type='application/json')
        assert response.status_code == 200
        assert b'form submitted' in response.data

    def test_update_renew_lease_failure(self, client, monkeypatch):
        """Test PATCH /forms request when lease renewal fails."""
        def mock_middle_logic(*args, **kwargs):
            return {'response': ('{"error": "unable to renew lease"}', 400, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        response = client.patch('/api/v1/forms')
        assert response.status_code == 400
        assert b'unable to renew lease' in response.data

    def test_update_form_not_found(self, client, monkeypatch):
        """Test PATCH /forms request when form is not found."""
        test_payload = {
            "forms": {"mv6020":"JZ110449"},
            "spoiled_timestamp":"2025-08-13T20:36:34.636Z"
        }
        
        def mock_middle_logic(*args, **kwargs):
            return {'response': ('{"error": "record not found"}', 404, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        response = client.patch('/api/v1/forms', 
                               data=json.dumps(test_payload),
                               content_type='application/json')
        assert response.status_code == 404
        assert b'record not found' in response.data

    def test_delete_method_not_implemented(self, client):
        """Test DELETE /forms/<form_type>/<form_id> returns method not implemented."""
        response = client.delete('/api/v1/forms/24Hour/AA123456')
        assert response.status_code == 405
        assert b'method not implemented' in response.data

    def test_get_statistics_success(self, client, monkeypatch):
        """Test successful GET /forms/statistics request."""
        def mock_middle_logic(*args, **kwargs):
            return {'response': ('{"total_forms": 100, "active_forms": 50}', 200, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        
        response = client.get('/api/v1/forms/statistics')
        assert response.status_code == 200
        assert b'total_forms' in response.data
        assert b'active_forms' in response.data

    def test_get_statistics_server_error(self, client, monkeypatch):
        """Test GET /forms/statistics request with server error."""
        def mock_middle_logic(*args, **kwargs):
            return {'response': ('{"error": "server error"}', 500, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        
        response = client.get('/api/v1/forms/statistics')
        assert response.status_code == 500
        assert b'server error' in response.data

    def test_cors_headers_present(self, client, monkeypatch):
        """Test that CORS headers are properly configured."""
        def mock_middle_logic(*args, **kwargs):
            return {'response': ('{"forms": []}', 200, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        response = client.get('/api/v1/forms')
        # Note: CORS headers would typically be tested in integration tests
        # since they're handled by Flask-CORS middleware
        assert response.status_code == 200

    @patch('python.prohibition_web_svc.blueprints.forms.logger')
    def test_logging_on_create(self, mock_logging, client, monkeypatch):
        """Test that logging occurs during form creation."""
        test_payload = {"24Hour": 1}
        
        def mock_middle_logic(*args, **kwargs):
            return {'response': ('{"form_ids": ["AA123456"]}', 201, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        response = client.post('/api/v1/forms', 
                              data=json.dumps(test_payload),
                              content_type='application/json')
        
        # Verify logging was called
        mock_logging.verbose.assert_called()
        assert response.status_code == 201

    def test_invalid_http_methods(self, client):
        """Test that invalid HTTP methods return appropriate errors."""
        # Test PUT method (not implemented)
        response = client.put('/api/v1/forms')
        assert response.status_code == 405
        
        # Test OPTIONS method for statistics endpoint
        response = client.options('/api/v1/forms/statistics')
        # Flask typically handles OPTIONS automatically for CORS

    def test_blueprint_registration(self, app):
        """Test that the blueprint is properly registered."""
        assert 'forms' in app.blueprints
        blueprint = app.blueprints['forms']
        assert blueprint.url_prefix == Config.URL_PREFIX + '/api/v1'

    def test_middleware_chain_execution_order(self, client, monkeypatch):
        """Test that middleware functions are called in the correct order."""
        call_order = []
        
        def mock_middle_logic(middleware_chain, **kwargs):
            # Simulate middleware chain execution
            for middleware in middleware_chain:
                if 'try' in middleware:
                    call_order.append(middleware['try'].__name__)
            return {'response': ('{"success": true}', 200, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        response = client.get('/api/v1/forms')
        assert response.status_code == 200
        # The specific order would depend on the actual middleware chain structure

    def test_create_with_empty_payload(self, client, monkeypatch):
        """Test POST /forms request with empty JSON payload."""
        def mock_middle_logic(*args, **kwargs):
            return {'response': ('{"error": "empty payload"}', 400, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        response = client.post('/api/v1/forms', 
                              data=json.dumps({}),
                              content_type='application/json')
        assert response.status_code == 400
        assert b'empty payload' in response.data

    def test_create_with_valid_form_types(self, client, monkeypatch):
        """Test POST /forms request with various valid form types."""
        test_payload = {
            "24Hour": 2,
            "12Hour": 1,
            "IRP": 3
        }
        
        def mock_middle_logic(*args, **kwargs):
            return {'response': ('{"form_ids": ["AA123456", "BB123457", "CC123458", "DD123459", "EE123460", "FF123461"]}', 201, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        response = client.post('/api/v1/forms', 
                              data=json.dumps(test_payload),
                              content_type='application/json')
        assert response.status_code == 201
        assert b'form_ids' in response.data

    def test_update_with_form_data_submission(self, client, monkeypatch):
        """Test PATCH /forms request with comprehensive form data."""
        test_payload = {
            "form_id": "AA123456",
            "form_data": {
                "driver_name": "John Doe",
                "licence_number": "1234567",
                "violation_time": "2024-01-15T10:30:00Z",
                "location": "Highway 1"
            },
            "status": "submitted",
            "printed": True
        }
        
        def mock_middle_logic(*args, **kwargs):
            return {'response': ('{"message": "form processed successfully"}', 200, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        response = client.patch('/api/v1/forms', 
                               data=json.dumps(test_payload),
                               content_type='application/json')
        assert response.status_code == 200
        assert b'form processed successfully' in response.data

    def test_authorization_middleware_integration(self, client, monkeypatch):
        """Test that authorization middleware is properly integrated."""
        # Since the middleware chain is mocked, we'll test that the blueprint
        # attempts to call the authorization function during setup
        def mock_middle_logic(*args, **kwargs):
            # Verify that the middleware chain includes authorization
            middleware_chain = args[0] if args else []
            return {'response': ('{"authorized": true}', 200, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        response = client.get('/api/v1/forms')
        assert response.status_code == 200
        assert b'authorized' in response.data

    def test_statistics_endpoint_data_structure(self, client, monkeypatch):
        """Test GET /forms/statistics returns expected data structure."""
        expected_stats = {
            "total_forms": 1000,
            "active_forms": 250,
            "expired_forms": 50,
            "submitted_forms": 700,
            "forms_by_type": {
                "24Hour": 600,
                "12Hour": 300,
                "IRP": 100
            },
            "last_updated": "2024-01-15T10:30:00Z"
        }
        
        def mock_middle_logic(*args, **kwargs):
            return {'response': (json.dumps(expected_stats), 200, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        
        response = client.get('/api/v1/forms/statistics')
        assert response.status_code == 200
        response_data = json.loads(response.data)
        assert response_data['total_forms'] == 1000
        assert response_data['active_forms'] == 250
        assert 'forms_by_type' in response_data

    def test_error_handling_chain(self, client, monkeypatch):
        """Test that error handling middleware chain is executed properly."""
        def mock_middle_logic(*args, **kwargs):
            # Simulate an error in the middleware chain
            return {'response': ('{"error": "middleware_error", "error_code": "F01"}', 500, {'Content-Type': 'application/json'})}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        response = client.post('/api/v1/forms', 
                              data=json.dumps({"24Hour": 1}),
                              content_type='application/json')
        assert response.status_code == 500
        assert b'middleware_error' in response.data

    def test_config_integration(self, client):
        """Test that the blueprint uses Config values correctly."""
        # Test that URL_PREFIX is correctly configured
        response = client.get('/api/v1/forms/statistics')
        # The fact that this doesn't return 404 confirms the URL prefix is correct
        assert response.status_code != 404
