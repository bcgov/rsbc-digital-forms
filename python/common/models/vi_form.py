from dataclasses import dataclass
from datetime import datetime
from .base import db

@dataclass
class VIForm(db.Model):
    __tablename__ = 'vi_form'

    form_id: int
    event_id: int
    created_dt: datetime
    updated_dt: datetime
    gender: str
    driver_is_regist_owner: bool
    driver_licence_expiry: datetime
    driver_licence_class: str
    unlicenced_prohibition_number: str
    belief_driver_bc_resident: str
    out_of_province_dl: str
    out_of_province_dl_number: str
    out_of_province_dl_expiry: str
    out_of_province_dl_jurisdiction: str
    date_of_impound: datetime
    irp_impound: str
    irp_impound_duration: str
    IRP_number: str
    VI_number: str
    excessive_speed: str
    prohibited: bool
    suspended: bool
    street_racing: bool
    stunt_driving: bool
    motorcycle_seating: bool
    motorcycle_restrictions: bool
    unlicensed: bool
    linkage_location_of_keys: bool
    linkage_location_of_keys_explanation: str
    linkage_driver_principal: bool
    linkage_owner_in_vehicle: bool
    linkage_owner_aware_possesion: bool
    linkage_vehicle_transfer_notice: bool
    linkage_other: bool
    speed_limit: str
    vehicle_speed: str
    speed_estimation_technique: str
    speed_confirmation_technique: str
    incident_details: str
    incident_details_extra_page: bool

    form_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    gender = db.Column(db.String)
    driver_is_regist_owner = db.Column(db.String)
    driver_licence_expiry = db.Column(db.DateTime)
    driver_licence_class = db.Column(db.String)
    unlicenced_prohibition_number = db.Column(db.String)
    belief_driver_bc_resident = db.Column(db.String)
    out_of_province_dl = db.Column(db.String)
    out_of_province_dl_number = db.Column(db.String)
    out_of_province_dl_expiry = db.Column(db.String)
    out_of_province_dl_jurisdiction = db.Column(db.String)
    date_of_impound = db.Column(db.DateTime)
    irp_impound = db.Column(db.String)
    irp_impound_duration = db.Column(db.String)
    IRP_number = db.Column(db.String)
    VI_number = db.Column(db.String)
    excessive_speed = db.Column(db.Boolean)
    prohibited = db.Column(db.Boolean)
    suspended = db.Column(db.Boolean)
    street_racing = db.Column(db.Boolean)
    stunt_driving = db.Column(db.Boolean)
    motorcycle_seating = db.Column(db.Boolean)
    motorcycle_restrictions = db.Column(db.Boolean)
    unlicensed = db.Column(db.Boolean)
    linkage_location_of_keys = db.Column(db.Boolean)
    linkage_location_of_keys_explanation = db.Column(db.String)
    linkage_driver_principal = db.Column(db.Boolean)
    linkage_owner_in_vehicle = db.Column(db.Boolean)
    linkage_owner_aware_possesion = db.Column(db.Boolean)
    linkage_vehicle_transfer_notice = db.Column(db.Boolean)
    linkage_other = db.Column(db.Boolean)
    speed_limit = db.Column(db.String)
    vehicle_speed = db.Column(db.String)
    speed_estimation_technique = db.Column(db.String)
    speed_confirmation_technique = db.Column(db.String)
    incident_details = db.Column(db.String)
    incident_details_extra_page = db.Column(db.Boolean)
    created_dt = db.Column(db.DateTime)
    updated_dt = db.Column(db.DateTime)
