from dataclasses import dataclass
from .base import db

@dataclass
class ImpoundReasonCodes(db.Model):
    __tablename__ = 'impound_reason_codes'

    df_unique_code: str
    impound_reason_name: str
    vips_value_cd: str
    vips_value_dsc: str
    vips_value_abbreviated_dsc: str  

    df_unique_code = db.Column(db.String, primary_key=True)
    impound_reason_name = db.Column(db.String)
    vips_value_cd = db.Column(db.String)
    vips_value_dsc = db.Column(db.String)
    vips_value_abbreviated_dsc = db.Column(db.String)
