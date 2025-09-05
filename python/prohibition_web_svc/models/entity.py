from datetime import date
from decimal import Decimal
from typing import TypedDict

from python.prohibition_web_svc.models.charges import Charges
from python.prohibition_web_svc.models.dropdown_option import DropdownOption
from python.prohibition_web_svc.models.involved_person import InvolvedPerson


class Entity(TypedDict):
    entity_type: DropdownOption
    entity_num: str
    possible_offender: str
    vehicle_parked: bool
    unknown_entity: bool
    driver_license_num: str
    license_prov_state: DropdownOption
    license_expiry: int
    surname: str
    given_name: str
    license_class: str
    graduated_license_type: str
    residential_address: str
    business_address: str
    business_phone_num: str
    date_of_birth: date
    age_at_collision: int
    contact_phone_num: str
    sex: str
    contributing_factor_1: DropdownOption
    contributing_factor_2: DropdownOption
    contributing_factor_3: DropdownOption
    contributing_factor_4: DropdownOption
    charges_blood_alc_tests_taken: str
    blood_alc_test: str
    result_1: str
    result_2: str

    # Vehicle
    vehicle_plate_num: str
    vehicle_plate_prov_state: DropdownOption
    vehicle_year: DropdownOption
    vehicle_make: DropdownOption
    vehicle_style: DropdownOption
    vehicle_colour: str
    trailer_towed_plate_num: str
    trailer_towed_plate_prov_state: DropdownOption
    is_registered_owner: bool
    vehicle_owner_name: str
    vehicle_owner_address: str
    nsc_num: str
    jur_code: str
    damage_location_code: DropdownOption
    severety_code: DropdownOption
    estimated_vehicle_damage: Decimal
    vehicle_stolen: str
    vehicle_towed: str
    vehicle_towed_by: DropdownOption
    dir_of_travel: str
    entity_street: str
    insurance_coverage: str
    other_insurer: str
    other_insurance_policy_num: str
    second_contact: DropdownOption
    pre_collision_vehicle_action_first_event: DropdownOption
    vehicle_type: DropdownOption
    vehicle_use: DropdownOption

    involved_persons: list[InvolvedPerson]
    charges: list[Charges]