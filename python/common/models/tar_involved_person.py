from dataclasses import dataclass
from datetime import date
from .base import db

@dataclass
class TarInvolvedPerson(db.Model):
    __tablename__ = 'involved_person'

    person_id: int
    entity_id: int
    status: str
    surname: str
    given_name: str
    vehicle_occupied: str
    position_of_person: str
    safety_equipment_used: str
    ejection_from_vehicle: str
    age: int
    sex: str
    severe_injury_location: str
    injury_type: str
    consciousness_state: str
    injured_taken_to: str
    injured_taken_by: str
    injury_classification: str
    date_of_death: date

    person_id = db.Column(db.Integer, primary_key=True)
    entity_id = db.Column(db.Integer, db.ForeignKey('entity.entity_id'), nullable=False)
    status = db.Column(db.String, nullable=False)
    surname = db.Column(db.String)
    given_name = db.Column(db.String)
    vehicle_occupied = db.Column(db.String)
    position_of_person = db.Column(db.String, nullable=False)
    safety_equipment_used = db.Column(db.String, nullable=False)
    ejection_from_vehicle = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String, nullable=False)
    severe_injury_location = db.Column(db.String)
    injury_type = db.Column(db.String, nullable=False)
    consciousness_state = db.Column(db.String)
    injured_taken_to = db.Column(db.String)
    injured_taken_by = db.Column(db.String)
    injury_classification = db.Column(db.String)
    date_of_death = db.Column(db.Date)
