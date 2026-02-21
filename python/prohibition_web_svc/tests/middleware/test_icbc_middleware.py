import time
from unittest.mock import MagicMock, patch

import pytest
from flask import Flask

from python.prohibition_web_svc.middleware import icbc_middleware


@pytest.fixture
def app():
	app = Flask(__name__)
	app.config["TESTING"] = True
	return app


@pytest.fixture(autouse=True)
def reset_token_caches():
	icbc_middleware._drivers_token_cache["access_token"] = None
	icbc_middleware._drivers_token_cache["expires_at"] = 0
	icbc_middleware._vehicles_token_cache["access_token"] = None
	icbc_middleware._vehicles_token_cache["expires_at"] = 0


class TestOAuthTokenCaching:
	def test_get_drivers_oauth_token_returns_cached(self):
		cached_token = "cached-token"
		icbc_middleware._drivers_token_cache["access_token"] = cached_token
		icbc_middleware._drivers_token_cache["expires_at"] = time.time() + 120

		with patch("python.prohibition_web_svc.middleware.icbc_middleware.get_oauth_token") as mock_get_token:
			token = icbc_middleware._get_drivers_oauth_token()

		assert token == cached_token
		mock_get_token.assert_not_called()

	def test_get_drivers_oauth_token_fetches_new(self):
		icbc_middleware._drivers_token_cache["access_token"] = "stale"
		icbc_middleware._drivers_token_cache["expires_at"] = 0

		with patch("python.prohibition_web_svc.middleware.icbc_middleware.time.time", return_value=1000), \
			patch("python.prohibition_web_svc.middleware.icbc_middleware.get_oauth_token") as mock_get_token:
			mock_get_token.return_value = {"access_token": "new-token", "expires_in": 120}

			token = icbc_middleware._get_drivers_oauth_token()

		assert token == "new-token"
		assert icbc_middleware._drivers_token_cache["expires_at"] == 1120

	def test_get_vehicles_oauth_token_fetches_new(self):
		icbc_middleware._vehicles_token_cache["access_token"] = "stale"
		icbc_middleware._vehicles_token_cache["expires_at"] = 0

		with patch("python.prohibition_web_svc.middleware.icbc_middleware.time.time", return_value=2000), \
			patch("python.prohibition_web_svc.middleware.icbc_middleware.get_oauth_token") as mock_get_token:
			mock_get_token.return_value = {"access_token": "vehicle-token", "expires_in": 300}

			token = icbc_middleware._get_vehicles_oauth_token()

		assert token == "vehicle-token"
		assert icbc_middleware._vehicles_token_cache["expires_at"] == 2300


class TestAuthorizationHeaders:
	def test_get_icbc_drivers_api_authorization_header_success(self):
		with patch("python.prohibition_web_svc.middleware.icbc_middleware._get_drivers_oauth_token", return_value="token"):
			result, kwargs = icbc_middleware.get_icbc_drivers_api_authorization_header(username="user1")

		assert result is True
		assert kwargs["icbc_header"]["Authorization"] == "Bearer token"
		assert kwargs["icbc_header"]["loginUserId"] == "user1"
		assert kwargs["icbc_header"]["Accept"] == "*/*"

	def test_get_icbc_drivers_api_authorization_header_failure(self):
		with patch("python.prohibition_web_svc.middleware.icbc_middleware._get_drivers_oauth_token", side_effect=Exception("fail")):
			result, kwargs = icbc_middleware.get_icbc_drivers_api_authorization_header(username="user1")

		assert result is False
		assert "icbc_header" not in kwargs

	def test_get_icbc_vehicles_api_authorization_header_success(self):
		with patch("python.prohibition_web_svc.middleware.icbc_middleware._get_vehicles_oauth_token", return_value="token"):
			result, kwargs = icbc_middleware.get_icbc_vehicles_api_authorization_header(username="user2")

		assert result is True
		assert kwargs["icbc_header"]["Authorization"] == "Bearer token"
		assert kwargs["icbc_header"]["loginUserId"] == "user2"


