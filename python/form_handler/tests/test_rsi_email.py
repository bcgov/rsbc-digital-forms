"""
Unit tests for python.form_handler.rsi_email
"""
from __future__ import annotations

from unittest.mock import MagicMock

import pytest

import python.form_handler.rsi_email as rsi_email


def _make_args(event_type):
    form_data = {
        "irp_number": "IRP-123" if event_type == "irp" else None,
        "VI_number": "VI-456" if event_type != "irp" else None,
    }
    return {
        "config": MagicMock(),
        "event_type": event_type,
        "form_data": form_data,
        "message": {"event_id": "event-789"},
        "file_data": "encoded-pdf",
        "storage_key": "forms/document.pdf",
    }


class TestEventToVipsDps:
    @pytest.mark.parametrize(
        ("event_type", "expected_title", "expected_filename"),
        [
            ("irp", "Notice of Driving Prohibition IRP-123", "IRP-123.pdf"),
            ("vi", "Vehicle Impoundment VI-456", "VI-456.pdf"),
        ],
    )
    def test_sends_correct_form_details_to_vips(
        self, monkeypatch, event_type, expected_title, expected_filename
    ):
        args = _make_args(event_type)
        send_email = MagicMock(
            return_value=(True, {"email_response": {"result": "success"}})
        )
        monkeypatch.setattr(rsi_email, "send_email_to_vips", send_email)

        result, out_args = rsi_email.event_to_vips_dps(**args)

        assert result is True
        send_email.assert_called_once_with(
            config=args["config"],
            title=expected_title,
            body="Sent to vips ",
            eventid="event-789",
            file_data="encoded-pdf",
            file_name=expected_filename,
        )
        assert out_args["splunk_data"] == {
            "event": "email sent to vips",
            "event_id": "event-789",
            "event_type": event_type,
            "email_response": {"result": "success"},
        }

    def test_returns_false_when_email_is_not_sent(self, monkeypatch):
        args = _make_args("vi")
        monkeypatch.setattr(
            rsi_email,
            "send_email_to_vips",
            MagicMock(return_value=(False, {"email_response": {}})),
        )

        result, out_args = rsi_email.event_to_vips_dps(**args)

        assert result is False
        assert "splunk_data" not in out_args

    def test_returns_false_when_email_sender_raises(self, monkeypatch):
        args = _make_args("irp")
        send_email = MagicMock(side_effect=RuntimeError("email service unavailable"))
        monkeypatch.setattr(rsi_email, "send_email_to_vips", send_email)

        result, out_args = rsi_email.event_to_vips_dps(**args)

        assert result is False
        assert out_args == args