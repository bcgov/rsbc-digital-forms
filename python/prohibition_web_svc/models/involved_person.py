from datetime import date
from typing import TypedDict

from python.prohibition_web_svc.models.dropdown_option import DropdownOption


class InvolvedPerson(TypedDict):
    status: str
    surname: str
    given_name: str
    vehicle_occupied: str
    position_of_person: DropdownOption
    safety_equipment_used: str
    ejection_from_vehicle: DropdownOption
    age: str
    sex: DropdownOption
    severe_injury_location: DropdownOption
    injury_type: DropdownOption
    consciousness_state: DropdownOption
    injured_taken_to: DropdownOption
    injured_taken_by: DropdownOption
    injury_classification: DropdownOption
    date_of_death: date