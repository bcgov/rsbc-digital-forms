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

    def test_vi_number_is_none_when_vi_is_false(self):
        payload = get_payload()
        payload['VI'] = False
        payload['VI_number'] = 221110893
        result = IRPMapper.map_to_irp_form(payload, DATE_CREATED)
        assert result.vi_number is None

    def test_vi_number_is_none_when_vi_is_missing(self):
        payload = get_payload()
        del payload['VI']
        payload['VI_number'] = 221110893
        result = IRPMapper.map_to_irp_form(payload, DATE_CREATED)
        assert result.vi_number is None

    def test_created_and_updated_dt(self):
        result = IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)
        assert result.created_dt == DATE_CREATED
        assert result.updated_dt == DATE_CREATED

    def test_driver_licence_expiry_year_is_mapped(self):
        payload = get_payload()
        payload['driver_licence_expiry_year'] = 2028
        result = IRPMapper.map_to_irp_form(payload, DATE_CREATED)
        assert result.driver_licence_expiry_year == 2028

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

    def test_first_test_not_mapped_when_required_field_missing(self):
        payload = get_payload()
        payload['irp_result_1st_test'] = None
        result = IRPMapper.map_to_irp_asd_test(payload)
        assert len(result) == 1
        assert result[0].test_number == 2

    def test_second_test_not_mapped_when_required_field_missing(self):
        payload = get_payload()
        payload['irp_asd_identification_2nd_test'] = None
        result = IRPMapper.map_to_irp_asd_test(payload)
        assert len(result) == 1
        assert result[0].test_number == 1


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

    def test_missing_driver_licence_expiry_year_returns_none(self):
        payload = get_payload()
        payload['driver_licence_expiry_year'] = None
        result = IRPMapper.map_to_irp_form(payload, DATE_CREATED)
        assert result.driver_licence_expiry_year is None

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

    def test_empty_optional_fields_are_mapped_to_none(self):
        payload = get_payload()
        payload['driver_licence_class'] = ''
        payload['time_suspicion_formed'] = ''
        payload['time_ASD_demand'] = ''
        payload['driver_refuse_breath_sample'] = ''
        payload['time_breath_sample_refusal'] = ''
        payload['irp_right_2nd_test'] = ''
        payload['irp_lower_test_prevail'] = ''
        payload['irp_right_different_asd'] = ''
        payload['irp_driver_request_2nd_test'] = ''
        payload['last_drink'] = ''
        payload['driver_continuously_observed'] = ''

        result = IRPMapper.map_to_irp_form(payload, DATE_CREATED)

        assert result.driver_licence_class is None
        assert result.time_of_suspicion is None
        assert result.time_of_asd is None
        assert result.refused_or_fail is None
        assert result.time_of_refusal is None
        assert result.right_to_second_test is None
        assert result.lower_asd_prevail is None
        assert result.right_to_test_different_asd is None
        assert result.driver_requested_second_asd is None
        assert result.last_drink is None
        assert result.continuous_observation is None


