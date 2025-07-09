from dataclasses import dataclass
from decimal import Decimal
from ..base import db

@dataclass
class TarEntityVehicle(db.Model):
    __tablename__ = 'entity_vehicle'
    __table_args__ = {'schema': 'TAR'}

    vehicle_id: int
    entity_id: int
    vehicle_plate_num: str
    vehicle_plate_prov_state: str
    vehicle_year: str
    vehicle_make: str
    vehicle_style: str
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

    vehicle_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entity_id = db.Column(db.Integer, db.ForeignKey('TAR.entity.entity_id'), nullable=False)
    vehicle_plate_num = db.Column(db.String(20))
    vehicle_plate_prov_state = db.Column(db.String(2))
    vehicle_year = db.Column(db.String(4))
    vehicle_make = db.Column(db.String(30))
    vehicle_style = db.Column(db.String(15))
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
