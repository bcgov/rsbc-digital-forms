from types import SimpleNamespace
from unittest.mock import MagicMock

from python.common.enums import ErrorCode
from python.prohibition_web_svc.middleware import offline_submission_middleware


def test_set_local_submission_id_uses_payload_values(monkeypatch):
    kwargs = {
        'payload': {'localSubmissionId': 'local-123', 'formId': 'VI123'},
        'unchanged': True,
    }

    result, out = offline_submission_middleware.set_local_submission_id(**kwargs)

    assert result is True
    assert out['local_submission_id'] == 'local-123'
    assert out['form_id'] == 'VI123'
    assert out['unchanged'] is True


def test_set_local_submission_id_generates_id_when_missing(monkeypatch):
    monkeypatch.setattr(
        offline_submission_middleware.uuid,
        'uuid4',
        lambda: SimpleNamespace(hex='generated-id'),
    )

    result, out = offline_submission_middleware.set_local_submission_id(
        payload={'formId': 'VI123'}
    )

    assert result is True
    assert out['local_submission_id'] == 'generated_generated-id'
    assert out['form_id'] == 'VI123'


def test_set_local_submission_id_without_payload_leaves_kwargs_unchanged():
    kwargs = {'local_submission_id': 'existing-id'}

    result, out = offline_submission_middleware.set_local_submission_id(**kwargs)

    assert result is True
    assert out == kwargs


def test_check_if_offline_submission_exists_returns_false_for_duplicate(monkeypatch):
    model = MagicMock()
    model.query.filter_by.return_value.count.return_value = 1
    monkeypatch.setattr(offline_submission_middleware, 'FormsflowOfflineSubmission', model)
    kwargs = {'local_submission_id': 'local-123', 'user_guid': 'user-456'}

    result, out = offline_submission_middleware.check_if_offline_submission_exists(**kwargs)

    assert result is False
    assert out == kwargs
    model.query.filter_by.assert_called_once_with(
        local_submission_id='local-123',
        created_by='user-456',
    )


def test_check_if_offline_submission_exists_returns_true_when_not_found(monkeypatch):
    model = MagicMock()
    model.query.filter_by.return_value.count.return_value = 0
    monkeypatch.setattr(offline_submission_middleware, 'FormsflowOfflineSubmission', model)

    result, out = offline_submission_middleware.check_if_offline_submission_exists(
        local_submission_id='local-123',
        user_guid='user-456',
    )

    assert result is True
    assert out['local_submission_id'] == 'local-123'


def test_check_if_offline_submission_exists_records_query_error(monkeypatch):
    model = MagicMock()
    model.query.filter_by.side_effect = RuntimeError('database unavailable')
    monkeypatch.setattr(offline_submission_middleware, 'FormsflowOfflineSubmission', model)

    result, out = offline_submission_middleware.check_if_offline_submission_exists(
        local_submission_id='local-123',
        user_guid='user-456',
    )

    assert result is False
    assert out['error'] == {
        'error_code': ErrorCode.O01,
        'error_details': 'database unavailable',
        'event_id': None,
        'event_type': 'offline_submission',
        'ticket_no': 'local-123',
        'func': offline_submission_middleware.check_if_offline_submission_exists,
    }


def test_create_offline_submission_adds_commits_and_sets_response(monkeypatch):
    model = MagicMock()
    submission = MagicMock(id=42)
    model.return_value = submission
    db = MagicMock()
    monkeypatch.setattr(offline_submission_middleware, 'FormsflowOfflineSubmission', model)
    monkeypatch.setattr(offline_submission_middleware, 'db', db)
    payload = {'localSubmissionId': 'local-123', 'answers': []}

    result, out = offline_submission_middleware.create_offline_submission(
        local_submission_id='local-123',
        payload=payload,
        user_guid='user-456',
        form_id='VI123',
    )

    assert result is True
    model.assert_called_once()
    created_values = model.call_args.kwargs
    assert created_values['local_submission_id'] == 'local-123'
    assert created_values['payload'] == payload
    assert created_values['status'] == 'pending'
    assert created_values['form_id'] == 'VI123'
    assert created_values['created_by'] == 'user-456'
    assert created_values['created_dt'] is not None
    db.session.add.assert_called_once_with(submission)
    db.session.commit.assert_called_once()
    assert out['response_dict'] == {'offline_submission_id': 42}


def test_create_offline_submission_rolls_back_and_records_error(monkeypatch):
    model = MagicMock()
    db = MagicMock()
    db.session.commit.side_effect = RuntimeError('commit failed')
    monkeypatch.setattr(offline_submission_middleware, 'FormsflowOfflineSubmission', model)
    monkeypatch.setattr(offline_submission_middleware, 'db', db)

    result, out = offline_submission_middleware.create_offline_submission(
        local_submission_id='local-123',
        payload={'answers': []},
        user_guid='user-456',
    )

    assert result is False
    db.session.add.assert_called_once()
    db.session.commit.assert_called_once()
    db.session.rollback.assert_called_once()
    assert out['error'] == {
        'error_code': ErrorCode.O01,
        'error_details': 'commit failed',
        'event_id': None,
        'event_type': 'offline_submission',
        'ticket_no': 'local-123',
        'func': offline_submission_middleware.create_offline_submission,
    }
