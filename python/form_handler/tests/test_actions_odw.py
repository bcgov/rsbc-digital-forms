"""
Unit tests for python.form_handler.actions_odw
"""
from __future__ import annotations

from unittest.mock import patch

import pytest

import python.form_handler.actions_odw as actions_odw


class TestSendToOdw:
    """Tests for actions_odw.send_to_odw()"""

    @pytest.mark.parametrize("event_type, ride_func", [
        ("vi", "vi_event"),
        ("12h", "twelve_hours_event"),
        ("24h", "twenty_four_hours_event"),
        ("irp", "irp_event"),
    ])
    def test_dispatches_to_ride_event(self, event_type, ride_func):
        with patch.object(actions_odw.ride_actions, ride_func, return_value=(True, {})) as mock_func:
            result = actions_odw.send_to_odw(event_type=event_type, message={'event_id': 1})
        mock_func.assert_called_once_with(event_type=event_type, message={'event_id': 1})
        assert result == (True, {})

    def test_unknown_event_type_returns_true(self):
        with patch.object(actions_odw.ride_actions, "irp_event") as mock_irp:
            flag, args = actions_odw.send_to_odw(event_type='unknown')
        mock_irp.assert_not_called()
        assert flag is True
