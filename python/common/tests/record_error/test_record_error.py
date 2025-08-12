import pytest
import os
from flask_api import FlaskAPI

# Set environment to indicate we're in test mode before importing models
os.environ['TESTING'] = 'true'

from python.common.error_middleware import record_error, get_safe_payload, get_function_info
from python.common.models.base import db
from python.common.models.df_errors import DFErrors
from python.common.enums import ErrorCode, ErrorStatus, EventType

application = FlaskAPI(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['TESTING'] = True
db.init_app(application)

@pytest.fixture
def error_data():
    return {
        'error_code': ErrorCode.G00,
        'error_details': 'Test error details',
        'event_id': 123,
        'event_type': EventType.TWELVE_HOUR,
    }

@pytest.fixture
def app():    
    with application.app_context():
        # Only create the specific table we need for testing
        DFErrors.__table__.create(db.engine, checkfirst=True)
        yield application
        # Clean up
        DFErrors.__table__.drop(db.engine, checkfirst=True)

@pytest.fixture
def client(app):
    return app.test_client()

def test_record_error_success(app, error_data):
    with app.app_context():
        record_error(
            error_data['error_code'],
            error_data['error_details'],
            error_data['event_id'],
            error_data['event_type']
        )
        
        error = DFErrors.query.first()
        assert error is not None
        assert error.error_cd == error_data['error_code'].code
        assert error.error_cd_desc == error_data['error_code'].description
        assert error.error_category_cd == str(error_data['error_code'].category)
        assert error.error_severity_level_cd == str(error_data['error_code'].severity)
        assert error.error_status_cd == str(ErrorStatus.NEW)
        assert error.event_id == error_data['event_id']
        assert error.event_type == str(error_data['event_type'])
        assert error.error_details == error_data['error_details']

@pytest.mark.parametrize("error_code,event_id,event_type", [
    (ErrorCode.E01, 456, EventType.IRP),
    (ErrorCode.F01, None, None),
    (ErrorCode.G00, 789, EventType.VI),
])
def test_record_error_different_scenarios(app, error_code, event_id, event_type):
    with app.app_context():
        record_error(error_code, "Test error", event_id, event_type)
        
        error = DFErrors.query.first()
        assert error is not None
        assert error.error_cd == error_code.code
        assert error.event_id == event_id
        assert error.event_type == (str(event_type) if event_type else None)

def test_get_safe_payload_json(client):
    with client.application.test_request_context(json={"key": "value"}):
        payload = get_safe_payload()
        assert payload == '{"key": "value"}'

def test_get_safe_payload_form(client):
    with client.application.test_request_context(data={"key": "value"}):
        payload = get_safe_payload()
        assert payload == '{"key": "value"}'

def test_get_safe_payload_query(client):
    with client.application.test_request_context("/?key=value"):
        payload = get_safe_payload()
        assert payload == '{"key": "value"}'

def test_get_safe_payload_empty(app):
    with app.test_request_context():
        payload = get_safe_payload()
        assert payload == '{"message": "No payload found in request"}'

def test_get_function_info():
    def test_function():
        pass
    
    function_info = get_function_info(test_function)
    assert "test_function" in function_info

def test_record_error_with_function_info(app):
    def test_function():
        pass

    with app.app_context():
        record_error(ErrorCode.G00, "Test error", func=test_function)
        
        error = DFErrors.query.first()
        assert error is not None
        assert "test_function" in error.error_path