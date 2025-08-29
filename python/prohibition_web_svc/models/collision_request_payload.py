
from typing import TypedDict
from python.prohibition_web_svc.models.dropdown_option import DropdownOption
from python.prohibition_web_svc.models.entity import Entity
from python.prohibition_web_svc.models.police_agency import PoliceAgency
from python.prohibition_web_svc.models.witness import Witness


class CollisionRequestPayload(TypedDict):
    collision_case_num: str
    collision_scenario: DropdownOption
    police_file_num: str
    prime_file_vjur: DropdownOption
    collision_case_prefix: str
    date_collision: str
    time_collision: str
    reported_same_day: bool
    time_collision_unknown: bool
    date_reported: str
    hit_and_run: bool
    police_attended: bool
    police_agency_code: PoliceAgency
    police_zone: str
    primary_collision_occ_code: DropdownOption
    first_contact_event: DropdownOption
    first_contact_loc: DropdownOption
    has_countable_fatal: bool
    countable_fatal_total: int
    completed_by_name: str
    completed_by_id: str
    detachment_unit: str
    icbc_submission_date: str
    reviewed_by: str
    investigated_by_traffic_analyst: str

    # Additional details
    pedestrian_location: DropdownOption
    pedestrian_action: DropdownOption
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
    summary_was_verified: bool

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
    road_class: DropdownOption
    traffic_flow: DropdownOption
    collision_loc: DropdownOption
    primary_speed_zone: DropdownOption
    secondary_speed_zone: DropdownOption
    land_usage: DropdownOption
    road_type: DropdownOption
    traffic_control: DropdownOption
    roadway_character: DropdownOption
    roadway_surface_cond: DropdownOption
    weather_cond: DropdownOption
    lighting_cond: DropdownOption
    ff_application_id: str
    submitted_user_guid: str

    entities: list[Entity]
    witnesses: list[Witness]
