import pytest
from unittest.mock import MagicMock, patch
from python.prohibition_web_svc.middleware import common_middleware

class DummyRequest:
    def __init__(self, json_data=None, data=None):
        self._json = json_data
        self._data = data
    def get_json(self):
        if isinstance(self._json, Exception):
            raise self._json
        return self._json
    def get_data(self):
        return self._data

def test_log_payload_to_splunk_logs_and_returns_true():
    req = DummyRequest(data=b'{"foo": "bar"}')
    result, kwargs = common_middleware.log_payload_to_splunk(request=req)
    assert result is True
    assert kwargs['request'] == req

def test_request_contains_a_payload_success():
    req = DummyRequest(json_data={"foo": "bar"})
    result, kwargs = common_middleware.request_contains_a_payload(request=req)
    assert result is True
    assert kwargs['payload'] == {"foo": "bar"}

def test_request_contains_a_payload_failure():
    req = DummyRequest(json_data=Exception("bad json"))
    result, kwargs = common_middleware.request_contains_a_payload(request=req)
    assert result is False

def test_check_if_application_id_exists_found(monkeypatch):
    mock_db = MagicMock()
    mock_submission = MagicMock(submission_id=123)
    mock_db.session.query().filter().first.return_value = mock_submission
    monkeypatch.setattr(common_middleware, 'db', mock_db)
    kwargs = {'payload': {'ff_application_id': 'abc'}, 'event_type': 'foo', 'ticket_no': 'bar'}
    result, out_kwargs = common_middleware.check_if_application_id_exists(**kwargs)
    assert result is False
    assert out_kwargs['error']['error_code']

def test_check_if_application_id_exists_not_found(monkeypatch):
    mock_db = MagicMock()
    mock_db.session.query().filter().first.return_value = None
    monkeypatch.setattr(common_middleware, 'db', mock_db)
    kwargs = {'payload': {'ff_application_id': 'abc'}}
    result, out_kwargs = common_middleware.check_if_application_id_exists(**kwargs)

    assert result is True

def test_check_if_application_id_exists_exception(monkeypatch):
    mock_db = MagicMock()
    mock_db.session.query.side_effect = Exception("db error")
    monkeypatch.setattr(common_middleware, 'db', mock_db)
    kwargs = {'payload': {'ff_application_id': 'abc'}}
    result, out_kwargs = common_middleware.check_if_application_id_exists(**kwargs)
    assert result is False
    assert 'error' in out_kwargs
    assert 'error_code' in out_kwargs['error']

def test_safe_get_value_dict():
    assert common_middleware.safe_get_value({'value': 42}) == 42

def test_safe_get_value_empty_string():
    assert common_middleware.safe_get_value("") is None

def test_safe_get_value_none():
    assert common_middleware.safe_get_value(None, default=5) == 5

def test_safe_get_value_other():
    assert common_middleware.safe_get_value(7) == 7

def test_get_user_guid_service_account():
    kwargs = {'payload': {'submitted_user_guid': 'abc'}, 'identity_provider': 'service_account', 'username': 'user'}
    assert common_middleware.get_user_guid(**kwargs) == 'abc'

def test_get_user_guid_other():
    kwargs = {'payload': {}, 'user_guid': 'xyz'}
    assert common_middleware.get_user_guid(**kwargs) == 'xyz'

def test_record_event_error_calls_record_error(monkeypatch):
    called = {}
    def fake_record_error(**kwargs):
        called['called'] = True
    monkeypatch.setattr(common_middleware, 'record_error', fake_record_error)
    kwargs = {'error': {'foo': 'bar'}}
    result, out_kwargs = common_middleware.record_event_error(**kwargs)
    assert called['called']
    assert result is True
    assert out_kwargs == kwargs

def test_record_event_error_handles_exception(monkeypatch):
    def fake_record_error(**kwargs):
        raise Exception('fail')
    monkeypatch.setattr(common_middleware, 'record_error', fake_record_error)
    kwargs = {'error': {'foo': 'bar'}}
    result, out_kwargs = common_middleware.record_event_error(**kwargs)
    assert result is True
    assert out_kwargs == kwargs
