import logging
import pytest
from flask import Flask, make_response, jsonify
from unittest.mock import MagicMock, patch

# Mock flask_caching before importing the blueprint
with patch.dict('sys.modules', {'flask_caching': MagicMock()}):
    from python.prohibition_web_svc.blueprints import static as static_blueprint


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.register_blueprint(static_blueprint.bp)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_get_static_resource_success(client, monkeypatch):
    """Test successful GET /static/<resource> request"""
    # Patch middle_logic to simulate a successful flow
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response(jsonify({"message": "success"}), 200)}
    monkeypatch.setattr(static_blueprint, 'middle_logic', fake_middle_logic)

    response = client.get('/api/v1/static/agencies')
    logging.debug(response)
    assert response.status_code == 200
    assert b'success' in response.data


def test_get_static_resource_bad_request(client, monkeypatch):
    """Test GET /static/<resource> with bad request"""
    # Patch middle_logic to simulate a bad request
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response(jsonify({"error": "bad request"}), 400)}
    monkeypatch.setattr(static_blueprint, 'middle_logic', fake_middle_logic)

    response = client.get('/api/v1/static/invalid_resource')
    assert response.status_code == 400
    assert b'bad request' in response.data


def test_get_static_resource_server_error(client, monkeypatch):
    """Test GET /static/<resource> with server error"""
    # Patch middle_logic to simulate a server error
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response(jsonify({"error": "server error"}), 500)}
    monkeypatch.setattr(static_blueprint, 'middle_logic', fake_middle_logic)

    response = client.get('/api/v1/static/agencies')
    assert response.status_code == 500
    assert b'server error' in response.data


def test_get_static_resource_keycloak(client, monkeypatch):
    """Test GET /static/keycloak returns keycloak config"""
    # Patch middle_logic to simulate keycloak config retrieval
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response(jsonify({"realm": "test", "url": "test", "clientId": "test"}), 200)}
    monkeypatch.setattr(static_blueprint, 'middle_logic', fake_middle_logic)

    response = client.get('/api/v1/static/keycloak')
    assert response.status_code == 200
    data = response.get_json()
    assert 'realm' in data
    assert 'url' in data
    assert 'clientId' in data


def test_get_static_resource_configuration(client, monkeypatch):
    """Test GET /static/configuration returns config"""
    # Patch middle_logic to simulate configuration retrieval
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response(jsonify({"environment": "test"}), 200)}
    monkeypatch.setattr(static_blueprint, 'middle_logic', fake_middle_logic)

    response = client.get('/api/v1/static/configuration')
    assert response.status_code == 200
    data = response.get_json()
    assert 'environment' in data


def test_get_static_resource_with_cache_hit(client, monkeypatch):
    """Test GET /static/<resource> with cache hit"""
    # Mock cache to return cached data
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response(jsonify({"cached": True}), 200)}
    monkeypatch.setattr(static_blueprint, 'middle_logic', fake_middle_logic)

    # Mock cache.get to return cached data
    monkeypatch.setattr(static_blueprint.cache, 'get', lambda key: {"cached": True})

    response = client.get('/api/v1/static/agencies')
    assert response.status_code == 200
    data = response.get_json()
    assert data.get('cached') is True


def test_get_static_resource_with_cache_miss(client, monkeypatch):
    """Test GET /static/<resource> with cache miss"""
    # Mock cache to return None (cache miss)
    monkeypatch.setattr(static_blueprint.cache, 'get', lambda key: None)

    # Patch middle_logic to simulate successful database retrieval
    def fake_middle_logic(*args, **kwargs):
        return {'response': make_response(jsonify({"from_db": True}), 200)}
    monkeypatch.setattr(static_blueprint, 'middle_logic', fake_middle_logic)

    response = client.get('/api/v1/static/agencies')
    assert response.status_code == 200
    data = response.get_json()
    assert data.get('from_db') is True


