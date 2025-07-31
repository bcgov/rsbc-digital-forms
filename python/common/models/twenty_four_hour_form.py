from dataclasses import dataclass
from datetime import datetime
from .base import db

@dataclass
class TwentyFourHourForm(db.Model):
    __tablename__ = 'twenty_four_hour_form'

    form_id: int
    event_id: int
    vehicle_impounded: str
    reason_for_not_impounding: str
    reasonable_ground_other_reason: str
    prescribed_test_used: str
    reasonable_date_of_test: datetime
    reasonable_time_of_test: str
    reason_for_not_using_prescribed_test: str
    resonable_test_used_alcohol: str
    reasonable_asd_expiry_date: datetime
    reasonable_result_alcohol: str
    reasonable_bac_result_mg: str
    resonable_approved_instrument_used: str
    reasonable_test_used_drugs: str
    reasonable_can_drive_drug: bool
    reasonable_can_drive_alcohol: bool
    requested_can_drive_alcohol: bool
    requested_can_drive_drug: bool
    requested_approved_instrument_used: str
    requested_BAC_result: str
    requested_alcohol_test_result: str
    requested_ASD_expiry_date: datetime
    time_of_requested_test: str
    requested_test_used_alcohol: str
    requested_test_used_drug: str
    requested_prescribed_test: str
    witnessed_by_officer: bool
    admission_by_driver: bool
    independent_witness: bool
    reasonable_ground_other: bool
    twenty_four_hour_number: str
    created_dt: datetime
    updated_dt: datetime

    form_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    vehicle_impounded = db.Column(db.String)
    reason_for_not_impounding = db.Column(db.String)
    reasonable_ground_other_reason = db.Column(db.String)
    prescribed_test_used = db.Column(db.String)
    reasonable_date_of_test = db.Column(db.DateTime)
    reasonable_time_of_test = db.Column(db.String)
    reason_for_not_using_prescribed_test = db.Column(db.String)
    resonable_test_used_alcohol = db.Column(db.String)
    reasonable_asd_expiry_date = db.Column(db.DateTime)
    reasonable_result_alcohol = db.Column(db.String)
    reasonable_bac_result_mg = db.Column(db.String)
    resonable_approved_instrument_used = db.Column(db.String)
    reasonable_test_used_drugs = db.Column(db.String)
    reasonable_can_drive_drug = db.Column(db.Boolean)
    reasonable_can_drive_alcohol = db.Column(db.Boolean)
    requested_can_drive_alcohol = db.Column(db.Boolean)
    requested_can_drive_drug = db.Column(db.Boolean)
    requested_approved_instrument_used = db.Column(db.String)
    requested_BAC_result = db.Column(db.String)
    requested_alcohol_test_result = db.Column(db.String)
    requested_ASD_expiry_date = db.Column(db.DateTime)
    time_of_requested_test = db.Column(db.String)
    requested_test_used_alcohol = db.Column(db.String)
    requested_test_used_drug = db.Column(db.String)
    requested_prescribed_test = db.Column(db.String)
    witnessed_by_officer = db.Column(db.Boolean)
    admission_by_driver = db.Column(db.Boolean)
    independent_witness = db.Column(db.Boolean)
    reasonable_ground_other = db.Column(db.Boolean)
    twenty_four_hour_number = db.Column(db.String)
    created_dt = db.Column(db.DateTime)
    updated_dt = db.Column(db.DateTime)
