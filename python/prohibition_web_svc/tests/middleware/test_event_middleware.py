import pytest
from unittest.mock import MagicMock, patch, mock_open
from python.common.models import Event
from python.common.enums import ErrorCode, EventType
from python.prohibition_web_svc.middleware.event_middleware import (
    check_if_application_id_exists, log_payload_to_splunk, save_event_data, save_event_pdf,
    _get_asd_expiry_date, check_if_form_number_was_used, commit_transaction, validate_form_payload,
    validate_update, get_event_type, get_ticket_no,
    request_contains_a_payload, get_json_payload,
    get_events_for_user,
    get_irp_form_by_event_id, log_irp_update_to_splunk, update_irp_form_data,
)


# ── helpers ──────────────────────────────────────────────────────────────────

def _make_scalar(value):
    """Return a mock chain that ends with .scalar() == value."""
    mock = MagicMock()
    mock.query.return_value.scalar.return_value = value
    return mock

@pytest.fixture
def mock_db_session():
    with patch('python.common.models.db.session') as mock_session:
        yield mock_session

@pytest.fixture
def mock_event():
  event = MagicMock(spec=Event)
  event.event_id = 1
  event.submission_id = 42
  return event

# ── tests ──────────────────────────────────────────────────────────────────

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
  assert updated_kwargs['error']['submission_id'] == mock_event.submission_id

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
        assert splunk_data['event'] == "create VI/24h/12h/IRP event"
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
        'IRP_form_png': 'base64data4',
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
        assert splunk_payload['IRP_form_png'] == '[REDACTED]'
        
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
        mock_db_session.add.assert_called_once()
        mock_db_session.flush.assert_called()


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
        mock_db_session.add.assert_called_once()
        mock_db_session.flush.assert_called()


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
        mock_db_session.add.assert_called_once()
        mock_db_session.flush.assert_called()


def test_save_event_data_irp_form_success(mock_db_session):
    """Test successful save_event_data with IRP form"""
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

    mock_event = MagicMock()
    mock_event.event_id = 4
    mock_irp_form = MagicMock()
    mock_irp_form.form_id = 4
    mock_event.irp_form = mock_irp_form

    with patch('python.prohibition_web_svc.middleware.event_middleware.Event', return_value=mock_event), \
         patch('python.prohibition_web_svc.middleware.event_middleware.IRPMapper') as mock_irp_mapper, \
         patch('python.prohibition_web_svc.middleware.event_middleware.Submission'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.datetime') as mock_datetime, \
         patch('python.prohibition_web_svc.middleware.event_middleware.jsonify') as mock_jsonify:

        mock_irp_mapper.map_to_irp_form.return_value = mock_irp_form
        mock_datetime.now.return_value = '2023-01-01T00:00:00'
        mock_jsonify.return_value = {'event': 'data'}

        result, updated_kwargs = save_event_data(**kwargs)

        assert result is True
        assert 'response_dict' in updated_kwargs
        assert 'event' in updated_kwargs
        assert updated_kwargs['event'] == mock_event
        mock_irp_mapper.map_to_irp_form.assert_called_once()
        mock_db_session.add.assert_called_once()
        mock_db_session.flush.assert_called()


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

    # Make database flush raise an exception
    mock_db_session.flush.side_effect = Exception("Database connection failed")

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
        mock_db_session.rollback.assert_called_once()


# Tests for save_event_pdf function
def test_save_event_pdf_vi_form_with_extra_page_success(mock_db_session):
    payload = {
        'VI': True,
        'VI_number': 'VI123',
        'VI_form_png': 'data:image/png;base64,aGVsbG8=',
        'incident_details': 'x' * 600,
        'form_details': {
            'form_version': '1.0',
        }
    }
    event = MagicMock()
    event.event_id = 10
    event.vi_form.form_id = 101
    kwargs = {'payload': payload, 'event': event, 'submission_id': 11}

    mock_uuid = MagicMock()
    mock_uuid.hex = 'abc123'

    with patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_CERT_FILE', '/tmp/cert.pem'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_BUCKET_URL', 'minio.local'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_AK', 'ak'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_SK', 'sk'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_SECURE', False), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.STORAGE_BUCKET_NAME', 'forms-bucket'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.ENCRYPT_KEY', 'enc-key'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.uuid.uuid4', return_value=mock_uuid), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Minio') as mock_minio_cls, \
         patch('python.prohibition_web_svc.middleware.event_middleware.split_image') as mock_split_image, \
         patch('python.prohibition_web_svc.middleware.event_middleware.create_pdf_with_images', return_value=b'%PDF') as mock_create_pdf, \
         patch('python.prohibition_web_svc.middleware.event_middleware.encryptPdf_method1') as mock_encrypt, \
         patch('python.prohibition_web_svc.middleware.event_middleware.FormStorageRefs') as mock_storage_ref, \
         patch('python.prohibition_web_svc.middleware.event_middleware.SubmissionFormRef') as mock_submission_ref, \
         patch('python.prohibition_web_svc.middleware.event_middleware.SubmissionEvent') as mock_submission_event, \
         patch('builtins.open', mock_open()):

        mock_client = MagicMock()
        mock_minio_cls.return_value = mock_client

        result, out = save_event_pdf(**kwargs)

        assert result is True
        assert out == kwargs
        mock_split_image.assert_called_once_with('/tmp/abc123.png', 3, 1, False, True, output_dir='/tmp')
        mock_create_pdf.assert_called_once_with('/tmp/abc123_0.png', '/tmp/abc123_1.png', '/tmp/abc123_2.png', is_landscape=False)
        mock_encrypt.assert_called_once_with('/tmp/abc123.pdf', 'enc-key', '/tmp/abc123_encrypted.pdf')
        mock_client.fput_object.assert_called_once_with('forms-bucket', 'abc123_encrypted.pdf', '/tmp/abc123_encrypted.pdf')
        mock_storage_ref.assert_called_once_with(
            form_id_vi=101,
            event_id=10,
            form_type='VI',
            storage_key='forms-bucket/abc123_encrypted.pdf',
            created_dt=mock_storage_ref.call_args.kwargs['created_dt'],
            updated_dt=mock_storage_ref.call_args.kwargs['updated_dt'],
        )
        mock_submission_ref.assert_called_once_with(
            submission_id=11,
            form_type='VI',
            form_id='VI123',
            form_version='1.0',
            storage_key='forms-bucket/abc123_encrypted.pdf',
        )
        mock_submission_event.assert_called_once_with(destination='VIPS')
        mock_db_session.add.assert_called()
        assert mock_db_session.add.call_count == 2  # FormStorageRefs + SubmissionFormRef
        mock_db_session.commit.assert_not_called()


