import pytest
from unittest.mock import MagicMock, patch
from python.common.models import Event
from python.common.enums import ErrorCode, EventType
from python.prohibition_web_svc.middleware.event_middleware import check_if_application_id_exists, log_payload_to_splunk, save_event_data

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


# Tests for save_event_data function
def test_save_event_data_vi_form_success(mock_db_session):
    """Test successful save_event_data with VI form"""
    payload = {
        'VI': True,
        'VI_number': 'VI123',
        'ff_application_id': 'app-123',
        'driver_licence_no': 'DL123456',
        'driver_last_name': 'Doe',
        'driver_given_name': 'John',
        'driver_dob': '1990-01-01T00:00:00.000Z',
        'vehicle_plate_no': 'ABC123',
        'VI_form_png': 'base64data',
        'submitted_offline': False
    }
    kwargs = {
        'payload': payload,
        'user_guid': 'user-guid-123',
        'username': 'testuser',
        'identity_provider': 'idir'
    }

    mock_event = MagicMock()
    mock_event.event_id = 1
    mock_vi_form = MagicMock()
    mock_vi_form.form_id = 1
    mock_event.vi_form = mock_vi_form

    with patch('python.prohibition_web_svc.middleware.event_middleware.Event', return_value=mock_event), \
         patch('python.prohibition_web_svc.middleware.event_middleware.VIForm', return_value=mock_vi_form), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Submission'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.datetime') as mock_datetime, \
         patch('python.prohibition_web_svc.middleware.event_middleware.jsonify') as mock_jsonify:

        mock_datetime.now.return_value = '2023-01-01T00:00:00'
        mock_jsonify.return_value = {'event': 'data'}

        result, updated_kwargs = save_event_data(**kwargs)

        assert result is True
        assert 'response_dict' in updated_kwargs
        assert 'event' in updated_kwargs
        assert updated_kwargs['event'] == mock_event
        mock_db_session.add.assert_any_call(mock_event)
        mock_db_session.commit.assert_called()


def test_save_event_data_twenty_four_hour_form_success(mock_db_session):
    """Test successful save_event_data with TwentyFourHour form"""
    payload = {
        'TwentyFourHour': True,
        'twenty_four_hour_number': '24H456',
        'ff_application_id': 'app-456',
        'driver_licence_no': 'DL789012',
        'driver_last_name': 'Smith',
        'driver_given_name': 'Jane',
        'vehicle_plate_no': 'XYZ789',
        'TwentyFourHour_form_png': 'base64data',
        'submitted_offline': True
    }
    kwargs = {
        'payload': payload,
        'user_guid': 'user-guid-456',
        'username': 'testuser',
        'identity_provider': 'idir'
    }

    mock_event = MagicMock()
    mock_event.event_id = 2
    mock_24h_form = MagicMock()
    mock_24h_form.form_id = 2
    mock_event.twenty_four_hour_form = mock_24h_form

    with patch('python.prohibition_web_svc.middleware.event_middleware.Event', return_value=mock_event), \
         patch('python.prohibition_web_svc.middleware.event_middleware.TwentyFourHourForm', return_value=mock_24h_form), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Submission'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.datetime') as mock_datetime, \
         patch('python.prohibition_web_svc.middleware.event_middleware.jsonify') as mock_jsonify:

        mock_datetime.now.return_value = '2023-01-01T00:00:00'
        mock_jsonify.return_value = {'event': 'data'}

        result, updated_kwargs = save_event_data(**kwargs)

        assert result is True
        assert 'response_dict' in updated_kwargs
        assert 'event' in updated_kwargs
        assert updated_kwargs['event'] == mock_event
        mock_db_session.add.assert_any_call(mock_event)
        mock_db_session.commit.assert_called()


