from python.common.models import TarCollision, TarLocation, TarAdditionalCollisionDetails, TarWitnessInfo, TarEntity, TarInvolvedPerson, TarCharges
from python.prohibition_web_svc.models.collision_request_payload import CollisionRequestPayload


class CollisionMapper:
    @staticmethod
    def map_to_tar_collision(collision_request_payload: CollisionRequestPayload) -> TarCollision:
        """
        Maps a CollisionRequestPayload to a TarCollision object.
        """
        tar_collision = TarCollision(
            collision_case_num = collision_request_payload.get('collision_case_num'),
            collision_scenario = collision_request_payload.get('collision_scenario'),
            police_file_num = collision_request_payload.get('police_file_num'),
            prime_file_vjur = collision_request_payload.get('prime_file_vjur'),
            police_file_prefix = collision_request_payload.get('police_file_prefix', None),
            date_collision = collision_request_payload.get('date_collision'),
            time_collision = collision_request_payload.get('time_collision'),
            reported_same_day = collision_request_payload.get('reported_same_day'),
            time_collision_unknown = collision_request_payload.get('time_collision_unknown'),
            date_reported = collision_request_payload.get('date_reported'),
            hit_and_run = collision_request_payload.get('hit_and_run'),
            police_attended = collision_request_payload.get('police_attended'),
            police_agency_code = collision_request_payload.get('police_agency_code'),
            police_zone = collision_request_payload.get('police_zone', None),
            primary_collision_occ_code = collision_request_payload.get('primary_collision_occ_code'),
            first_contact_event = collision_request_payload.get('first_contact_event'),
            first_contact_loc = collision_request_payload.get('first_contact_loc'),
            has_countable_fatal = collision_request_payload.get('has_countable_fatal'),
            countable_fatal_total = collision_request_payload.get('countable_fatal_total'),
            completed_by_name = collision_request_payload.get('completed_by_name'),
            completed_by_id = collision_request_payload.get('completed_by_id'),
            detachment_unit = collision_request_payload.get('detachment_unit'),
            icbc_submission_date = collision_request_payload.get('icbc_submission_date', None),
            reviewed_by = collision_request_payload.get('reviewed_by', None),
            investigated_by_traffic_analyst = collision_request_payload.get('investigated_by_traffic_analyst'),
            location=CollisionMapper.map_to_tar_location(collision_request_payload),
            additional_details=CollisionMapper.map_to_tar_additional_details(collision_request_payload),
            witnesses=CollisionMapper.map_to_tar_witnesses(collision_request_payload),
            entities=CollisionMapper.map_to_tar_entities(collision_request_payload)
        )
        return tar_collision

    @staticmethod
    def map_to_tar_location(collision_request_payload: CollisionRequestPayload) -> TarLocation:
        """
        Maps the location part of CollisionRequestPayload to a TarLocation object.
        """
        return TarLocation(
            collision_case_num = collision_request_payload['collision_case_num'],
            hwy_code = collision_request_payload['hwy_code'],
            hwy_route_num = collision_request_payload.get('hwy_route_num', None),
            segment_num = collision_request_payload.get('segment_num', None),
            loc_code_km = collision_request_payload.get('loc_code_km', None),
            city_name = collision_request_payload['city_name'],
            city_status = collision_request_payload.get('city_status', None),
            street_on = collision_request_payload.get('street_on', None),
            street_at = collision_request_payload.get('street_at', None),
            street_desc = collision_request_payload.get('street_desc', None),
            gps_format = collision_request_payload.get('gps_format', None),
            lat_decim_degrees = collision_request_payload['lat_decim_degrees'],
            long_decim_degrees = collision_request_payload['long_decim_degrees'],
            lat_degree = collision_request_payload.get('lat_degree', None),
            lat_min = collision_request_payload.get('lat_min', None),
            lat_sec = collision_request_payload.get('lat_sec', None),
            long_degree = collision_request_payload.get('long_degree', None),
            long_min = collision_request_payload.get('long_min', None),
            long_sec = collision_request_payload.get('long_sec', None),
            road_class = collision_request_payload['road_class'],
            traffic_flow = collision_request_payload['traffic_flow'],
            collision_loc = collision_request_payload['collision_loc'],
            primary_speed_zone = collision_request_payload['primary_speed_zone'],
            secondary_speed_zone = collision_request_payload.get('secondary_speed_zone', None),
            land_usage = collision_request_payload['land_usage'],
            road_type = collision_request_payload['road_type'],
            traffic_control = collision_request_payload.get('traffic_control', None),
            roadway_character = collision_request_payload['roadway_character'],
            roadway_surface_cond = collision_request_payload['roadway_surface_cond'],
            weather_cond = collision_request_payload['weather_cond'],
            lighting_cond = collision_request_payload['lighting_cond'],
        )

    @staticmethod
    def map_to_tar_additional_details(collision_request_payload: CollisionRequestPayload) -> TarAdditionalCollisionDetails:
        """
        Maps the additional details part of CollisionRequestPayload to a TarAdditionalCollisionDetails object.
        """
        return TarAdditionalCollisionDetails(
            pedestrian_location=collision_request_payload.get('pedestrian_location', None),
            pedestrian_action=collision_request_payload.get('pedestrian_action', None),
            has_other_prop_damage=collision_request_payload['has_other_prop_damage'],
            other_prop_damage_desc=collision_request_payload.get('other_prop_damage_desc', None),
            prop_damage_est_value=collision_request_payload.get('prop_damage_est_value', None),
            has_witnesses=collision_request_payload['has_witnesses'],
            police_comments=collision_request_payload.get('police_comments', None),
            collision_type=collision_request_payload['collision_type'],
            total_est_damage=collision_request_payload['total_est_damage'],
            total_injured=collision_request_payload['total_injured'],
            total_killed=collision_request_payload['total_killed'],
            total_vehicles=collision_request_payload['total_vehicles'],
            summary_was_verified=collision_request_payload['summary_was_verified']
        )

    @staticmethod
    def map_to_tar_witnesses(collision_request_payload: CollisionRequestPayload) -> list:
        """
        Maps the witnesses part of CollisionRequestPayload to a list of TarWitnessInfo objects.
        """
        result = []
        for witness in collision_request_payload.get('witnesses', []):
            tar_witness = TarWitnessInfo(
            collision_case_num=witness.get('collision_case_num'),
            witness_name=witness.get('witness_name'),
            address=witness.get('address'),
            contact_phn_num=witness.get('contact_phn_num')
            )
            result.append(tar_witness)
        return result
    
    @staticmethod
    def map_to_tar_involved_person(person_data: dict) -> TarInvolvedPerson:
        """
        Maps a person dictionary to a TarInvolvedPerson object field by field.
        """
        return TarInvolvedPerson(
            status=person_data.get('status'),
            surname=person_data.get('surname'),
            given_name=person_data.get('given_name'),
            vehicle_occupied=person_data.get('vehicle_occupied'),
            position_of_person=person_data.get('position_of_person'),
            safety_equipment_used=person_data.get('safety_equipment_used'),
            ejection_from_vehicle=person_data.get('ejection_from_vehicle'),
            age=person_data.get('age'),
            sex=person_data.get('sex'),
            severe_injury_location=person_data.get('severe_injury_location'),
            injury_type=person_data.get('injury_type'),
            consciousness_state=person_data.get('consciousness_state'),
            injured_taken_to=person_data.get('injured_taken_to'),
            injured_taken_by=person_data.get('injured_taken_by'),
            injury_classification=person_data.get('injury_classification'),
            date_of_death=person_data.get('date_of_death')
        )
    
    @staticmethod
    def map_to_tar_charges(charge_data: dict) -> TarCharges:
        """
        Maps a charge dictionary to a TarCharges object field by field.
        """
        return TarCharges(
            charge_id=charge_data.get('charge_id'),
            charge_type=charge_data.get('charge_type'),
            section_num=charge_data.get('section_num'),
            offence_title=charge_data.get('offence_title')
        )
    
    @staticmethod
    def map_to_tar_entity(entity_data: dict) -> TarEntity:
        """
        Maps an entity dictionary to a TarEntity object field by field.
        """
        return TarEntity(
            collision_case_num=entity_data.get('collision_case_num'),
            entity_type=entity_data.get('entity_type'),
            entity_num=entity_data.get('entity_num'),
            possible_offender=entity_data.get('possible_offender'),
            vehicle_parked=entity_data.get('vehicle_parked'),
            unknown_entity=entity_data.get('unknown_entity'),
            driver_license_num=entity_data.get('driver_license_num'),
            license_prov_state=entity_data.get('license_prov_state'),
            license_expiry=entity_data.get('license_expiry'),
            surname=entity_data.get('surname'),
            given_name=entity_data.get('given_name'),
            license_class=entity_data.get('license_class'),
            graduated_license_type=entity_data.get('graduated_license_type'),
            residential_address=entity_data.get('residential_address'),
            business_address=entity_data.get('business_address'),
            business_phone_num=entity_data.get('business_phone_num'),
            date_of_birth=entity_data.get('date_of_birth'),
            age_at_collision=entity_data.get('age_at_collision'),
            contact_phone_num=entity_data.get('contact_phone_num'),
            sex=entity_data.get('sex'),
            contributing_factor_1=entity_data.get('contributing_factor_1'),
            contributing_factor_2=entity_data.get('contributing_factor_2'),
            contributing_factor_3=entity_data.get('contributing_factor_3'),
            contributing_factor_4=entity_data.get('contributing_factor_4'),
            charges_blood_alc_tests_taken=entity_data.get('charges_blood_alc_tests_taken'),
            blood_alc_test=entity_data.get('blood_alc_test'),
            result_1=entity_data.get('result_1'),
            result_2=entity_data.get('result_2'),
            vehicle_plate_num=entity_data.get('vehicle_plate_num'),
            vehicle_plate_prov_state=entity_data.get('vehicle_plate_prov_state'),
            vehicle_year=entity_data.get('vehicle_year'),
            vehicle_make=entity_data.get('vehicle_make'),
            vehicle_style=entity_data.get('vehicle_style'),
            vehicle_colour=entity_data.get('vehicle_colour'),
            trailer_towed_plate_num=entity_data.get('trailer_towed_plate_num'),
            trailer_towed_plate_prov_state=entity_data.get('trailer_towed_plate_prov_state'),
            is_registered_owner=entity_data.get('is_registered_owner'),
            vehicle_owner_name=entity_data.get('vehicle_owner_name'),
            vehicle_owner_address=entity_data.get('vehicle_owner_address'),
            nsc_num=entity_data.get('nsc_num'),
            jur_code=entity_data.get('jur_code'),
            damage_location_code=entity_data.get('damage_location_code'),
            severety_code=entity_data.get('severety_code'),
            estimated_vehicle_damage=entity_data.get('estimated_vehicle_damage'),
            vehicle_stolen=entity_data.get('vehicle_stolen'),
            vehicle_towed=entity_data.get('vehicle_towed'),
            vehicle_towed_by=entity_data.get('vehicle_towed_by'),
            dir_of_travel=entity_data.get('dir_of_travel'),
            entity_street=entity_data.get('entity_street'),
            insurance_coverage=entity_data.get('insurance_coverage'),
            other_insurer=entity_data.get('other_insurer'),
            other_insurance_policy_num=entity_data.get('other_insurance_policy_num'),
            second_contact=entity_data.get('second_contact'),
            pre_collision_vehicle_action_first_event=entity_data.get('pre_collision_vehicle_action_first_event'),
            vehicle_type=entity_data.get('vehicle_type'),
            vehicle_use=entity_data.get('vehicle_use'),
            involved_persons=entity_data.get('involved_persons'),
            charges=entity_data.get('charges')
        )
    
    @staticmethod
    def map_to_tar_entities(collision_request_payload: CollisionRequestPayload) -> list:
        """
        Maps the entities part of CollisionRequestPayload to a list of TarEntity objects.
        """
        # Assuming collision_request_payload['entities'] is a list of entity data
        result = []
        for entity in collision_request_payload.get('entities', []):
            involved_persons = [CollisionMapper.map_to_tar_involved_person(person) for person in entity.get('involved_persons', [])]
            charges = [CollisionMapper.map_to_tar_charges(charge) for charge in entity.get('charges', [])]
            entity['involved_persons'] = involved_persons
            entity['charges'] = charges
            # Create TarEntity object with the updated entity data
            result.append(CollisionMapper.map_to_tar_entity(entity))
        return result