from datetime import datetime
from unittest.mock import MagicMock, patch
from python.common.enums import ErrorCode
from python.prohibition_web_svc.middleware import collision_middleware

DB = 'python.prohibition_web_svc.middleware.collision_middleware.db'


def _collision(revision=0, ff_application_id=123, submission=True):
    collision = MagicMock(revision=revision)
    if submission:
        collision.submission.submission_id = 7 + revision
        collision.submission.ff_application_id = ff_application_id
        collision.submission.task_processing_status = 'pending'
        collision.submission.submitted_offline = False
        collision.submission.created_dt = datetime(2026, 10, 23, 9, 0, revision)
    else:
        collision.submission = None
    return collision


def _form_ref(icbc_status='sent'):
    event = MagicMock(destination='ICBC', status=icbc_status)
    return MagicMock(form_version='MV6020E (022026)', events=[event])


def _mock_metadata(mock_db, collisions, form_refs):
    query = mock_db.session.query.return_value
    query.filter.return_value.order_by.return_value.all.return_value = collisions
    query.filter.return_value.first.side_effect = form_refs


def test_get_collision_metadata_single_revision():
    with patch(DB) as mock_db:
        _mock_metadata(mock_db, [_collision()], [_form_ref()])
        result, kwargs = collision_middleware.get_collision_metadata(collision_case_num='RZ000101')
    assert result is True
    assert kwargs['response_dict'] == {
        'collision_case_num': 'RZ000101',
        'latest_revision': 0,
        'revisions': [{
            'revision': 0,
            'ff_application_id': 123,
            'task_processing_status': 'pending',
            'submitted_offline': False,
            'created_dt': '2026-10-23T09:00:00',
            'form_version': 'MV6020E (022026)',
            'icbc_status': 'sent',
        }],
    }


def test_get_collision_metadata_revision_chain():
    with patch(DB) as mock_db:
        _mock_metadata(mock_db, [_collision(0, 101), _collision(1, 102), _collision(2, None)],
                       [_form_ref(), _form_ref(), _form_ref('pending')])
        result, kwargs = collision_middleware.get_collision_metadata(collision_case_num='RZ000101')
    assert result is True
    assert kwargs['response_dict']['latest_revision'] == 2
    assert [(r['revision'], r['ff_application_id']) for r in kwargs['response_dict']['revisions']] == [
        (0, 101), (1, 102), (2, None)]


def test_get_collision_metadata_without_form_ref():
    with patch(DB) as mock_db:
        _mock_metadata(mock_db, [_collision()], [None])
        result, kwargs = collision_middleware.get_collision_metadata(collision_case_num='RZ000101')
    assert result is True
    assert kwargs['response_dict']['revisions'][0]['form_version'] is None
    assert kwargs['response_dict']['revisions'][0]['icbc_status'] is None


def test_get_collision_metadata_not_found():
    with patch(DB) as mock_db:
        _mock_metadata(mock_db, [], [])
        result, kwargs = collision_middleware.get_collision_metadata(collision_case_num='RZ999999')
    assert result is False
    assert kwargs['error']['error_code'] == ErrorCode.C03
    assert collision_middleware.collision_metadata_not_found(**kwargs)[0] is True


def test_get_collision_metadata_collision_without_submission():
    with patch(DB) as mock_db:
        _mock_metadata(mock_db, [_collision(submission=False)], [])
        result, kwargs = collision_middleware.get_collision_metadata(collision_case_num='RZ000101')
    assert result is False
    assert kwargs['error']['error_code'] == ErrorCode.C03


def test_get_collision_metadata_db_error_is_not_a_not_found():
    with patch(DB) as mock_db:
        mock_db.session.query.side_effect = Exception('db down')
        result, kwargs = collision_middleware.get_collision_metadata(collision_case_num='RZ000101')
    assert result is False
    assert kwargs['error']['error_code'] == ErrorCode.C02
    assert collision_middleware.collision_metadata_not_found(**kwargs)[0] is False