def test_save_event_data_twelve_hour_form_success(mock_db_session):
    """Test successful save_event_data with TwelveHour form"""
    payload = {
        'TwelveHour': True,
        'twelve_hour_number': '12H789',
        'ff_application_id': 'app-789',
        'driver_licence_no': 'DL345678',
        'driver_last_name': 'Johnson',
        'driver_given_name': 'Bob',
        'vehicle_plate_no': 'DEF456',
        'TwelveHour_form_png': 'base64data',
        'submitted_offline': False
    }
    kwargs = {
        'payload': payload,
        'user_guid': 'user-guid-789',
        'username': 'testuser',
        'identity_provider': 'idir'
    }

    mock_event = MagicMock()
    mock_event.event_id = 3
    mock_12h_form = MagicMock()
    mock_12h_form.form_id = 3
    mock_event.twelve_hour_form = mock_12h_form

    with patch('python.prohibition_web_svc.middleware.event_middleware.Event', return_value=mock_event), \
         patch('python.prohibition_web_svc.middleware.event_middleware.TwelveHourForm', return_value=mock_12h_form), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Submission'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.datetime') as mock_datetime, \
         patch('python.prohibition_web_svc.middleware.event_middleware.jsonify') as mock_jsonify:

        mock_datetime.now.return_value = '2023-01-01T00:00:00'
        mock_jsonify.return_value = {'event': 'data'}

        result, updated_kwargs = save_event_data(**kwargs)

        assert result is True
        assert 'response_dict' in updated_kwargs
        assert 'event' in updated_kwargs
        assert updated_kwargs['event'] == mock_event
        mock_db_session.add.assert_any_call(mock_event)
        mock_db_session.commit.assert_called()


def test_save_event_data_irp_form_returns_early(mock_db_session):
    """Test save_event_data with IRP form (returns early without saving)"""
    payload = {
        'IRP': True,
        'IRP_number': 'IRP999',
        'ff_application_id': 'app-999'
    }
    kwargs = {
        'payload': payload,
        'user_guid': 'user-guid-999',
        'username': 'testuser',
        'identity_provider': 'idir'
    }

    # IRP forms return early without any return value (None)
    result = save_event_data(**kwargs)

    # Should return None (not a tuple) for IRP forms
    assert result is None
    # No database operations should have been performed
    mock_db_session.add.assert_not_called()
    mock_db_session.commit.assert_not_called()


def test_save_event_data_service_account_identity_provider(mock_db_session):
    """Test save_event_data with service_account identity provider"""
    payload = {
        'VI': True,
        'VI_number': 'VI999',
        'ff_application_id': 'app-999',
        'driver_licence_no': 'DL999999',
        'submitted_user_guid': 'submitted-user-guid',
        'submitted_offline': False
    }
    kwargs = {
        'payload': payload,
        'username': 'service-account-user',
        'identity_provider': 'service_account'
    }

    mock_event = MagicMock()
    mock_event.event_id = 4
    mock_vi_form = MagicMock()
    mock_vi_form.form_id = 4
    mock_event.vi_form = mock_vi_form

    with patch('python.prohibition_web_svc.middleware.event_middleware.Event', return_value=mock_event), \
         patch('python.prohibition_web_svc.middleware.event_middleware.VIForm', return_value=mock_vi_form), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Submission'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.datetime') as mock_datetime, \
         patch('python.prohibition_web_svc.middleware.event_middleware.jsonify') as mock_jsonify:

        mock_datetime.now.return_value = '2023-01-01T00:00:00'
        mock_jsonify.return_value = {'event': 'data'}

        result, updated_kwargs = save_event_data(**kwargs)

        assert result is True
        # Verify that submitted_user_guid was used instead of username
        # This would be verified by checking the Event constructor call


def test_save_event_data_database_exception_handling(mock_db_session):
    """Test save_event_data handles database exceptions properly"""
    payload = {
        'VI': True,
        'VI_number': 'VI000',
        'ff_application_id': 'app-000',
        'driver_licence_no': 'DL000000'
    }
    kwargs = {
        'payload': payload,
        'user_guid': 'user-guid-000',
        'username': 'testuser',
        'identity_provider': 'idir'
    }

    # Make database commit raise an exception
    mock_db_session.commit.side_effect = Exception("Database connection failed")

    with patch('python.prohibition_web_svc.middleware.event_middleware.Event'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.VIForm'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Submission'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.datetime'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.get_event_type', return_value=EventType.VI), \
         patch('python.prohibition_web_svc.middleware.event_middleware.get_ticket_no', return_value='VI000'):

        result, updated_kwargs = save_event_data(**kwargs)

        assert result is False
        assert 'error' in updated_kwargs
        assert updated_kwargs['error']['error_code'] == ErrorCode.E01
        assert 'Database connection failed' in updated_kwargs['error']['error_details']
        assert updated_kwargs['error']['event_type'] == EventType.VI
        assert updated_kwargs['error']['ticket_no'] == 'VI000'
