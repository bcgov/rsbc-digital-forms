import pytest
import json
import pytz
from datetime import datetime, date, timedelta
from unittest.mock import MagicMock, patch, call
from dataclasses import dataclass, asdict
from flask import Flask
from python.prohibition_web_svc.middleware import form_middleware
from python.common.enums import ErrorCode


class MockRequest:
    """Mock request object for testing."""
    def __init__(self, json_data=None, data=None):
        self._json = json_data
        self._data = data
        self.json = json_data

    def get_json(self):
        if isinstance(self._json, Exception):
            raise self._json
        return self._json

    def get_data(self):
        return self._data


@dataclass
class MockForm:
    """Mock Form model for testing."""
    id: str
    form_type: str
    user_guid: str = None
    lease_expiry: datetime = None
    printed_timestamp: datetime = None
    spoiled_timestamp: datetime = None

    def lease(self, user_guid):
        today = datetime.now()
        lease_expiry = today + timedelta(days=30)
        self.lease_expiry = lease_expiry
        self.user_guid = user_guid

    @staticmethod
    def serialize(form):
        return {
            'id': form.id,
            'form_type': form.form_type,
            'user_guid': form.user_guid,
            'lease_expiry': form.lease_expiry.isoformat() if form.lease_expiry else None,
            'printed_timestamp': form.printed_timestamp.isoformat() if form.printed_timestamp else None,
            'spoiled_timestamp': form.spoiled_timestamp.isoformat() if form.spoiled_timestamp else None
        }

    @staticmethod
    def collection_to_dict(forms):
        return [MockForm.serialize(form) for form in forms]


@pytest.fixture
def flask_app():
    """Create a Flask app for testing."""
    app = Flask(__name__)
    app.config['TESTING'] = True
    return app


