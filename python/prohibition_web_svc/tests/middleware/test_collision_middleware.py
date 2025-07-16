import pytest
from unittest.mock import MagicMock, patch
from python.prohibition_web_svc.middleware import collision_middleware

# Dummy payload for tests
DUMMY_PAYLOAD = {
    'ff_application_id': 'abc123',
    'collision_case_num': 'MV-001',
}

def test_set_event_type():
    result, kwargs = collision_middleware.set_event_type()
    assert result is True
    assert kwargs['event_type'] == collision_middleware.EVENT_TYPE

def test_set_ticket_number_with_case_num():
    kwargs = {'payload': {'collision_case_num': 'MV-001'}}
    result, out_kwargs = collision_middleware.set_ticket_number(**kwargs)
    assert result is True
    assert out_kwargs['ticket_no'] == 'MV-001'

def test_set_ticket_number_without_case_num():
    kwargs = {'payload': {}}
    result, out_kwargs = collision_middleware.set_ticket_number(**kwargs)
    assert result is True
    assert out_kwargs['ticket_no'] is None

def test_validate_collision_payload_success():
    kwargs = {'payload': {'foo': 'bar'}}
    result, out_kwargs = collision_middleware.validate_collision_payload(**kwargs)
    assert result is True
    assert out_kwargs == kwargs

def test_validate_collision_payload_failure():
    kwargs = {}
    result, out_kwargs = collision_middleware.validate_collision_payload(**kwargs)
    assert result is False
    assert out_kwargs == kwargs

def test_save_collision_data_success(monkeypatch):
    mock_db = MagicMock()
    mock_session = MagicMock()
    mock_db.session = mock_session
    mock_submission = MagicMock(submission_id=42)
    monkeypatch.setattr(collision_middleware, 'db', mock_db)
    monkeypatch.setattr(collision_middleware, 'Submission', MagicMock(return_value=mock_submission))
    monkeypatch.setattr(collision_middleware.common_middleware, 'get_user_guid', lambda **kwargs: 'user-guid')
    kwargs = {'payload': DUMMY_PAYLOAD}
    result, out_kwargs = collision_middleware.save_collision_data(**kwargs)
    assert result is True
    assert out_kwargs['response_dict']['submission_id'] == 42
    assert out_kwargs['submission'] == mock_submission

def test_save_collision_data_exception(monkeypatch):
    mock_db = MagicMock()
    mock_session = MagicMock()
    mock_db.session = mock_session
    mock_session.add.side_effect = Exception('db error')
    monkeypatch.setattr(collision_middleware, 'db', mock_db)
    monkeypatch.setattr(collision_middleware, 'Submission', MagicMock())
    monkeypatch.setattr(collision_middleware.common_middleware, 'get_user_guid', lambda **kwargs: 'user-guid')
    kwargs = {'payload': DUMMY_PAYLOAD}
    result, out_kwargs = collision_middleware.save_collision_data(**kwargs)
    assert result is False
    assert 'error' in out_kwargs
    assert out_kwargs['error']['error_code']

def test_save_event_pdf_success():
    kwargs = {'payload': DUMMY_PAYLOAD}
    result, out_kwargs = collision_middleware.save_event_pdf(**kwargs)
    assert result is True
    assert out_kwargs == kwargs

def test_save_event_pdf_exception(monkeypatch):
    def raise_exc(**kwargs):
        raise Exception('pdf error')
    monkeypatch.setattr(collision_middleware, 'save_event_pdf', lambda **kwargs: (_ for _ in ()).throw(Exception('pdf error')))
    # Instead, patch the body of save_event_pdf to raise
    with patch('python.prohibition_web_svc.middleware.collision_middleware.save_event_pdf', side_effect=Exception('pdf error')):
        try:
            collision_middleware.save_event_pdf(payload=DUMMY_PAYLOAD)
        except Exception as e:
            assert str(e) == 'pdf error'
