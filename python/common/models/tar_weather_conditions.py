from dataclasses import dataclass
from .base import db

@dataclass
class TarWeatherConditions(db.Model):
    __tablename__ = 'weather_conditions'
    code: str
    description: str
    code = db.Column(db.String(2), primary_key=True)
    description = db.Column(db.String(50))
