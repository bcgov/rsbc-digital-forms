from dataclasses import dataclass
from datetime import date
from .base import db

@dataclass
class TarEntity(db.Model):
    __tablename__ = 'entity'

    entity_id: int
    collision_case_num: str
    entity_type: str
    entity_num: int
    possible_offender: bool
    vehicle_parked: bool
    unknown_entity: bool
    driver_license_num: str
    license_prov_state: str
    license_expiry: str
    surname: str
    given_name: str
    license_class: str
    graduated_license_type: str
    residential_address: str
    business_address: str
    date_of_birth: date
    age_at_collision: int
    contact_phone_num: str
    sex: str
    contributing_factor_1: str
    contributing_factor_2: str
    contributing_factor_3: str
    contributing_factor_4: str
    charges_blood_alc_tests_taken: bool
    blood_alc_test: str
    result_1: str
    result_2: str

    entity_id = db.Column(db.Integer, primary_key=True)
    collision_case_num = db.Column(db.String, db.ForeignKey('collision.collision_case_num'), nullable=False)
    entity_type = db.Column(db.String, nullable=False)
    entity_num = db.Column(db.Integer, nullable=False)
    possible_offender = db.Column(db.Boolean, nullable=False, default=False)
    vehicle_parked = db.Column(db.Boolean)
    unknown_entity = db.Column(db.Boolean)
    driver_license_num = db.Column(db.String)
    license_prov_state = db.Column(db.String)
    license_expiry = db.Column(db.String)
    surname = db.Column(db.String)
    given_name = db.Column(db.String)
    license_class = db.Column(db.String)
    graduated_license_type = db.Column(db.String)
    residential_address = db.Column(db.String)
    business_address = db.Column(db.String)
    date_of_birth = db.Column(db.Date)
    age_at_collision = db.Column(db.Integer)
    contact_phone_num = db.Column(db.String)
    sex = db.Column(db.String)
    contributing_factor_1 = db.Column(db.String, nullable=False)
    contributing_factor_2 = db.Column(db.String, nullable=False)
    contributing_factor_3 = db.Column(db.String, nullable=False)
    contributing_factor_4 = db.Column(db.String, nullable=False)
    charges_blood_alc_tests_taken = db.Column(db.Boolean)
    blood_alc_test = db.Column(db.String)
    result_1 = db.Column(db.String)
    result_2 = db.Column(db.String)
