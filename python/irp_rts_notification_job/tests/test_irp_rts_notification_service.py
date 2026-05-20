from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from python.irp_rts_notification_job import irp_rts_notification_service as service


class TestFetchPendingNotifications:
    def test_returns_rows(self):
        conn = MagicMock()
        cursor = MagicMock()
        cursor.fetchall.return_value = [(1,), (2,)]

        cursor_cm = MagicMock()
        cursor_cm.__enter__.return_value = cursor
        conn.cursor.return_value = cursor_cm

        rows = service._fetch_pending_notifications(conn)

        assert rows == [(1,), (2,)]
        cursor.execute.assert_called_once()


class TestRunNotification:
    def test_run_notification_completes_without_error(self):
        service.run_notification()
