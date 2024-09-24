import datetime
import json
import pytest
from flask_api import FlaskAPI

from python.common.error_middleware import record_error, get_safe_payload, get_function_info
from python.common.models import db, DFErrors
from python.form_handler.config import Config
from python.common.enums import ErrorCode, ErrorStatus, ErrorCategory, ErrorSeverity, EventType

application = FlaskAPI(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI
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
    return application

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
        
        # Clear the database after the test
        db.session.query(DFErrors).delete()
        db.session.commit()

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
        
        # Clear the database after each test
        db.session.query(DFErrors).delete()
        db.session.commit()

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
        
        # Clear the database after the test
        db.session.query(DFErrors).delete()
        db.session.commit()