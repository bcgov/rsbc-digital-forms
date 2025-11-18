from dataclasses import dataclass
from ..base import db

@dataclass
class TarLkiHighway(db.Model):
    __tablename__ = 'lki_highway'
    __table_args__ = {'schema': 'TAR'}
    
    code: str
    number: int
    letter: str
    description: str

    code = db.Column(db.String(4), primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    letter = db.Column(db.String(1), nullable=False)
    description = db.Column(db.String(100), nullable=False)


