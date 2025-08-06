import pytest
from unittest.mock import MagicMock, patch
from python.common.models import Event
from python.common.enums import ErrorCode
from python.prohibition_web_svc.middleware.event_middleware import check_if_application_id_exists

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