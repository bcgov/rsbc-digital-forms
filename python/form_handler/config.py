import os
from python.common.config import Config as BaseConfig


class Config(BaseConfig):
    WATCH_QUEUE                         = os.getenv('WATCH_QUEUE', 'DF.valid')
    HOLD_QUEUE                          = os.getenv('HOLD_QUEUE', 'DF.hold')
    FAIL_QUEUE                          = os.getenv('FAIL_QUEUE', 'DF.fail')
    STORAGE_WATCH_QUEUE = os.getenv('STORAGE_WATCH_QUEUE', 'df-storage-events')
    STORAGE_HOLD_QUEUE = os.getenv('STORAGE_HOLD_QUEUE', 'df-storage-events-hold')
    STORAGE_FAIL_QUEUE = os.getenv('STORAGE_FAIL_QUEUE', 'df-storage-events-fail')

    DB_HOST = os.environ.get('DB_HOST', 'db')
    DB_USER = os.environ.get('DB_USER', 'testuser')
    DB_PASS = os.environ.get('DB_PASS', 'pass')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    DB_NAME = os.environ.get('DB_NAME', 'test')
    DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    FLASK_SECRET_KEY = "12345"
    LOGGERS_IN_USE = os.getenv('LOGGERS_IN_USE', 'console').split()
    LOG_FORMAT = "%(asctime)s::%(levelname)s::%(name)s::%(message)s"
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG').upper()
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'json': {
                '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
                'format': '%(asctime)s %(filename)s %(funcName)s %(levelname)s %(lineno)d %(module)s %(message)s %(pathname)s'
            },
            'brief': {
                'format': LOG_FORMAT
            }
        },
        'handlers': {
            'console': {
                'level': LOG_LEVEL,
                'class': 'logging.StreamHandler',
                'formatter': 'brief'
            }
        },
        'loggers': {
            '': {
                'handlers': LOGGERS_IN_USE,
                'level': LOG_LEVEL
            }
        }
    }

    # DAYS_TO_DELAY_FOR_VIPS_DATA_ENTRY   = os.getenv('DAYS_TO_DELAY_FOR_VIPS_DATA_ENTRY', '8')
    # HOURS_TO_HOLD_BEFORE_TRYING_VIPS    = os.getenv('HOURS_TO_HOLD_BEFORE_TRYING_VIPS', '12')
    #
    # HOURS_TO_HOLD_BEFORE_DISCLOSURE     = os.getenv('HOURS_TO_HOLD_BEFORE_DISCLOSURE', '24')
    # DAYS_ELAPSED_TO_RESEND_DISCLOSURE   = int(os.getenv('DAYS_ELAPSED_TO_RESEND_DISCLOSURE', '30'))
    #
    # VIPS_API_ROOT_URL                   = os.getenv('VIPS_API_ROOT_URL', 'http://localhost')
    # VIPS_API_USERNAME                   = os.getenv('VIPS_API_USERNAME', 'user')
    # VIPS_API_PASSWORD                   = os.getenv('VIPS_API_PASSWORD', 'password')
    #
    # LINK_TO_PAYBC                       = os.getenv('LINK_TO_PAYBC', 'http://localhost')
    # LINK_TO_SCHEDULE_FORM               = os.getenv('LINK_TO_SCHEDULE_FORM', 'http://localhost')
    # LINK_TO_EVIDENCE_FORM               = os.getenv('LINK_TO_EVIDENCE_FORM', 'http://localhost')
    # LINK_TO_APPLICATION_FORM            = os.getenv('LINK_TO_APPLICATION_FORM', 'http://localhost')
    #
    # LINK_TO_ICBC                        = os.getenv('LINK_TO_ICBC', 'http://localhost')
    #
    # LINK_TO_SERVICE_BC                  = os.getenv('LINK_TO_SERVICE_BC', 'http://localhost')
    #
    # LINK_TO_GET_DRIVING_RECORD          = os.getenv('LINK_TO_GET_DRIVING_RECORD', 'http://localhost')
