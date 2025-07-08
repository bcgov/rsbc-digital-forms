from dataclasses import dataclass
from .base import db

@dataclass
class TarLandUsage(db.Model):
    __tablename__ = 'tar_land_usage'
    code: str
    description: str
    code = db.Column(db.String(2), primary_key=True)
    description = db.Column(db.String(50))
