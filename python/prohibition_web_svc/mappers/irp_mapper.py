from datetime import datetime
from python.common.models import IRPForm, IRPASDTest


class IRPMapper:
    @staticmethod
    def map_to_irp_form(data, date_created):
        irp_form = IRPForm(
                created_dt=date_created,
                updated_dt=date_created,
                irp_number=data.get('IRP_number'),
                vi_number=data.get('VI_number'),
                driver_licence_expiry=datetime.strptime(
                    data.get('driver_licence_expiry'), "%Y-%m-%dT%H:%M:%S.%f%z") if data.get('driver_licence_expiry') else None,
                driver_licence_class=data.get('driver_licence_class'),
                gender=data.get('gender').get('value') if data.get('gender') else None,
                driver_licence_seized=data.get('seized_DL'),
                vehicle_impounded=data.get('VI', False),
                irp_prohibition_type=data.get('irp_impound_duration'),
                witnessed_by_officer=data.get('irp_reason_grounds').get('witnessedByOfficer') if data.get('irp_reason_grounds') else False ,
                admission_by_driver=data.get('irp_reason_grounds').get('admissionByDriver') if data.get('irp_reason_grounds') else False,
                independent_witness=data.get('irp_reason_grounds').get('independentWitness') if data.get('irp_reason_grounds') else False,
                reasonable_ground_other=data.get('irp_reason_grounds').get('other') if data.get('irp_reason_grounds') else False,
                time_of_suspicion=data.get('time_suspicion_formed'),
                time_of_asd=data.get('time_ASD_demand'),
                refused_or_fail=data.get('driver_refuse_breath_sample'),
                time_of_refusal=data.get('time_breath_sample_refusal'),
                right_to_second_test=data.get('irp_right_2nd_test'),
                lower_asd_prevail=data.get('irp_lower_test_prevail'),
                right_to_test_different_asd=data.get('irp_right_different_asd'),
                driver_requested_second_asd=data.get('irp_driver_request_2nd_test'),
                reasonable_suspicion_odor_of_liquor=data.get('grounds_for_reasonable_suspicion').get('odorOnBreath') if data.get('grounds_for_reasonable_suspicion') else False,
                reasonable_suspicion_admission=data.get('grounds_for_reasonable_suspicion').get('admissionByDriver') if data.get('grounds_for_reasonable_suspicion') else False,
                reasonable_suspicion_witnessed=data.get('grounds_for_reasonable_suspicion').get('witnessedConsumption') if data.get('grounds_for_reasonable_suspicion') else False,
                reasonable_suspicion_other=data.get('grounds_for_reasonable_suspicion').get('other') if data.get('grounds_for_reasonable_suspicion') else False,
                last_drink=data.get('last_drink'),
                continuous_observation=data.get('driver_continuously_observed'),
                asd_tests = IRPMapper.map_to_irp_asd_test(data)
            )
        return irp_form

    @staticmethod
    def map_to_irp_asd_test(data):
        asd_test = []
        if data.get('irp_time_1st_test'):
            asd_test.append(IRPASDTest(
                test_number=1,
                asd_identification=data.get('irp_asd_identification_1st_test'),
                serial_number=data.get('irp_serial_1st_test'),
                test_time=data.get('irp_time_1st_test'),
                result=data.get('irp_result_1st_test'),
                result_shown_to_driver=data.get('irp_result_shown_driver_1st_test'),
            ))
        if data.get('irp_time_2nd_test'):
            asd_test.append(IRPASDTest(
                test_number=2,
                asd_identification=data.get('irp_asd_identification_2nd_test'),
                serial_number=data.get('irp_serial_2nd_test'),
                test_time=data.get('irp_time_2nd_test'),
                result=data.get('irp_result_2nd_test'),
                result_shown_to_driver=data.get('irp_result_shown_driver_2nd_test'),
            ))

        return asd_test