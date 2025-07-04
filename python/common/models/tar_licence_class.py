from dataclasses import dataclass
from .base import db

@dataclass
class TarLicenceClass(db.Model):
    __tablename__ = 'licence_class'
    code: str
    description: str
    code = db.Column(db.String(4), primary_key=True)
    description = db.Column(db.String(50))
