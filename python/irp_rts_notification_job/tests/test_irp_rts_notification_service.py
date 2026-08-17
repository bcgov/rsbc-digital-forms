from __future__ import annotations

from unittest.mock import MagicMock, call

import pytest

from python.irp_rts_notification_job import irp_rts_notification_service as service

# Sample row tuples:
# (submission_event_id, username, display_name, ff_application_id, form_type, form_id, driver_last_name, date_of_driving)
ROW_USER_A_1 = (1, "user_a@idir", "User A", "app-001", "IRP", "form-001", "Smith", "2024-01-01")
ROW_USER_A_2 = (2, "user_a@idir", "User A", "app-002", "IRP", "form-002", "Smith", "2024-01-02")
ROW_USER_B_1 = (3, "user_b@idir", "User B", "app-003", "IRP", "form-003", "Jones", "2024-01-03")


def _make_conn():
    """Return a MagicMock that behaves as a psycopg2 connection with a cursor context manager."""
    conn = MagicMock()
    cursor = MagicMock()
    cursor_cm = MagicMock()
    cursor_cm.__enter__.return_value = cursor
    conn.cursor.return_value = cursor_cm
    return conn, cursor


class TestFetchPendingRTS:
    def test_returns_rows(self):
        conn, cursor = _make_conn()
        cursor.fetchall.return_value = [ROW_USER_A_1, ROW_USER_B_1]

        rows = service._fetch_pending_RTS(conn)

        assert rows == [ROW_USER_A_1, ROW_USER_B_1]
        cursor.execute.assert_called_once()

    def test_returns_empty_list_when_no_rows(self):
        conn, cursor = _make_conn()
        cursor.fetchall.return_value = []

        rows = service._fetch_pending_RTS(conn)

        assert rows == []


class TestRunNotification:
    def test_run_notification_calls_fetch_and_process(self, monkeypatch):
        mock_conn = MagicMock()
        mock_conn.__enter__ = MagicMock(return_value=mock_conn)
        mock_conn.__exit__ = MagicMock(return_value=False)

        mock_fetch = MagicMock(return_value=[ROW_USER_A_1])
        mock_process = MagicMock()

        monkeypatch.setattr(service.psycopg2, "connect", lambda **kwargs: mock_conn)
        monkeypatch.setattr(service, "_fetch_pending_RTS", mock_fetch)
        monkeypatch.setattr(service, "_process_pending_RTS", mock_process)

        service.run_notification()

        mock_fetch.assert_called_once_with(mock_conn)
        mock_process.assert_called_once_with(mock_conn, [ROW_USER_A_1])

    def test_run_notification_raises_on_db_error(self, monkeypatch):
        monkeypatch.setattr(
            service.psycopg2,
            "connect",
            MagicMock(side_effect=Exception("DB connection failed")),
        )

        with pytest.raises(Exception, match="DB connection failed"):
            service.run_notification()


