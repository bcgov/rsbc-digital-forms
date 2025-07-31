from datetime import date
from typing import TypedDict


class InvolvedPerson(TypedDict):
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