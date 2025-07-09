from dataclasses import dataclass
from ..base import db

@dataclass
class TarSpeedZone(db.Model):
    __tablename__ = 'tar_speed_zone'
    __table_args__ = {'schema': 'TAR'}
    code: str
    description: str
    code = db.Column(db.String(3), primary_key=True)
    description = db.Column(db.String(50))
