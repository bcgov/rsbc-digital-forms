import pytest
from flask import Flask
from unittest.mock import MagicMock
from python.prohibition_web_svc.middleware import detachment_middleware


@pytest.fixture
def app():
    """Minimal Flask app so jsonify/make_response work in middleware tests."""
    a = Flask(__name__)
    a.config['TESTING'] = True
    return a


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_agency(id=1, agency_name='Vancouver', vjur='VAN'):
    a = MagicMock()
    a.id = id
    a.agency_name = agency_name
    a.vjur = vjur
    return a


def make_user(user_guid='officer-1', agency_id=1, agency_ref=None):
    u = MagicMock()
    u.user_guid = user_guid
    u.agency_id = agency_id
    u.agency_ref = agency_ref or make_agency(agency_id)
    return u


# ---------------------------------------------------------------------------
# get_all_detachments
# ---------------------------------------------------------------------------

class TestGetAllDetachments:
    def test_returns_all_agencies(self, app, monkeypatch):
        mock_db = MagicMock()
        agencies = [make_agency(1, 'Vancouver', 'VAN'), make_agency(2, 'Burnaby', 'BUR')]
        mock_db.session.query().all.return_value = agencies
        monkeypatch.setattr(detachment_middleware, 'db', mock_db)

        with app.app_context():
            result, kwargs = detachment_middleware.get_all_detachments()

        assert result is True
        assert kwargs.get('response') is not None

    def test_handles_db_exception(self, monkeypatch):
        mock_db = MagicMock()
        mock_db.session.query.side_effect = Exception('db down')
        monkeypatch.setattr(detachment_middleware, 'db', mock_db)

        result, kwargs = detachment_middleware.get_all_detachments()

        assert result is False


# ---------------------------------------------------------------------------
# get_officer_current_detachment
# ---------------------------------------------------------------------------

class TestGetOfficerCurrentDetachment:
    def test_returns_current_detachment(self, app, monkeypatch):
        mock_db = MagicMock()
        user = make_user('officer-1', 1)
        mock_db.session.query().filter().first.return_value = user
        monkeypatch.setattr(detachment_middleware, 'db', mock_db)

        with app.app_context():
            result, kwargs = detachment_middleware.get_officer_current_detachment(officer_id='officer-1')

        assert result is True
        assert kwargs.get('response') is not None

    def test_officer_not_found(self, monkeypatch):
        mock_db = MagicMock()
        mock_db.session.query().filter().first.return_value = None
        monkeypatch.setattr(detachment_middleware, 'db', mock_db)

        result, kwargs = detachment_middleware.get_officer_current_detachment(officer_id='ghost')

        assert result is False

    def test_handles_db_exception(self, monkeypatch):
        mock_db = MagicMock()
        mock_db.session.query.side_effect = Exception('db error')
        monkeypatch.setattr(detachment_middleware, 'db', mock_db)

        result, kwargs = detachment_middleware.get_officer_current_detachment(officer_id='officer-1')

        assert result is False


# ---------------------------------------------------------------------------
# validate_detachment_change_request_payload
# ---------------------------------------------------------------------------

