
import logging
from python.common.models import City


def get_city_name(city_code, args) -> str:
    application = args.get('app')
    db = args.get('db')
    with application.app_context():
        city_data = db.session.query(City) \
                        .filter(City.objectCd == city_code) \
                        .all()
        if len(city_data) == 0:
            logging.error("city not found")
        else:
            return city_data[0].objectDsc