def test_get_static_resource_not_implemented(client):
    """Test GET /static/<resource>/<static_id> returns method not implemented"""
    response = client.get('/api/v1/static/agencies/1')
    assert response.status_code == 405
    assert b'method not implemented' in response.data


def test_create_static_resource_not_implemented(client):
    """Test POST /static/<resource> returns method not implemented"""
    response = client.post('/api/v1/static/agencies', json={"test": "data"})
    assert response.status_code == 405
    assert b'method not implemented' in response.data


def test_update_static_resource_not_implemented(client):
    """Test PATCH /static/<resource>/<static_id> returns method not implemented"""
    response = client.patch('/api/v1/static/agencies/1', json={"test": "data"})
    assert response.status_code == 405
    assert b'method not implemented' in response.data


def test_ping(client, app, monkeypatch):
    """Test GET /ping endpoint returns cached cities data"""
    # Mock _get_resource_cached to return a successful response
    with app.app_context():
        mock_response = make_response(jsonify([{"id": 1, "name": "Vancouver"}]), 200)
    
    def mock_get_resource_cached(**kwargs):
        assert kwargs.get('resource') == 'cities'
        return True, {'response': mock_response}
    
    monkeypatch.setattr(static_blueprint, '_get_resource_cached', mock_get_resource_cached)
    
    response = client.get('/api/v1/ping')
    
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]['name'] == 'Vancouver'


def test_helper_functions():
    """Test helper functions directly"""
    # Test _is_known_resource
    result, kwargs = static_blueprint._is_known_resource(resource='agencies')
    assert result is True

    result, kwargs = static_blueprint._is_known_resource(resource='unknown')
    assert result is False

    # Test _is_not_keycloak
    result, kwargs = static_blueprint._is_not_keycloak(resource='agencies')
    assert result is True

    result, kwargs = static_blueprint._is_not_keycloak(resource='keycloak')
    assert result is False

    # Test _is_not_configuration
    result, kwargs = static_blueprint._is_not_configuration(resource='agencies')
    assert result is True

    result, kwargs = static_blueprint._is_not_configuration(resource='configuration')
    assert result is False


def test_resource_map():
    """Test that resource_map contains expected resources"""
    expected_resources = [
        'tar_police_agencies', 'agencies', 'cities', 'countries',
        'impound_lot_operators', 'jurisdictions', 'permissions',
        'provinces', 'vehicle_styles', 'vehicle_types', 'vehicle_colours',
        'vehicles', 'nsc_puj', 'jurisdiction_country', 'lki_highway',
        'lki_segment'
    ]

    for resource in expected_resources:
        assert resource in static_blueprint.resource_map


