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
            police_agency_type_district = collision_request_payload.get('police_agency_type_district'),
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
            total_vehicles=collision_request_payload['total_vehicles']
        )

    @staticmethod
    def map_to_tar_witnesses(collision_request_payload: CollisionRequestPayload) -> list:
        """
        Maps the witnesses part of CollisionRequestPayload to a list of TarWitnessInfo objects.
        """
        # Assuming collision_request_payload['witnesses'] is a list of witness data
        return [TarWitnessInfo(**witness) for witness in collision_request_payload.get('witnesses', [])]
    
    @staticmethod
    def map_to_tar_entities(collision_request_payload: CollisionRequestPayload) -> list:
        """
        Maps the entities part of CollisionRequestPayload to a list of TarEntity objects.
        """
        # Assuming collision_request_payload['entities'] is a list of entity data
        result = []
        for entity in collision_request_payload.get('entities', []):
            involved_persons = [TarInvolvedPerson(**person) for person in entity.get('involved_persons', [])]
            charges = [TarCharges(**charge) for charge in entity.get('charges', [])]
            entity['involved_persons'] = involved_persons
            entity['charges'] = charges
            # Create TarEntity object with the updated entity data
            result.append(TarEntity(**entity))
        return result