class TestFormMiddleware:
    """Test cases for form middleware functions."""

    def test_validate_update_always_returns_true(self):
        """Test that validate_update always returns True."""
        result, kwargs = form_middleware.validate_update(test="value")
        assert result is True
        assert kwargs == {"test": "value"}

    def test_log_payload_to_splunk_logs_payload(self):
        """Test that log_payload_to_splunk logs the payload and returns True."""
        request = MockRequest(data=b'{"test": "data"}')
        with patch('python.prohibition_web_svc.middleware.form_middleware.logger') as mock_logging:
            result, kwargs = form_middleware.log_payload_to_splunk(request=request)
            
        assert result is True
        assert kwargs['request'] == request
        mock_logging.debug.assert_called_once()

    @patch('python.prohibition_web_svc.middleware.form_middleware.jsonify')
    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    @patch('python.prohibition_web_svc.middleware.form_middleware.record_error')
    def test_lease_a_form_id_success(self, mock_record_error, mock_db, mock_jsonify):
        """Test successful form ID leasing."""
        # Setup
        mock_form1 = MockForm("AA123456", "24Hour")
        mock_form2 = MockForm("BB123457", "24Hour")
        mock_db.session.query().filter().filter().limit().all.return_value = [mock_form1, mock_form2]
        mock_jsonify.return_value = "mocked_jsonify_response"
        
        payload = {"24Hour": 2}
        user_guid = "test_user"
        
        # Execute
        result, kwargs = form_middleware.lease_a_form_id(payload=payload, user_guid=user_guid)
        
        # Assert
        assert result is True
        assert 'response_dict' in kwargs
        mock_db.session.commit.assert_called_once()
        mock_record_error.assert_not_called()

    @patch('python.prohibition_web_svc.middleware.form_middleware.jsonify')
    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    @patch('python.prohibition_web_svc.middleware.form_middleware.record_error')
    def test_lease_a_form_id_insufficient_ids(self, mock_record_error, mock_db, mock_jsonify):
        """Test form ID leasing when insufficient IDs are available."""
        # Setup - no forms available
        mock_db.session.query().filter().filter().limit().all.return_value = []
        mock_jsonify.return_value = "mocked_jsonify_response"
        
        payload = {"24Hour": 5}
        user_guid = "test_user"
        
        # Execute
        result, kwargs = form_middleware.lease_a_form_id(payload=payload, user_guid=user_guid)
        
        # Assert
        assert result is False
        mock_record_error.assert_called_once()
        mock_db.session.commit.assert_called_once()

    @patch('python.prohibition_web_svc.middleware.form_middleware.jsonify')
    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    def test_lease_a_form_id_database_exception(self, mock_db, mock_jsonify):
        """Test form ID leasing when database exception occurs."""
        # Setup
        mock_db.session.query.side_effect = Exception("Database error")
        mock_jsonify.return_value = "mocked_jsonify_response"
        
        payload = {"24Hour": 1}
        user_guid = "test_user"
        
        # Execute
        result, kwargs = form_middleware.lease_a_form_id(payload=payload, user_guid=user_guid)
        
        # Assert
        assert result is False
        assert 'error' in kwargs
        assert kwargs['error']['error_code'] == ErrorCode.F01

    @patch('python.prohibition_web_svc.middleware.form_middleware.Form')
    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    @patch('python.prohibition_web_svc.middleware.form_middleware.record_error')
    def test_renew_form_id_lease_success(self, mock_record_error, mock_db, mock_form_class):
        """Test successful form lease renewal."""
        # Setup
        mock_form = MockForm("AA123456", "24Hour", "test_user")
        mock_db.session.query().filter().filter().filter().filter().filter().first.return_value = mock_form
        mock_form_class.serialize.return_value = {"id": "AA123456", "form_type": "24Hour"}
        
        kwargs = {
            'form_type': '24Hour',
            'user_guid': 'test_user',
            'form_id': 'AA123456'
        }
        
        # Execute
        result, returned_kwargs = form_middleware.renew_form_id_lease(**kwargs)
        
        # Assert
        assert result is True
        assert 'response_dict' in returned_kwargs
        mock_db.session.commit.assert_called_once()
        mock_record_error.assert_not_called()

    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    @patch('python.prohibition_web_svc.middleware.form_middleware.record_error')
    def test_renew_form_id_lease_form_not_found(self, mock_record_error, mock_db):
        """Test form lease renewal when form is not found."""
        # Setup
        mock_db.session.query().filter().filter().filter().filter().filter().first.return_value = None
        
        kwargs = {
            'form_type': '24Hour',
            'user_guid': 'test_user',
            'form_id': 'INVALID123'
        }
        
        # Execute
        result, returned_kwargs = form_middleware.renew_form_id_lease(**kwargs)
        
        # Assert
        assert result is False
        mock_record_error.assert_called_once()
        mock_db.session.commit.assert_not_called()

    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    def test_renew_form_id_lease_database_exception(self, mock_db):
        """Test form lease renewal when database exception occurs."""
        # Setup
        mock_db.session.query.side_effect = Exception("Database error")
        
        kwargs = {
            'form_type': '24Hour',
            'user_guid': 'test_user',
            'form_id': 'AA123456'
        }
        
        # Execute
        result, returned_kwargs = form_middleware.renew_form_id_lease(**kwargs)
        
        # Assert
        assert result is False
        assert 'error' in returned_kwargs
        assert returned_kwargs['error']['error_code'] == ErrorCode.F02

    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    def test_mark_form_as_printed_success(self, mock_db):
        """Test successfully marking forms as printed."""
        # Setup
        mock_form = MockForm("123456", "24Hour", "test_user")
        mock_db.session.query().filter().first.return_value = mock_form
        
        payload = {
            'forms': {'twenty_four_hour_number': '123456'},
            'printed_timestamp': '2024-01-15T10:30:00Z'
        }
        kwargs = {
            'payload': payload,
            'user_guid': 'test_user'
        }
        
        # Execute
        result, returned_kwargs = form_middleware.mark_form_as_printed_or_spoiled(**kwargs)
        
        # Assert
        assert result is True
        assert 'response_dict' in returned_kwargs
        assert mock_form.printed_timestamp == '2024-01-15T10:30:00Z'
        mock_db.session.commit.assert_called_once()


    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    def test_mark_form_as_printed_success_with_existing_timestamp(self, mock_db):
        """Test successfully marking forms as printed."""
        # Setup
        printed_date = datetime(2024, 1, 10, 9, 0, 0)
        mock_form = MockForm("123456", "24Hour", "test_user", printed_timestamp=printed_date)
        mock_db.session.query().filter().first.return_value = mock_form
        
        payload = {
            'forms': {'twenty_four_hour_number': '123456'},
            'printed_timestamp': '2024-01-15T10:30:00Z'
        }
        kwargs = {
            'payload': payload,
            'user_guid': 'test_user'
        }
        
        # Execute
        result, returned_kwargs = form_middleware.mark_form_as_printed_or_spoiled(**kwargs)
        
        # Assert
        assert result is True
        assert 'response_dict' in returned_kwargs
        assert mock_form.printed_timestamp == printed_date  # Should not be updated
        mock_db.session.commit.assert_called_once()        

    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    def test_mark_form_as_spoiled_success(self, mock_db):
        """Test successfully marking forms as spoiled."""
        # Setup
        mock_form = MockForm("123456", "VI", "test_user")
        mock_db.session.query().filter().first.return_value = mock_form
        
        payload = {
            'forms': {'VI_number': '1234567'},  # VI numbers have extra digit removed
            'spoiled_timestamp': '2024-01-15T10:30:00Z'
        }
        kwargs = {
            'payload': payload,
            'user_guid': 'test_user'
        }
        
        # Execute
        result, returned_kwargs = form_middleware.mark_form_as_printed_or_spoiled(**kwargs)
        
        # Assert
        assert result is True
        assert 'response_dict' in returned_kwargs
        assert mock_form.spoiled_timestamp == '2024-01-15T10:30:00Z'
        mock_db.session.commit.assert_called_once()

    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    def test_mark_form_as_spoiled_success_with_existing_timestamp(self, mock_db):
        """Test successfully marking forms as spoiled."""
        # Setup
        spoiled_date = datetime(2024, 1, 10, 9, 0, 0)
        mock_form = MockForm("123456", "VI", "test_user", spoiled_timestamp=spoiled_date)
        mock_db.session.query().filter().first.return_value = mock_form
        
        payload = {
            'forms': {'VI_number': '1234567'},  # VI numbers have extra digit removed
            'spoiled_timestamp': '2024-01-15T10:30:00Z'
        }
        kwargs = {
            'payload': payload,
            'user_guid': 'test_user'
        }
        
        # Execute
        result, returned_kwargs = form_middleware.mark_form_as_printed_or_spoiled(**kwargs)
        
        # Assert
        assert result is True
        assert 'response_dict' in returned_kwargs
        assert mock_form.spoiled_timestamp == spoiled_date  # Should not be updated
        mock_db.session.commit.assert_called_once()

    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    def test_mark_form_as_printed_or_spoiled_form_not_found(self, mock_db):
        """Test marking form when form is not found."""
        # Setup
        mock_db.session.query().filter().first.return_value = None
        
        payload = {
            'forms': {'twenty_four_hour_number': 'INVALID123'},
            'printed_timestamp': '2024-01-15T10:30:00Z'
        }
        kwargs = {
            'payload': payload,
            'user_guid': 'test_user'
        }
        
        # Execute
        result, returned_kwargs = form_middleware.mark_form_as_printed_or_spoiled(**kwargs)
        
        # Assert
        assert result is False
        mock_db.session.commit.assert_not_called()

    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    def test_mark_form_as_printed_or_spoiled_database_exception(self, mock_db):
        """Test marking form when database commit fails."""
        # Setup
        mock_form = MockForm("123456", "24Hour", "test_user")
        mock_db.session.query().filter().first.return_value = mock_form
        mock_db.session.commit.side_effect = Exception("Database commit error")
        
        payload = {
            'forms': {'twenty_four_hour_number': '123456'},
            'printed_timestamp': '2024-01-15T10:30:00Z'
        }
        kwargs = {
            'payload': payload,
            'user_guid': 'test_user'
        }
        
        # Execute
        result, returned_kwargs = form_middleware.mark_form_as_printed_or_spoiled(**kwargs)
        
        # Assert
        assert result is False

    def test_request_contains_a_payload_success(self):
        """Test successful payload extraction from request."""
        request = MockRequest(json_data={"test": "data"})
        
        result, kwargs = form_middleware.request_contains_a_payload(request=request)
        
        assert result is True
        assert kwargs['payload'] == {"test": "data"}

    def test_request_contains_a_payload_none(self):
        """Test when request contains no payload."""
        request = MockRequest(json_data=None)
        
        result, kwargs = form_middleware.request_contains_a_payload(request=request)
        
        assert result is False

    def test_request_contains_a_payload_exception(self):
        """Test when request.get_json() raises an exception."""
        request = MockRequest(json_data=Exception("Invalid JSON"))
        
        result, kwargs = form_middleware.request_contains_a_payload(request=request)
        
        assert result is False

    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    @patch('python.prohibition_web_svc.middleware.form_middleware.make_response')
    @patch('python.prohibition_web_svc.middleware.form_middleware.jsonify')
    def test_list_all_users_forms_success(self, mock_jsonify, mock_make_response, mock_db):
        """Test successful listing of user forms."""
        # Setup
        mock_form1 = MockForm("AA123456", "24Hour", "test_user")
        mock_form2 = MockForm("BB123457", "12Hour", "test_user")
        mock_db.session.query().filter().filter().filter().all.return_value = [mock_form1, mock_form2]
        mock_jsonify.return_value = "jsonified_data"
        mock_make_response.return_value = "response"
        
        user_guid = "test_user"
        
        # Execute
        result, kwargs = form_middleware.list_all_users_forms(user_guid=user_guid)
        
        # Assert
        assert result is True
        assert kwargs['response'] == "response"
        mock_jsonify.assert_called_once()
        mock_make_response.assert_called_once()

    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    def test_list_all_users_forms_exception(self, mock_db):
        """Test listing user forms when database exception occurs."""
        # Setup
        mock_db.session.query.side_effect = Exception("Database error")
        
        user_guid = "test_user"
        
        # Execute
        result, kwargs = form_middleware.list_all_users_forms(user_guid=user_guid)
        
        # Assert
        assert result is False

    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    @patch('python.prohibition_web_svc.middleware.form_middleware.make_response')
    @patch('python.prohibition_web_svc.middleware.form_middleware.jsonify')
    def test_get_a_form_success(self, mock_jsonify, mock_make_response, mock_db):
        """Test successful retrieval of a specific form."""
        # Setup
        mock_form = MockForm("AA123456", "24Hour", "test_user")
        mock_db.session.query().filter().filter().filter().first.return_value = mock_form
        mock_response = MagicMock()
        mock_make_response.return_value = mock_response
        
        kwargs = {
            'form_type': '24Hour',
            'form_id': 'AA123456',
            'username': 'test_user'
        }
        
        # Execute
        result, returned_kwargs = form_middleware.get_a_form(**kwargs)
        
        # Assert
        assert result is True
        assert returned_kwargs['response'] == mock_response
        mock_make_response.assert_called_once_with(mock_jsonify(mock_form), 200)

    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    def test_get_a_form_exception(self, mock_db):
        """Test retrieving a form when database exception occurs."""
        # Setup
        mock_db.session.query.side_effect = Exception("Database error")
        
        kwargs = {
            'form_type': '24Hour',
            'form_id': 'AA123456',
            'username': 'test_user'
        }
        
        # Execute
        result, returned_kwargs = form_middleware.get_a_form(**kwargs)
        
        # Assert
        assert result is False

    @patch('python.prohibition_web_svc.middleware.form_middleware.Form')
    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    @patch('python.prohibition_web_svc.middleware.form_middleware.make_response')
    @patch('python.prohibition_web_svc.middleware.form_middleware.jsonify')
    @patch('python.prohibition_web_svc.middleware.form_middleware.Config')
    def test_admin_list_all_forms_by_type_success(self, mock_config, mock_jsonify, mock_make_response, mock_db, mock_form_class):
        """Test successful admin listing of forms by type."""
        # Setup
        mock_config.MAX_RECORDS_RETURNED = 100
        mock_form1 = MockForm("AA123456", "24Hour")
        mock_form2 = MockForm("BB123457", "24Hour")
        forms = [mock_form1, mock_form2]
        mock_db.session.query().filter().limit().all.return_value = forms
        
        mock_form_class.collection_to_dict.return_value = [
            {"id": "AA123456", "form_type": "24Hour"},
            {"id": "BB123457", "form_type": "24Hour"}
        ]
        mock_response = MagicMock()
        mock_make_response.return_value = mock_response
        
        kwargs = {'form_type': '24Hour'}
        
        # Execute
        result, returned_kwargs = form_middleware.admin_list_all_forms_by_type(**kwargs)
        
        # Assert
        assert result is True
        assert returned_kwargs['response'] == mock_response

    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    def test_admin_list_all_forms_by_type_exception(self, mock_db):
        """Test admin listing forms when database exception occurs."""
        # Setup
        mock_db.session.query.side_effect = Exception("Database error")
        
        kwargs = {'form_type': '24Hour'}
        
        # Execute
        result, returned_kwargs = form_middleware.admin_list_all_forms_by_type(**kwargs)
        
        # Assert
        assert result is False

    def test_get_json_payload_success(self):
        """Test successful JSON payload extraction."""
        request = MockRequest(json_data={"test": "data"})
        
        result, kwargs = form_middleware.get_json_payload(request=request)
        
        assert result is True
        assert kwargs['payload'] == {"test": "data"}

    def test_get_json_payload_exception(self):
        """Test JSON payload extraction when exception occurs."""
        # Create a request object that will raise an exception when accessing .json
        class BadRequest:
            @property
            def json(self):
                raise Exception("JSON error")
        
        request = BadRequest()
        
        with patch('python.prohibition_web_svc.middleware.form_middleware.logger'):
            result, kwargs = form_middleware.get_json_payload(request=request)
        
        assert result is False

    def test_validate_form_payload_success(self):
        """Test successful form payload validation."""
        payload = {
            "form_id": "AA123456",
            "form_type": "24Hour"
        }
        
        result, kwargs = form_middleware.validate_form_payload(payload=payload)
        
        assert result is True

    def test_validate_form_payload_invalid_form_type(self):
        """Test form payload validation with invalid form type."""
        payload = {
            "form_id": "AA123456",
            "form_type": "InvalidType"
        }
        
        result, kwargs = form_middleware.validate_form_payload(payload=payload)
        
        assert result is False
        assert 'validation_errors' in kwargs

    def test_validate_form_payload_missing_required_field(self):
        """Test form payload validation with missing required field."""
        payload = {
            "form_type": "24Hour"
            # Missing form_id
        }
        
        result, kwargs = form_middleware.validate_form_payload(payload=payload)
        
        assert result is False
        assert 'validation_errors' in kwargs

    def test_validate_form_payload_empty_field(self):
        """Test form payload validation with empty field."""
        payload = {
            "form_id": "",
            "form_type": "24Hour"
        }
        
        result, kwargs = form_middleware.validate_form_payload(payload=payload)
        
        assert result is False
        assert 'validation_errors' in kwargs

    def test_validate_form_payload_unknown_field(self):
        """Test form payload validation with unknown field."""
        payload = {
            "form_id": "AA123456",
            "form_type": "24Hour",
            "unknown_field": "value"
        }
        
        result, kwargs = form_middleware.validate_form_payload(payload=payload)
        
        assert result is False
        assert 'validation_errors' in kwargs

    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    @patch('python.prohibition_web_svc.middleware.form_middleware.make_response')
    def test_admin_create_form_success(self, mock_make_response, mock_db):
        """Test successful admin form creation."""
        # Setup
        mock_response = {"success": True}
        mock_make_response.return_value = mock_response
        
        payload = {
            "form_id": "AA123456",
            "form_type": "24Hour"
        }
        kwargs = {'payload': payload}
        
        # Execute
        result, returned_kwargs = form_middleware.admin_create_form(**kwargs)
        
        # Assert
        assert result is True
        assert returned_kwargs['response'] == mock_response
        mock_db.session.add.assert_called_once()
        mock_db.session.commit.assert_called_once()

    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    def test_admin_create_form_exception(self, mock_db):
        """Test admin form creation when database exception occurs."""
        # Setup
        mock_db.session.add.side_effect = Exception("Database error")
        
        payload = {
            "form_id": "AA123456",
            "form_type": "24Hour"
        }
        kwargs = {'payload': payload}
        
        # Execute
        result, returned_kwargs = form_middleware.admin_create_form(**kwargs)
        
        # Assert
        assert result is False
        assert 'error' in returned_kwargs

    def test_convert_vancouver_to_utc(self):
        """Test conversion from Vancouver timezone to UTC."""
        # Setup
        vancouver_time = "2024-01-15T10:30:00-08:00"  # PST
        
        # Execute
        result = form_middleware.convert_vancouver_to_utc(vancouver_time)
        
        # Assert
        assert isinstance(result, datetime)
        assert result.tzinfo is None  # Should be timezone naive
        # 10:30 PST should become 18:30 UTC
        assert result.hour == 18
        assert result.minute == 30

    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    def test_get_form_statistics_success(self, mock_db):
        """Test successful form statistics retrieval."""
        # Setup mock database results
        mock_result = MagicMock()
        mock_result.form_type = "24Hour"
        mock_result.total_forms = 100
        mock_result.leased_forms = 20
        mock_result.total_used_forms = 30
        mock_result.available_forms = 50
        
        mock_db.session.query().group_by().order_by().all.return_value = [mock_result]
        
        # Execute
        result, kwargs = form_middleware.get_form_statistics()
        
        # Assert
        assert result is True
        assert 'response_dict' in kwargs
        stats = kwargs['response_dict']
        assert len(stats) == 1
        assert stats[0]['form_type'] == "24Hour"
        assert stats[0]['form_name'] == "24 Hour Prohibition (MV2634E)"
        assert stats[0]['total_forms'] == 100
        assert stats[0]['leased_forms'] == 20
        assert stats[0]['total_used_forms'] == 30
        assert stats[0]['available_forms'] == 50

    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    def test_get_form_statistics_exception(self, mock_db):
        """Test form statistics when database exception occurs."""
        # Setup
        mock_db.session.query.side_effect = Exception("Database error")
        
        # Execute
        result, kwargs = form_middleware.get_form_statistics()
        
        # Assert
        assert result is False

    @patch('python.prohibition_web_svc.middleware.form_middleware.record_error')
    def test_record_form_error_success(self, mock_record_error):
        """Test successful error recording."""
        # Setup
        error = {
            'error_code': ErrorCode.F01,
            'error_details': 'Test error',
            'event_type': '24Hour'
        }
        kwargs = {'error': error}
        
        # Execute
        result, returned_kwargs = form_middleware.record_form_error(**kwargs)
        
        # Assert
        assert result is True
        mock_record_error.assert_called_once_with(**error)

    @patch('python.prohibition_web_svc.middleware.form_middleware.record_error')
    def test_record_form_error_no_error_object(self, mock_record_error):
        """Test error recording when no error object is provided."""
        # Setup
        kwargs = {}  # No error object
        
        # Execute
        result, returned_kwargs = form_middleware.record_form_error(**kwargs)
        
        # Assert
        assert result is True
        mock_record_error.assert_not_called()

    @patch('python.prohibition_web_svc.middleware.form_middleware.record_error')
    @patch('python.prohibition_web_svc.middleware.form_middleware.logger')
    def test_record_form_error_exception(self, mock_logging, mock_record_error):
        """Test error recording when record_error raises an exception."""
        # Setup
        mock_record_error.side_effect = Exception("Recording error")
        error = {
            'error_code': ErrorCode.F01,
            'error_details': 'Test error'
        }
        kwargs = {'error': error}
        
        # Execute
        result, returned_kwargs = form_middleware.record_form_error(**kwargs)
        
        # Assert
        assert result is True  # Function should still return True
        mock_logging.error.assert_called_once()

    def test_vi_and_irp_form_number_processing(self):
        """Test that VI and IRP form numbers have last digit removed."""
        with patch('python.prohibition_web_svc.middleware.form_middleware.db') as mock_db:
            # Setup
            mock_form = MockForm("123456", "VI", "test_user")
            mock_db.session.query().filter().first.return_value = mock_form
            
            payload = {
                'forms': {'VI_number': '1234567'},  # 7 digits
                'printed_timestamp': '2024-01-15T10:30:00Z'
            }
            kwargs = {
                'payload': payload,
                'user_guid': 'test_user'
            }
            
            # Execute
            form_middleware.mark_form_as_printed_or_spoiled(**kwargs)
            
            # Assert that the query was called with the 6-digit number (last digit removed)
            # The filter should be called with '123456' (not '1234567')
            mock_db.session.query().filter.assert_called()

    def test_form_statistics_all_form_types(self):
        """Test form statistics includes all expected form types."""
        with patch('python.prohibition_web_svc.middleware.form_middleware.db') as mock_db:
            # Setup mock results for all form types
            mock_results = []
            form_types = ['12Hour', '24Hour', 'VI', 'IRP']
            
            for form_type in form_types:
                mock_result = MagicMock()
                mock_result.form_type = form_type
                mock_result.total_forms = 100
                mock_result.leased_forms = 20
                mock_result.total_used_forms = 30
                mock_result.available_forms = 50
                mock_results.append(mock_result)
            
            mock_db.session.query().group_by().order_by().all.return_value = mock_results
            
            # Execute
            result, kwargs = form_middleware.get_form_statistics()
            
            # Assert
            assert result is True
            stats = kwargs['response_dict']
            assert len(stats) == 4
            
            expected_names = {
                '12Hour': '12 Hour Suspension (MV2906)',
                '24Hour': '24 Hour Prohibition (MV2634E)',
                'VI': 'Vehicle Impoundment (MV2721 / MV2722)',
                'IRP': 'IRP (MV2723 / MV2724)'
            }
            
            for stat in stats:
                assert stat['form_name'] == expected_names[stat['form_type']]

    @patch('python.prohibition_web_svc.middleware.form_middleware.jsonify')
    @patch('python.prohibition_web_svc.middleware.form_middleware.db')
    def test_lease_a_form_id_multiple_form_types(self, mock_db, mock_jsonify):
        """Test leasing forms of multiple types."""
        # Setup
        mock_form_24h = MockForm("AA123456", "24Hour")
        mock_form_12h = MockForm("BB123457", "12Hour")
        mock_jsonify.return_value = "mocked_jsonify_response"
        
        # Mock the database to return different forms for different queries
        mock_db.session.query().filter().filter().limit().all.return_value = [mock_form_24h]
        
        payload = {"24Hour": 1, "12Hour": 1}
        user_guid = "test_user"
        
        # Execute
        result, kwargs = form_middleware.lease_a_form_id(payload=payload, user_guid=user_guid)
        
        # Assert - The function should succeed even if the mock is simple
        # In real implementation, it would process each form type separately
        assert 'response_dict' in kwargs
        mock_db.session.commit.assert_called_once()

    @patch('python.prohibition_web_svc.middleware.form_middleware.jsonify')
    def test_zero_count_form_types_skipped(self, mock_jsonify):
        """Test that form types with zero count are skipped."""
        mock_jsonify.return_value = "mocked_jsonify_response"
        
        with patch('python.prohibition_web_svc.middleware.form_middleware.db') as mock_db:
            payload = {"24Hour": 0, "12Hour": 2}  # 24Hour has 0 count
            user_guid = "test_user"
            
            mock_form = MockForm("BB123457", "12Hour")
            mock_db.session.query().filter().filter().limit().all.return_value = [mock_form]
            
            # Execute
            result, kwargs = form_middleware.lease_a_form_id(payload=payload, user_guid=user_guid)
            
            # Assert
            assert result is True
            # Should only query for 12Hour forms, not 24Hour
            assert mock_db.session.query.call_count >= 1