class TestIcbcApiCalls:
	def test_get_icbc_driver_success(self, app):
		mock_response = MagicMock()
		mock_response.status_code = 200
		mock_response.json.return_value = {"ok": True}

		with app.app_context(), \
			patch("python.prohibition_web_svc.middleware.icbc_middleware.requests.get", return_value=mock_response), \
			patch("python.prohibition_web_svc.middleware.icbc_middleware.Config.ICBC_API_ROOT", "https://example"):
			result, kwargs = icbc_middleware.get_icbc_driver(icbc_header={"Authorization": "Bearer t"}, dl_number="123")

		assert result is True
		assert kwargs["response"].status_code == 200
		assert kwargs["response"].get_json() == {"ok": True}

	def test_get_icbc_driver_maps_400_to_200(self, app):
		mock_response = MagicMock()
		mock_response.status_code = 400
		mock_response.json.return_value = {"error": "bad"}

		with app.app_context(), \
			patch("python.prohibition_web_svc.middleware.icbc_middleware.requests.get", return_value=mock_response), \
			patch("python.prohibition_web_svc.middleware.icbc_middleware.Config.ICBC_API_ROOT", "https://example"):
			result, kwargs = icbc_middleware.get_icbc_driver(icbc_header={"Authorization": "Bearer t"}, dl_number="123")

		assert result is True
		assert kwargs["response"].status_code == 200
		assert kwargs["response"].get_json() == {}

	def test_get_icbc_driver_exception(self):
		with patch("python.prohibition_web_svc.middleware.icbc_middleware.requests.get", side_effect=Exception("boom")), \
			patch("python.prohibition_web_svc.middleware.icbc_middleware.Config.ICBC_API_ROOT", "https://example"):
			result, kwargs = icbc_middleware.get_icbc_driver(icbc_header={"Authorization": "Bearer t"}, dl_number="123")

		assert result is False
		assert kwargs["icbc_header"]["Authorization"] == "Bearer t"

	def test_get_icbc_vehicle_success(self, app):
		mock_response = MagicMock()
		mock_response.status_code = 200
		mock_response.json.return_value = {"vehicle": "ok"}

		with app.app_context(), \
			patch("python.prohibition_web_svc.middleware.icbc_middleware.requests.get", return_value=mock_response) as mock_get, \
			patch("python.prohibition_web_svc.middleware.icbc_middleware.Config.ICBC_API_ROOT", "https://example"):
			result, kwargs = icbc_middleware.get_icbc_vehicle(icbc_header={"Authorization": "Bearer t"}, plate_number="ABC123")

		assert result is True
		assert kwargs["response"].status_code == 200
		assert kwargs["response"].get_json() == {"vehicle": "ok"}
		mock_get.assert_called_once()
		assert mock_get.call_args.kwargs["params"] == {"plateNumber": "ABC123"}

	def test_get_icbc_vehicle_exception(self):
		with patch("python.prohibition_web_svc.middleware.icbc_middleware.requests.get", side_effect=Exception("boom")), \
			patch("python.prohibition_web_svc.middleware.icbc_middleware.Config.ICBC_API_ROOT", "https://example"):
			result, kwargs = icbc_middleware.get_icbc_vehicle(icbc_header={"Authorization": "Bearer t"}, plate_number="ABC123")

		assert result is False


class TestSplunkPayloads:
	def test_splunk_get_driver(self):
		result, kwargs = icbc_middleware.splunk_get_driver(
			username="user",
			user_guid="guid",
			request_id="req",
			dl_number="D123"
		)

		assert result is True
		assert kwargs["splunk_data"]["event"] == "icbc_get_driver"
		assert kwargs["splunk_data"]["queried_bcdl"] == "D123"

	def test_splunk_get_vehicle(self):
		result, kwargs = icbc_middleware.splunk_get_vehicle(
			username="user",
			user_guid="guid",
			request_id="req",
			plate_number="ABC123"
		)

		assert result is True
		assert kwargs["splunk_data"]["event"] == "icbc_get_vehicle"
		assert kwargs["splunk_data"]["queried_plate"] == "ABC123"
