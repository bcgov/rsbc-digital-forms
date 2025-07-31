from dataclasses import dataclass
from datetime import datetime
from .base import db

@dataclass
class Event(db.Model):
    __tablename__ = 'event'

    event_id: int
    icbc_sent_status: str
    vi_sent_status: str
    icbc_retry_count: int
    vi_retry_count: int
    driver_licence_no: str
    driver_jurisdiction: str
    driver_last_name: str
    driver_given_name: str
    driver_dob: datetime
    driver_address: str
    driver_city: str
    driver_prov: str
    driver_postal: str
    driver_phone: str
    date_of_driving: datetime
    time_of_driving: str
    vehicle_jurisdiction: str
    vehicle_plate_no: str
    vehicle_registration_no: str
    vehicle_year: str
    vehicle_mk_md: str
    vehicle_style: str
    vehicle_type: int
    vehicle_colour: str
    vehicle_vin_no: str
    nsc_prov_state: str
    location_of_keys: str
    nsc_no: str
    type_of_prohibition: str
    owned_by_corp: bool
    vehicle_released_to: str
    date_released: datetime
    time_released: str
    intersection_or_address_of_offence: str
    offence_city: str
    corporation_name: str
    regist_owner_last_name: str
    regist_owner_first_name: str
    regist_owner_address: str
    regist_owner_dob: datetime
    regist_owner_city: str
    regist_owner_prov: str
    regist_owner_postal: str
    regist_owner_phone: str
    regist_owner_email: str
    agency_file_no: str
    submitted: bool
    confirmation_of_service: bool
    confirmation_of_service_date: datetime
    impound_lot_operator: int
    task_processing_status: str
    created_dt: datetime
    updated_dt: datetime
    created_by: str
    updated_by: str
    ff_application_id: int

    event_id = db.Column(db.Integer, primary_key=True)
    icbc_sent_status = db.Column(db.String)
    vi_sent_status = db.Column(db.String)
    icbc_retry_count = db.Column(db.Integer)
    vi_retry_count = db.Column(db.Integer)
    type_of_prohibition = db.Column(db.String)
    driver_licence_no = db.Column(db.String)
    driver_jurisdiction = db.Column(db.String)
    driver_last_name = db.Column(db.String)
    driver_given_name = db.Column(db.String)
    driver_dob = db.Column(db.DateTime)
    driver_address = db.Column(db.String)
    driver_city = db.Column(db.String)
    driver_prov = db.Column(db.String)
    driver_postal = db.Column(db.String)
    driver_phone = db.Column(db.String)
    agency_file_no = db.Column(db.String)
    date_of_driving = db.Column(db.DateTime)
    time_of_driving = db.Column(db.String)
    vehicle_jurisdiction = db.Column(db.String)
    vehicle_plate_no = db.Column(db.String)
    vehicle_registration_no = db.Column(db.String)
    vehicle_year = db.Column(db.String)
    vehicle_mk_md = db.Column(db.String)
    vehicle_style = db.Column(db.String)
    vehicle_type = db.Column(db.Integer, db.ForeignKey('vehicle_type.type_cd'))
    vehicle_colour = db.Column(db.String)
    vehicle_vin_no = db.Column(db.String)
    nsc_prov_state = db.Column(db.String)
    location_of_keys = db.Column(db.String)
    nsc_no = db.Column(db.String)
    submitted = db.Column(db.Boolean)
    owned_by_corp = db.Column(db.Boolean)
    vehicle_released_to = db.Column(db.String)
    date_released = db.Column(db.DateTime)
    time_released = db.Column(db.String)
    intersection_or_address_of_offence = db.Column(db.String)
    offence_city = db.Column(db.String)
    corporation_name = db.Column(db.String)
    regist_owner_last_name = db.Column(db.String)
    regist_owner_first_name = db.Column(db.String)
    regist_owner_address = db.Column(db.String)
    regist_owner_dob = db.Column(db.DateTime)
    regist_owner_city = db.Column(db.String)
    regist_owner_prov = db.Column(db.String)
    regist_owner_postal = db.Column(db.String)
    regist_owner_phone = db.Column(db.String)
    regist_owner_email = db.Column(db.String)
    impound_lot_operator = db.Column(db.Integer, db.ForeignKey('impound_lot_operator.id'))
    confirmation_of_service = db.Column(db.Boolean)
    confirmation_of_service_date = db.Column(db.DateTime)
    task_processing_status = db.Column(db.String)
    created_by = db.Column(db.String, db.ForeignKey('user.user_guid'))
    updated_by = db.Column(db.String)
    created_dt = db.Column(db.DateTime)
    updated_dt = db.Column(db.DateTime)
    ff_application_id = db.Column(db.Integer)

    twenty_four_hour_form = db.relationship('TwentyFourHourForm', backref='event', lazy='joined', uselist=False)
    twelve_hour_form = db.relationship('TwelveHourForm', backref='event', lazy='joined', uselist=False)
    vi_form = db.relationship('VIForm', backref='event', lazy='joined', uselist=False)
    irp_form = db.relationship('IRPForm', backref='event', lazy='joined', uselist=False)
