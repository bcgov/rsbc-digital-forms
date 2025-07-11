from dataclasses import dataclass
from datetime import date
from ..base import db

@dataclass
class TarEntity(db.Model):
    __tablename__ = 'entity'
    __table_args__ = {'schema': 'TAR'}

    entity_id: int
    collision_case_num: str
    entity_type: str
    entity_num: int
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

    entity_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    collision_case_num = db.Column(db.String(10), db.ForeignKey('TAR.collision.collision_case_num'), nullable=False)
    entity_type = db.Column(db.String(1), db.ForeignKey('TAR.entity_type.code'), nullable=False)
    entity_num = db.Column(db.Integer, nullable=False)
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
    date_of_birth = db.Column(db.Date)
    age_at_collision = db.Column(db.Integer)
    contact_phone_num = db.Column(db.String(25))
    sex = db.Column(db.String(1))
    contributing_factor_1 = db.Column(db.String(2), db.ForeignKey('TAR.contributing_factors.code'), nullable=False)
    contributing_factor_2 = db.Column(db.String(2), db.ForeignKey('TAR.contributing_factors.code'), nullable=False)
    contributing_factor_3 = db.Column(db.String(2), db.ForeignKey('TAR.contributing_factors.code'), nullable=False)
    contributing_factor_4 = db.Column(db.String(2), db.ForeignKey('TAR.contributing_factors.code'), nullable=False)
    charges_blood_alc_tests_taken = db.Column(db.Boolean)
    blood_alc_test = db.Column(db.String(3))
    result_1 = db.Column(db.String(8))
    result_2 = db.Column(db.String(8))

    vehicle = db.relationship('TarEntityVehicle', backref='entity', uselist=False, lazy='select')
    involved_person = db.relationship('TarInvolvedPerson', backref='entity', uselist=True, lazy='select')
    charges = db.relationship('TarCharges', backref='entity', uselist=True, lazy='select')