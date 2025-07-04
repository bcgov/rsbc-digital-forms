import json
import csv
import pytz
import logging
import logging.config
import datetime
from python.common.config import Config

logging.config.dictConfig(Config.LOGGING)

local_tz = pytz.timezone('America/Vancouver')

def load_permissions_into_dict(data):
    officer_roles = {'permissions':[]}
    admin_roles = {'permissions':[]}
    for permission in data:
        if permission.role == 'officer':
            officer_roles['permissions'].append(permission.permission)
        elif permission.role == 'administrator':
            admin_roles['permissions'].append(permission.permission)
    return {'officer':officer_roles, 'administrator':admin_roles}

def load_json_into_dict(file_name) -> dict:
    with open(file_name, 'r') as f:
        data = f.read()
    return json.loads(data)


def get_csv_test_data(file_and_path):
    test_data = list()
    with open(file_and_path, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row_number, row in enumerate(data):
            # exclude the header row
            if row_number != 0:
                test_data.append(row)
    return test_data


def load_xml_to_string(file_name) -> str:
    with open(file_name, 'r') as f:
        return f.read()


def validate_form_number(number: str) -> bool:
    """
    Validate check digit used in IRP, VI and UL forms
    :param number:
    :return:
    """
    number_list = list(number)
    check_digit = int(number_list.pop())

    n = list()
    for element in number_list:
        # cast each element to an int
        n.append(int(element))

    # ignore the first two digits, sum the number
    # using a special formula
    number_sum = (
            n[2] +
            _times_2(n[3]) +
            n[4] +
            _times_2(n[5]) +
            n[6] +
            _times_2(n[7]))

    # compare modulus of the sum with check digit
    return number_sum % 10 == check_digit


def _times_2(number: int) -> int:
    """
    If number * 2 is greater than 9, return 1
    otherwise return the number * 2
    :param number:
    :return:
    """
    return int(list(str(number * 2))[0])


def middle_logic(functions: list, **args):
    """
    Recursive function that calls each node in the list.
    Each node has a "try" function that is executed first. If the try
    function returns True, the next node in the list is returned.  If the
    try function returns False, the node's "fail" list is executed in the
    same way.

    example = dict({
            "rules": [
                {
                    "pass": success1,
                    "fail": [
                        {
                            "pass": failure1,
                            "fail": []
                        }
                    ],
                },
            ]
        })

    The middleware is called like this: middle_logic(example['rules'])
    """
    if functions:
        try_fail_node = functions.pop(0)
        logging.debug('calling try function: ' + try_fail_node['try'].__name__)
        flag, args = try_fail_node['try'](**args)
        logging.debug("result from {} is {}".format(try_fail_node['try'].__name__, flag))
        if flag:
            args = middle_logic(functions, **args)
        else:
            logging.debug('calling try function: ' + try_fail_node['try'].__name__)
            args = middle_logic(try_fail_node['fail'], **args)
    return args


def get_listeners(listeners: dict, key: str) -> list:
    """
    Get the list of nested list of functions to invoke
    for a particular form type
    """
    if key in listeners:
        return listeners[key]
    else:
        return listeners['unknown_event']


def localize_timezone(date_time: datetime) -> datetime:
    localized = local_tz.localize(date_time)
    logging.debug("localized datetime: {}".format(localized))
    return localized


def check_credentials(username, password, username_submitted, password_submitted) -> bool:
    logging.debug('credentials: {}:{}'.format(username, password))
    if username_submitted == username and password_submitted == password:
        return True
    return False

def date_time_to_local_tz_string(date: datetime, format_string: str = "%Y-%m-%d %H:%M:%S") -> str:
    tmp_formatted=date.replace(tzinfo=datetime.timezone.utc).astimezone(tz=local_tz)
    return format_date_time(tmp_formatted, format_string)

def format_date_time(date, format_string: str = "%Y-%m-%d %H:%M:%S") -> str:
    if date is None or date == '':
        return None
    return date.strftime(format_string)

def format_date_only(date) -> str:
    if date is None or date == '':
        return None
    format_string = "%Y-%m-%d"
    return date.replace(tzinfo=datetime.timezone.utc).astimezone(tz=local_tz).strftime(format_string)

def yes_no_string_to_bool(value):
    if value is None or value == '':
        return None
    return value.upper() == 'YES'