def test_save_event_pdf_irp_form_success(mock_db_session):
    payload = {
        'IRP': True,
        'IRP_number': 'IRP123',
        'IRP_form_png': 'data:image/png;base64,aGVsbG8=',
        'form_details': {
            'form_version': '1.0',
        }
    }
    event = MagicMock()
    event.event_id = 11
    event.irp_form.form_id = 202
    kwargs = {'payload': payload, 'event': event, 'submission_id': 11}

    mock_uuid = MagicMock()
    mock_uuid.hex = 'irp123'

    with patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_CERT_FILE', '/tmp/cert.pem'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_BUCKET_URL', 'minio.local'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_AK', 'ak'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_SK', 'sk'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_SECURE', False), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.STORAGE_BUCKET_NAME', 'forms-bucket'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.ENCRYPT_KEY', 'enc-key'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.uuid.uuid4', return_value=mock_uuid), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Minio') as mock_minio_cls, \
         patch('python.prohibition_web_svc.middleware.event_middleware.split_image') as mock_split_image, \
         patch('python.prohibition_web_svc.middleware.event_middleware.create_pdf_with_images', return_value=b'%PDF') as mock_create_pdf, \
         patch('python.prohibition_web_svc.middleware.event_middleware.encryptPdf_method1') as mock_encrypt, \
         patch('python.prohibition_web_svc.middleware.event_middleware.FormStorageRefs') as mock_storage_ref, \
         patch('python.prohibition_web_svc.middleware.event_middleware.SubmissionFormRef') as mock_submission_ref, \
         patch('python.prohibition_web_svc.middleware.event_middleware.SubmissionEvent') as mock_submission_event, \
         patch('builtins.open', mock_open()):

        mock_client = MagicMock()
        mock_minio_cls.return_value = mock_client

        result, _ = save_event_pdf(**kwargs)

        assert result is True
        mock_split_image.assert_not_called()
        mock_create_pdf.assert_called_once_with('/tmp/irp123.png', is_landscape=False)
        mock_encrypt.assert_called_once_with('/tmp/irp123.pdf', 'enc-key', '/tmp/irp123_encrypted.pdf')
        mock_client.fput_object.assert_called_once_with('forms-bucket', 'irp123_encrypted.pdf', '/tmp/irp123_encrypted.pdf')
        mock_storage_ref.assert_called_once_with(
            form_id_irp=202,
            event_id=11,
            form_type='IRP',
            storage_key='forms-bucket/irp123_encrypted.pdf',
            created_dt=mock_storage_ref.call_args.kwargs['created_dt'],
            updated_dt=mock_storage_ref.call_args.kwargs['updated_dt'],
        )
        mock_submission_ref.assert_called_once_with(
            submission_id=11,
            form_type='IRP',
            form_id='IRP123',
            form_version='1.0',
            storage_key='forms-bucket/irp123_encrypted.pdf',
        )
        mock_submission_event.assert_any_call(destination='VIPS')
        mock_submission_event.assert_any_call(destination='RTS')
        mock_db_session.add.assert_called()
        assert mock_db_session.add.call_count == 2  # FormStorageRefs + SubmissionFormRef
        mock_db_session.commit.assert_not_called()


def test_save_event_pdf_returns_error_when_upload_fails(mock_db_session):
    payload = {
        'VI': True,
        'VI_number': 'VI-1000',
        'VI_form_png': 'data:image/png;base64,aGVsbG8=',
    }
    event = MagicMock()
    event.event_id = 12
    kwargs = {'payload': payload, 'event': event}

    with patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_CERT_FILE', '/tmp/cert.pem'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Minio', side_effect=Exception('minio unavailable')), \
         patch('python.prohibition_web_svc.middleware.event_middleware.get_event_type', return_value=EventType.VI), \
         patch('python.prohibition_web_svc.middleware.event_middleware.get_ticket_no', return_value='VI-1000'):

        result, out = save_event_pdf(**kwargs)

        assert result is False
        assert 'error' in out
        assert out['error']['error_code'] == ErrorCode.E02
        assert str(out['error']['error_details']) == 'minio unavailable'
        assert out['error']['event_id'] == 12
        assert out['error']['event_type'] == EventType.VI
        assert out['error']['ticket_no'] == 'VI-1000'
        mock_db_session.rollback.assert_called_once()