class TestValidatePayload:
    def _valid_payload(self, **overrides):
        base = {
            'officer_id': 'officer-1',
            'new_detachment_id': 2,
            'reason': 'OVERTIME_ASSIGNMENT',
            'comments': 'Working overtime at another detachment',
        }
        base.update(overrides)
        return base

    def test_valid_payload_passes(self):
        result, kwargs = detachment_middleware.validate_detachment_change_request_payload(
            payload=self._valid_payload()
        )
        assert result is True

    def test_missing_officer_id_fails(self):
        payload = self._valid_payload()
        del payload['officer_id']
        result, kwargs = detachment_middleware.validate_detachment_change_request_payload(payload=payload)
        assert result is False
        assert 'officer_id' in kwargs['validation_errors']

    def test_missing_new_detachment_id_fails(self):
        payload = self._valid_payload()
        del payload['new_detachment_id']
        result, kwargs = detachment_middleware.validate_detachment_change_request_payload(payload=payload)
        assert result is False
        assert 'new_detachment_id' in kwargs['validation_errors']

    def test_invalid_reason_fails(self):
        result, kwargs = detachment_middleware.validate_detachment_change_request_payload(
            payload=self._valid_payload(reason='INVALID')
        )
        assert result is False
        assert 'reason' in kwargs['validation_errors']

    def test_all_valid_reasons_accepted(self):
        for reason in ('OVERTIME_ASSIGNMENT', 'TRANSFER', 'TEMPORARY_COVERAGE',
                       'OPERATIONAL_REQUIREMENT', 'OTHER'):
            result, _ = detachment_middleware.validate_detachment_change_request_payload(
                payload=self._valid_payload(reason=reason)
            )
            assert result is True, f"reason {reason} should be valid"

    def test_comments_is_optional(self):
        payload = self._valid_payload()
        del payload['comments']
        result, kwargs = detachment_middleware.validate_detachment_change_request_payload(payload=payload)
        assert result is True


# ---------------------------------------------------------------------------
# validate_officer_is_self
# ---------------------------------------------------------------------------

class TestValidateOfficerIsSelf:
    def test_matching_guids_passes(self):
        result, _ = detachment_middleware.validate_officer_is_self(
            user_guid='officer-1',
            payload={'officer_id': 'officer-1'}
        )
        assert result is True

    def test_mismatched_guids_fails(self):
        result, _ = detachment_middleware.validate_officer_is_self(
            user_guid='officer-1',
            payload={'officer_id': 'officer-2'}
        )
        assert result is False


# ---------------------------------------------------------------------------
# get_officer_for_change_request
# ---------------------------------------------------------------------------

class TestGetOfficerForChangeRequest:
    def test_happy_path_sets_officer_and_previous_agency(self, monkeypatch):
        mock_db = MagicMock()
        user = make_user('officer-1', agency_id=5)
        mock_db.session.query().filter().first.return_value = user
        monkeypatch.setattr(detachment_middleware, 'db', mock_db)

        result, kwargs = detachment_middleware.get_officer_for_change_request(
            payload={'officer_id': 'officer-1'}
        )

        assert result is True
        assert kwargs['officer'] is user
        assert kwargs['previous_agency_id'] == 5

    def test_officer_not_found_returns_false(self, monkeypatch):
        mock_db = MagicMock()
        mock_db.session.query().filter().first.return_value = None
        monkeypatch.setattr(detachment_middleware, 'db', mock_db)

        result, kwargs = detachment_middleware.get_officer_for_change_request(
            payload={'officer_id': 'unknown'}
        )

        assert result is False

    def test_db_exception_returns_false(self, monkeypatch):
        mock_db = MagicMock()
        mock_db.session.query.side_effect = Exception('db error')
        monkeypatch.setattr(detachment_middleware, 'db', mock_db)

        result, kwargs = detachment_middleware.get_officer_for_change_request(
            payload={'officer_id': 'officer-1'}
        )

        assert result is False


# ---------------------------------------------------------------------------
# get_new_detachment
# ---------------------------------------------------------------------------

class TestGetNewDetachment:
    def test_happy_path_sets_new_agency(self, monkeypatch):
        mock_db = MagicMock()
        agency = make_agency(id=2)
        mock_db.session.query().filter().first.return_value = agency
        monkeypatch.setattr(detachment_middleware, 'db', mock_db)

        result, kwargs = detachment_middleware.get_new_detachment(
            payload={'new_detachment_id': 2}
        )

        assert result is True
        assert kwargs['new_agency'] is agency

    def test_detachment_not_found_returns_false(self, monkeypatch):
        mock_db = MagicMock()
        mock_db.session.query().filter().first.return_value = None
        monkeypatch.setattr(detachment_middleware, 'db', mock_db)

        result, _ = detachment_middleware.get_new_detachment(
            payload={'new_detachment_id': 999}
        )

        assert result is False

    def test_db_exception_returns_false(self, monkeypatch):
        mock_db = MagicMock()
        mock_db.session.query.side_effect = Exception('db error')
        monkeypatch.setattr(detachment_middleware, 'db', mock_db)

        result, _ = detachment_middleware.get_new_detachment(
            payload={'new_detachment_id': 2}
        )

        assert result is False


