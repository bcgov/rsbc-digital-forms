from dataclasses import dataclass
from .base import db

@dataclass
class TarWitnessInfo(db.Model):
    __tablename__ = 'tar_witness_info'

    id: int
    collision_case_num: str
    witness_name: str
    address: str
    contact_phn_num: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    collision_case_num = db.Column(db.String(10), db.ForeignKey('collision.collision_case_num'), nullable=False)
    witness_name = db.Column(db.String(100))
    address = db.Column(db.String(255))
    contact_phn_num = db.Column(db.String(100))