class TestProcessPendingRTS:
    def test_groups_rows_by_username(self, monkeypatch):
        mock_process_user = MagicMock()
        monkeypatch.setattr(service, "_process_pending_rts_for_user", mock_process_user)
        conn = MagicMock()

        result = service._process_pending_RTS(conn, [ROW_USER_A_1, ROW_USER_A_2, ROW_USER_B_1])

        assert set(result.keys()) == {"user_a@idir", "user_b@idir"}
        assert len(result["user_a@idir"]) == 2
        assert len(result["user_b@idir"]) == 1

    def test_calls_process_user_for_each_unique_user(self, monkeypatch):
        mock_process_user = MagicMock()
        monkeypatch.setattr(service, "_process_pending_rts_for_user", mock_process_user)
        conn = MagicMock()

        service._process_pending_RTS(conn, [ROW_USER_A_1, ROW_USER_A_2, ROW_USER_B_1])

        assert mock_process_user.call_count == 2

    def test_passes_conn_to_process_user(self, monkeypatch):
        mock_process_user = MagicMock()
        monkeypatch.setattr(service, "_process_pending_rts_for_user", mock_process_user)
        conn = MagicMock()

        service._process_pending_RTS(conn, [ROW_USER_A_1])

        args, _ = mock_process_user.call_args
        assert args[0] is conn

    def test_returns_empty_dict_when_input_is_empty(self, monkeypatch):
        mock_process_user = MagicMock()
        monkeypatch.setattr(service, "_process_pending_rts_for_user", mock_process_user)
        conn = MagicMock()

        result = service._process_pending_RTS(conn, [])

        assert result == {}
        mock_process_user.assert_not_called()

    def test_returns_empty_dict_when_input_is_none(self, monkeypatch):
        mock_process_user = MagicMock()
        monkeypatch.setattr(service, "_process_pending_rts_for_user", mock_process_user)
        conn = MagicMock()

        result = service._process_pending_RTS(conn, None)

        assert result == {}
        mock_process_user.assert_not_called()

    def test_raises_on_user_processing_error(self, monkeypatch):
        def _side_effect(conn, username, rts_list):
            raise RuntimeError("boom")

        monkeypatch.setattr(service, "_process_pending_rts_for_user", _side_effect)
        conn = MagicMock()

        with pytest.raises(RuntimeError, match="boom"):
            service._process_pending_RTS(conn, [ROW_USER_A_1])


class TestProcessPendingRtsForUser:
    def test_skips_update_and_splunk_when_email_is_none(self, monkeypatch):
        monkeypatch.setattr(service, "_get_user_email_from_keycloak", lambda u: None)
        mock_update = MagicMock()
        mock_splunk = MagicMock()
        monkeypatch.setattr(service, "_update_rts_status", mock_update)
        monkeypatch.setattr(service, "_write_notification_report_to_splunk", mock_splunk)
        conn = MagicMock()

        service._process_pending_rts_for_user(conn, "user_a@idir", [ROW_USER_A_1])

        mock_update.assert_not_called()
        mock_splunk.assert_not_called()

    def test_skips_update_and_splunk_when_email_is_empty_string(self, monkeypatch):
        monkeypatch.setattr(service, "_get_user_email_from_keycloak", lambda u: "")
        mock_update = MagicMock()
        mock_splunk = MagicMock()
        monkeypatch.setattr(service, "_update_rts_status", mock_update)
        monkeypatch.setattr(service, "_write_notification_report_to_splunk", mock_splunk)
        conn = MagicMock()

        service._process_pending_rts_for_user(conn, "user_a@idir", [ROW_USER_A_1])

        mock_update.assert_not_called()
        mock_splunk.assert_not_called()

    def test_calls_send_email_update_and_splunk_when_email_is_present(self, monkeypatch):
        monkeypatch.setattr(
            service, "_get_user_email_from_keycloak", lambda u: "user_a@example.com"
        )
        mock_send = MagicMock()
        mock_update = MagicMock()
        mock_splunk = MagicMock()
        monkeypatch.setattr(service, "_send_notification_email", mock_send)
        monkeypatch.setattr(service, "_update_rts_status", mock_update)
        monkeypatch.setattr(service, "_write_notification_report_to_splunk", mock_splunk)
        conn = MagicMock()

        service._process_pending_rts_for_user(conn, "user_a@idir", [ROW_USER_A_1, ROW_USER_A_2])

        mock_send.assert_called_once_with("user_a@example.com", [ROW_USER_A_1, ROW_USER_A_2])
        mock_update.assert_called_once_with(conn, [ROW_USER_A_1, ROW_USER_A_2])
        mock_splunk.assert_called_once_with("user_a@example.com", [ROW_USER_A_1, ROW_USER_A_2])

    def test_does_not_call_send_email_when_email_is_none(self, monkeypatch):
        monkeypatch.setattr(service, "_get_user_email_from_keycloak", lambda u: None)
        mock_send = MagicMock()
        monkeypatch.setattr(service, "_send_notification_email", mock_send)
        conn = MagicMock()

        service._process_pending_rts_for_user(conn, "user_a@idir", [ROW_USER_A_1])

        mock_send.assert_not_called()


