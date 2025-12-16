from dataclasses import dataclass
from ..base import db

@dataclass
class TarSafetyEquipment(db.Model):
    __tablename__ = 'safety_equipment'
    __table_args__ = {'schema': 'TAR'}
    code: str
    description: str
    entity_type: str

    code = db.Column(db.String(2), primary_key=True)
    description = db.Column(db.String(50))
    entity_type = db.Column(db.String(1), db.ForeignKey('TAR.entity_type.code'), primary_key=True)