def test_save_event_pdf_twenty_four_hour_form_success(mock_db_session):
    payload = {
        'TwentyFourHour': True,
        'twenty_four_hour_number': '24H123',
        'TwentyFourHour_form_png': 'data:image/png;base64,aGVsbG8=',
        'form_details': {
            'form_version': '2.0',
        }
    }
    event = MagicMock()
    event.event_id = 20
    event.twenty_four_hour_form.form_id = 301
    kwargs = {'payload': payload, 'event': event, 'submission_id': 20}

    mock_uuid = MagicMock()
    mock_uuid.hex = '24h123'

    with patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_CERT_FILE', '/tmp/cert.pem'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_BUCKET_URL', 'minio.local'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_AK', 'ak'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_SK', 'sk'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_SECURE', False), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.STORAGE_BUCKET_NAME', 'forms-bucket'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.ENCRYPT_KEY', 'enc-key'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.uuid.uuid4', return_value=mock_uuid), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Minio') as mock_minio_cls, \
         patch('python.prohibition_web_svc.middleware.event_middleware.split_image') as mock_split_image, \
         patch('python.prohibition_web_svc.middleware.event_middleware.create_pdf_with_images', return_value=b'%PDF') as mock_create_pdf, \
         patch('python.prohibition_web_svc.middleware.event_middleware.encryptPdf_method1') as mock_encrypt, \
         patch('python.prohibition_web_svc.middleware.event_middleware.os.path.exists', return_value=False), \
         patch('python.prohibition_web_svc.middleware.event_middleware.FormStorageRefs') as mock_storage_ref, \
         patch('python.prohibition_web_svc.middleware.event_middleware.SubmissionFormRef') as mock_submission_ref, \
         patch('python.prohibition_web_svc.middleware.event_middleware.SubmissionEvent') as mock_submission_event, \
         patch('builtins.open', mock_open()):

        mock_client = MagicMock()
        mock_minio_cls.return_value = mock_client

        result, _ = save_event_pdf(**kwargs)

        assert result is True
        mock_split_image.assert_not_called()
        mock_create_pdf.assert_called_once_with('/tmp/24h123.png', is_landscape=True)
        mock_encrypt.assert_called_once_with('/tmp/24h123.pdf', 'enc-key', '/tmp/24h123_encrypted.pdf')
        mock_client.fput_object.assert_called_once_with('forms-bucket', '24h123_encrypted.pdf', '/tmp/24h123_encrypted.pdf')
        mock_storage_ref.assert_called_once_with(
            form_id_24h=301,
            event_id=20,
            form_type='24h',
            storage_key='forms-bucket/24h123_encrypted.pdf',
            created_dt=mock_storage_ref.call_args.kwargs['created_dt'],
            updated_dt=mock_storage_ref.call_args.kwargs['updated_dt'],
        )
        mock_submission_ref.assert_called_once_with(
            submission_id=20,
            form_type='24h',
            form_id='24H123',
            form_version='2.0',
            storage_key='forms-bucket/24h123_encrypted.pdf',
        )
        mock_submission_event.assert_called_once_with(destination='ICBC')
        mock_db_session.add.assert_called()
        assert mock_db_session.add.call_count == 2  # FormStorageRefs + SubmissionFormRef
        mock_db_session.commit.assert_not_called()


def test_save_event_pdf_twelve_hour_form_success(mock_db_session):
    payload = {
        'TwelveHour': True,
        'twelve_hour_number': '12H456',
        'TwelveHour_form_png': 'data:image/png;base64,aGVsbG8=',
        'form_details': {
            'form_version': '3.0',
        }
    }
    event = MagicMock()
    event.event_id = 30
    event.twelve_hour_form.form_id = 401
    kwargs = {'payload': payload, 'event': event, 'submission_id': 30}

    mock_uuid = MagicMock()
    mock_uuid.hex = '12h456'

    with patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_CERT_FILE', '/tmp/cert.pem'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_BUCKET_URL', 'minio.local'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_AK', 'ak'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_SK', 'sk'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_SECURE', False), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.STORAGE_BUCKET_NAME', 'forms-bucket'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Config.ENCRYPT_KEY', 'enc-key'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.uuid.uuid4', return_value=mock_uuid), \
         patch('python.prohibition_web_svc.middleware.event_middleware.Minio') as mock_minio_cls, \
         patch('python.prohibition_web_svc.middleware.event_middleware.split_image') as mock_split_image, \
         patch('python.prohibition_web_svc.middleware.event_middleware.create_pdf_with_images', return_value=b'%PDF') as mock_create_pdf, \
         patch('python.prohibition_web_svc.middleware.event_middleware.encryptPdf_method1') as mock_encrypt, \
         patch('python.prohibition_web_svc.middleware.event_middleware.os.path.exists', return_value=False), \
         patch('python.prohibition_web_svc.middleware.event_middleware.FormStorageRefs') as mock_storage_ref, \
         patch('python.prohibition_web_svc.middleware.event_middleware.SubmissionFormRef') as mock_submission_ref, \
         patch('python.prohibition_web_svc.middleware.event_middleware.SubmissionEvent') as mock_submission_event, \
         patch('builtins.open', mock_open()):

        mock_client = MagicMock()
        mock_minio_cls.return_value = mock_client

        result, _ = save_event_pdf(**kwargs)

        assert result is True
        mock_split_image.assert_not_called()
        mock_create_pdf.assert_called_once_with('/tmp/12h456.png', is_landscape=True)
        mock_encrypt.assert_called_once_with('/tmp/12h456.pdf', 'enc-key', '/tmp/12h456_encrypted.pdf')
        mock_client.fput_object.assert_called_once_with('forms-bucket', '12h456_encrypted.pdf', '/tmp/12h456_encrypted.pdf')
        mock_storage_ref.assert_called_once_with(
            form_id_12h=401,
            event_id=30,
            form_type='12h',
            storage_key='forms-bucket/12h456_encrypted.pdf',
            created_dt=mock_storage_ref.call_args.kwargs['created_dt'],
            updated_dt=mock_storage_ref.call_args.kwargs['updated_dt'],
        )
        mock_submission_ref.assert_called_once_with(
            submission_id=30,
            form_type='12h',
            form_id='12H456',
            form_version='3.0',
            storage_key='forms-bucket/12h456_encrypted.pdf',
        )
        mock_submission_event.assert_called_once_with(destination='ICBC')
        mock_db_session.add.assert_called()
        assert mock_db_session.add.call_count == 2  # FormStorageRefs + SubmissionFormRef
        mock_db_session.commit.assert_not_called()