class TestMapUpdateIrpForm:
    """Tests for IRPMapper.map_update_irp_form — mutates an existing IRPForm in place."""

    def _base_form(self):
        """Return an IRPForm pre-populated from the standard fixture."""
        return IRPMapper.map_to_irp_form(get_payload(), DATE_CREATED)

    # ── return value ────────────────────────────────────────────────────────

    def test_returns_none(self):
        IRPMapper.map_update_irp_form(self._base_form(), get_payload())

    # ── scalar field updates ─────────────────────────────────────────────────

    def test_updates_irp_number(self):
        form = self._base_form()
        data = get_payload()
        data['IRP_number'] = 'NEW-IRP'
        IRPMapper.map_update_irp_form(form, data)
        assert form.irp_number == 'NEW-IRP'

    def test_updates_vi_number(self):
        form = self._base_form()
        data = get_payload()
        data['VI_number'] = 999888777
        IRPMapper.map_update_irp_form(form, data)
        assert form.vi_number == 999888777

    def test_updates_vi_number_to_none_when_vi_is_false(self):
        form = self._base_form()
        data = get_payload()
        data['VI'] = False
        data['VI_number'] = 999888777
        IRPMapper.map_update_irp_form(form, data)
        assert form.vi_number is None

    def test_updates_vi_number_to_none_when_vi_is_missing(self):
        form = self._base_form()
        data = get_payload()
        del data['VI']
        data['VI_number'] = 999888777
        IRPMapper.map_update_irp_form(form, data)
        assert form.vi_number is None

    def test_updates_driver_licence_expiry_year(self):
        form = self._base_form()
        data = get_payload()
        data['driver_licence_expiry_year'] = 2030
        IRPMapper.map_update_irp_form(form, data)
        assert form.driver_licence_expiry_year == 2030

    def test_updates_driver_licence_expiry_year_to_none_when_absent(self):
        form = self._base_form()
        data = get_payload()
        data['driver_licence_expiry_year'] = None
        IRPMapper.map_update_irp_form(form, data)
        assert form.driver_licence_expiry_year is None

    def test_updates_driver_licence_class(self):
        form = self._base_form()
        data = get_payload()
        data['driver_licence_class'] = '7'
        IRPMapper.map_update_irp_form(form, data)
        assert form.driver_licence_class == '7'

    def test_updates_driver_licence_class_to_none_when_empty(self):
        form = self._base_form()
        data = get_payload()
        data['driver_licence_class'] = ''
        IRPMapper.map_update_irp_form(form, data)
        assert form.driver_licence_class is None

    def test_updates_gender(self):
        form = self._base_form()
        data = get_payload()
        data['gender'] = {'value': 'F', 'label': 'Female'}
        IRPMapper.map_update_irp_form(form, data)
        assert form.gender == 'F'

    def test_updates_gender_to_none_when_absent(self):
        form = self._base_form()
        data = get_payload()
        data['gender'] = None
        IRPMapper.map_update_irp_form(form, data)
        assert form.gender is None

    def test_updates_driver_licence_seized(self):
        form = self._base_form()
        data = get_payload()
        data['seized_DL'] = 'NO'
        IRPMapper.map_update_irp_form(form, data)
        assert form.driver_licence_seized == 'NO'

    def test_updates_vehicle_impounded(self):
        form = self._base_form()
        data = get_payload()
        data['VI'] = False
        IRPMapper.map_update_irp_form(form, data)
        assert form.vehicle_impounded is False

    def test_vehicle_impounded_defaults_to_false_when_absent(self):
        form = self._base_form()
        data = get_payload()
        del data['VI']
        IRPMapper.map_update_irp_form(form, data)
        assert form.vehicle_impounded is False

    def test_updates_irp_prohibition_type(self):
        form = self._base_form()
        data = get_payload()
        data['irp_impound_duration'] = 'BACWARN90'
        IRPMapper.map_update_irp_form(form, data)
        assert form.irp_prohibition_type == 'BACWARN90'

    # ── irp_reason_grounds ───────────────────────────────────────────────────

    def test_updates_irp_reason_grounds_fields(self):
        form = self._base_form()
        data = get_payload()
        data['irp_reason_grounds'] = {
            'witnessedByOfficer': False,
            'admissionByDriver': False,
            'independentWitness': True,
            'other': False,
        }
        IRPMapper.map_update_irp_form(form, data)
        assert form.witnessed_by_officer is False
        assert form.admission_by_driver is False
        assert form.independent_witness is True
        assert form.reasonable_ground_other is False

    def test_irp_reason_grounds_defaults_to_false_when_absent(self):
        form = self._base_form()
        data = get_payload()
        data['irp_reason_grounds'] = None
        IRPMapper.map_update_irp_form(form, data)
        assert form.witnessed_by_officer is False
        assert form.admission_by_driver is False
        assert form.independent_witness is False
        assert form.reasonable_ground_other is False

    # ── time / optional fields ───────────────────────────────────────────────

    def test_updates_time_of_suspicion(self):
        form = self._base_form()
        data = get_payload()
        data['time_suspicion_formed'] = '08:30'
        IRPMapper.map_update_irp_form(form, data)
        assert form.time_of_suspicion == '08:30'

    def test_updates_time_of_suspicion_to_none_when_empty(self):
        form = self._base_form()
        data = get_payload()
        data['time_suspicion_formed'] = ''
        IRPMapper.map_update_irp_form(form, data)
        assert form.time_of_suspicion is None

    def test_updates_time_of_asd(self):
        form = self._base_form()
        data = get_payload()
        data['time_ASD_demand'] = '09:00'
        IRPMapper.map_update_irp_form(form, data)
        assert form.time_of_asd == '09:00'

    def test_updates_refused_or_fail(self):
        form = self._base_form()
        data = get_payload()
        data['driver_refuse_breath_sample'] = 'YES'
        IRPMapper.map_update_irp_form(form, data)
        assert form.refused_or_fail == 'YES'

    def test_updates_time_of_refusal(self):
        form = self._base_form()
        data = get_payload()
        data['time_breath_sample_refusal'] = '09:15'
        IRPMapper.map_update_irp_form(form, data)
        assert form.time_of_refusal == '09:15'

    def test_updates_right_to_second_test(self):
        form = self._base_form()
        data = get_payload()
        data['irp_right_2nd_test'] = 'NO'
        IRPMapper.map_update_irp_form(form, data)
        assert form.right_to_second_test == 'NO'

    def test_updates_lower_asd_prevail(self):
        form = self._base_form()
        data = get_payload()
        data['irp_lower_test_prevail'] = 'NO'
        IRPMapper.map_update_irp_form(form, data)
        assert form.lower_asd_prevail == 'NO'

    def test_updates_right_to_test_different_asd(self):
        form = self._base_form()
        data = get_payload()
        data['irp_right_different_asd'] = 'NO'
        IRPMapper.map_update_irp_form(form, data)
        assert form.right_to_test_different_asd == 'NO'

    def test_updates_driver_requested_second_asd(self):
        form = self._base_form()
        data = get_payload()
        data['irp_driver_request_2nd_test'] = 'NO'
        IRPMapper.map_update_irp_form(form, data)
        assert form.driver_requested_second_asd == 'NO'

    def test_updates_last_drink(self):
        form = self._base_form()
        data = get_payload()
        data['last_drink'] = 'one hour ago'
        IRPMapper.map_update_irp_form(form, data)
        assert form.last_drink == 'one hour ago'

    def test_updates_continuous_observation(self):
        form = self._base_form()
        data = get_payload()
        data['driver_continuously_observed'] = 'YES'
        IRPMapper.map_update_irp_form(form, data)
        assert form.continuous_observation == 'YES'

    # ── grounds_for_reasonable_suspicion ────────────────────────────────────

    def test_updates_reasonable_suspicion_fields(self):
        form = self._base_form()
        data = get_payload()
        data['grounds_for_reasonable_suspicion'] = {
            'odorOnBreath': False,
            'admissionByDriver': True,
            'witnessedConsumption': False,
            'other': True,
        }
        IRPMapper.map_update_irp_form(form, data)
        assert form.reasonable_suspicion_odor_of_liquor is False
        assert form.reasonable_suspicion_admission is True
        assert form.reasonable_suspicion_witnessed is False
        assert form.reasonable_suspicion_other is True

    def test_reasonable_suspicion_defaults_to_false_when_absent(self):
        form = self._base_form()
        data = get_payload()
        data['grounds_for_reasonable_suspicion'] = None
        IRPMapper.map_update_irp_form(form, data)
        assert form.reasonable_suspicion_odor_of_liquor is False
        assert form.reasonable_suspicion_admission is False
        assert form.reasonable_suspicion_witnessed is False
        assert form.reasonable_suspicion_other is False

    def test_empty_optional_fields_updated_to_none(self):
        form = self._base_form()
        data = get_payload()
        for key in ('driver_licence_class', 'time_suspicion_formed', 'time_ASD_demand',
                    'driver_refuse_breath_sample', 'time_breath_sample_refusal',
                    'irp_right_2nd_test', 'irp_lower_test_prevail', 'irp_right_different_asd',
                    'irp_driver_request_2nd_test', 'last_drink', 'driver_continuously_observed'):
            data[key] = ''
        IRPMapper.map_update_irp_form(form, data)
        assert form.driver_licence_class is None
        assert form.time_of_suspicion is None
        assert form.time_of_asd is None
        assert form.refused_or_fail is None
        assert form.time_of_refusal is None
        assert form.right_to_second_test is None
        assert form.lower_asd_prevail is None
        assert form.right_to_test_different_asd is None
        assert form.driver_requested_second_asd is None
        assert form.last_drink is None
        assert form.continuous_observation is None

    # ── ASD test update logic ────────────────────────────────────────────────

    def test_asd_test1_updated_in_place_when_existing(self):
        """When asd_tests already has a first entry, it is mutated rather than appended."""
        form = self._base_form()   # starts with 2 ASD tests
        assert len(form.asd_tests) == 2
        data = get_payload()
        data['irp_asd_identification_1st_test'] = 'new-sensor'
        data['irp_serial_1st_test'] = 'SER-001'
        data['irp_time_1st_test'] = '10:00'
        data['irp_result_1st_test'] = 'FAIL'
        data['irp_result_shown_driver_1st_test'] = 'NO'
        IRPMapper.map_update_irp_form(form, data)
        assert len(form.asd_tests) == 2          # no new entry added
        assert form.asd_tests[0].asd_identification == 'new-sensor'
        assert form.asd_tests[0].serial_number == 'SER-001'
        assert form.asd_tests[0].test_time == '10:00'
        assert form.asd_tests[0].result == 'FAIL'
        assert form.asd_tests[0].result_shown_to_driver == 'NO'

    def test_asd_test1_appended_when_no_existing_tests(self):
        """When asd_tests is empty, a new IRPASDTest is appended for test 1."""
        form = self._base_form()
        form.asd_tests = []          # clear existing tests
        data = get_payload()
        IRPMapper.map_update_irp_form(form, data)
        assert len(form.asd_tests) >= 1
        assert isinstance(form.asd_tests[0], IRPASDTest)
        assert form.asd_tests[0].test_number == 1
        assert form.asd_tests[0].asd_identification == data['irp_asd_identification_1st_test']

    def test_asd_test1_not_updated_when_data_incomplete(self):
        """Missing any of the 5 required 1st-test fields → asd_tests[0] is untouched."""
        form = self._base_form()
        original_id = form.asd_tests[0].asd_identification
        data = get_payload()
        data['irp_result_1st_test'] = None       # break the guard condition
        IRPMapper.map_update_irp_form(form, data)
        assert form.asd_tests[0].asd_identification == original_id

    def test_asd_test2_updated_in_place_when_two_existing(self):
        """When asd_tests already has two entries, the second is mutated."""
        form = self._base_form()   # starts with 2 ASD tests
        data = get_payload()
        data['irp_asd_identification_2nd_test'] = 'updated-sensor'
        data['irp_serial_2nd_test'] = 'SER-002'
        data['irp_time_2nd_test'] = '11:00'
        data['irp_result_2nd_test'] = 'PASS'
        data['irp_result_shown_driver_2nd_test'] = 'NO'
        IRPMapper.map_update_irp_form(form, data)
        assert len(form.asd_tests) == 2
        assert form.asd_tests[1].asd_identification == 'updated-sensor'
        assert form.asd_tests[1].serial_number == 'SER-002'
        assert form.asd_tests[1].test_time == '11:00'
        assert form.asd_tests[1].result == 'PASS'
        assert form.asd_tests[1].result_shown_to_driver == 'NO'

    def test_asd_test2_appended_when_only_one_existing_test(self):
        """When only one ASD test exists, the second is appended."""
        form = self._base_form()
        form.asd_tests = form.asd_tests[:1]   # keep only the first test
        assert len(form.asd_tests) == 1
        data = get_payload()
        IRPMapper.map_update_irp_form(form, data)
        assert len(form.asd_tests) == 2
        assert isinstance(form.asd_tests[1], IRPASDTest)
        assert form.asd_tests[1].test_number == 2
        assert form.asd_tests[1].asd_identification == data['irp_asd_identification_2nd_test']

    def test_asd_test2_not_updated_when_data_incomplete(self):
        """Missing any of the 5 required 2nd-test fields → asd_tests[1] is untouched."""
        form = self._base_form()
        original_id = form.asd_tests[1].asd_identification
        data = get_payload()
        data['irp_result_2nd_test'] = None       # break the guard condition
        IRPMapper.map_update_irp_form(form, data)
        assert form.asd_tests[1].asd_identification == original_id

    def test_no_asd_tests_appended_when_both_incomplete(self):
        """No tests added when neither test's required fields are present."""
        form = self._base_form()
        form.asd_tests = []
        data = get_payload()
        data['irp_time_1st_test'] = None
        data['irp_time_2nd_test'] = None
        IRPMapper.map_update_irp_form(form, data)
        assert len(form.asd_tests) == 0
