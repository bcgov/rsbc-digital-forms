from dataclasses import dataclass
from datetime import date
from ..base import db

@dataclass
class TarInvolvedPerson(db.Model):
    __tablename__ = 'tar_involved_person'
    __table_args__ = {'schema': 'TAR'}

    person_id: int
    entity_id: int
    status: str
    surname: str
    given_name: str
    vehicle_occupied: str
    position_of_person: str
    safety_equipment_used: str
    ejection_from_vehicle: str
    age: str
    sex: str
    severe_injury_location: str
    injury_type: str
    consciousness_state: str
    injured_taken_to: str
    injured_taken_by: str
    injury_classification: str
    date_of_death: date

    person_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entity_id = db.Column(db.Integer, db.ForeignKey('tar_entity.entity_id'), nullable=False)
    status = db.Column(db.String(1), nullable=False)
    surname = db.Column(db.String(30))
    given_name = db.Column(db.String(30))
    vehicle_occupied = db.Column(db.String(2))
    position_of_person = db.Column(db.String(2), db.ForeignKey('tar_position.code'), nullable=False)
    safety_equipment_used = db.Column(db.String(2), db.ForeignKey('tar_safety_equipment.code'), nullable=False)
    ejection_from_vehicle = db.Column(db.String(2), db.ForeignKey('tar_ejection.code'), nullable=False)
    age = db.Column(db.String(10), nullable=False)
    sex = db.Column(db.String(1), nullable=False)
    severe_injury_location = db.Column(db.String(2), db.ForeignKey('tar_injury_location.code'), nullable=False)
    injury_type = db.Column(db.String, db.ForeignKey('tar_injury_type.code'), nullable=False)
    consciousness_state = db.Column(db.String, db.ForeignKey('tar_victim_status.code'))
    injured_taken_to = db.Column(db.String, db.ForeignKey('tar_taken_to.code'))
    injured_taken_by = db.Column(db.String, db.ForeignKey('tar_taken_by.code'))
    injury_classification = db.Column(db.String, db.ForeignKey('tar_injury_classification.code'))
    date_of_death = db.Column(db.Date)
