from dataclasses import dataclass
from decimal import Decimal
from ..base import db

@dataclass
class TarAdditionalCollisionDetails(db.Model):
    __tablename__ = 'additional_collision_details'
    __table_args__ = {'schema': 'TAR'}

    collision_case_num: str
    pedestrian_location: str
    pedestrian_action: str
    has_other_prop_damage: str
    other_prop_damage_desc: str
    prop_damage_est_value: Decimal
    has_witnesses: bool
    police_comments: str
    collision_type: str
    total_est_damage: Decimal
    total_injured: int
    total_killed: int
    total_vehicles: int
    summary_was_verified: bool = False

    collision_case_num = db.Column(db.String(10), db.ForeignKey('TAR.collision.collision_case_num'), primary_key=True)
    pedestrian_location = db.Column(db.String(2), db.ForeignKey('TAR.pedestrian_location.code'))
    pedestrian_action = db.Column(db.String(2), db.ForeignKey('TAR.pedestrian_action.code'))
    has_other_prop_damage = db.Column(db.String(2), nullable=False)
    other_prop_damage_desc = db.Column(db.String(3000))
    prop_damage_est_value = db.Column(db.Numeric(precision=12, scale=2))
    has_witnesses = db.Column(db.Boolean, nullable=False, default=False)
    police_comments = db.Column(db.String(3000))
    collision_type = db.Column(db.String(2), nullable=False)
    total_est_damage = db.Column(db.Numeric(precision=12, scale=2), nullable=False, default=0)
    total_injured = db.Column(db.Integer, nullable=False, default=0)
    total_killed = db.Column(db.Integer, nullable=False, default=0)
    total_vehicles = db.Column(db.Integer, nullable=False, default=0)
    summary_was_verified = db.Column(db.Boolean, nullable=False, default=False)
