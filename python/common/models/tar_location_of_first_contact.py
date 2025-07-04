from dataclasses import dataclass
from .base import db

@dataclass
class TarLocationOfFirstContact(db.Model):
    __tablename__ = 'location_of_first_contact'
    code: str
    description: str
    code = db.Column(db.String(2), primary_key=True)
    description = db.Column(db.String(50))
