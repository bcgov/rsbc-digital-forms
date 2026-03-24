import json
import os
from datetime import datetime

from python.prohibition_web_svc.mappers.irp_mapper import IRPMapper
from python.common.models import IRPForm, IRPASDTest


def get_payload():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    irp_json_path = os.path.join(test_dir, '..', 'tests-data', 'irp.json')
    with open(irp_json_path) as f:
        return json.load(f)


DATE_CREATED = datetime(2026, 3, 24, 7, 0, 0)


class TestMapToIrpForm:

    def test_returns_irp_form_instance(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert isinstance(result, IRPForm)

    def test_irp_number(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.irp_number == "1234"

    def test_vi_number(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.vi_number == 221110893

    def test_created_and_updated_dt(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.created_dt == DATE_CREATED
        assert result.updated_dt == DATE_CREATED

    def test_driver_licence_expiry_is_parsed(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.driver_licence_expiry is not None
        assert result.driver_licence_expiry.year == 2028
        assert result.driver_licence_expiry.month == 4
        assert result.driver_licence_expiry.day == 13

    def test_driver_licence_class(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.driver_licence_class == "5"

    def test_gender(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.gender == "M"

    def test_driver_licence_seized(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.driver_licence_seized == "YES"

    def test_vehicle_impounded(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.vehicle_impounded is True

    def test_irp_prohibition_type(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.irp_prohibition_type == "BACWARN30"

    def test_irp_reason_grounds_witnessed_by_officer(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.witnessed_by_officer is True

    def test_irp_reason_grounds_admission_by_driver(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.admission_by_driver is True

    def test_irp_reason_grounds_independent_witness(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.independent_witness is True

    def test_irp_reason_grounds_other(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.reasonable_ground_other is True

    def test_time_of_suspicion(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.time_of_suspicion == "07:06"

    def test_time_of_asd(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.time_of_asd == "07:08"

    def test_refused_or_fail(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.refused_or_fail == "NO"

    def test_time_of_refusal_is_none(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.time_of_refusal is None

    def test_right_to_second_test(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.right_to_second_test == "YES"

    def test_lower_asd_prevail(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.lower_asd_prevail == "YES"

    def test_right_to_test_different_asd(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.right_to_test_different_asd == "YES"

    def test_driver_requested_second_asd(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.driver_requested_second_asd == "YES"

    def test_reasonable_suspicion_odor_of_liquor(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.reasonable_suspicion_odor_of_liquor is True

    def test_reasonable_suspicion_admission(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.reasonable_suspicion_admission is True

    def test_reasonable_suspicion_witnessed(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.reasonable_suspicion_witnessed is True

    def test_reasonable_suspicion_other(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.reasonable_suspicion_other is True

    def test_last_drink(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.last_drink == "do not remember"

    def test_continuous_observation(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.continuous_observation == "NO"

    def test_asd_tests_count(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert len(result.asd_tests) == 2


class TestMapToIrpAsdTest:

    def test_returns_list(self):
        result = IRPMapper.map_to_irp_asd_test(get_payload())
        assert isinstance(result, list)

    def test_two_tests_mapped(self):
        result = IRPMapper.map_to_irp_asd_test(get_payload())
        assert len(result) == 2

    def test_first_test_is_irp_asd_test_instance(self):
        result = IRPMapper.map_to_irp_asd_test(get_payload())
        assert isinstance(result[0], IRPASDTest)

    def test_first_test_number(self):
        result = IRPMapper.map_to_irp_asd_test(get_payload())
        assert result[0].test_number == 1

    def test_first_test_asd_identification(self):
        result = IRPMapper.map_to_irp_asd_test(get_payload())
        assert result[0].asd_identification == "alco-sensor"

    def test_first_test_serial_number(self):
        result = IRPMapper.map_to_irp_asd_test(get_payload())
        assert result[0].serial_number == "533455"

    def test_first_test_time(self):
        result = IRPMapper.map_to_irp_asd_test(get_payload())
        assert result[0].test_time == "07:09"

    def test_first_test_result(self):
        result = IRPMapper.map_to_irp_asd_test(get_payload())
        assert result[0].result == "WARN"

    def test_first_test_result_shown_to_driver(self):
        result = IRPMapper.map_to_irp_asd_test(get_payload())
        assert result[0].result_shown_to_driver == "YES"

    def test_second_test_number(self):
        result = IRPMapper.map_to_irp_asd_test(get_payload())
        assert result[1].test_number == 2

    def test_second_test_asd_identification(self):
        result = IRPMapper.map_to_irp_asd_test(get_payload())
        assert result[1].asd_identification == "alcotest-6000"

    def test_second_test_serial_number(self):
        result = IRPMapper.map_to_irp_asd_test(get_payload())
        assert result[1].serial_number == "3345777"

    def test_second_test_time(self):
        result = IRPMapper.map_to_irp_asd_test(get_payload())
        assert result[1].test_time == "07:10"

    def test_second_test_result(self):
        result = IRPMapper.map_to_irp_asd_test(get_payload())
        assert result[1].result == "WARN"

    def test_second_test_result_shown_to_driver(self):
        result = IRPMapper.map_to_irp_asd_test(get_payload())
        assert result[1].result_shown_to_driver == "YES"


class TestMapToIrpFormEdgeCases:

    def test_missing_gender_returns_none(self):
        payload = get_payload()
        del payload['gender']
        result = IRPMapper.map_to_irp_form(payload, DATE_CREATED)
        assert result.gender is None

    def test_missing_irp_reason_grounds_defaults_to_false(self):
        payload = get_payload()
        del payload['irp_reason_grounds']
        result = IRPMapper.map_to_irp_form(payload, DATE_CREATED)
        assert result.witnessed_by_officer is False
        assert result.admission_by_driver is False
        assert result.independent_witness is False
        assert result.reasonable_ground_other is False

    def test_missing_grounds_for_reasonable_suspicion_defaults_to_false(self):
        payload = get_payload()
        del payload['grounds_for_reasonable_suspicion']
        result = IRPMapper.map_to_irp_form(payload, DATE_CREATED)
        assert result.reasonable_suspicion_odor_of_liquor is False
        assert result.reasonable_suspicion_admission is False
        assert result.reasonable_suspicion_witnessed is False
        assert result.reasonable_suspicion_other is False

    def test_missing_driver_licence_expiry_returns_none(self):
        payload = get_payload()
        payload['driver_licence_expiry'] = None
        result = IRPMapper.map_to_irp_form(payload, DATE_CREATED)
        assert result.driver_licence_expiry is None

    def test_no_asd_tests_when_times_absent(self):
        payload = get_payload()
        del payload['irp_time_1st_test']
        del payload['irp_time_2nd_test']
        result = IRPMapper.map_to_irp_asd_test(payload)
        assert result == []

    def test_only_first_asd_test_when_second_time_absent(self):
        payload = get_payload()
        del payload['irp_time_2nd_test']
        result = IRPMapper.map_to_irp_asd_test(payload)
        assert len(result) == 1
        assert result[0].test_number == 1
