import pytest
import json
from unittest.mock import patch, MagicMock
from flask import Flask
from python.prohibition_web_svc.blueprints import print as print_blueprint
from python.prohibition_web_svc.config import Config


@pytest.fixture
def app():
    """Create a test Flask application."""
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['URL_PREFIX'] = '/api/v1'
    app.register_blueprint(print_blueprint.bp)
    return app


@pytest.fixture
def client(app):
    """Create a test client."""
    return app.test_client()


class TestPrintBlueprint:
    """Test cases for the print blueprint."""

    def test_render_pdf_success(self, client, monkeypatch):
        """Test successful PDF document rendering."""
        def mock_middle_logic(*args, **kwargs):
            from flask import Response
            # Mock PDF content
            pdf_content = b'%PDF-1.4\n1 0 obj\n<<\n/Type /Catalog\n/Pages 2 0 R\n>>\nendobj\n'
            response = Response(
                pdf_content,
                mimetype='application/pdf',
                headers={
                    'Content-Disposition': 'inline; filename=document.pdf',
                    'Content-Type': 'application/pdf'
                }
            )
            return {'response': response}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        test_payload = {
            "template": "test_template.html",
            "data": {"name": "John Doe", "date": "2025-01-01"},
            "options": {"type": "pdf", "filename": "test.pdf"}
        }
        response = client.post('/api/v1/print',
                              data=json.dumps(test_payload),
                              content_type='application/json')
        assert response.status_code == 200
        assert response.mimetype == 'application/pdf'
        assert b'PDF' in response.data

    def test_render_html_success(self, client, monkeypatch):
        """Test successful HTML document rendering."""
        def mock_middle_logic(*args, **kwargs):
            from flask import Response
            html_content = '<html><body><h1>Test Document</h1></body></html>'
            response = Response(
                html_content,
                mimetype='text/html; charset=utf-8',
                headers={
                    'Content-Disposition': 'inline; filename=document.html',
                    'Content-Type': 'text/html; charset=utf-8'
                }
            )
            return {'response': response}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        test_payload = {
            "template": "test_template.html",
            "data": {"name": "John Doe"},
            "options": {"type": "html", "filename": "test.html"}
        }
        response = client.post('/api/v1/print',
                              data=json.dumps(test_payload),
                              content_type='application/json')
        assert response.status_code == 200
        assert response.mimetype == 'text/html'
        assert b'Test Document' in response.data

    def test_render_missing_payload(self, client, monkeypatch):
        """Test POST /print request with missing payload."""
        def mock_middle_logic(*args, **kwargs):
            from flask import make_response
            mock_response = make_response('{"error": "payload required"}', 400)
            mock_response.headers['Content-Type'] = 'application/json'
            return {'response': mock_response}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        response = client.post('/api/v1/print',
                              data='{}',
                              content_type='application/json')
        assert response.status_code == 400
        assert b'payload required' in response.data

    def test_render_invalid_json(self, client, monkeypatch):
        """Test POST /print request with invalid JSON."""
        def mock_middle_logic(*args, **kwargs):
            from flask import make_response
            mock_response = make_response('{"error": "Invalid JSON payload"}', 400)
            mock_response.headers['Content-Type'] = 'application/json'
            return {'response': mock_response}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        response = client.post('/api/v1/print',
                              data='invalid json',
                              content_type='application/json')
        assert response.status_code == 400
        assert b'Invalid JSON payload' in response.data

    def test_render_missing_template(self, client, monkeypatch):
        """Test POST /print request with missing template field."""
        def mock_middle_logic(*args, **kwargs):
            from flask import make_response
            mock_response = make_response('{"error": "Missing required field: template"}', 400)
            mock_response.headers['Content-Type'] = 'application/json'
            return {'response': mock_response}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        test_payload = {
            "data": {"name": "John Doe"}
        }
        response = client.post('/api/v1/print',
                              data=json.dumps(test_payload),
                              content_type='application/json')
        assert response.status_code == 400
        assert b'Missing required field: template' in response.data

    def test_render_missing_data(self, client, monkeypatch):
        """Test POST /print request with missing data field."""
        def mock_middle_logic(*args, **kwargs):
            from flask import make_response
            mock_response = make_response('{"error": "Missing required field: data"}', 400)
            mock_response.headers['Content-Type'] = 'application/json'
            return {'response': mock_response}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        test_payload = {
            "template": "test_template.html"
        }
        response = client.post('/api/v1/print',
                              data=json.dumps(test_payload),
                              content_type='application/json')
        assert response.status_code == 400
        assert b'Missing required field: data' in response.data

    def test_render_invalid_data_type(self, client, monkeypatch):
        """Test POST /print request with invalid data field type."""
        def mock_middle_logic(*args, **kwargs):
            from flask import make_response
            mock_response = make_response('{"error": "Field \'data\' must be an object"}', 400)
            mock_response.headers['Content-Type'] = 'application/json'
            return {'response': mock_response}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        test_payload = {
            "template": "test_template.html",
            "data": "invalid data type"
        }
        response = client.post('/api/v1/print',
                              data=json.dumps(test_payload),
                              content_type='application/json')
        assert response.status_code == 400
        assert b'must be an object' in response.data

    def test_render_template_not_found(self, client, monkeypatch):
        """Test POST /print request with template not found."""
        def mock_middle_logic(*args, **kwargs):
            from flask import make_response
            mock_response = make_response('{"error": "Template \'nonexistent.html\' not found in templates folder"}', 400)
            mock_response.headers['Content-Type'] = 'application/json'
            return {'response': mock_response}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        test_payload = {
            "template": "nonexistent.html",
            "data": {"name": "John Doe"}
        }
        response = client.post('/api/v1/print',
                              data=json.dumps(test_payload),
                              content_type='application/json')
        assert response.status_code == 400
        assert b'not found in templates folder' in response.data

    def test_render_playwright_error(self, client, monkeypatch):
        """Test POST /print request with Playwright rendering error."""
        def mock_middle_logic(*args, **kwargs):
            from flask import make_response
            mock_response = make_response('{"error": "Playwright rendering failed"}', 500)
            mock_response.headers['Content-Type'] = 'application/json'
            return {'response': mock_response}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        test_payload = {
            "template": "test_template.html",
            "data": {"name": "John Doe"}
        }
        response = client.post('/api/v1/print',
                              data=json.dumps(test_payload),
                              content_type='application/json')
        assert response.status_code == 500
        assert b'Playwright rendering failed' in response.data

    def test_render_unauthorized(self, client, monkeypatch):
        """Test POST /print request with unauthorized user."""
        def mock_middle_logic(*args, **kwargs):
            from flask import make_response
            mock_response = make_response('{"error": "unauthorized"}', 401)
            mock_response.headers['Content-Type'] = 'application/json'
            return {'response': mock_response}
        
        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])
        
        test_payload = {
            "template": "test_template.html",
            "data": {"name": "John Doe"}
        }
        response = client.post('/api/v1/print',
                              data=json.dumps(test_payload),
                              content_type='application/json')
        assert response.status_code == 401
        assert b'unauthorized' in response.data

    def test_get_method_not_allowed(self, client):
        """Test GET /print request goes through authorization."""
        response = client.get('/api/v1/print')
        # GET method is allowed but will fail authorization since no auth is provided
        assert response.status_code == 401  # Unauthorized

    def test_cors_headers_present(self, client):
        """Test that CORS headers are present in responses."""
        response = client.post('/api/v1/print',
                              data=json.dumps({"template": "test.html", "data": {}}),
                              content_type='application/json')
        assert 'Access-Control-Allow-Origin' in response.headers

    def test_logging_on_render(self, client, monkeypatch, caplog):
        """Test that appropriate logging occurs during document rendering."""
        test_payload = {
            "template": "test_template.html",
            "data": {"name": "John Doe"}
        }

        def mock_middle_logic(*args, **kwargs):
            from flask import Response
            pdf_content = b'%PDF-1.4\n1 0 obj\n<<\n/Type /Catalog\n/Pages 2 0 R\n>>\nendobj\n'
            response = Response(
                pdf_content,
                mimetype='application/pdf',
                headers={
                    'Content-Disposition': 'inline; filename=document.pdf',
                    'Content-Type': 'application/pdf'
                }
            )
            return {'response': response}

        monkeypatch.setattr('python.common.helper.middle_logic', mock_middle_logic)
        monkeypatch.setattr('python.prohibition_web_svc.business.keycloak_logic.get_authorized_keycloak_user', lambda: [])

        with caplog.at_level('VERBOSE'):
            response = client.post('/api/v1/print',
                                  data=json.dumps(test_payload),
                                  content_type='application/json')

        assert response.status_code == 200
        # Check that verbose logging occurred
        assert any('Inside render_document()' in record.message for record in caplog.records)

    def test_blueprint_registration(self, app):
        """Test that the blueprint is properly registered."""
        blueprint = app.blueprints.get('print')
        assert blueprint is not None
        assert hasattr(blueprint, 'name')
        assert blueprint.name == 'print'