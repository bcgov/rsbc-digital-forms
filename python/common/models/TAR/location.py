from dataclasses import dataclass
from decimal import Decimal
from ..base import db

@dataclass
class TarLocation(db.Model):
    __tablename__ = 'tar_location'
    __table_args__ = {'schema': 'TAR'}

    location_id: int
    collision_case_num: str
    hwy_code: str
    hwy_route_num: str
    segment_num: str
    loc_code_km: Decimal
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
    collision_case_num = db.Column(db.String, db.ForeignKey('tar_collision.collision_case_num'), nullable=False)
    hwy_code = db.Column(db.String, nullable=False)
    hwy_route_num = db.Column(db.String(4))
    segment_num = db.Column(db.String(4))
    loc_code_km = db.Column(db.Numeric(precision=6, scale=2))
    city_name = db.Column(db.String, nullable=False)
    city_status = db.Column(db.String(30))
    street_on = db.Column(db.String(255))
    street_at = db.Column(db.String(255))
    street_desc = db.Column(db.String(60))
    gps_format = db.Column(db.String(1))
    lat_decim_degrees = db.Column(db.Numeric(precision=9, scale=6), nullable=False)
    long_decim_degrees = db.Column(db.Numeric(precision=9, scale=6), nullable=False)
    lat_degree = db.Column(db.Integer)
    lat_min = db.Column(db.Integer)
    lat_sec = db.Column(db.Numeric(precision=4, scale=10))
    long_degree = db.Column(db.Integer)
    long_min = db.Column(db.Integer)
    long_sec = db.Column(db.Numeric(precision=4, scale=10))
    road_class = db.Column(db.String(2), db.ForeignKey('tar_road_class.code'), nullable=False)
    traffic_flow = db.Column(db.String(2), db.ForeignKey('tar_traffic_flow.code'), nullable=False)
    collision_loc = db.Column(db.String(2), db.ForeignKey('tar_collision_location.code'), nullable=False)
    primary_speed_zone = db.Column(db.String(3), db.ForeignKey('tar_speed_zone.code'), nullable=False)
    secondary_speed_zone = db.Column(db.String(3), db.ForeignKey('tar_speed_zone.code'))
    land_usage = db.Column(db.String(2), db.ForeignKey('tar_land_usage.code'), nullable=False)
    road_type = db.Column(db.String(2), db.ForeignKey('tar_road_type.code'), nullable=False)
    traffic_control = db.Column(db.String(2), db.ForeignKey('tar_traffic_control.code'))
    roadway_character = db.Column(db.String(2), db.ForeignKey('tar_roadway_character.code'), nullable=False)
    roadway_surface_cond = db.Column(db.String(2), db.ForeignKey('tar_roadway_condition.code'), nullable=False)
    weather_cond = db.Column(db.String(2), db.ForeignKey('tar_weather_condition.code'), nullable=False)
    lighting_cond = db.Column(db.String(2), db.ForeignKey('tar_lighting_condition.code'), nullable=False)
