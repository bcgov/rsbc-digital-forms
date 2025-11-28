from dataclasses import dataclass
from datetime import date
from sqlalchemy import ForeignKeyConstraint, and_
from ..base import db
from .position import TarPosition

@dataclass
class TarInvolvedPerson(db.Model):
    __tablename__ = 'involved_person'
    __table_args__ = (
        ForeignKeyConstraint(
            ['entity_type', 'position_of_person'],
            ['TAR.position.entity_type', 'TAR.position.code'],
            name='involved_person_position_of_person_entity_type_fkey'
        ),
        ForeignKeyConstraint(
            ['entity_type', 'safety_equipment_used'],
            ['TAR.safety_equipment.entity_type', 'TAR.safety_equipment.code'],
            name='involved_person_safety_equipment_used_entity_type_fkey'
        ),
        {'schema': 'TAR'}
    )

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
    entity_type: str

    person_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entity_id = db.Column(db.Integer, db.ForeignKey('TAR.entity.entity_id'), nullable=False)
    entity_type = db.Column(db.String(1), db.ForeignKey('TAR.entity_type.code'), nullable=False)
    status = db.Column(db.String(15), nullable=False)
    surname = db.Column(db.String(30))
    given_name = db.Column(db.String(30))
    vehicle_occupied = db.Column(db.String(2))
    position_of_person = db.Column(db.String(2), nullable=False)
    safety_equipment_used = db.Column(db.String(2), nullable=False)
    ejection_from_vehicle = db.Column(db.String(2), db.ForeignKey('TAR.ejection.code'), nullable=False)
    age = db.Column(db.String(10), nullable=False)
    sex = db.Column(db.String(1), nullable=False)
    severe_injury_location = db.Column(db.String(2), db.ForeignKey('TAR.injury_location.code'), nullable=False)
    injury_type = db.Column(db.String(2), db.ForeignKey('TAR.injury_type.code'), nullable=False)
    consciousness_state = db.Column(db.String(2), db.ForeignKey('TAR.victim_status.code'))
    injured_taken_to = db.Column(db.String(4), db.ForeignKey('TAR.taken_to.code'))
    injured_taken_by = db.Column(db.String(4), db.ForeignKey('TAR.taken_by.code'))
    injury_classification = db.Column(db.String(2), db.ForeignKey('TAR.injury_classification.code'))
    date_of_death = db.Column(db.Date)

    # Relationship to TarPosition using composite foreign key
    position = db.relationship(
        'TarPosition',
        primaryjoin='and_(TarInvolvedPerson.entity_type == TarPosition.entity_type, '
                   'TarInvolvedPerson.position_of_person == TarPosition.code)'
    )
