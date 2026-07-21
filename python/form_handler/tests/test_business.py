"""
Unit tests for python.form_handler.business
"""
from __future__ import annotations

import pytest

import python.form_handler.business as business
import python.form_handler.actions as actions
import python.form_handler.rsi_email as rsi_email


class TestProcessIncomingForm:
    """Tests for process_incoming_form()"""

    @pytest.fixture(autouse=True)
    def _result(self):
        self.result = business.process_incoming_form()

    # -----------------------------------------------------------------------
    # Structure – top-level keys
    # -----------------------------------------------------------------------

    def test_returns_dict(self):
        assert isinstance(self.result, dict)

    def test_contains_all_expected_event_types(self):
        expected_keys = {"unknown_event", "vi", "24h", "12h", "irp"}
        assert expected_keys == set(self.result.keys())

    # -----------------------------------------------------------------------
    # Each pipeline is a non-empty list of step dicts
    # -----------------------------------------------------------------------

    @pytest.mark.parametrize("event_type", ["unknown_event", "vi", "24h", "12h", "irp"])
    def test_pipeline_is_non_empty_list(self, event_type):
        pipeline = self.result[event_type]
        assert isinstance(pipeline, list)
        assert len(pipeline) > 0

    @pytest.mark.parametrize("event_type", ["unknown_event", "vi", "24h", "12h", "irp"])
    def test_each_step_has_try_and_fail_keys(self, event_type):
        for step in self.result[event_type]:
            assert "try" in step, f"Step in '{event_type}' missing 'try' key: {step}"
            assert "fail" in step, f"Step in '{event_type}' missing 'fail' key: {step}"

    @pytest.mark.parametrize("event_type", ["unknown_event", "vi", "24h", "12h", "irp"])
    def test_each_step_try_is_callable(self, event_type):
        for step in self.result[event_type]:
            assert callable(step["try"]), (
                f"'try' in '{event_type}' step is not callable: {step['try']}"
            )

    @pytest.mark.parametrize("event_type", ["unknown_event", "vi", "24h", "12h", "irp"])
    def test_each_step_fail_is_list(self, event_type):
        for step in self.result[event_type]:
            assert isinstance(step["fail"], list), (
                f"'fail' in '{event_type}' step is not a list: {step['fail']}"
            )

    # -----------------------------------------------------------------------
    # Fail-handler steps also have the correct shape
    # -----------------------------------------------------------------------

    @pytest.mark.parametrize("event_type", ["vi", "24h", "12h", "irp"])
    def test_nested_fail_steps_have_try_and_fail_keys(self, event_type):
        for step in self.result[event_type]:
            for fail_step in step["fail"]:
                assert "try" in fail_step
                assert "fail" in fail_step
                assert callable(fail_step["try"])
                assert isinstance(fail_step["fail"], list)

    # -----------------------------------------------------------------------
    # Specific actions are wired correctly
    # -----------------------------------------------------------------------

    def test_vi_pipeline_starts_with_validate_retry_count(self):
        first_step = self.result["vi"][0]
        assert first_step["try"] is actions.validate_event_retry_count

    def test_24h_pipeline_starts_with_validate_retry_count(self):
        first_step = self.result["24h"][0]
        assert first_step["try"] is actions.validate_event_retry_count

    def test_12h_pipeline_starts_with_validate_retry_count(self):
        first_step = self.result["12h"][0]
        assert first_step["try"] is actions.validate_event_retry_count

    def test_irp_pipeline_starts_with_validate_retry_count(self):
        first_step = self.result["irp"][0]
        assert first_step["try"] is actions.validate_event_retry_count

    def test_unknown_event_first_step_is_add_error_to_message(self):
        first_step = self.result["unknown_event"][0]
        assert first_step["try"] is actions.add_unknown_event_error_to_message

    def test_vi_pipeline_contains_get_storage_ref_event_type(self):
        callables = [s["try"] for s in self.result["vi"]]
        assert actions.get_storage_ref_event_type in callables

    def test_vi_pipeline_contains_get_event_form_data(self):
        callables = [s["try"] for s in self.result["vi"]]
        assert actions.get_event_form_data in callables

    def test_vi_pipeline_contains_validate_event_data(self):
        callables = [s["try"] for s in self.result["vi"]]
        assert actions.validate_event_data in callables

    def test_vi_pipeline_contains_update_event_status(self):
        callables = [s["try"] for s in self.result["vi"]]
        assert actions.update_event_status in callables

    def test_24h_pipeline_contains_prep_icbc_payload(self):
        callables = [s["try"] for s in self.result["24h"]]
        assert actions.prep_icbc_payload in callables

    def test_24h_pipeline_contains_send_to_icbc(self):
        callables = [s["try"] for s in self.result["24h"]]
        assert actions.send_to_icbc in callables

    def test_12h_pipeline_contains_prep_icbc_payload(self):
        callables = [s["try"] for s in self.result["12h"]]
        assert actions.prep_icbc_payload in callables

    def test_12h_pipeline_contains_send_to_icbc(self):
        callables = [s["try"] for s in self.result["12h"]]
        assert actions.send_to_icbc in callables

    def test_irp_pipeline_does_not_contain_send_to_icbc(self):
        """IRP is sent via VIPS/email, not ICBC."""
        callables = [s["try"] for s in self.result["irp"]]
        assert actions.send_to_icbc not in callables

    def test_irp_pipeline_contains_event_to_vips_dps(self):
        callables = [s["try"] for s in self.result["irp"]]
        assert rsi_email.event_to_vips_dps in callables

    def test_vi_pipeline_contains_event_to_vips_dps(self):
        callables = [s["try"] for s in self.result["vi"]]
        assert rsi_email.event_to_vips_dps in callables

    # -----------------------------------------------------------------------
    # Retry / error actions in fail handlers
    # -----------------------------------------------------------------------

    @pytest.mark.parametrize("event_type", ["vi", "24h", "12h", "irp"])
    def test_retry_count_fail_handler_includes_add_to_retry_queue(self, event_type):
        """The first step's fail handler must enqueue for retry."""
        first_fail_steps = self.result[event_type][0]["fail"]
        callables = [s["try"] for s in first_fail_steps]
        assert actions.add_to_retry_queue in callables

    # -----------------------------------------------------------------------
    # Idempotency – each call returns a fresh dict
    # -----------------------------------------------------------------------

    def test_each_call_returns_independent_dict(self):
        result1 = business.process_incoming_form()
        result2 = business.process_incoming_form()
        assert result1 is not result2
        assert result1["vi"] is not result2["vi"]
