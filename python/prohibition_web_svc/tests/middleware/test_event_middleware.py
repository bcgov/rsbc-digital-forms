import pytest
from unittest.mock import MagicMock, patch
from python.common.models import Event
from python.common.enums import ErrorCode, EventType
from python.prohibition_web_svc.middleware.event_middleware import _mask_sensitive_data, check_if_application_id_exists, log_payload_to_splunk

@pytest.fixture
def mock_db_session():
  with patch('python.common.models.db.session') as mock_session:
    yield mock_session

@pytest.fixture
def mock_event():
  event = MagicMock(spec=Event)
  event.event_id = 1
  return event

def test_check_if_application_id_exists_no_application_id(mock_db_session):
  kwargs = {'payload': {}}
  result, updated_kwargs = check_if_application_id_exists(**kwargs)
  assert result is True
  assert 'error' not in updated_kwargs

def test_check_if_application_id_exists_application_id_not_found(mock_db_session):
  mock_db_session.query.return_value.filter.return_value.first.return_value = None
  kwargs = {'payload': {'ff_application_id': '12345'}}
  result, updated_kwargs = check_if_application_id_exists(**kwargs)
  assert result is True
  assert 'error' not in updated_kwargs

def test_check_if_application_id_exists_application_id_exists(mock_db_session, mock_event):
  mock_db_session.query.return_value.filter.return_value.first.return_value = mock_event
  kwargs = {'payload': {'ff_application_id': '12345'}}
  with patch('python.prohibition_web_svc.middleware.event_middleware.get_event_type', return_value='VI'), \
     patch('python.prohibition_web_svc.middleware.event_middleware.get_ticket_no', return_value='VI123'):
    result, updated_kwargs = check_if_application_id_exists(**kwargs)
  assert result is False
  assert 'error' in updated_kwargs
  assert updated_kwargs['error']['error_code'] == ErrorCode.E09
  assert updated_kwargs['error']['error_details'] == 'Application ID already exists'
  assert updated_kwargs['error']['event_id'] == mock_event.event_id

def test_check_if_application_id_exists_exception_handling(mock_db_session):
  mock_db_session.query.side_effect = Exception("Database error")
  kwargs = {'payload': {'ff_application_id': '12345'}}
  result, updated_kwargs = check_if_application_id_exists(**kwargs)
  assert result is False
  assert 'error' not in updated_kwargs


def test_log_payload_to_splunk_success_with_all_fields():
    """Test log_payload_to_splunk with all required fields present"""
    payload = {
        'VI': True,
        'VI_number': 'VI123',
        'driver_licence_no': 'sensitive_data',
        'driver_last_name': 'sensitive_name'
    }
    kwargs = {
        'payload': payload,
        'request_id': 'req-123',
        'user_guid': 'user-guid-456',
        'username': 'testuser'
    }
    
    with patch('python.prohibition_web_svc.middleware.event_middleware.get_event_type', return_value=EventType.VI), \
         patch('python.prohibition_web_svc.middleware.event_middleware.get_ticket_no', return_value='VI123'):
        
        result, updated_kwargs = log_payload_to_splunk(**kwargs)
        
        assert result is True
        assert 'splunk_data' in updated_kwargs
        splunk_data = updated_kwargs['splunk_data']
        assert splunk_data['event'] == "create VI/24h/12h event"
        assert splunk_data['request_id'] == 'req-123'
        assert splunk_data['user_guid'] == 'user-guid-456'
        assert splunk_data['username'] == 'testuser'
        assert splunk_data['form_type'] == EventType.VI.code
        assert splunk_data['ticket_no'] == 'VI123'
        assert 'payload' in splunk_data
        # Check that sensitive data is masked
        assert splunk_data['payload']['driver_licence_no'] == '[REDACTED]'
        assert splunk_data['payload']['driver_last_name'] == '[REDACTED]'

def test_log_payload_to_splunk_success_with_missing_optional_fields():
    """Test log_payload_to_splunk with missing optional fields"""
    payload = {
        'TwentyFourHour': True,
        'twenty_four_hour_number': '24H456'
    }
    kwargs = {
        'payload': payload
        # Missing request_id, user_guid, username
    }
    
    with patch('python.prohibition_web_svc.middleware.event_middleware.get_event_type', return_value=EventType.TWENTY_FOUR_HOUR), \
         patch('python.prohibition_web_svc.middleware.event_middleware.get_ticket_no', return_value='24H456'):
        
        result, updated_kwargs = log_payload_to_splunk(**kwargs)
        
        assert result is True
        assert 'splunk_data' in updated_kwargs
        splunk_data = updated_kwargs['splunk_data']
        assert splunk_data['request_id'] == ''  # Default empty string
        assert splunk_data['user_guid'] == ''  # Default empty string
        assert splunk_data['username'] is None  # Default None
        assert splunk_data['form_type'] == EventType.TWENTY_FOUR_HOUR.code
        assert splunk_data['ticket_no'] == '24H456'

