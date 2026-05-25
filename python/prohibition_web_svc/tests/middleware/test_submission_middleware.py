import pytest
from unittest.mock import MagicMock, patch
from python.prohibition_web_svc.middleware.submission_middleware import (
    log_status_update_payload_to_splunk,
    request_contains_a_payload,
    validate_update_event_status_payload,
    update_submission_event_status,
    commit_transaction,
)


# ── request_contains_a_payload ────────────────────────────────────────────────

def test_request_contains_a_payload_success():
    """Returns True and sets payload when JSON is present."""
    mock_request = MagicMock()
    mock_request.get_json.return_value = {'ff_application_id': 'app-001'}
    result, out = request_contains_a_payload(request=mock_request)
    assert result is True
    assert out['payload'] == {'ff_application_id': 'app-001'}


def test_request_contains_a_payload_none():
    """Returns False when get_json returns None."""
    mock_request = MagicMock()
    mock_request.get_json.return_value = None
    result, out = request_contains_a_payload(request=mock_request)
    assert result is False


def test_request_contains_a_payload_exception():
    """Returns False when get_json raises an exception."""
    mock_request = MagicMock()
    mock_request.get_json.side_effect = Exception("bad json")
    result, out = request_contains_a_payload(request=mock_request)
    assert result is False


# ── log_status_update_payload_to_splunk ──────────────────────────────────────

def test_log_status_update_payload_to_splunk_sets_splunk_data():
    """Returns True and stores a structured splunk payload."""
    payload = {
        'ff_application_id': 'app-001',
        'form_id': 'VI123',
        'destination': 'VIPS',
        'status': 'sent',
    }
    result, out = log_status_update_payload_to_splunk(payload=payload)

    assert result is True
    assert out['splunk_data'] == {
        'event': 'update_submission_event_status',
        'payload': payload,
    }


def test_log_status_update_payload_to_splunk_handles_missing_payload():
    """Returns True and includes payload=None when not provided."""
    result, out = log_status_update_payload_to_splunk()

    assert result is True
    assert out['splunk_data'] == {
        'event': 'update_submission_event_status',
        'payload': None,
    }


# ── validate_update_event_status_payload ─────────────────────────────────────

def test_validate_update_event_status_payload_success():
    """Returns True when all required fields are present."""
    kwargs = {'payload': {'ff_application_id': 'app-001', 'form_id': 'VI123', 'destination': 'VIPS', 'status': 'sent'}}
    result, out = validate_update_event_status_payload(**kwargs)
    assert result is True
    assert 'response_dict' not in out


def test_validate_update_event_status_payload_no_payload():
    """Returns False when payload is absent."""
    result, out = validate_update_event_status_payload()
    assert result is False
    assert 'error_details' in out.get('response_dict', {})


def test_validate_update_event_status_payload_missing_destination():
    """Returns False when destination is missing."""
    kwargs = {'payload': {'ff_application_id': 'app-001', 'form_id': 'VI123', 'status': 'sent'}}
    result, out = validate_update_event_status_payload(**kwargs)
    assert result is False
    assert 'destination' in out['response_dict']['error_details']


def test_validate_update_event_status_payload_missing_status():
    """Returns False when status is missing."""
    kwargs = {'payload': {'ff_application_id': 'app-001', 'form_id': 'VI123', 'destination': 'VIPS'}}
    result, out = validate_update_event_status_payload(**kwargs)
    assert result is False
    assert 'status' in out['response_dict']['error_details']


def test_validate_update_event_status_payload_missing_ff_application_id():
    """Returns False when ff_application_id is missing."""
    kwargs = {'payload': {'form_id': 'VI123', 'destination': 'VIPS', 'status': 'sent'}}
    result, out = validate_update_event_status_payload(**kwargs)
    assert result is False
    assert 'ff_application_id' in out['response_dict']['error_details']


def test_validate_update_event_status_payload_missing_form_id():
    """Returns False when form_id is missing."""
    kwargs = {'payload': {'ff_application_id': 'app-001', 'destination': 'VIPS', 'status': 'sent'}}
    result, out = validate_update_event_status_payload(**kwargs)
    assert result is False
    assert 'form_id' in out['response_dict']['error_details']


# ── update_submission_event_status ────────────────────────────────────────────

@patch('python.prohibition_web_svc.middleware.submission_middleware.db')
def test_update_submission_event_status_success(mock_db):
    """Returns True and sets response_dict when submission and event are found."""
    mock_submission = MagicMock()
    mock_submission.submission_id = 42

    mock_event = MagicMock()
    mock_event.submission_event_id = 7
    mock_event.destination = 'VIPS'
    mock_event.status = 'sent'

    mock_db.session.query.return_value.filter.return_value.first.return_value = mock_submission
    (mock_db.session.query.return_value
     .join.return_value
     .filter.return_value
     .first.return_value) = mock_event

    kwargs = {'payload': {'ff_application_id': 'app-001', 'form_id': 'VI123', 'destination': 'VIPS', 'status': 'sent'}}
    result, out = update_submission_event_status(**kwargs)

    assert result is True
    assert out['response_dict']['submission_event_id'] == 7
    assert out['response_dict']['status'] == 'sent'


@patch('python.prohibition_web_svc.middleware.submission_middleware.db')
def test_update_submission_event_status_submission_not_found(mock_db):
    """Returns False when no matching submission exists."""
    mock_db.session.query.return_value.filter.return_value.first.return_value = None

    kwargs = {'payload': {'ff_application_id': 'no-such-app', 'form_id': 'VI123', 'destination': 'VIPS', 'status': 'sent'}}
    result, out = update_submission_event_status(**kwargs)

    assert result is False


@patch('python.prohibition_web_svc.middleware.submission_middleware.db')
def test_update_submission_event_status_event_not_found(mock_db):
    """Returns False when submission exists but no matching submission event is found."""
    mock_submission = MagicMock()
    mock_submission.submission_id = 42

    mock_db.session.query.return_value.filter.return_value.first.return_value = mock_submission
    (mock_db.session.query.return_value
     .join.return_value
     .filter.return_value
     .first.return_value) = None

    kwargs = {'payload': {'ff_application_id': 'app-001', 'form_id': 'VI123', 'destination': 'UNKNOWN', 'status': 'sent'}}
    result, out = update_submission_event_status(**kwargs)

    assert result is False


@patch('python.prohibition_web_svc.middleware.submission_middleware.db')
def test_update_submission_event_status_db_exception(mock_db):
    """Returns False and rolls back when a database error occurs."""
    mock_db.session.query.side_effect = Exception("DB failure")

    kwargs = {'payload': {'ff_application_id': 'app-001', 'form_id': 'VI123', 'destination': 'VIPS', 'status': 'sent'}}
    result, out = update_submission_event_status(**kwargs)

    assert result is False
    mock_db.session.rollback.assert_called_once()


# ── commit_transaction ────────────────────────────────────────────────────────

@patch('python.prohibition_web_svc.middleware.submission_middleware.db')
def test_commit_transaction_success(mock_db):
    """Returns True on successful commit."""
    result, out = commit_transaction()
    assert result is True
    mock_db.session.commit.assert_called_once()


@patch('python.prohibition_web_svc.middleware.submission_middleware.db')
def test_commit_transaction_failure(mock_db):
    """Returns False and rolls back on commit error."""
    mock_db.session.commit.side_effect = Exception("commit failed")
    result, out = commit_transaction()
    assert result is False
    mock_db.session.rollback.assert_called_once()