# Tests for commit_transaction function

def test_commit_transaction_success(mock_db_session):
    """commit_transaction commits the session and returns True."""
    kwargs = {'payload': {'VI': True, 'VI_number': 'VI123'}}
    result, out = commit_transaction(**kwargs)
    assert result is True
    assert out == kwargs
    mock_db_session.commit.assert_called_once()
    mock_db_session.rollback.assert_not_called()


def test_commit_transaction_db_exception(mock_db_session):
    """commit_transaction rolls back and returns False with error on DB failure."""
    mock_db_session.commit.side_effect = Exception("commit failed")
    payload = {'VI': True, 'VI_number': 'VI-ERR'}
    kwargs = {'payload': payload}

    with patch('python.prohibition_web_svc.middleware.event_middleware.get_event_type', return_value=EventType.VI), \
         patch('python.prohibition_web_svc.middleware.event_middleware.get_ticket_no', return_value='VI-ERR'):
        result, out = commit_transaction(**kwargs)

    assert result is False
    assert 'error' in out
    assert out['error']['error_code'] == ErrorCode.E01
    assert 'commit failed' in out['error']['error_details']
    mock_db_session.rollback.assert_called_once()


def test_commit_transaction_no_payload(mock_db_session):
    """commit_transaction handles missing payload gracefully on error."""
    mock_db_session.commit.side_effect = Exception("oops")
    kwargs = {}

    with patch('python.prohibition_web_svc.middleware.event_middleware.get_event_type', return_value=None), \
         patch('python.prohibition_web_svc.middleware.event_middleware.get_ticket_no', return_value=None):
        result, out = commit_transaction(**kwargs)

    assert result is False
    assert 'error' in out
    mock_db_session.rollback.assert_called_once()


# Tests for _get_asd_expiry_date

def test_get_asd_expiry_date_alco_sensor_returns_parsed_datetime():
    """Returns a parsed datetime when test_used is 'alco-sensor' and date is present"""
    data = {
        'test_used': 'alco-sensor',
        'asd_expiry': '2024-06-15T08:30:00.000000+00:00',
    }
    result = _get_asd_expiry_date(data, 'test_used', 'asd_expiry', 'asd_expiry_6000')
    assert result is not None
    assert result.year == 2024
    assert result.month == 6
    assert result.day == 15


def test_get_asd_expiry_date_alcotest_6000_returns_parsed_datetime():
    """Returns a parsed datetime when test_used is 'alcotest-6000' and date is present"""
    data = {
        'test_used': 'alcotest-6000',
        'asd_expiry_6000': '2025-12-31T23:59:59.999999+00:00',
    }
    result = _get_asd_expiry_date(data, 'test_used', 'asd_expiry', 'asd_expiry_6000')
    assert result is not None
    assert result.year == 2025
    assert result.month == 12
    assert result.day == 31


def test_get_asd_expiry_date_alco_sensor_missing_date_returns_none():
    """Returns None when test_used is 'alco-sensor' but the date key is absent"""
    data = {'test_used': 'alco-sensor'}
    result = _get_asd_expiry_date(data, 'test_used', 'asd_expiry', 'asd_expiry_6000')
    assert result is None


def test_get_asd_expiry_date_alcotest_6000_missing_date_returns_none():
    """Returns None when test_used is 'alcotest-6000' but the date key is absent"""
    data = {'test_used': 'alcotest-6000'}
    result = _get_asd_expiry_date(data, 'test_used', 'asd_expiry', 'asd_expiry_6000')
    assert result is None


def test_get_asd_expiry_date_unknown_test_type_returns_none():
    """Returns None when test_used is neither 'alco-sensor' nor 'alcotest-6000'"""
    data = {
        'test_used': 'breathalyzer',
        'asd_expiry': '2024-06-15T08:30:00.000000+00:00',
        'asd_expiry_6000': '2024-06-15T08:30:00.000000+00:00',
    }
    result = _get_asd_expiry_date(data, 'test_used', 'asd_expiry', 'asd_expiry_6000')
    assert result is None


def test_get_asd_expiry_date_empty_data_returns_none():
    """Returns None when data dict is empty"""
    result = _get_asd_expiry_date({}, 'test_used', 'asd_expiry', 'asd_expiry_6000')
    assert result is None


def test_get_asd_expiry_date_invalid_date_format_returns_none():
    """Returns None and logs a warning when the date string cannot be parsed"""
    data = {
        'test_used': 'alco-sensor',
        'asd_expiry': 'not-a-date',
    }
    with patch('python.prohibition_web_svc.middleware.event_middleware.logger') as mock_logger:
        result = _get_asd_expiry_date(data, 'test_used', 'asd_expiry', 'asd_expiry_6000')
    assert result is None
    mock_logger.warning.assert_called_once()


# ── no form type present ──────────────────────────────────────────────────────

def test_check_if_form_number_was_used_no_form_type(mock_db_session):
    """Returns True without hitting the DB when no form type is set."""
    kwargs = {'payload': {}}
    result, out = check_if_form_number_was_used(**kwargs)
    assert result is True
    assert 'error' not in out
    mock_db_session.query.assert_not_called()


# ── VI form ───────────────────────────────────────────────────────────────────

def test_check_if_form_number_was_used_vi_not_found(mock_db_session):
    """Returns True when VI number does not exist in the DB."""
    mock_db_session.query.return_value.scalar.return_value = False
    kwargs = {'payload': {'VI': True, 'VI_number': 'V00001'}}
    result, out = check_if_form_number_was_used(**kwargs)
    assert result is True
    assert 'error' not in out


