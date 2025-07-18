
from typing import TypedDict
from python.prohibition_web_svc.models.entity import Entity
from python.prohibition_web_svc.models.witness import Witness


class CollisionRequestPayload(TypedDict):
    collision_case_num: str
    collision_scenario: str
    police_file_num: str
    prime_file_vjur: str
    police_file_prefix: str
    date_collision: str
    time_collision: str
    reported_same_day: bool
    time_collision_unknown: bool
    date_reported: str
    hit_and_run: bool
    police_attended: bool
    police_agency_type_district: str
    police_agency_code: str
    police_zone: str
    primary_collision_occ_code: str
    first_contact_event: str
    first_contact_loc: str
    has_countable_fatal: bool
    countable_fatal_total: int
    completed_by_name: str
    completed_by_id: str
    detachment_unit: str
    icbc_submission_date: str
    reviewed_by: str
    investigated_by_traffic_analyst: str

    # Additional details
    pedestrian_location: str
    pedestrian_action: str
    has_other_prop_damage: bool
    other_prop_damage_desc: str
    prop_damage_est_value: float
    has_witnesses: bool
    police_comments: str
    collision_type: str
    total_est_damage: float
    total_injured: int
    total_killed: int
    total_vehicles: int

    # Location
    hwy_code: str
    hwy_route_num: str
    segment_num: int
    loc_code_km: float
    city_name: str
    city_status: str
    street_on: str
    street_at: str
    street_desc: str
    gps_format: str
    lat_decim_degrees: float
    long_decim_degrees: float
    lat_degree: int
    lat_min: int
    lat_sec: int
    long_degree: int
    long_min: int
    long_sec: int
    road_class: str
    traffic_flow: str
    collision_loc: str
    primary_speed_zone: str
    secondary_speed_zone: str
    land_usage: str
    road_type: str
    traffic_control: str
    roadway_character: str
    roadway_surface_cond: str
    weather_cond: str
    lighting_cond: str
    ff_application_id: str
    submitted_user_guid: str

    entities: list[Entity]
    witnesses: list[Witness]