class TestGetResourceCached:
	"""Test the _get_resource_cached function directly"""

	def test_get_resource_cached_hit(self, monkeypatch):
		"""Test _get_resource_cached when data is in cache"""
		cached_data = {"test": "cached_data"}
		mock_cache = MagicMock()
		mock_cache.get.return_value = cached_data
		monkeypatch.setattr(static_blueprint, 'cache', mock_cache)

		mock_response = MagicMock()
		mock_make_response = MagicMock(return_value=mock_response)
		monkeypatch.setattr(static_blueprint, 'make_response', mock_make_response)

		result, kwargs = static_blueprint._get_resource_cached(resource="agencies")

		assert result is True
		assert kwargs['response'] == mock_response
		mock_cache.get.assert_called_once_with('static_resource::agencies')
		mock_make_response.assert_called_once_with(cached_data, 200)
		mock_cache.set.assert_not_called()

	def test_get_resource_cached_miss_success(self, monkeypatch):
		"""Test _get_resource_cached when data is not in cache and _get_resource succeeds"""
		mock_cache = MagicMock()
		mock_cache.get.return_value = None
		monkeypatch.setattr(static_blueprint, 'cache', mock_cache)

		fresh_response = MagicMock()
		fresh_response.get_json.return_value = {"test": "fresh_data"}
		mock_get_resource = MagicMock(return_value=(True, {'response': fresh_response}))
		monkeypatch.setattr(static_blueprint, '_get_resource', mock_get_resource)

		mock_make_response = MagicMock()
		monkeypatch.setattr(static_blueprint, 'make_response', mock_make_response)

		result, kwargs = static_blueprint._get_resource_cached(resource="agencies")

		assert result is True
		assert kwargs == {'response': fresh_response}
		mock_cache.get.assert_called_once_with('static_resource::agencies')
		mock_get_resource.assert_called_once_with(resource="agencies")
		mock_cache.set.assert_called_once_with('static_resource::agencies', {"test": "fresh_data"})
		mock_make_response.assert_not_called()

	def test_get_resource_cached_miss_failure(self, monkeypatch):
		"""Test _get_resource_cached when data is not in cache and _get_resource fails"""
		mock_cache = MagicMock()
		mock_cache.get.return_value = None
		monkeypatch.setattr(static_blueprint, 'cache', mock_cache)

		mock_get_resource = MagicMock(return_value=(False, {'error': 'failed'}))
		monkeypatch.setattr(static_blueprint, '_get_resource', mock_get_resource)

		result, kwargs = static_blueprint._get_resource_cached(resource="agencies")

		assert result is False
		assert kwargs == {'error': 'failed'}
		mock_cache.get.assert_called_once_with('static_resource::agencies')
		mock_get_resource.assert_called_once_with(resource="agencies")
		mock_cache.set.assert_not_called()

	def test_get_resource_cached_exception_handling(self, monkeypatch):
		"""Test _get_resource_cached handles exceptions properly"""
		mock_cache = MagicMock()
		mock_cache.get.return_value = None
		monkeypatch.setattr(static_blueprint, 'cache', mock_cache)

		mock_get_resource = MagicMock(side_effect=Exception("Test exception"))
		monkeypatch.setattr(static_blueprint, '_get_resource', mock_get_resource)

		mock_logger = MagicMock()
		monkeypatch.setattr(static_blueprint, 'logger', mock_logger)

		result, kwargs = static_blueprint._get_resource_cached(resource="agencies")

		assert result is False
		assert 'resource' in kwargs
		mock_cache.get.assert_called_once_with('static_resource::agencies')
		mock_get_resource.assert_called_once_with(resource="agencies")
		mock_logger.warning.assert_called_once()
		warning_call_args = mock_logger.warning.call_args[0][0]
		assert "error getting cached agencies data" in warning_call_args
		assert "Test exception" in warning_call_args
		mock_cache.set.assert_not_called()

	def test_get_resource_cached_cache_key_format(self, monkeypatch):
		"""Test _get_resource_cached uses correct cache key format"""
		cached_data = {"test": "data"}
		mock_cache = MagicMock()
		mock_cache.get.return_value = cached_data
		monkeypatch.setattr(static_blueprint, 'cache', mock_cache)

		mock_response = MagicMock()
		mock_make_response = MagicMock(return_value=mock_response)
		monkeypatch.setattr(static_blueprint, 'make_response', mock_make_response)

		for resource in ["agencies", "cities", "vehicle_types"]:
			mock_cache.get.reset_mock()
			mock_make_response.reset_mock()
			static_blueprint._get_resource_cached(resource=resource)

			expected_key = f'static_resource::{resource}'
			mock_cache.get.assert_called_once_with(expected_key)

	def test_get_resource_cached_preserves_kwargs(self, monkeypatch):
		"""Test _get_resource_cached preserves additional kwargs on cache hit"""
		cached_data = {"test": "cached_data"}
		mock_cache = MagicMock()
		mock_cache.get.return_value = cached_data
		monkeypatch.setattr(static_blueprint, 'cache', mock_cache)

		mock_response = MagicMock()
		mock_make_response = MagicMock(return_value=mock_response)
		monkeypatch.setattr(static_blueprint, 'make_response', mock_make_response)

		mock_get_resource = MagicMock()
		monkeypatch.setattr(static_blueprint, '_get_resource', mock_get_resource)

		result, kwargs = static_blueprint._get_resource_cached(resource="agencies", extra_param="test")

		assert result is True
		assert kwargs['response'] == mock_response
		assert kwargs['resource'] == "agencies"
		assert kwargs['extra_param'] == "test"
		mock_get_resource.assert_not_called()


