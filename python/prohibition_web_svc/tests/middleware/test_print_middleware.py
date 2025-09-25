import pytest
import json
from unittest.mock import patch, MagicMock
from python.prohibition_web_svc.middleware import print_middleware


class TestPrintMiddleware:
    """Test cases for print middleware functions."""

    def test_log_payload_to_splunk_success(self):
        """Test successful logging of payload to splunk data structure."""
        # Mock request with JSON payload
        mock_request = MagicMock()
        mock_request.get_json.return_value = {
            "template": "test.html",
            "data": {"name": "John Doe", "ssn": "123-45-6789"},
            "options": {"type": "pdf"}
        }
        
        # Mock masked data
        masked_payload = {
            "template": "test.html", 
            "data": {"name": "John Doe", "ssn": "***-**-****"},
            "options": {"type": "pdf"}
        }
        
        with patch('python.prohibition_web_svc.middleware.collision_middleware.mask_sensitive_data') as mock_mask:
            mock_mask.return_value = masked_payload
            
            kwargs = {
                'request': mock_request,
                'request_id': 'test-request-123',
                'user_guid': 'user-guid-456',
                'username': 'testuser'
            }
            
            result, updated_kwargs = print_middleware.log_payload_to_splunk(**kwargs)
            
            assert result is True
            assert 'splunk_data' in updated_kwargs
            assert updated_kwargs['splunk_data']['event'] == 'print request received'
            assert updated_kwargs['splunk_data']['request_id'] == 'test-request-123'
            assert updated_kwargs['splunk_data']['user_guid'] == 'user-guid-456'
            assert updated_kwargs['splunk_data']['username'] == 'testuser'
            assert updated_kwargs['splunk_data']['payload'] == masked_payload
            
            # Verify mask_sensitive_data was called with the original payload
            mock_mask.assert_called_once()
            called_payload = mock_mask.call_args[0][0]
            assert called_payload['data']['ssn'] == '123-45-6789'

    def test_log_payload_to_splunk_request_exception(self):
        """Test exception handling when request.get_json() fails."""
        # Mock request that raises exception
        mock_request = MagicMock()
        mock_request.get_json.side_effect = Exception("Invalid JSON")
        
        kwargs = {
            'request': mock_request,
            'request_id': 'test-request-123'
        }
        
        with patch('python.prohibition_web_svc.middleware.print_middleware.logger') as mock_logger:
            result, updated_kwargs = print_middleware.log_payload_to_splunk(**kwargs)
            
            assert result is True
            assert 'splunk_data' not in updated_kwargs
            
            # Verify error was logged
            mock_logger.error.assert_called_once()

    def test_log_payload_to_splunk_mask_exception(self):
        """Test exception handling when mask_sensitive_data fails."""
        # Mock request with valid payload
        mock_request = MagicMock()
        mock_request.get_json.return_value = {"template": "test.html", "data": {"name": "John"}}
        
        kwargs = {
            'request': mock_request,
            'request_id': 'test-request-123'
        }
        
        with patch('python.prohibition_web_svc.middleware.collision_middleware.mask_sensitive_data') as mock_mask:
            mock_mask.side_effect = Exception("Masking failed")
            
            with patch('python.prohibition_web_svc.middleware.print_middleware.logger') as mock_logger:
                result, updated_kwargs = print_middleware.log_payload_to_splunk(**kwargs)
                
                assert result is True
                assert 'splunk_data' not in updated_kwargs
                
                # Verify error was logged
                mock_logger.error.assert_called_once()

    def test_log_payload_to_splunk_missing_request(self):
        """Test handling when request is missing from kwargs."""
        kwargs = {
            'request_id': 'test-request-123'
        }
        
        with patch('python.prohibition_web_svc.middleware.print_middleware.logger') as mock_logger:
            result, updated_kwargs = print_middleware.log_payload_to_splunk(**kwargs)
            
            assert result is True
            assert 'splunk_data' not in updated_kwargs
            
            # Verify error was logged
            mock_logger.error.assert_called_once()

    def test_log_payload_to_splunk_empty_kwargs(self):
        """Test handling with completely empty kwargs."""
        kwargs = {}
        
        with patch('python.prohibition_web_svc.middleware.print_middleware.logger') as mock_logger:
            result, updated_kwargs = print_middleware.log_payload_to_splunk(**kwargs)
            
            assert result is True
            assert 'splunk_data' not in updated_kwargs
            
            # Verify error was logged
            mock_logger.error.assert_called_once()

    def test_log_payload_to_splunk_deep_copy(self):
        """Test that payload is deep copied to avoid modifying original."""
        original_payload = {
            "template": "test.html",
            "data": {"name": "John", "nested": {"value": 123}},
            "options": {"type": "pdf"}
        }
        
        mock_request = MagicMock()
        mock_request.get_json.return_value = original_payload
        
        # Mock mask function to modify the payload
        def mock_mask_func(payload):
            # Modify the payload to ensure it's a copy
            payload['data']['nested']['value'] = 999
            return payload
        
        with patch('python.prohibition_web_svc.middleware.collision_middleware.mask_sensitive_data', side_effect=mock_mask_func):
            kwargs = {'request': mock_request}
            
            result, updated_kwargs = print_middleware.log_payload_to_splunk(**kwargs)
            
            # Original payload should be unchanged
            assert original_payload['data']['nested']['value'] == 123
            
            # But the splunk_data should have the modified value
            assert updated_kwargs['splunk_data']['payload']['data']['nested']['value'] == 999

    def test_log_payload_to_splunk_default_values(self):
        """Test that missing optional fields get default empty string values."""
        mock_request = MagicMock()
        mock_request.get_json.return_value = {"template": "test.html", "data": {"name": "John"}}
        
        with patch('python.prohibition_web_svc.middleware.collision_middleware.mask_sensitive_data') as mock_mask:
            mock_mask.return_value = {"template": "test.html", "data": {"name": "John"}}
            
            # Test with missing optional fields
            kwargs = {'request': mock_request}
            
            result, updated_kwargs = print_middleware.log_payload_to_splunk(**kwargs)
            
            assert result is True
            splunk_data = updated_kwargs['splunk_data']
            assert splunk_data['request_id'] == ''
            assert splunk_data['user_guid'] == ''
            assert splunk_data['username'] == ''