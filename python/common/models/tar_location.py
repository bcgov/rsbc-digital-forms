from dataclasses import dataclass
from decimal import Decimal
from .base import db

@dataclass
class TarLocation(db.Model):
    __tablename__ = 'location'

    location_id: int
    collision_case_num: str
    hwy_code: str
    hwy_route_num: str
    segment_num: str
    loc_code_km: str
    city_name: str
    city_status: str
    street_on: str
    street_at: str
    street_desc: str
    gps_format: str
    lat_decim_degrees: Decimal
    long_decim_degrees: Decimal
    lat_degree: int
    lat_min: int
    lat_sec: Decimal
    long_degree: int
    long_min: int
    long_sec: Decimal
    road_class: str
    traffic_flow: str
    collision_loc: str
    primary_speed_zone: str
    secondary_speed_zone: str
    land_usage: str
    road_type: str
    traffic_control: str
    roadway_character: str
    roadway_surface_cond: str
    weather_cond: str
    lighting_cond: str

    location_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    collision_case_num = db.Column(db.String, db.ForeignKey('collision.collision_case_num'), nullable=False)
    hwy_code = db.Column(db.String, nullable=False)
    hwy_route_num = db.Column(db.String)
    segment_num = db.Column(db.String)
    loc_code_km = db.Column(db.String)
    city_name = db.Column(db.String, nullable=False)
    city_status = db.Column(db.String)
    street_on = db.Column(db.String)
    street_at = db.Column(db.String)
    street_desc = db.Column(db.String)
    gps_format = db.Column(db.String)
    lat_decim_degrees = db.Column(db.Numeric(precision=9, scale=6), nullable=False)
    long_decim_degrees = db.Column(db.Numeric(precision=9, scale=6), nullable=False)
    lat_degree = db.Column(db.Integer)
    lat_min = db.Column(db.Integer)
    lat_sec = db.Column(db.Decimal(precision=4, scale=10))
    long_degree = db.Column(db.Integer)
    long_min = db.Column(db.Integer)
    long_sec = db.Column(db.Decimal(precision=4, scale=10))
    road_class = db.Column(db.String, nullable=False)
    traffic_flow = db.Column(db.String, nullable=False)
    collision_loc = db.Column(db.String, nullable=False)
    primary_speed_zone = db.Column(db.String, nullable=False)
    secondary_speed_zone = db.Column(db.String, nullable=False)
    land_usage = db.Column(db.String, nullable=False)
    road_type = db.Column(db.String, nullable=False)
    traffic_control = db.Column(db.String, nullable=False)
    roadway_character = db.Column(db.String, nullable=False)
    roadway_surface_cond = db.Column(db.String, nullable=False)
    weather_cond = db.Column(db.String, )
    lighting_cond = db.Column(db.String, nullable=False)
