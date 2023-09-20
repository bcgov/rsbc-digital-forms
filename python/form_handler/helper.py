
import json
import csv
import pytz
import logging
import logging.config
import datetime
from python.common.config import Config

logging.config.dictConfig(Config.LOGGING)


def get_listeners(listeners: dict, key: str) -> list:
    """
    Get the list of nested list of functions to invoke
    for a particular form type
    """
    if key in listeners:
        return listeners[key]
    else:
        return listeners['unknown_event']