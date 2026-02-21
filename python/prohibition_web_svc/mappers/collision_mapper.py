from python.common.helper import str_to_integer
from python.common.models import TarCollision, TarLocation, TarAdditionalCollisionDetails, TarWitnessInfo, TarEntity, TarInvolvedPerson, TarCharges
from python.prohibition_web_svc.models.collision_request_payload import CollisionRequestPayload


class CollisionMapper:
    @staticmethod
    def map_to_tar_collision(collision_request_payload: CollisionRequestPayload) -> TarCollision:
        """
        Maps a CollisionRequestPayload to a TarCollision object.
        """
        tar_collision = TarCollision(
            collision_case_num=collision_request_payload['collision_case_num'],
            collision_scenario=collision_request_payload['collision_scenario']['value'] if collision_request_payload.get('collision_scenario') else None,
            police_file_num=collision_request_payload['police_file_num'],
            prime_file_vjur=collision_request_payload['prime_file_vjur']['value'] if collision_request_payload.get('prime_file_vjur') else None,
            collision_case_prefix=collision_request_payload.get('collision_case_prefix'),
            date_collision=collision_request_payload['date_collision'],
            time_collision=collision_request_payload['time_collision'] if not collision_request_payload['time_collision_unknown'] else None,
            reported_same_day=collision_request_payload['reported_same_day'],
            time_collision_unknown=collision_request_payload['time_collision_unknown'],
            date_reported=collision_request_payload['date_reported'],
            hit_and_run=collision_request_payload['hit_and_run'],
            police_attended=collision_request_payload['police_attended'],
            police_agency_code=collision_request_payload['police_agency_code']['code'] if collision_request_payload.get('police_agency_code') else None,
            police_zone=collision_request_payload.get('police_zone'),
            primary_collision_occ_code=collision_request_payload['primary_collision_occ_code']['value'] if collision_request_payload.get('primary_collision_occ_code') else None,
            first_contact_event=collision_request_payload['first_contact_event']['value'] if collision_request_payload.get('first_contact_event') else None,
            first_contact_loc=collision_request_payload['first_contact_loc']['value'] if collision_request_payload.get('first_contact_loc') else None,
            has_countable_fatal=collision_request_payload['has_countable_fatal'],
            countable_fatal_total=str_to_integer(collision_request_payload['countable_fatal_total']),
            completed_by_name=collision_request_payload['completed_by_name'],
            completed_by_id=collision_request_payload['completed_by_id'],
            icbc_submission_date=collision_request_payload.get('icbc_submission_date'),
            reviewed_by=collision_request_payload.get('reviewed_by'),
            investigated_by_traffic_analyst=collision_request_payload['investigated_by_traffic_analyst'],
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
            collision_case_num=collision_request_payload['collision_case_num'],
            hwy_code=collision_request_payload['hwy_code'],
            hwy_route_num=collision_request_payload['hwy_route_num']['code'] if collision_request_payload.get('hwy_route_num') else None,
            segment_num=collision_request_payload['segment_num']['code'] if collision_request_payload.get('segment_num') else None,
            loc_code_km=collision_request_payload.get('loc_code_km') if collision_request_payload.get('loc_code_km') is not None and collision_request_payload.get('loc_code_km') != '' else None,
            city_name=collision_request_payload['city_name'],
            city_status=collision_request_payload.get('city_status'),
            street_on=collision_request_payload.get('street_on'),
            street_at=collision_request_payload.get('street_at'),
            street_desc=collision_request_payload.get('street_desc'),
            gps_format=collision_request_payload.get('gps_format'),
            lat_decim_degrees=collision_request_payload['lat_decim_degrees'],
            long_decim_degrees=collision_request_payload['long_decim_degrees'],
            lat_degree=collision_request_payload.get('lat_degree'),
            lat_min=collision_request_payload.get('lat_min'),
            lat_sec=collision_request_payload.get('lat_sec'),
            long_degree=collision_request_payload.get('long_degree'),
            long_min=collision_request_payload.get('long_min'),
            long_sec=collision_request_payload.get('long_sec'),
            road_class=collision_request_payload['road_class']['value'] if collision_request_payload.get('road_class') else None,
            traffic_flow=collision_request_payload['traffic_flow']['value'] if collision_request_payload.get('traffic_flow') else None,
            collision_loc=collision_request_payload['collision_loc']['value'] if collision_request_payload.get('collision_loc') else None,
            primary_speed_zone=collision_request_payload['primary_speed_zone']['value'] if collision_request_payload.get('primary_speed_zone') else None,
            secondary_speed_zone=collision_request_payload['secondary_speed_zone']['value'] if collision_request_payload.get('secondary_speed_zone') else None,
            land_usage=collision_request_payload['land_usage']['value'] if collision_request_payload.get('land_usage') else None,
            road_type=collision_request_payload['road_type']['value'] if collision_request_payload.get('road_type') else None,
            traffic_control=collision_request_payload['traffic_control']['value'] if collision_request_payload.get('traffic_control') else None,
            roadway_character=collision_request_payload['roadway_character']['value'] if collision_request_payload.get('roadway_character') else None,
            roadway_surface_cond=collision_request_payload['roadway_surface_cond']['value'] if collision_request_payload.get('roadway_surface_cond') else None,
            weather_cond=collision_request_payload['weather_cond']['value'] if collision_request_payload.get('weather_cond') else None,
            lighting_cond=collision_request_payload['lighting_cond']['value'] if collision_request_payload.get('lighting_cond') else None,
        )

    @staticmethod
    def map_to_tar_additional_details(collision_request_payload: CollisionRequestPayload) -> TarAdditionalCollisionDetails:
        """
        Maps the additional details part of CollisionRequestPayload to a TarAdditionalCollisionDetails object.
        """
        return TarAdditionalCollisionDetails(
            collision_case_num=collision_request_payload['collision_case_num'],
            pedestrian_location=collision_request_payload['pedestrian_location']['value'] if collision_request_payload.get('pedestrian_location') else None,
            pedestrian_action=collision_request_payload['pedestrian_action']['value'] if collision_request_payload.get('pedestrian_action') else None,
            has_other_prop_damage=collision_request_payload['has_other_prop_damage'],
            other_prop_damage_desc=collision_request_payload.get('other_prop_damage_desc'),
            prop_damage_est_value=collision_request_payload.get('prop_damage_est_value'),
            has_witnesses=collision_request_payload['has_witnesses'],
            police_comments=collision_request_payload.get('police_comments'),
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
        witnesses = collision_request_payload.get('witnesses', [])
        for witness in witnesses:
            tar_witness = TarWitnessInfo(
                collision_case_num=collision_request_payload['collision_case_num'],
                witness_name=witness.get('witness_name'),
                address=witness.get('address'),
                contact_phn_num=witness.get('contact_phn_num')
            )
            result.append(tar_witness)
        return result
    
    @staticmethod
    def map_to_tar_involved_person(person_data: dict, entity_type: str) -> TarInvolvedPerson:
        """
        Maps a person dictionary to a TarInvolvedPerson object field by field.
        """
        return TarInvolvedPerson(
            status=person_data.get('status'),
            surname=person_data.get('surname'),
            given_name=person_data.get('given_name'),
            vehicle_occupied=person_data.get('vehicle_occupied'),
            position_of_person=person_data['position_of_person']['value'] if person_data.get('position_of_person') else None,
            safety_equipment_used=person_data['safety_equipment_used']['value'] if person_data.get('safety_equipment_used') else None,
            ejection_from_vehicle=person_data['ejection_from_vehicle']['value'] if person_data.get('ejection_from_vehicle') else None,
            age=person_data.get('age') if person_data.get('age') is not None and person_data.get('age') != "" else None,
            sex=person_data['sex']['value'] if person_data.get('sex') else None,
            severe_injury_location=person_data['severe_injury_location']['value'] if person_data.get('severe_injury_location') else None,
            injury_type=person_data['injury_type']['value'] if person_data.get('injury_type') else None,
            consciousness_state=person_data['consciousness_state']['value'] if person_data.get('consciousness_state') else None,
            injured_taken_to=person_data['injured_taken_to']['value'] if person_data.get('injured_taken_to') else None,
            injured_taken_by=person_data['injured_taken_by']['value'] if person_data.get('injured_taken_by') else None,
            injury_classification=person_data['injury_classification']['value'] if person_data.get('injury_classification') else None,
            date_of_death=person_data.get('date_of_death'),
            entity_type=entity_type
        )
    
    @staticmethod
    def map_to_tar_charges(charge_data: dict) -> TarCharges:
        """
        Maps a charge dictionary to a TarCharges object field by field.
        """
        return TarCharges(
            charge_id=charge_data.get('charge_id'),
            charge_type=charge_data['charge_type']['value'] if charge_data.get('charge_type') else None,
            section_num=charge_data.get('section_num'),
            offence_title=charge_data.get('offence_title')
        )
    
    @staticmethod
    def map_to_tar_entity(entity_data: dict) -> TarEntity:
        """
        Maps an entity dictionary to a TarEntity object field by field.
        """
        return TarEntity(
            entity_type=entity_data['entity_type']['value'] if entity_data.get('entity_type') else None,
            entity_num=entity_data.get('entity_num'),
            possible_offender=entity_data.get('possible_offender'),
            vehicle_parked=entity_data.get('vehicle_parked'),
            unknown_entity=entity_data.get('unknown_entity'),
            driver_license_num=entity_data.get('driver_license_num'),
            license_prov_state=entity_data['license_prov_state']['value'] if entity_data.get('license_prov_state') else None,
            license_expiry=str_to_integer(entity_data.get('license_expiry')),
            surname=entity_data.get('surname'),
            given_name=entity_data.get('given_name'),
            license_class=entity_data.get('license_class'),
            graduated_license_type=entity_data.get('graduated_license_type'),
            residential_address=entity_data.get('residential_address'),
            business_address=entity_data.get('business_address'),
            business_phone_num=entity_data.get('business_phone_num'),
            date_of_birth=entity_data.get('date_of_birth'),
            age_at_collision=str_to_integer(entity_data.get('age_at_collision')),
            contact_phone_num=entity_data.get('contact_phone_num'),
            sex=entity_data['sex']['value'] if entity_data.get('sex') else None,
            contributing_factor_1=entity_data['contributing_factor_1']['value'] if entity_data.get('contributing_factor_1') else None,
            contributing_factor_2=entity_data['contributing_factor_2']['value'] if entity_data.get('contributing_factor_2') else None,
            contributing_factor_3=entity_data['contributing_factor_3']['value'] if entity_data.get('contributing_factor_3') else None,
            contributing_factor_4=entity_data['contributing_factor_4']['value'] if entity_data.get('contributing_factor_4') else None,
            charges_blood_alc_tests_taken=entity_data.get('charges_blood_alc_tests_taken'),
            has_charges=entity_data.get('has_charges'),
            blood_alc_tests_taken=entity_data.get('blood_alc_tests_taken'),
            blood_alc_test=entity_data.get('blood_alc_test'),
            result_1=entity_data.get('result_1'),
            result_2=entity_data.get('result_2'),
            vehicle_plate_num=entity_data.get('vehicle_plate_num'),
            vehicle_plate_prov_state=entity_data['vehicle_plate_prov_state']['value'] if entity_data.get('vehicle_plate_prov_state') else None,
            vehicle_year=entity_data['vehicle_year']['value'] if entity_data.get('vehicle_year') else None,
            vehicle_make=entity_data['vehicle_make']['value'] if entity_data.get('vehicle_make') else None,
            vehicle_style=entity_data['vehicle_style']['value'] if entity_data.get('vehicle_style') else None,
            vehicle_colour=entity_data.get('vehicle_colour'),
            trailer_towed_plate_num=entity_data.get('trailer_towed_plate_num'),
            trailer_towed_plate_prov_state=entity_data['trailer_towed_plate_prov_state']['value'] if entity_data.get('trailer_towed_plate_prov_state') else None,
            is_registered_owner=entity_data.get('is_registered_owner'),
            vehicle_owner_name=entity_data.get('vehicle_owner_name'),
            vehicle_owner_address=entity_data.get('vehicle_owner_address'),
            nsc_num=entity_data.get('nsc_num'),
            jur_code=entity_data.get('jur_code'),
            damage_location_code=entity_data['damage_location_code']['value'] if entity_data.get('damage_location_code') else None,
            severety_code=entity_data['severety_code']['value'] if entity_data.get('severety_code') else None,
            estimated_vehicle_damage=entity_data.get('estimated_vehicle_damage'),
            vehicle_stolen=entity_data.get('vehicle_stolen'),
            vehicle_towed=entity_data.get('vehicle_towed'),
            vehicle_towed_by=entity_data['vehicle_towed_by']['value'] if entity_data.get('vehicle_towed_by') else None,
            dir_of_travel=entity_data.get('dir_of_travel'),
            entity_street=entity_data.get('entity_street'),
            insurance_coverage=entity_data.get('insurance_coverage'),
            other_insurer=entity_data.get('other_insurer'),
            other_insurance_policy_num=entity_data.get('other_insurance_policy_num'),
            second_contact=entity_data['second_contact']['value'] if entity_data.get('second_contact') else None,
            pre_collision_vehicle_action_first_event=entity_data['pre_collision_vehicle_action_first_event']['value'] if entity_data.get('pre_collision_vehicle_action_first_event') else None,
            vehicle_type=entity_data['vehicle_type']['value'] if entity_data.get('vehicle_type') else None,
            vehicle_use=entity_data['vehicle_use']['value'] if entity_data.get('vehicle_use') else None,
            involved_persons=entity_data.get('involved_persons', []),
            charges=entity_data.get('charges', [])
        )
    
    @staticmethod
    def map_to_tar_entities(collision_request_payload: CollisionRequestPayload) -> list:
        """
        Maps the entities part of CollisionRequestPayload to a list of TarEntity objects.
        """
        result = []
        collision_case_num = collision_request_payload['collision_case_num']
        entities = collision_request_payload.get('entities', [])
        
        for entity in entities:
            # Convert Entity objects to dict if needed
            entity_dict = entity if isinstance(entity, dict) else entity.__dict__
            
            # Map involved persons
            involved_persons = []
            for person in entity_dict.get('involved_persons', []):
                person_dict = person if isinstance(person, dict) else person.__dict__
                involved_persons.append(
                    CollisionMapper.map_to_tar_involved_person(person_dict, entity_dict['entity_type']['value'])
                )
            
            # Map charges
            charges = []
            for charge in entity_dict.get('charges', []):
                charge_dict = charge if isinstance(charge, dict) else charge.__dict__
                charges.append(
                    CollisionMapper.map_to_tar_charges(charge_dict)
                )
            
            # Update entity data with mapped objects
            entity_dict['involved_persons'] = involved_persons
            entity_dict['charges'] = charges
            
            # Create TarEntity object
            result.append(CollisionMapper.map_to_tar_entity(entity_dict))

        return result