def test_check_if_form_number_was_used_vi_duplicate(mock_db_session):
    """Returns False with E09 error when VI number already exists."""
    mock_db_session.query.return_value.scalar.return_value = True
    kwargs = {'payload': {'VI': True, 'VI_number': 'V00001'}}
    with patch('python.prohibition_web_svc.middleware.event_middleware.get_event_type'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.get_ticket_no'):
        result, out = check_if_form_number_was_used(**kwargs)
    assert result is False
    assert out['error']['error_code'] == ErrorCode.E09
    assert 'V00001' in out['error']['error_details']


def test_check_if_form_number_was_used_vi_number_is_none(mock_db_session):
    """Skips DB check and returns True when VI_number is None."""
    kwargs = {'payload': {'VI': True, 'VI_number': None}}
    result, out = check_if_form_number_was_used(**kwargs)
    assert result is True
    assert 'error' not in out
    mock_db_session.query.assert_not_called()


# ── TwentyFourHour form ───────────────────────────────────────────────────────

def test_check_if_form_number_was_used_24h_not_found(mock_db_session):
    """Returns True when 24h number does not exist in the DB."""
    mock_db_session.query.return_value.scalar.return_value = False
    kwargs = {'payload': {'TwentyFourHour': True, 'twenty_four_hour_number': '24H001'}}
    result, out = check_if_form_number_was_used(**kwargs)
    assert result is True
    assert 'error' not in out


def test_check_if_form_number_was_used_24h_duplicate(mock_db_session):
    """Returns False with E09 error when 24h number already exists."""
    mock_db_session.query.return_value.scalar.return_value = True
    kwargs = {'payload': {'TwentyFourHour': True, 'twenty_four_hour_number': '24H001'}}
    with patch('python.prohibition_web_svc.middleware.event_middleware.get_event_type'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.get_ticket_no'):
        result, out = check_if_form_number_was_used(**kwargs)
    assert result is False
    assert out['error']['error_code'] == ErrorCode.E09
    assert '24H001' in out['error']['error_details']


def test_check_if_form_number_was_used_24h_number_is_none(mock_db_session):
    """Skips DB check and returns True when twenty_four_hour_number is None."""
    kwargs = {'payload': {'TwentyFourHour': True, 'twenty_four_hour_number': None}}
    result, out = check_if_form_number_was_used(**kwargs)
    assert result is True
    assert 'error' not in out
    mock_db_session.query.assert_not_called()


# ── TwelveHour form ───────────────────────────────────────────────────────────

def test_check_if_form_number_was_used_12h_not_found(mock_db_session):
    """Returns True when 12h number does not exist in the DB."""
    mock_db_session.query.return_value.scalar.return_value = False
    kwargs = {'payload': {'TwelveHour': True, 'twelve_hour_number': '12H001'}}
    result, out = check_if_form_number_was_used(**kwargs)
    assert result is True
    assert 'error' not in out


def test_check_if_form_number_was_used_12h_duplicate(mock_db_session):
    """Returns False with E09 error when 12h number already exists."""
    mock_db_session.query.return_value.scalar.return_value = True
    kwargs = {'payload': {'TwelveHour': True, 'twelve_hour_number': '12H001'}}
    with patch('python.prohibition_web_svc.middleware.event_middleware.get_event_type'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.get_ticket_no'):
        result, out = check_if_form_number_was_used(**kwargs)
    assert result is False
    assert out['error']['error_code'] == ErrorCode.E09
    assert '12H001' in out['error']['error_details']


def test_check_if_form_number_was_used_12h_number_is_none(mock_db_session):
    """Skips DB check and returns True when twelve_hour_number is None."""
    kwargs = {'payload': {'TwelveHour': True, 'twelve_hour_number': None}}
    result, out = check_if_form_number_was_used(**kwargs)
    assert result is True
    assert 'error' not in out
    mock_db_session.query.assert_not_called()


# ── multiple duplicates ───────────────────────────────────────────────────────

def test_check_if_form_number_was_used_multiple_duplicates(mock_db_session):
    """Error details lists all duplicate form numbers when multiple forms are present."""
    mock_db_session.query.return_value.scalar.return_value = True
    kwargs = {'payload': {
        'VI': True, 'VI_number': 'V00001',
        'TwentyFourHour': True, 'twenty_four_hour_number': '24H001',
    }}
    with patch('python.prohibition_web_svc.middleware.event_middleware.get_event_type'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.get_ticket_no'):
        result, out = check_if_form_number_was_used(**kwargs)
    assert result is False
    assert 'V00001' in out['error']['error_details']
    assert '24H001' in out['error']['error_details']


# ── DB exception ──────────────────────────────────────────────────────────────

def test_check_if_form_number_was_used_db_exception(mock_db_session):
    """Returns False and logs error when a DB exception is raised."""
    mock_db_session.query.side_effect = Exception("DB connection error")
    kwargs = {'payload': {'VI': True, 'VI_number': 'V00001'}}
    with patch('python.prohibition_web_svc.middleware.event_middleware.logger') as mock_logger:
        result, out = check_if_form_number_was_used(**kwargs)
    assert result is False
    mock_logger.error.assert_called_once()


# ── IRP form ──────────────────────────────────────────────────────────────────

def test_check_if_form_number_was_used_irp_not_found(mock_db_session):
    """Returns True when IRP number does not exist in the DB ."""
    mock_db_session.query.return_value.scalar.return_value = False
    kwargs = {'payload': {'IRP': True, 'IRP_number': 'IRP001'}}
    result, out = check_if_form_number_was_used(**kwargs)
    assert result is True
    assert 'error' not in out


def test_check_if_form_number_was_used_irp_duplicate(mock_db_session):
    """Returns False with E09 error when IRP number already exists."""
    mock_db_session.query.return_value.scalar.return_value = True
    kwargs = {'payload': {'IRP': True, 'IRP_number': 'IRP001'}}
    with patch('python.prohibition_web_svc.middleware.event_middleware.get_event_type'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.get_ticket_no'):
        result, out = check_if_form_number_was_used(**kwargs)
    assert result is False
    assert out['error']['error_code'] == ErrorCode.E09
    assert 'IRP001' in out['error']['error_details']


def test_check_if_form_number_was_used_irp_number_is_none(mock_db_session):
    """Skips IRP DB check and returns True when IRP_number is None (combined with VI to bypass early return)."""
    mock_db_session.query.return_value.scalar.return_value = False
    kwargs = {'payload': {'IRP': True, 'IRP_number': None}}
    result, out = check_if_form_number_was_used(**kwargs)
    assert result is True
    assert 'error' not in out


# ── validate_form_payload ─────────────────────────────────────────────────────

def test_validate_form_payload_valid_vi_payload():
    """Returns True for a valid VI payload with all required fields."""
    kwargs = {'payload': {'VI': True, 'VI_number': 'V00001', 'ff_application_id': 'app-001'}}
    result, out = validate_form_payload(**kwargs)
    assert result is True
    assert 'error' not in out


def test_validate_form_payload_valid_twenty_four_hour_payload():
    """Returns True for a valid TwentyFourHour payload."""
    kwargs = {'payload': {'TwentyFourHour': True, 'twenty_four_hour_number': '24H001', 'ff_application_id': 'app-002'}}
    result, out = validate_form_payload(**kwargs)
    assert result is True
    assert 'error' not in out


def test_validate_form_payload_valid_twelve_hour_payload():
    """Returns True for a valid TwelveHour payload."""
    kwargs = {'payload': {'TwelveHour': True, 'twelve_hour_number': '12H001', 'ff_application_id': 'app-003'}}
    result, out = validate_form_payload(**kwargs)
    assert result is True
    assert 'error' not in out


def test_validate_form_payload_valid_irp_payload():
    """Returns True for a valid IRP payload."""
    kwargs = {'payload': {'IRP': True, 'IRP_number': 'IRP001', 'ff_application_id': 'app-004'}}
    result, out = validate_form_payload(**kwargs)
    assert result is True
    assert 'error' not in out


def test_validate_form_payload_no_payload():
    """Returns False with E10 error when no payload is provided."""
    kwargs = {'payload': None}
    result, out = validate_form_payload(**kwargs)
    assert result is False
    assert out['error']['error_code'] == ErrorCode.E10
    assert out['error']['error_details'] == 'No payload provided'


def test_validate_form_payload_empty_payload():
    """Returns False with E10 error when payload is an empty dict."""
    kwargs = {'payload': {}}
    result, out = validate_form_payload(**kwargs)
    assert result is False
    assert out['error']['error_code'] == ErrorCode.E10


def test_validate_form_payload_vi_missing_form_number():
    """Returns False with E10 error when VI is True but VI_number is absent."""
    kwargs = {'payload': {'VI': True, 'ff_application_id': 'app-001'}}
    result, out = validate_form_payload(**kwargs)
    assert result is False
    assert out['error']['error_code'] == ErrorCode.E10
    assert 'missing form number' in out['error']['error_details']


def test_validate_form_payload_twenty_four_hour_missing_form_number():
    """Returns False with E10 error when TwentyFourHour is True but number is absent."""
    kwargs = {'payload': {'TwentyFourHour': True, 'ff_application_id': 'app-002'}}
    result, out = validate_form_payload(**kwargs)
    assert result is False
    assert out['error']['error_code'] == ErrorCode.E10
    assert 'missing form number' in out['error']['error_details']


def test_validate_form_payload_twelve_hour_missing_form_number():
    """Returns False with E10 error when TwelveHour is True but number is absent."""
    kwargs = {'payload': {'TwelveHour': True, 'ff_application_id': 'app-003'}}
    result, out = validate_form_payload(**kwargs)
    assert result is False
    assert out['error']['error_code'] == ErrorCode.E10
    assert 'missing form number' in out['error']['error_details']


def test_validate_form_payload_irp_missing_form_number():
    """Returns False with E10 error when IRP is True but IRP_number is absent."""
    kwargs = {'payload': {'IRP': True, 'ff_application_id': 'app-004'}}
    result, out = validate_form_payload(**kwargs)
    assert result is False
    assert out['error']['error_code'] == ErrorCode.E10
    assert 'missing form number' in out['error']['error_details']


def test_validate_form_payload_no_form_type_indicated():
    """Returns False with E10 error when payload has no recognized form type."""
    kwargs = {'payload': {'ff_application_id': 'app-005', 'driver_licence_no': 'DL123'}}
    result, out = validate_form_payload(**kwargs)
    assert result is False
    assert out['error']['error_code'] == ErrorCode.E10
    assert 'no form type indicated' in out['error']['error_details']


def test_validate_form_payload_missing_ff_application_id():
    """Returns False with E10 error when ff_application_id is absent."""
    kwargs = {'payload': {'VI': True, 'VI_number': 'V00001'}}
    result, out = validate_form_payload(**kwargs)
    assert result is False
    assert out['error']['error_code'] == ErrorCode.E10
    assert 'ff_application_id' in out['error']['error_details']


# ── validate_update ───────────────────────────────────────────────────────────

def test_validate_update_always_returns_true():
    """validate_update is a no-op that always returns (True, kwargs)."""
    kwargs = {'payload': {'VI': True}, 'user_guid': 'uid-1'}
    result, out = validate_update(**kwargs)
    assert result is True
    assert out == kwargs


# ── get_event_type ────────────────────────────────────────────────────────────

def test_get_event_type_twelve_hour():
    assert get_event_type({'TwelveHour': True}) == EventType.TWELVE_HOUR


def test_get_event_type_twenty_four_hour():
    assert get_event_type({'TwentyFourHour': True}) == EventType.TWENTY_FOUR_HOUR


def test_get_event_type_irp():
    assert get_event_type({'IRP': True}) == EventType.IRP


def test_get_event_type_vi():
    assert get_event_type({'VI': True}) == EventType.VI


def test_get_event_type_twelve_hour_takes_priority():
    """TwelveHour is checked first; mixed payload resolves to TWELVE_HOUR."""
    assert get_event_type({'TwelveHour': True, 'VI': True}) == EventType.TWELVE_HOUR


def test_get_event_type_no_form_type_returns_none():
    assert get_event_type({}) is None


def test_get_event_type_all_false_returns_none():
    assert get_event_type({'TwelveHour': False, 'TwentyFourHour': False, 'IRP': False, 'VI': False}) is None


# ── get_ticket_no ─────────────────────────────────────────────────────────────

def test_get_ticket_no_twelve_hour():
    assert get_ticket_no({'TwelveHour': True, 'twelve_hour_number': '12H001'}) == '12H001'


def test_get_ticket_no_twenty_four_hour():
    assert get_ticket_no({'TwentyFourHour': True, 'twenty_four_hour_number': '24H001'}) == '24H001'


def test_get_ticket_no_irp():
    assert get_ticket_no({'IRP': True, 'IRP_number': 'IRP001'}) == 'IRP001'


def test_get_ticket_no_vi():
    assert get_ticket_no({'VI': True, 'VI_number': 'V00001'}) == 'V00001'


def test_get_ticket_no_twelve_hour_takes_priority():
    assert get_ticket_no({'TwelveHour': True, 'twelve_hour_number': '12H001', 'VI': True, 'VI_number': 'V00001'}) == '12H001'


def test_get_ticket_no_no_form_type_returns_none():
    assert get_ticket_no({}) is None


# ── request_contains_a_payload ────────────────────────────────────────────────

def test_request_contains_a_payload_success():
    mock_request = MagicMock()
    mock_request.get_json.return_value = {'VI': True}
    kwargs = {'request': mock_request}
    result, out = request_contains_a_payload(**kwargs)
    assert result is True
    assert out['payload'] == {'VI': True}


def test_request_contains_a_payload_returns_false_when_json_is_none():
    mock_request = MagicMock()
    mock_request.get_json.return_value = None
    kwargs = {'request': mock_request}
    result, out = request_contains_a_payload(**kwargs)
    assert result is False


def test_request_contains_a_payload_returns_false_on_exception():
    mock_request = MagicMock()
    mock_request.get_json.side_effect = Exception("parse error")
    kwargs = {'request': mock_request}
    result, out = request_contains_a_payload(**kwargs)
    assert result is False


# ── get_json_payload ──────────────────────────────────────────────────────────

def test_get_json_payload_success():
    mock_request = MagicMock()
    mock_request.json = {'IRP': True, 'IRP_number': 'IRP999'}
    kwargs = {'request': mock_request}
    result, out = get_json_payload(**kwargs)
    assert result is True
    assert out['payload'] == {'IRP': True, 'IRP_number': 'IRP999'}


def test_get_json_payload_returns_false_on_exception():
    mock_request = MagicMock()
    type(mock_request).json = property(lambda self: (_ for _ in ()).throw(Exception("bad json")))
    kwargs = {'request': mock_request}
    result, out = get_json_payload(**kwargs)
    assert result is False


# ── get_events_for_user ───────────────────────────────────────────────────────

def test_get_events_for_user_success(mock_db_session):
    mock_event = MagicMock()
    mock_event.vi_form = None
    mock_event.twelve_hour_form = None
    mock_event.irp_form = None
    mock_event.twenty_four_hour_form = None
    mock_db_session.query.return_value.filter.return_value.all.return_value = [mock_event]

    with patch('python.prohibition_web_svc.middleware.event_middleware.asdict', return_value={'event_id': 1}) as mock_asdict, \
         patch('python.prohibition_web_svc.middleware.event_middleware.jsonify', return_value='<response>'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.make_response', return_value='<response>') as mock_make_response:
        kwargs = {'user_guid': 'uid-123'}
        result, out = get_events_for_user(**kwargs)

    assert result is True
    assert 'response' in out
    mock_make_response.assert_called_once()


def test_get_events_for_user_returns_empty_list(mock_db_session):
    mock_db_session.query.return_value.filter.return_value.all.return_value = []

    with patch('python.prohibition_web_svc.middleware.event_middleware.jsonify', return_value='[]'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.make_response', return_value='<response>'):
        kwargs = {'user_guid': 'uid-000'}
        result, out = get_events_for_user(**kwargs)

    assert result is True
    assert 'response' in out


def test_get_events_for_user_returns_false_on_db_exception(mock_db_session):
    mock_db_session.query.side_effect = Exception("DB error")
    kwargs = {'user_guid': 'uid-err'}
    result, out = get_events_for_user(**kwargs)
    assert result is False


def test_get_events_for_user_includes_sub_forms(mock_db_session):
    """asdict is called for each sub-form when present."""
    mock_event = MagicMock()
    mock_event.vi_form = MagicMock()
    mock_event.twelve_hour_form = MagicMock()
    mock_event.irp_form = MagicMock()
    mock_event.twenty_four_hour_form = MagicMock()
    mock_db_session.query.return_value.filter.return_value.all.return_value = [mock_event]

    call_count = {'n': 0}
    def fake_asdict(obj):
        call_count['n'] += 1
        return {}

    with patch('python.prohibition_web_svc.middleware.event_middleware.asdict', side_effect=fake_asdict), \
         patch('python.prohibition_web_svc.middleware.event_middleware.jsonify', return_value='[]'), \
         patch('python.prohibition_web_svc.middleware.event_middleware.make_response', return_value='<r>'):
        result, _ = get_events_for_user(user_guid='uid-x')

    # asdict called once for event + once each for vi_form, twelve_hour_form, irp_form, twenty_four_hour_form
    assert call_count['n'] == 5


# ── save_event_pdf – no form in payload ──────────────────────────────────────

def test_save_event_pdf_returns_true_when_no_form_type(mock_db_session):
    """When payload contains no recognized form type, PDF processing is skipped."""
    payload = {'driver_licence_no': 'DL123'}  # no VI/TwentyFourHour/TwelveHour/IRP
    kwargs = {'payload': payload, 'event': MagicMock(), 'submission_id': 1}
    with patch('python.prohibition_web_svc.middleware.event_middleware.Config.MINIO_CERT_FILE', ''):
        result, out = save_event_pdf(**kwargs)
    assert result is True


# ── get_irp_form_by_event_id ──────────────────────────────────────────────────

def test_get_irp_form_by_event_id_found(mock_db_session):
    mock_irp_form = MagicMock()
    mock_db_session.query.return_value.filter.return_value.first.return_value = mock_irp_form
    kwargs = {'event_id': 42}
    result, out = get_irp_form_by_event_id(**kwargs)
    assert result is True
    assert out['irp_form'] is mock_irp_form


def test_get_irp_form_by_event_id_not_found_returns_false(mock_db_session):
    mock_db_session.query.return_value.filter.return_value.first.return_value = None
    kwargs = {'event_id': 99}
    result, out = get_irp_form_by_event_id(**kwargs)
    assert result is False
    assert 'irp_form' not in out


def test_get_irp_form_by_event_id_db_exception_returns_false(mock_db_session):
    mock_db_session.query.side_effect = Exception("DB error")
    kwargs = {'event_id': 1}
    result, out = get_irp_form_by_event_id(**kwargs)
    assert result is False


# ── log_irp_update_to_splunk ──────────────────────────────────────────────────

def test_log_irp_update_to_splunk_sets_splunk_data():
    mock_irp_form = MagicMock()
    mock_irp_form.event_id = 7
    mock_irp_form.irp_number = 'IRP-007'
    payload = {'driver_licence_no': 'DL123', 'IRP': True}
    kwargs = {'payload': payload, 'irp_form': mock_irp_form}
    result, out = log_irp_update_to_splunk(**kwargs)
    assert result is True
    assert out['splunk_data']['event'] == 'update IRP RTS event'
    assert out['splunk_data']['event_id'] == 7
    assert out['splunk_data']['irp_number'] == 'IRP-007'
    assert out['splunk_data']['payload']['driver_licence_no'] == '[REDACTED]'


def test_log_irp_update_to_splunk_returns_true_when_no_irp_form():
    kwargs = {'payload': {}, 'irp_form': None}
    result, out = log_irp_update_to_splunk(**kwargs)
    assert result is True
    assert out['splunk_data']['event_id'] is None
    assert out['splunk_data']['irp_number'] is None


def test_log_irp_update_to_splunk_returns_true_on_exception():
    """Even when an exception occurs the function still returns True."""
    kwargs = {}  # missing 'payload' key will trigger AttributeError in _mask_sensitive_data
    with patch('python.prohibition_web_svc.middleware.event_middleware.logger'):
        result, out = log_irp_update_to_splunk(**kwargs)
    assert result is True


# ── update_irp_form_data ──────────────────────────────────────────────────────

def test_update_irp_form_data_success():
    mock_irp_form = MagicMock()
    mock_irp_form.event_id = 5
    payload = {'IRP_number': 'IRP-005'}
    kwargs = {'irp_form': mock_irp_form, 'payload': payload}

    with patch('python.prohibition_web_svc.middleware.event_middleware.IRPMapper') as mock_mapper:
        result, out = update_irp_form_data(**kwargs)

    assert result is True
    mock_mapper.map_update_irp_form.assert_called_once_with(mock_irp_form, payload)
    assert out['response_dict'] == {'event_id': 5}


def test_update_irp_form_data_returns_false_on_mapper_exception(mock_db_session):
    mock_irp_form = MagicMock()
    mock_irp_form.event_id = 6
    mock_irp_form.irp_number = 'IRP-006'
    payload = {}
    kwargs = {'irp_form': mock_irp_form, 'payload': payload}

    with patch('python.prohibition_web_svc.middleware.event_middleware.IRPMapper') as mock_mapper:
        mock_mapper.map_update_irp_form.side_effect = Exception("mapper error")
        result, out = update_irp_form_data(**kwargs)

    assert result is False
    assert 'error' in out
    assert out['error']['error_code'] == ErrorCode.E01
    assert 'mapper error' in out['error']['error_details']
    assert out['error']['event_type'] == EventType.IRP
    assert out['error']['ticket_no'] == 'IRP-006'
    mock_db_session.rollback.assert_called_once()


def test_update_irp_form_data_error_includes_event_id(mock_db_session):
    mock_irp_form = MagicMock()
    mock_irp_form.event_id = 9
    kwargs = {'irp_form': mock_irp_form, 'payload': {}}

    with patch('python.prohibition_web_svc.middleware.event_middleware.IRPMapper') as mock_mapper:
        mock_mapper.map_update_irp_form.side_effect = Exception("fail")
        result, out = update_irp_form_data(**kwargs)

    assert out['error']['event_id'] == 9