class TestGetResource:
	"""Test the _get_resource function directly"""

	def test_get_resource_dataclass_success(self, monkeypatch):
		"""Test _get_resource with dataclass resource (database model)"""
		mock_query = MagicMock()
		mock_query.all.return_value = [{'id': 1, 'name': 'Test Agency'}]
		mock_db = MagicMock()
		mock_db.session.query.return_value = mock_query
		monkeypatch.setattr(static_blueprint, 'db', mock_db)

		mock_jsonified_data = MagicMock()
		mock_jsonify = MagicMock(return_value=mock_jsonified_data)
		monkeypatch.setattr(static_blueprint, 'jsonify', mock_jsonify)

		mock_response = MagicMock()
		mock_make_response = MagicMock(return_value=mock_response)
		monkeypatch.setattr(static_blueprint, 'make_response', mock_make_response)

		mock_logger = MagicMock()
		monkeypatch.setattr(static_blueprint, 'logger', mock_logger)

		result, kwargs = static_blueprint._get_resource(resource="agencies", request_id="test-123")

		assert result is True
		assert kwargs['response'] == mock_response
		assert kwargs['resource'] == "agencies"
		assert kwargs['request_id'] == "test-123"
		mock_db.session.query.assert_called_once_with(static_blueprint.resource_map["agencies"])
		mock_query.all.assert_called_once()
		mock_jsonify.assert_called_once_with([{'id': 1, 'name': 'Test Agency'}])
		mock_make_response.assert_called_once_with(mock_jsonified_data, 200)
		mock_logger.verbose.assert_called_once_with("test-123 inside _get_resource() for resource: agencies")

	def test_get_resource_function_success(self, monkeypatch):
		"""Test _get_resource with function resource"""
		mock_function_result = [{'id': 1, 'code': 'TEST', 'description': 'Test Charge'}]
		mock_function = MagicMock(return_value=mock_function_result)
		static_blueprint.resource_map["test"] = lambda: mock_function()

		mock_jsonified_data = MagicMock()
		mock_jsonify = MagicMock(return_value=mock_jsonified_data)
		monkeypatch.setattr(static_blueprint, 'jsonify', mock_jsonify)

		mock_response = MagicMock()
		mock_make_response = MagicMock(return_value=mock_response)
		monkeypatch.setattr(static_blueprint, 'make_response', mock_make_response)

		mock_logger = MagicMock()
		monkeypatch.setattr(static_blueprint, 'logger', mock_logger)

		result, kwargs = static_blueprint._get_resource(resource="test", request_id="test-456")

		assert result is True
		assert kwargs['response'] == mock_response
		assert kwargs['resource'] == "test"
		assert kwargs['request_id'] == "test-456"
		mock_jsonify.assert_called_once_with(mock_function_result)
		mock_make_response.assert_called_once_with(mock_jsonified_data, 200)
		mock_logger.verbose.assert_called_once_with("test-456 inside _get_resource() for resource: test")

	def test_get_resource_dataclass_exception(self, monkeypatch):
		"""Test _get_resource handles database exceptions properly"""
		mock_db = MagicMock()
		mock_db.session.query.side_effect = Exception("Database connection failed")
		monkeypatch.setattr(static_blueprint, 'db', mock_db)

		mock_logger = MagicMock()
		monkeypatch.setattr(static_blueprint, 'logger', mock_logger)

		result, kwargs = static_blueprint._get_resource(resource="agencies", request_id="test-789")

		assert result is False
		assert kwargs['resource'] == "agencies"
		assert kwargs['request_id'] == "test-789"
		assert 'response' not in kwargs
		mock_logger.verbose.assert_called_once_with("test-789 inside _get_resource() for resource: agencies")
		mock_logger.warning.assert_called_once()
		warning_call_args = mock_logger.warning.call_args[0][0]
		assert "test-789 error getting agencies data" in warning_call_args
		assert "Database connection failed" in warning_call_args

	def test_get_resource_function_exception(self, monkeypatch):
		"""Test _get_resource handles function call exceptions properly"""
		mock_function = MagicMock(side_effect=Exception("API call failed"))
		static_blueprint.resource_map["tests"] = lambda: mock_function()

		mock_logger = MagicMock()
		monkeypatch.setattr(static_blueprint, 'logger', mock_logger)

		result, kwargs = static_blueprint._get_resource(resource="tests", request_id="test-999")

		assert result is False
		assert kwargs['resource'] == "tests"
		assert kwargs['request_id'] == "test-999"
		assert 'response' not in kwargs
		mock_logger.verbose.assert_called_once_with("test-999 inside _get_resource() for resource: tests")
		mock_logger.warning.assert_called_once()
		warning_call_args = mock_logger.warning.call_args[0][0]
		assert "test-999 error getting tests data" in warning_call_args
		assert "API call failed" in warning_call_args

	def test_get_resource_preserves_kwargs(self, monkeypatch):
		"""Test _get_resource preserves additional kwargs"""
		mock_query = MagicMock()
		mock_query.all.return_value = [{'id': 1}]
		mock_db = MagicMock()
		mock_db.session.query.return_value = mock_query
		monkeypatch.setattr(static_blueprint, 'db', mock_db)

		mock_jsonified_data = MagicMock()
		mock_jsonify = MagicMock(return_value=mock_jsonified_data)
		monkeypatch.setattr(static_blueprint, 'jsonify', mock_jsonify)

		mock_response = MagicMock()
		mock_make_response = MagicMock(return_value=mock_response)
		monkeypatch.setattr(static_blueprint, 'make_response', mock_make_response)

		mock_logger = MagicMock()
		monkeypatch.setattr(static_blueprint, 'logger', mock_logger)

		result, kwargs = static_blueprint._get_resource(
			resource="agencies",
			request_id="test-123",
			extra_param="test_value",
			another_param=42
		)

		assert result is True
		assert kwargs['response'] == mock_response
		assert kwargs['resource'] == "agencies"
		assert kwargs['request_id'] == "test-123"
		assert kwargs['extra_param'] == "test_value"
		assert kwargs['another_param'] == 42

	def test_get_resource_empty_database_result(self, monkeypatch):
		"""Test _get_resource handles empty database results"""
		mock_query = MagicMock()
		mock_query.all.return_value = []
		mock_db = MagicMock()
		mock_db.session.query.return_value = mock_query
		monkeypatch.setattr(static_blueprint, 'db', mock_db)

		mock_jsonified_data = MagicMock()
		mock_jsonify = MagicMock(return_value=mock_jsonified_data)
		monkeypatch.setattr(static_blueprint, 'jsonify', mock_jsonify)

		mock_response = MagicMock()
		mock_make_response = MagicMock(return_value=mock_response)
		monkeypatch.setattr(static_blueprint, 'make_response', mock_make_response)

		mock_logger = MagicMock()
		monkeypatch.setattr(static_blueprint, 'logger', mock_logger)

		result, kwargs = static_blueprint._get_resource(resource="agencies", request_id="test-123")

		assert result is True
		assert kwargs['response'] == mock_response
		mock_jsonify.assert_called_once_with([])
		mock_make_response.assert_called_once_with(mock_jsonified_data, 200)

