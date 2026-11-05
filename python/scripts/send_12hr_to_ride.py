# This script looks up 12hr forms by 12hr number from the database
# and sends the corresponding events to RIDE via ride_actions.twelve_hours_event.

import argparse
import logging
import sys

from flask import Flask

from python.common.models.base import db
from python.common.models.event import Event
from python.common.models.user import User
from python.common.models.twelve_hour_form import TwelveHourForm
from python.common.verbose_logging import VERBOSE_LEVEL_NUM, verbose
import python.common.ride_actions as ride_actions
from python.form_handler.config import Config
from python.form_handler import actions as form_actions

logging.addLevelName(VERBOSE_LEVEL_NUM, 'VERBOSE')
logging.verbose = verbose
logging.basicConfig(level=Config.LOG_LEVEL, format=Config.LOG_FORMAT)

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['SQLALCHEMY_ECHO'] = False

db.init_app(application)


def get_twelve_hour_numbers(file_path, header_1st_row=False):
    with open(file_path, encoding='utf-8') as numbers_file:
        lines = [line.strip().split(',')[0].replace('"', '')
                 for line in numbers_file if line.strip()]
        if header_1st_row:
            lines = lines[1:]
        return lines


def build_ride_args(twelve_hour_number):
    with application.app_context():
        form = db.session.query(TwelveHourForm) \
            .filter(TwelveHourForm.twelve_hour_number == twelve_hour_number).first()
        if form is None:
            logging.error(f"No 12hr form found for 12hr number: {twelve_hour_number}")
            return None

        event = db.session.query(Event).filter(Event.event_id == form.event_id).first()
        if event is None:
            logging.error(f"No event found for event_id: {form.event_id}")
            return None

        user = db.session.query(User).filter(User.user_guid == event.created_by).first()
        if user is None:
            logging.error(f"No user found for user_guid: {event.created_by}")
            return None

        if user.agency_ref is None:
            logging.error(f"No agency found for user_guid: {event.created_by}")
            return None

        event_data = {
            'created_dt': event.created_dt,
            'type_of_prohibition': event.type_of_prohibition,
            'driver_licence_no': event.driver_licence_no,
            'driver_city': event.driver_city,
            'driver_prov': event.driver_prov,
            'driver_postal': event.driver_postal,
            'driver_jurisdiction': event.driver_jurisdiction,
            'driver_dob': event.driver_dob,
            'vehicle_jurisdiction': event.vehicle_jurisdiction,
            'vehicle_plate_no': event.vehicle_plate_no,
            'vehicle_registration_no': event.vehicle_registration_no,
            'vehicle_year': event.vehicle_year,
            'vehicle_mk_md': event.vehicle_mk_md,
            'vehicle_style': event.vehicle_style,
            'owned_by_corp': event.owned_by_corp,
            'corporation_name': event.corporation_name,
            'date_of_driving': event.date_of_driving,
            'time_of_driving': event.time_of_driving,
            'agency_file_no': event.agency_file_no,
            'date_released': event.date_released,
            'time_released': event.time_released,
            'vehicle_type': event.vehicle_type,
            'intersection_or_address_of_offence': event.intersection_or_address_of_offence,
            'offence_city': event.offence_city,
            'impound_lot_operator': event.impound_lot_operator,
        }

        form_data = {
            'twelve_hour_number': form.twelve_hour_number,
            'driver_phone': form.driver_phone,
            'vehicle_location': form.vehicle_location,
        }

        user_data = {
            'display_name': user.display_name,
            'badge_number': user.badge_number,
            'agency_ref': {
                'id': user.agency_ref.id,
                'agency_name': user.agency_ref.agency_name,
                'vjur': user.agency_ref.vjur,
            },
        }

        event_id = event.event_id

    return {
        'message': {'event_id': event_id, 'event_type': '12hr'},
        'event_data': event_data,
        'form_data': form_data,
        'user_data': user_data,
        'db': db,
        'app': application,
    }


def send_twelve_hour_to_ride(twelve_hour_number):
    ride_args = build_ride_args(twelve_hour_number)
    if ride_args is None:
        return False

    _, ride_args = form_actions.get_event_coordinates(**ride_args)
    success, result = ride_actions.twelve_hours_event(**ride_args)
    if success:
        logging.info(f"Successfully sent 12hr event to RIDE for 12hr number: {twelve_hour_number}")
        return True

    error = result.get('error', {})
    logging.error(
        f"Failed to send 12hr event to RIDE for 12hr number: {twelve_hour_number}. "
        f"Error: {error.get('error_details', 'unknown')}"
    )
    return False


def main():
    parser = argparse.ArgumentParser(
        description="Fetch 12hr forms from the database and send them to RIDE"
    )
    parser.add_argument(
        '--twelve_hour_numbers_file',
        required=True,
        help='Path to a text file containing one 12hr number per line',
    )
    parser.add_argument(
        '--header-1st-row',
        action='store_true',
        help='Indicates that the first row of the numbers file is a header and should be skipped',
    )
    args = parser.parse_args()

    numbers = get_twelve_hour_numbers(
        args.twelve_hour_numbers_file, header_1st_row=args.header_1st_row)
    if len(numbers) == 0:
        logging.error(f"No 12hr numbers found in file: {args.twelve_hour_numbers_file}")
        sys.exit(1)

    failed = []
    with open('sent_12hr_number.txt', mode='a') as sent_file:
        for number in numbers:
            if not send_twelve_hour_to_ride(number):
                failed.append(number)
            else:
                sent_file.write(number)
                sent_file.write('\n')
                sent_file.flush()

    if len(failed) > 0:
        logging.error(
            "Failed to send %s 12hr event(s) to RIDE: %s",
            len(failed),
            ", ".join(failed),
        )
        sys.exit(1)

    logging.info("Successfully sent %s 12hr event(s) to RIDE", len(numbers))


if __name__ == "__main__":
    main()