# ---------------------------------------------------------------------------
# validate_not_duplicate_request
# ---------------------------------------------------------------------------

class TestValidateNotDuplicate:
    def test_different_detachment_passes(self):
        result, _ = detachment_middleware.validate_not_duplicate_request(
            previous_agency_id=1,
            payload={'new_detachment_id': 2}
        )
        assert result is True

    def test_same_detachment_fails(self):
        result, _ = detachment_middleware.validate_not_duplicate_request(
            previous_agency_id=3,
            payload={'new_detachment_id': 3}
        )
        assert result is False


# ---------------------------------------------------------------------------
# update_officer_detachment
# ---------------------------------------------------------------------------

class TestUpdateOfficerDetachment:
    def test_updates_agency_id(self):
        officer = make_user('officer-1', agency_id=1)
        new_agency = make_agency(id=2)

        result, kwargs = detachment_middleware.update_officer_detachment(
            officer=officer, new_agency=new_agency
        )

        assert result is True
        assert officer.agency_id == 2

    def test_exception_returns_false(self):
        class ReadOnly:
            @property
            def agency_id(self):
                return 1

        officer = ReadOnly()  # no setter → AttributeError on assignment
        new_agency = make_agency(id=2)

        result, _ = detachment_middleware.update_officer_detachment(
            officer=officer, new_agency=new_agency
        )

        assert result is False


# ---------------------------------------------------------------------------
# create_change_audit_record
# ---------------------------------------------------------------------------

class TestCreateChangeAuditRecord:
    def test_happy_path_adds_record_and_sets_response_dict(self, monkeypatch):
        mock_db = MagicMock()
        monkeypatch.setattr(detachment_middleware, 'db', mock_db)

        officer = make_user('officer-1', agency_id=1)
        new_agency = make_agency(id=2, agency_name='Burnaby', vjur='BUR')

        result, kwargs = detachment_middleware.create_change_audit_record(
            officer=officer,
            new_agency=new_agency,
            previous_agency_id=1,
            payload={'reason': 'OVERTIME_ASSIGNMENT', 'comments': 'Overtime at Burnaby'},
            username='admin',
        )

        assert result is True
        assert mock_db.session.add.called
        assert kwargs['response_dict']['new_detachment']['id'] == 2
        assert kwargs['response_dict']['new_detachment']['agency_name'] == 'Burnaby'
        assert kwargs['response_dict']['session_refreshed'] is True
        assert 'updated_at' in kwargs['response_dict']

    def test_db_add_exception_returns_false(self, monkeypatch):
        mock_db = MagicMock()
        mock_db.session.add.side_effect = Exception('db error')
        monkeypatch.setattr(detachment_middleware, 'db', mock_db)

        officer = make_user('officer-1')
        new_agency = make_agency(id=2)

        result, _ = detachment_middleware.create_change_audit_record(
            officer=officer,
            new_agency=new_agency,
            previous_agency_id=1,
            payload={'reason': 'TRANSFER'},
            username='admin',
        )

        assert result is False


# ---------------------------------------------------------------------------
# commit_transaction
# ---------------------------------------------------------------------------

class TestCommitTransaction:
    def test_happy_path_commits(self, monkeypatch):
        mock_db = MagicMock()
        monkeypatch.setattr(detachment_middleware, 'db', mock_db)

        result, _ = detachment_middleware.commit_transaction()

        assert result is True
        mock_db.session.commit.assert_called_once()

    def test_exception_rolls_back_and_returns_false(self, monkeypatch):
        mock_db = MagicMock()
        mock_db.session.commit.side_effect = Exception('db error')
        monkeypatch.setattr(detachment_middleware, 'db', mock_db)

        result, _ = detachment_middleware.commit_transaction()

        assert result is False
        mock_db.session.rollback.assert_called_once()
