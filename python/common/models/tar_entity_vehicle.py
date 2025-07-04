from dataclasses import dataclass
from .base import db

@dataclass
class TarEntityVehicle(db.Model):
    __tablename__ = 'entity_vehicle'

    vehicle_id: int
    entity_id: int
    vehicle_plate_num: str
    vehicle_plate_prov_state: str
    vehicle_year: str
    vehicle_make: str
    vehicle_style: str
    trailer_towed_plate_num: str
    trailer_towed_plate_prov_state: str
    registered_owner: str
    vehicle_owner_name: str
    vehicle_owner_address: str
    nsc_num: str
    jur_code: str
    damage_location_code: str
    severety_code: str
    estimated_vehicle_damage: str
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

    vehicle_id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.Integer, db.ForeignKey('entity.entity_id'), nullable=False)
    vehicle_plate_num = db.Column(db.String)
    vehicle_plate_prov_state = db.Column(db.String)
    vehicle_year = db.Column(db.String)
    vehicle_make = db.Column(db.String)
    vehicle_style = db.Column(db.String)
    trailer_towed_plate_num = db.Column(db.String)
    trailer_towed_plate_prov_state = db.Column(db.String)
    registered_owner = db.Column(db.String)
    vehicle_owner_name = db.Column(db.String)
    vehicle_owner_address = db.Column(db.String)
    nsc_num = db.Column(db.String)
    jur_code = db.Column(db.String)
    damage_location_code = db.Column(db.String, nullable=False)
    severety_code = db.Column(db.String)
    estimated_vehicle_damage = db.Column(db.String)
    vehicle_stolen = db.Column(db.String)
    vehicle_towed = db.Column(db.String)
    vehicle_towed_by = db.Column(db.String)
    dir_of_travel = db.Column(db.String)
    entity_street = db.Column(db.String)
    insurance_coverage = db.Column(db.String)
    other_insurer = db.Column(db.String)
    other_insurance_policy_num = db.Column(db.String)
    second_contact = db.Column(db.String)
    pre_collision_vehicle_action_first_event = db.Column(db.String)
    vehicle_type = db.Column(db.String)