class TestSendNotificationEmail:
    _PATCH_TARGET = "python.common.rsi_email.send_irp_pending_rts"

    def test_calls_send_irp_pending_rts_with_correct_args(self, monkeypatch):
        mock_send = MagicMock()
        monkeypatch.setattr("python.common.rsi_email.send_irp_pending_rts", mock_send)

        service._send_notification_email("user@example.com", [ROW_USER_A_1, ROW_USER_A_2])

        mock_send.assert_called_once()
        _, kwargs = mock_send.call_args
        assert kwargs["email_address"] == "user@example.com"
        assert kwargs["officer_name"] == ROW_USER_A_1[2]
        assert kwargs["message"]["pending_rts_count"] == 2

    def test_subject_matches_expected_value(self, monkeypatch):
        mock_send = MagicMock()
        monkeypatch.setattr("python.common.rsi_email.send_irp_pending_rts", mock_send)

        service._send_notification_email("user@example.com", [ROW_USER_A_1, ROW_USER_A_2])

        _, kwargs = mock_send.call_args
        assert kwargs["subject"] == "Action Required – Outstanding Immediate Roadside Prohibition (IRP) Files"

    def test_officer_name_defaults_to_officer_when_list_empty(self, monkeypatch):
        mock_send = MagicMock()
        monkeypatch.setattr("python.common.rsi_email.send_irp_pending_rts", mock_send)

        service._send_notification_email("user@example.com", [])

        _, kwargs = mock_send.call_args
        assert kwargs["officer_name"] == "Officer"

    def test_raises_when_send_irp_pending_rts_raises(self, monkeypatch):
        monkeypatch.setattr(
            "python.common.rsi_email.send_irp_pending_rts",
            MagicMock(side_effect=RuntimeError("SMTP failure")),
        )

        with pytest.raises(RuntimeError, match="SMTP failure"):
            service._send_notification_email("user@example.com", [ROW_USER_A_1])

    def test_message_contains_superintendent_email(self, monkeypatch):
        mock_send = MagicMock()
        monkeypatch.setattr("python.common.rsi_email.send_irp_pending_rts", mock_send)

        service._send_notification_email("user@example.com", [ROW_USER_A_1])

        _, kwargs = mock_send.call_args
        from python.irp_rts_notification_job.config import Config
        assert kwargs["message"]["superintendent_email"] == Config.SUPERINTENDENT_EMAIL

    def test_message_includes_rts_list(self, monkeypatch):
        mock_send = MagicMock()
        monkeypatch.setattr("python.common.rsi_email.send_irp_pending_rts", mock_send)

        service._send_notification_email("user@example.com", [ROW_USER_A_1, ROW_USER_A_2])

        _, kwargs = mock_send.call_args
        assert kwargs["message"]["pending_rts"] == [ROW_USER_A_1, ROW_USER_A_2]


class TestUpdateRtsStatus:
    def test_executes_update_query_with_correct_ids(self):
        conn, cursor = _make_conn()

        service._update_rts_status(conn, [ROW_USER_A_1, ROW_USER_A_2])

        cursor.execute.assert_called_once()
        query = cursor.execute.call_args[0][0]
        assert "1" in query
        assert "2" in query
        assert "notified" in query

    def test_commits_after_update(self):
        conn, _ = _make_conn()

        service._update_rts_status(conn, [ROW_USER_A_1])

        conn.commit.assert_called_once()

    def test_handles_single_row(self):
        conn, cursor = _make_conn()

        service._update_rts_status(conn, [ROW_USER_B_1])

        cursor.execute.assert_called_once()
        query = cursor.execute.call_args[0][0]
        assert "3" in query


