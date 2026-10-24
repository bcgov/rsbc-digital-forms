from unittest.mock import MagicMock, patch
from python.common.enums import ErrorCode
from python.prohibition_web_svc.middleware import collision_middleware

DB = 'python.prohibition_web_svc.middleware.collision_middleware.db'


def _collision(ff_application_id=123, submission=True):
    collision = MagicMock()
    if submission:
        collision.submission.submission_id = 7
        collision.submission.ff_application_id = ff_application_id
        collision.submission.task_processing_status = 'pending'
        collision.submission.submitted_offline = False
    else:
        collision.submission = None
    return collision


def _form_ref(icbc_status='sent'):
    event = MagicMock(destination='ICBC', status=icbc_status)
    return MagicMock(form_version='MV6020E (022026)', events=[event])


def _mock_queries(mock_db, collision, form_ref):
    mock_db.session.query.return_value.filter.return_value.first.side_effect = [collision, form_ref]


def test_get_collision_metadata_success():
    with patch(DB) as mock_db:
        _mock_queries(mock_db, _collision(), _form_ref())
        result, kwargs = collision_middleware.get_collision_metadata(collision_case_num='EZ005648')
    assert result is True
    assert kwargs['response_dict'] == {
        'collision_case_num': 'EZ005648',
        'ff_application_id': 123,
        'task_processing_status': 'pending',
        'submitted_offline': False,
        'form_version': 'MV6020E (022026)',
        'icbc_status': 'sent',
    }


def test_get_collision_metadata_not_yet_linked_to_formsflow():
    with patch(DB) as mock_db:
        _mock_queries(mock_db, _collision(ff_application_id=None), _form_ref())
        result, kwargs = collision_middleware.get_collision_metadata(collision_case_num='EZ005648')
    assert result is True
    assert kwargs['response_dict']['ff_application_id'] is None


def test_get_collision_metadata_without_form_ref():
    with patch(DB) as mock_db:
        _mock_queries(mock_db, _collision(), None)
        result, kwargs = collision_middleware.get_collision_metadata(collision_case_num='EZ005648')
    assert result is True
    assert kwargs['response_dict']['form_version'] is None
    assert kwargs['response_dict']['icbc_status'] is None


def test_get_collision_metadata_not_found():
    with patch(DB) as mock_db:
        _mock_queries(mock_db, None, None)
        result, kwargs = collision_middleware.get_collision_metadata(collision_case_num='EZ999999')
    assert result is False
    assert kwargs['error']['error_code'] == ErrorCode.C03
    assert collision_middleware.collision_metadata_not_found(**kwargs)[0] is True


def test_get_collision_metadata_collision_without_submission():
    with patch(DB) as mock_db:
        _mock_queries(mock_db, _collision(submission=False), None)
        result, kwargs = collision_middleware.get_collision_metadata(collision_case_num='EZ005648')
    assert result is False
    assert kwargs['error']['error_code'] == ErrorCode.C03


def test_get_collision_metadata_db_error_is_not_a_not_found():
    with patch(DB) as mock_db:
        mock_db.session.query.side_effect = Exception('db down')
        result, kwargs = collision_middleware.get_collision_metadata(collision_case_num='EZ005648')
    assert result is False
    assert kwargs['error']['error_code'] == ErrorCode.C02
    assert collision_middleware.collision_metadata_not_found(**kwargs)[0] is False


def test_log_get_collision_metadata_to_splunk_has_no_contents():
    result, kwargs = collision_middleware.log_get_collision_metadata_to_splunk(
        collision_case_num='EZ005648', username='u', user_guid='g', request_id='r')
    assert result is True
    assert kwargs['splunk_data'] == {
        'event': 'get collision metadata', 'request_id': 'r', 'user_guid': 'g', 'username': 'u',
        'form_type': 'MV6020', 'collision_case_number': 'EZ005648'}
