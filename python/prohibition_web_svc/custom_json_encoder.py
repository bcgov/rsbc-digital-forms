from datetime import date, time, datetime
from decimal import Decimal
from json import JSONEncoder

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (date, time, datetime)):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)