class TestWriteNotificationReportToSplunk:
    def test_calls_splunk_log_with_correct_payload(self, monkeypatch):
        mock_log = MagicMock(return_value=(True, {}))
        monkeypatch.setattr(service.splunk, "log_to_splunk", mock_log)

        service._write_notification_report_to_splunk("user@example.com", [ROW_USER_A_1, ROW_USER_A_2])

        mock_log.assert_called_once()
        kwargs = mock_log.call_args[1]
        payload = kwargs["splunk_data"]
        assert payload["event"] == "irp_rts_notification_report"
        assert payload["email"] == "user@example.com"
        assert payload["pending_rts_count"] == 2
        assert "1" in payload["pending_rts_ids"]
        assert "2" in payload["pending_rts_ids"]

    def test_does_not_raise_when_splunk_fails(self, monkeypatch):
        monkeypatch.setattr(
            service.splunk, "log_to_splunk", MagicMock(side_effect=Exception("Splunk down"))
        )

        # Should complete without raising — Splunk errors must not disrupt business flow
        service._write_notification_report_to_splunk("user@example.com", [ROW_USER_A_1])


class TestGetUserEmailFromKeycloak:
    def _make_token_response(self, token="test-token"):
        mock = MagicMock()
        mock.json.return_value = {"access_token": token}
        return mock

    def _make_users_response(self, users):
        mock = MagicMock()
        mock.json.return_value = users
        return mock

    def test_returns_email_for_known_user(self, monkeypatch):
        token_resp = self._make_token_response()
        users_resp = self._make_users_response([{"email": "user@example.com"}])

        monkeypatch.setattr(service.requests, "post", MagicMock(return_value=token_resp))
        monkeypatch.setattr(service.requests, "get", MagicMock(return_value=users_resp))

        email = service._get_user_email_from_keycloak("user_a@idir")

        assert email == "user@example.com"

    def test_returns_none_when_no_user_found(self, monkeypatch):
        token_resp = self._make_token_response()
        users_resp = self._make_users_response([])

        monkeypatch.setattr(service.requests, "post", MagicMock(return_value=token_resp))
        monkeypatch.setattr(service.requests, "get", MagicMock(return_value=users_resp))

        email = service._get_user_email_from_keycloak("unknown_user@idir")

        assert email is None

    def test_passes_username_unchanged_to_keycloak(self, monkeypatch):
        token_resp = self._make_token_response()
        users_resp = self._make_users_response([{"email": "user@example.com"}])

        mock_get = MagicMock(return_value=users_resp)
        monkeypatch.setattr(service.requests, "post", MagicMock(return_value=token_resp))
        monkeypatch.setattr(service.requests, "get", mock_get)

        service._get_user_email_from_keycloak("someuser@idir")

        _, kwargs = mock_get.call_args
        assert kwargs["params"]["username"] == "someuser@idir"

    def test_uses_exact_match_param(self, monkeypatch):
        token_resp = self._make_token_response()
        users_resp = self._make_users_response([{"email": "user@example.com"}])

        mock_get = MagicMock(return_value=users_resp)
        monkeypatch.setattr(service.requests, "post", MagicMock(return_value=token_resp))
        monkeypatch.setattr(service.requests, "get", mock_get)

        service._get_user_email_from_keycloak("someuser@idir")

        _, kwargs = mock_get.call_args
        assert kwargs["params"]["exact"] is True

    def test_raises_on_token_request_failure(self, monkeypatch):
        token_resp = MagicMock()
        token_resp.raise_for_status.side_effect = Exception("401 Unauthorized")

        monkeypatch.setattr(service.requests, "post", MagicMock(return_value=token_resp))

        with pytest.raises(Exception, match="401 Unauthorized"):
            service._get_user_email_from_keycloak("someuser@idir")

    def test_raises_on_users_request_failure(self, monkeypatch):
        token_resp = self._make_token_response()
        users_resp = MagicMock()
        users_resp.raise_for_status.side_effect = Exception("403 Forbidden")

        monkeypatch.setattr(service.requests, "post", MagicMock(return_value=token_resp))
        monkeypatch.setattr(service.requests, "get", MagicMock(return_value=users_resp))

        with pytest.raises(Exception, match="403 Forbidden"):
            service._get_user_email_from_keycloak("someuser@idir")
