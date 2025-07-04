from dataclasses import dataclass
from .base import db

@dataclass
class TarCharges(db.Model):
    __tablename__ = 'charges'

    charge_id: int
    entity_id: int
    charge_type: str
    section_num: str
    offence_title: str

    charge_id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.Integer, db.ForeignKey('entity.entity_id'), nullable=False)
    charge_type = db.Column(db.String)
    section_num = db.Column(db.String)
    offence_title = db.Column(db.String)
