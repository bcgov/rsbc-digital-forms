from dataclasses import dataclass
from decimal import Decimal
from .base import db

@dataclass
class TarAdditionalCollisionDetails(db.Model):
    __tablename__ = 'additional_collision_details'

    collision_case_num: str
    pedestrian_location: str
    pedestrian_action: str
    has_other_prop_damage: bool
    other_prop_damage_desc: str
    prop_damage_est_value: str
    has_witnesses: bool
    police_comments: str
    collision_type: str
    total_est_damage: Decimal
    total_injured: int
    total_killed: int
    total_vehicles: int

    collision_case_num = db.Column(db.String, db.ForeignKey('collision.collision_case_num'), primary_key=True)
    pedestrian_location = db.Column(db.String)
    pedestrian_action = db.Column(db.String)
    has_other_prop_damage = db.Column(db.Boolean, nullable=False, default=False)
    other_prop_damage_desc = db.Column(db.String)
    prop_damage_est_value = db.Column(db.String)
    has_witnesses = db.Column(db.Boolean, nullable=False, default=False)
    police_comments = db.Column(db.String)
    collision_type = db.Column(db.String, nullable=False)
    total_est_damage = db.Column(db.Integer, nullable=False, default=0)
    total_injured = db.Column(db.Integer, nullable=False, default=0)
    total_killed = db.Column(db.Integer, nullable=False, default=0)
    total_vehicles = db.Column(db.Integer, nullable=False, default=0)
