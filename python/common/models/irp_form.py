from dataclasses import dataclass
from datetime import datetime, timezone
from .base import db

@dataclass
class IRPForm(db.Model):
    __tablename__ = 'irp_form'

    form_id: int
    event_id: int
    created_dt: datetime
    updated_dt: datetime
    irp_number: str
    vi_number: str
    driver_licence_expiry: datetime
    driver_licence_class: str
    gender: str
    driver_licence_seized: str
    vehicle_impounded: bool
    irp_prohibition_type: str
    witnessed_by_officer: bool
    admission_by_driver: bool
    independent_witness: bool
    reasonable_ground_other: bool
    time_of_suspicion: str
    time_of_asd: str
    refused_or_fail: str
    time_of_refusal: str
    right_to_second_test: str
    lower_asd_prevail: str
    right_to_test_different_asd: str
    driver_requested_second_asd: str
    reasonable_suspicion_odor_of_liquor: bool
    reasonable_suspicion_admission: bool
    reasonable_suspicion_witnessed: bool
    reasonable_suspicion_other: bool
    last_drink: str
    continuous_observation: str

    form_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'), nullable=False)
    created_dt = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_dt = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    irp_number = db.Column(db.String(20), nullable=False)
    vi_number = db.Column(db.String(20))
    driver_licence_expiry = db.Column(db.DateTime)
    driver_licence_class = db.Column(db.String(5))
    gender = db.Column(db.String(1))
    driver_licence_seized = db.Column(db.String(5), nullable=False)
    vehicle_impounded = db.Column(db.Boolean, nullable=False)
    irp_prohibition_type = db.Column(db.String(20), nullable=False)
    witnessed_by_officer = db.Column(db.Boolean, nullable=False)
    admission_by_driver = db.Column(db.Boolean, nullable=False)
    independent_witness = db.Column(db.Boolean, nullable=False)
    reasonable_ground_other = db.Column(db.Boolean, nullable=False)
    time_of_suspicion = db.Column(db.String(5))
    time_of_asd = db.Column(db.String(5))
    refused_or_fail = db.Column(db.String(5))
    time_of_refusal = db.Column(db.String(5))
    right_to_second_test = db.Column(db.String(5))
    lower_asd_prevail = db.Column(db.String(5))
    right_to_test_different_asd = db.Column(db.String(5))
    driver_requested_second_asd = db.Column(db.String(5))
    reasonable_suspicion_odor_of_liquor = db.Column(db.Boolean)
    reasonable_suspicion_admission = db.Column(db.Boolean)
    reasonable_suspicion_witnessed = db.Column(db.Boolean)
    reasonable_suspicion_other = db.Column(db.Boolean)
    last_drink = db.Column(db.String(100))
    continuous_observation = db.Column(db.String(5))

    asd_tests = db.relationship('IRPASDTest', backref='irp_form', cascade='all, delete-orphan')