def test_log_payload_to_splunk_success_twelve_hour_form():
    """Test log_payload_to_splunk with TwelveHour form"""
    payload = {
        'TwelveHour': True,
        'twelve_hour_number': '12H789'
    }
    kwargs = {'payload': payload}
    
    with patch('python.prohibition_web_svc.middleware.event_middleware.get_event_type', return_value=EventType.TWELVE_HOUR), \
         patch('python.prohibition_web_svc.middleware.event_middleware.get_ticket_no', return_value='12H789'):
        
        result, updated_kwargs = log_payload_to_splunk(**kwargs)
        
        assert result is True
        splunk_data = updated_kwargs['splunk_data']
        assert splunk_data['form_type'] == EventType.TWELVE_HOUR.code
        assert splunk_data['ticket_no'] == '12H789'

def test_log_payload_to_splunk_exception_handling():
    """Test log_payload_to_splunk handles exceptions gracefully"""
    payload = {'invalid': 'data'}
    kwargs = {'payload': payload}
    
    # Mock get_event_type to raise an exception
    with patch('python.prohibition_web_svc.middleware.event_middleware.get_event_type', side_effect=Exception('Test error')), \
         patch('python.prohibition_web_svc.middleware.event_middleware.logger') as mock_logger:
        
        result, updated_kwargs = log_payload_to_splunk(**kwargs)
        
        assert result is True  # Function always returns True
        assert 'splunk_data' not in updated_kwargs  # splunk_data not added on error
        mock_logger.error.assert_called_once()  # Error was logged

def test_log_payload_to_splunk_sensitive_data_masking():
    """Test that sensitive data is properly masked in splunk payload"""
    payload = {
        'VI': True,
        'VI_number': 'VI123',
        'driver_licence_no': 'ABC123456',
        'driver_last_name': 'Doe',
        'driver_given_name': 'John',
        'regist_owner_last_name': 'Smith',
        'regist_owner_first_name': 'Jane',
        'TwelveHour_form_png': 'base64data',
        'TwentyFourHour_form_png': 'base64data2',
        'VI_form_png': 'base64data3',
        'normal_field': 'normal_value'
    }
    kwargs = {'payload': payload}
    
    with patch('python.prohibition_web_svc.middleware.event_middleware.get_event_type', return_value=EventType.VI), \
         patch('python.prohibition_web_svc.middleware.event_middleware.get_ticket_no', return_value='VI123'):
        
        result, updated_kwargs = log_payload_to_splunk(**kwargs)
        
        assert result is True
        splunk_payload = updated_kwargs['splunk_data']['payload']
        
        # Sensitive fields should be masked
        assert splunk_payload['driver_licence_no'] == '[REDACTED]'
        assert splunk_payload['driver_last_name'] == '[REDACTED]'
        assert splunk_payload['driver_given_name'] == '[REDACTED]'
        assert splunk_payload['regist_owner_last_name'] == '[REDACTED]'
        assert splunk_payload['regist_owner_first_name'] == '[REDACTED]'
        assert splunk_payload['TwelveHour_form_png'] == '[REDACTED]'
        assert splunk_payload['TwentyFourHour_form_png'] == '[REDACTED]'
        assert splunk_payload['VI_form_png'] == '[REDACTED]'
        
        # Normal fields should remain unchanged
        assert splunk_payload['normal_field'] == 'normal_value'
        assert splunk_payload['VI'] is True
        assert splunk_payload['VI_number'] == 'VI123'

def test_log_payload_to_splunk_no_payload():
    """Test log_payload_to_splunk with no payload"""
    kwargs = {}  # No payload
    
    with patch('python.prohibition_web_svc.middleware.event_middleware.logger') as mock_logger:
        result, updated_kwargs = log_payload_to_splunk(**kwargs)
        
        assert result is True
        assert 'splunk_data' not in updated_kwargs  # No splunk_data added
        mock_logger.error.assert_called_once()  # Error was logged due to None payload
