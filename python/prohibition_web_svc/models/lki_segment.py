from typing import TypedDict


class LkiSegment(TypedDict):
    code: str
    hwy_code: str
    description: str
    direction: str
    length_km: float