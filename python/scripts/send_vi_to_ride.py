# This script looks up VI forms by VI number from the database
# and sends the corresponding events to RIDE via ride_actions.vi_event.

import argparse
import logging
import sys

from flask import Flask

from python.common.models.base import db
from python.common.models.event import Event
from python.common.models.user import User
from python.common.models.vi_form import VIForm
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


def get_vi_numbers(file_path, header_1st_row=False):
    with open(file_path, encoding='utf-8') as vi_numbers_file:
        lines = [line.strip().split(',')[0].replace('"', '') \
                 for line in vi_numbers_file if line.strip()]
        if header_1st_row:
            lines = lines[1:]
        return lines


def build_ride_args(vi_number):
    with application.app_context():
        vi_form = db.session.query(VIForm).filter(VIForm.VI_number == vi_number).first()
        if vi_form is None:
            logging.error(f"No VI form found for VI number: {vi_number}")
            return None

        event = db.session.query(Event).filter(Event.event_id == vi_form.event_id).first()
        if event is None:
            logging.error(f"No event found for event_id: {vi_form.event_id}")
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
            'VI_number': vi_form.VI_number,
            'gender': vi_form.gender,
            'driver_licence_class': vi_form.driver_licence_class,
            'out_of_province_dl': vi_form.out_of_province_dl,
            'date_of_impound': vi_form.date_of_impound,
            'unlicenced_prohibition_number': vi_form.unlicenced_prohibition_number,
            'irp_impound': vi_form.irp_impound,
            'IRP_number': vi_form.IRP_number,
            'irp_impound_duration': vi_form.irp_impound_duration,
            'excessive_speed': vi_form.excessive_speed,
            'prohibited': vi_form.prohibited,
            'suspended': vi_form.suspended,
            'street_racing': vi_form.street_racing,
            'stunt_driving': vi_form.stunt_driving,
            'motorcycle_seating': vi_form.motorcycle_seating,
            'motorcycle_restrictions': vi_form.motorcycle_restrictions,
            'unlicensed': vi_form.unlicensed,
            'driver_is_regist_owner': vi_form.driver_is_regist_owner,
            'speed_limit': vi_form.speed_limit,
            'vehicle_speed': vi_form.vehicle_speed,
            'speed_estimation_technique': vi_form.speed_estimation_technique,
            'speed_confirmation_technique': vi_form.speed_confirmation_technique,
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

    return {
        'message': {'event_id': event.event_id, 'event_type': 'vi'},
        'event_data': event_data,
        'form_data': form_data,
        'user_data': user_data,
        'db': db,
        'app': application,
    }


def send_vi_to_ride(vi_number):
    ride_args = build_ride_args(vi_number)
    if ride_args is None:
        return False

    _, ride_args = form_actions.get_event_coordinates(**ride_args)
    success, result = ride_actions.vi_event(**ride_args)
    if success:
        logging.info(f"Successfully sent VI event to RIDE for VI number: {vi_number}")
        return True

    error = result.get('error', {})
    logging.error(
        f"Failed to send VI event to RIDE for VI number: {vi_number}. "
        f"Error: {error.get('error_details', 'unknown')}"
    )
    return False


def main():
    parser = argparse.ArgumentParser(
        description="Fetch VI forms from the database and send them to RIDE"
    )
    parser.add_argument(
        '--vi_numbers_file',
        required=True,
        help='Path to a text file containing one VI number per line',
    )
    parser.add_argument(
        '--header-1st-row',
        help='Indicates that the first row of the VI numbers file is a header and should be skipped',
    )
    args = parser.parse_args()

    vi_numbers = get_vi_numbers(args.vi_numbers_file, header_1st_row=args.header_1st_row)
    if len(vi_numbers) == 0:
        logging.error(f"No VI numbers found in file: {args.vi_numbers_file}")
        sys.exit(1)

    failed_vi_numbers = []
    with open('sent_vi_number.txt', mode='a') as sent_vi_file:
        for vi_number in vi_numbers:
            if not send_vi_to_ride(vi_number):
                failed_vi_numbers.append(vi_number)
            else:
                sent_vi_file.write(vi_number)
                sent_vi_file.write('\n')
                sent_vi_file.flush()

    if len(failed_vi_numbers) > 0:
        logging.error(
            "Failed to send %s VI event(s) to RIDE: %s",
            len(failed_vi_numbers),
            ", ".join(failed_vi_numbers),
        )
        sys.exit(1)

    logging.info("Successfully sent %s VI event(s) to RIDE", len(vi_numbers))


if __name__ == "__main__":
    main()
