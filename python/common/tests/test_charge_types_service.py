import pytest
from unittest.mock import patch, MagicMock, Mock
import requests
from python.common.charge_types_service import get_charge_types


class TestGetChargeTypes:
    """Test the get_charge_types function."""

    @patch('python.common.charge_types_service.requests.get')
    @patch('python.common.charge_types_service.logger')
    def test_get_charge_types_success(self, mock_logger, mock_get):
        """Test successful retrieval of charge types."""
        # Mock the config object
        config = Mock()
        config.ETK_ISSUANCE_SVC_URL = "https://test-api.com"

        # Mock successful API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                'cmnChargeId': 1,
                'cmnStatuteCode': 'TEST001',
                'cmnChargeCode': 'T001',
                'cmnChargeDesc': 'Test Charge 1'
            },
            {
                'cmnChargeId': 2,
                'cmnStatuteCode': 'TEST002',
                'cmnChargeCode': 'T002',
                'cmnChargeDesc': 'Test Charge 2'
            }
        ]
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Call the function
        result = get_charge_types(config)

        # Assertions
        assert len(result) == 2
        assert result[0]['id'] == 1
        assert result[0]['statuteCode'] == 'TEST001'
        assert result[0]['code'] == 'T001'
        assert result[0]['description'] == 'Test Charge 1'
        assert result[1]['id'] == 2
        assert result[1]['statuteCode'] == 'TEST002'
        assert result[1]['code'] == 'T002'
        assert result[1]['description'] == 'Test Charge 2'

        # Verify the API call was made correctly
        mock_get.assert_called_once_with("https://test-api.com/chargetypes")
        mock_logger.debug.assert_any_call("Fetching charge types from https://test-api.com/chargetypes")
        mock_logger.debug.assert_any_call("Response status code: 200")
        mock_logger.debug.assert_any_call("Received charge types count: 2")

    @patch('python.common.charge_types_service.requests.get')
    @patch('python.common.charge_types_service.logger')
    def test_get_charge_types_empty_response(self, mock_logger, mock_get):
        """Test handling of empty response from API."""
        config = Mock()
        config.ETK_ISSUANCE_SVC_URL = "https://test-api.com"

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = []
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = get_charge_types(config)

        assert result == []
        mock_logger.debug.assert_any_call("Received charge types count: 0")

    @patch('python.common.charge_types_service.requests.get')
    @patch('python.common.charge_types_service.logger')
    def test_get_charge_types_http_error_404(self, mock_logger, mock_get):
        """Test handling of 404 HTTP error."""
        config = Mock()
        config.ETK_ISSUANCE_SVC_URL = "https://test-api.com"

        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
        mock_get.return_value = mock_response

        result = get_charge_types(config)

        assert result == []
        mock_logger.error.assert_called_once()
        error_call_args = mock_logger.error.call_args[0][0]
        assert "Error fetching charge types" in error_call_args
        assert "404 Not Found" in error_call_args

    @patch('python.common.charge_types_service.requests.get')
    @patch('python.common.charge_types_service.logger')
    def test_get_charge_types_http_error_500(self, mock_logger, mock_get):
        """Test handling of 500 HTTP error."""
        config = Mock()
        config.ETK_ISSUANCE_SVC_URL = "https://test-api.com"

        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("500 Internal Server Error")
        mock_get.return_value = mock_response

        result = get_charge_types(config)

        assert result == []
        mock_logger.error.assert_called_once()

    @patch('python.common.charge_types_service.requests.get')
    @patch('python.common.charge_types_service.logger')
    def test_get_charge_types_connection_error(self, mock_logger, mock_get):
        """Test handling of connection/network errors."""
        config = Mock()
        config.ETK_ISSUANCE_SVC_URL = "https://test-api.com"

        mock_get.side_effect = requests.exceptions.ConnectionError("Connection refused")

        result = get_charge_types(config)

        assert result == []
        mock_logger.error.assert_called_once()
        error_call_args = mock_logger.error.call_args[0][0]
        assert "Error fetching charge types" in error_call_args
        assert "Connection refused" in error_call_args

    @patch('python.common.charge_types_service.requests.get')
    @patch('python.common.charge_types_service.logger')
    def test_get_charge_types_timeout_error(self, mock_logger, mock_get):
        """Test handling of timeout errors."""
        config = Mock()
        config.ETK_ISSUANCE_SVC_URL = "https://test-api.com"

        mock_get.side_effect = requests.exceptions.Timeout("Request timed out")

        result = get_charge_types(config)

        assert result == []
        mock_logger.error.assert_called_once()
        error_call_args = mock_logger.error.call_args[0][0]
        assert "Error fetching charge types" in error_call_args
        assert "Request timed out" in error_call_args

    @patch('python.common.charge_types_service.requests.get')
    @patch('python.common.charge_types_service.logger')
    def test_get_charge_types_malformed_json(self, mock_logger, mock_get):
        """Test handling of malformed JSON response."""
        config = Mock()
        config.ETK_ISSUANCE_SVC_URL = "https://test-api.com"

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = get_charge_types(config)

        assert result == []
        mock_logger.error.assert_called_once()
        error_call_args = mock_logger.error.call_args[0][0]
        assert "Error fetching charge types" in error_call_args
        assert "Invalid JSON" in error_call_args

    @patch('python.common.charge_types_service.requests.get')
    @patch('python.common.charge_types_service.logger')
    def test_get_charge_types_missing_fields(self, mock_logger, mock_get):
        """Test handling of response with missing required fields."""
        config = Mock()
        config.ETK_ISSUANCE_SVC_URL = "https://test-api.com"

        # Response missing some required fields - this should cause KeyError and return empty list
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                'cmnChargeId': 1,
                # Missing cmnStatuteCode, cmnChargeCode, cmnChargeDesc
            }
        ]
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = get_charge_types(config)

        # Function fails with KeyError and returns empty list
        assert result == []
        mock_logger.error.assert_called_once()
        error_call_args = mock_logger.error.call_args[0][0]
        assert "Error fetching charge types" in error_call_args

    @patch('python.common.charge_types_service.requests.get')
    @patch('python.common.charge_types_service.logger')
    def test_get_charge_types_partial_data(self, mock_logger, mock_get):
        """Test handling of response with partial data."""
        config = Mock()
        config.ETK_ISSUANCE_SVC_URL = "https://test-api.com"

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                'cmnChargeId': 1,
                'cmnStatuteCode': 'TEST001',
                'cmnChargeCode': 'T001',
                'cmnChargeDesc': 'Test Charge 1'
            },
            {
                # Missing all fields - this causes KeyError and function returns empty list
            }
        ]
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = get_charge_types(config)

        # Function fails with KeyError on second item and returns empty list
        assert result == []
        mock_logger.error.assert_called_once()
        error_call_args = mock_logger.error.call_args[0][0]
        assert "Error fetching charge types" in error_call_args

    @patch('python.common.charge_types_service.requests.get')
    @patch('python.common.charge_types_service.logger')
    def test_get_charge_types_config_url_formatting(self, mock_logger, mock_get):
        """Test that the URL is constructed correctly from config."""
        config = Mock()
        config.ETK_ISSUANCE_SVC_URL = "https://api.example.com/v1"

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = []
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        get_charge_types(config)

        # Verify the URL was constructed correctly
        mock_get.assert_called_once_with("https://api.example.com/v1/chargetypes")

    @patch('python.common.charge_types_service.requests.get')
    @patch('python.common.charge_types_service.logger')
    def test_get_charge_types_generic_exception(self, mock_logger, mock_get):
        """Test handling of unexpected exceptions."""
        config = Mock()
        config.ETK_ISSUANCE_SVC_URL = "https://test-api.com"

        mock_get.side_effect = Exception("Unexpected error")

        result = get_charge_types(config)

        assert result == []
        mock_logger.error.assert_called_once()
        error_call_args = mock_logger.error.call_args[0][0]
        assert "Error fetching charge types" in error_call_args
        assert "Unexpected error" in error_call_args
