from datetime import date, time, datetime
from decimal import Decimal
from flask.json.provider import DefaultJSONProvider

class CustomJSONEncoder(DefaultJSONProvider):
    def default(self, obj):
        if isinstance(obj, (date, time, datetime)):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)