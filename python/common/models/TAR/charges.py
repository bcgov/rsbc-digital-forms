from dataclasses import dataclass
from ..base import db

@dataclass
class TarCharges(db.Model):
    __tablename__ = 'charges'
    __table_args__ = {'schema': 'TAR'}

    charge_id: int
    entity_id: int
    charge_type: str
    section_num: str
    offence_title: str

    charge_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entity_id = db.Column(db.Integer, db.ForeignKey('TAR.entity.entity_id'), nullable=False)
    charge_type = db.Column(db.String(1))
    section_num = db.Column(db.String(10))
    offence_title = db.Column(db.String(70))
