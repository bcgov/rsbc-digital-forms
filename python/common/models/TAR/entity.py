from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from ..base import db

@dataclass
class TarEntity(db.Model):
    __tablename__ = 'entity'
    __table_args__ = {'schema': 'TAR'}

    entity_id: int
    collision_case_num: str
    entity_type: str
    entity_num: str
    possible_offender: str
    vehicle_parked: bool
    unknown_entity: bool
    driver_license_num: str
    license_prov_state: str
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
    contributing_factor_1: str
    contributing_factor_2: str
    contributing_factor_3: str
    contributing_factor_4: str
    charges_blood_alc_tests_taken: str
    blood_alc_test: str
    result_1: str
    result_2: str

    vehicle_plate_num: str
    vehicle_plate_prov_state: str
    vehicle_year: str
    vehicle_make: str
    vehicle_style: str
    vehicle_colour: str
    trailer_towed_plate_num: str
    trailer_towed_plate_prov_state: str
    is_registered_owner: bool
    vehicle_owner_name: str
    vehicle_owner_address: str
    nsc_num: str
    jur_code: str
    damage_location_code: str
    severety_code: str
    estimated_vehicle_damage: Decimal
    vehicle_stolen: str
    vehicle_towed: str
    vehicle_towed_by: str
    dir_of_travel: str
    entity_street: str
    insurance_coverage: str
    other_insurer: str
    other_insurance_policy_num: str
    second_contact: str
    pre_collision_vehicle_action_first_event: str
    vehicle_type: str
    vehicle_use: str

    entity_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    collision_case_num = db.Column(db.String(10), db.ForeignKey('TAR.collision.collision_case_num'), nullable=False)
    entity_type = db.Column(db.String(1), db.ForeignKey('TAR.entity_type.code'), nullable=False)
    entity_num = db.Column(db.String(2), nullable=False)
    possible_offender = db.Column(db.String(1), nullable=False)
    vehicle_parked = db.Column(db.Boolean)
    unknown_entity = db.Column(db.Boolean)
    driver_license_num = db.Column(db.String(25))
    license_prov_state = db.Column(db.String(2))
    license_expiry = db.Column(db.Integer)
    surname = db.Column(db.String(28))
    given_name = db.Column(db.String(25))
    license_class = db.Column(db.String(10))
    graduated_license_type = db.Column(db.String(1))
    residential_address = db.Column(db.String(90))
    business_address = db.Column(db.String(68))
    business_phone_num = db.Column(db.String(25))
    date_of_birth = db.Column(db.Date)
    age_at_collision = db.Column(db.Integer)
    contact_phone_num = db.Column(db.String(25))
    sex = db.Column(db.String(1))
    contributing_factor_1 = db.Column(db.String(2), db.ForeignKey('TAR.contributing_factors.code'), nullable=False)
    contributing_factor_2 = db.Column(db.String(2), db.ForeignKey('TAR.contributing_factors.code'), nullable=False)
    contributing_factor_3 = db.Column(db.String(2), db.ForeignKey('TAR.contributing_factors.code'), nullable=False)
    contributing_factor_4 = db.Column(db.String(2), db.ForeignKey('TAR.contributing_factors.code'), nullable=False)
    charges_blood_alc_tests_taken = db.Column(db.String(1))
    blood_alc_test = db.Column(db.String(3))
    result_1 = db.Column(db.String(8))
    result_2 = db.Column(db.String(8))

    vehicle_plate_num = db.Column(db.String(20))
    vehicle_plate_prov_state = db.Column(db.String(2))
    vehicle_year = db.Column(db.String(4))
    vehicle_make = db.Column(db.String(30))
    vehicle_style = db.Column(db.String(15))
    vehicle_colour = db.Column(db.String(15))
    trailer_towed_plate_num = db.Column(db.String(20))
    trailer_towed_plate_prov_state = db.Column(db.String(2))
    is_registered_owner = db.Column(db.Boolean)
    vehicle_owner_name = db.Column(db.String(60))
    vehicle_owner_address = db.Column(db.String(90))
    nsc_num = db.Column(db.String(50))
    jur_code = db.Column(db.String(45))
    damage_location_code = db.Column(db.String(2), db.ForeignKey('TAR.damage_location.code'), nullable=False)
    severety_code = db.Column(db.String(2), db.ForeignKey('TAR.damage_severity.code'), nullable=False)
    estimated_vehicle_damage = db.Column(db.Numeric(16, 2))
    vehicle_stolen = db.Column(db.String(1))
    vehicle_towed = db.Column(db.String(1))
    vehicle_towed_by = db.Column(db.String(30))
    dir_of_travel = db.Column(db.String(1))
    entity_street = db.Column(db.String(60))
    insurance_coverage = db.Column(db.String(1))
    other_insurer = db.Column(db.String(20))
    other_insurance_policy_num = db.Column(db.String(20))
    second_contact = db.Column(db.String(2), db.ForeignKey('TAR.type_of_collision.code'))
    pre_collision_vehicle_action_first_event = db.Column(db.String(2), db.ForeignKey('TAR.pre_collision_action.code'))
    vehicle_type = db.Column(db.String(2), db.ForeignKey('TAR.vehicle_type.code'))
    vehicle_use = db.Column(db.String(2), db.ForeignKey('TAR.vehicle_use.code'))
    

    involved_persons = db.relationship('TarInvolvedPerson', backref='entity', uselist=True, lazy='select')
    charges = db.relationship('TarCharges', backref='entity', uselist=True, lazy='select')