def test_log_get_collision_metadata_to_splunk_has_no_contents():
    result, kwargs = collision_middleware.log_get_collision_metadata_to_splunk(
        collision_case_num='RZ000101', username='u', user_guid='g', request_id='r')
    assert result is True
    assert kwargs['splunk_data'] == {
        'event': 'get collision metadata', 'request_id': 'r', 'user_guid': 'g', 'username': 'u',
        'form_type': 'MV6020', 'collision_case_number': 'RZ000101'}


# --- revision assignment on POST /collision ---

def _set_revision(payload, latest):
    with patch(DB) as mock_db:
        mock_db.session.query.return_value.filter.return_value.scalar.return_value = latest
        return collision_middleware.set_collision_revision(payload=payload, ticket_no='RZ000101')


def test_original_submission_is_revision_zero():
    result, kwargs = _set_revision({'collision_case_num': 'RZ000101'}, latest=None)
    assert result is True
    assert kwargs['revision'] == 0


def test_change_report_from_latest_gets_next_revision():
    result, kwargs = _set_revision({'isChangeReport': True, 'parentRevision': 1}, latest=1)
    assert result is True
    assert kwargs['revision'] == 2


def test_change_report_parent_revision_may_be_a_string():
    result, kwargs = _set_revision({'isChangeReport': 'true', 'parentRevision': '0'}, latest=0)
    assert result is True
    assert kwargs['revision'] == 1


def test_change_report_from_older_revision_is_rejected():
    result, kwargs = _set_revision({'isChangeReport': True, 'parentRevision': 0}, latest=1)
    assert result is False
    assert kwargs['error']['error_code'] == ErrorCode.C05
    assert kwargs['response_dict']['error_details'] == \
        'Change report was created from revision 0, but the latest revision is 1'


def test_change_report_without_parent_revision_is_rejected():
    result, kwargs = _set_revision({'isChangeReport': True}, latest=0)
    assert result is False
    assert kwargs['response_dict']['error_details'] == 'Change report is missing a valid parentRevision'


def test_change_report_for_unknown_case_number_is_rejected():
    result, kwargs = _set_revision({'isChangeReport': True, 'parentRevision': 0}, latest=None)
    assert result is False
    assert kwargs['error']['error_code'] == ErrorCode.C05
    assert 'No collision found' in kwargs['response_dict']['error_details']


def test_set_collision_revision_db_error():
    with patch(DB) as mock_db:
        mock_db.session.query.side_effect = Exception('db down')
        result, kwargs = collision_middleware.set_collision_revision(
            payload={'isChangeReport': True, 'parentRevision': 0}, ticket_no='RZ000101')
    assert result is False
    assert kwargs['error']['error_code'] == ErrorCode.G00


def test_case_number_check_is_skipped_for_change_reports():
    with patch(DB) as mock_db:
        result, _ = collision_middleware.check_if_case_number_exists(
            payload={'isChangeReport': True}, ticket_no='RZ000101')
    assert result is True
    mock_db.session.query.assert_not_called()


def test_is_change_report():
    assert collision_middleware.is_change_report({'isChangeReport': True})
    assert collision_middleware.is_change_report({'isChangeReport': 'true'})
    assert not collision_middleware.is_change_report({'isChangeReport': False})
    assert not collision_middleware.is_change_report({})
    assert not collision_middleware.is_change_report(None)


def test_save_collision_data_uses_assigned_revision():
    captured = {}

    def fake_map(payload):
        captured['revision'] = payload['revision']
        return MagicMock()

    with patch(DB), \
         patch('python.prohibition_web_svc.middleware.collision_middleware.CollisionMapper.map_to_tar_collision', side_effect=fake_map), \
         patch('python.prohibition_web_svc.middleware.collision_middleware.update_form_status', return_value=True), \
         patch('python.prohibition_web_svc.middleware.collision_middleware.common_middleware.get_user_guid', return_value='g'):
        result, _ = collision_middleware.save_collision_data(
            payload={'ff_application_id': 1, 'revision': 99}, revision=3)
    assert result is True
    assert captured['revision'] == 3
