import os
# from python.common.config import Config as BaseConfig


class Config():
    WATCH_QUEUE                         = os.getenv('WATCH_QUEUE', 'DF.valid')
    HOLD_QUEUE                          = os.getenv('HOLD_QUEUE', 'DF.hold')
    FAIL_QUEUE                          = os.getenv('FAIL_QUEUE', 'DF.fail')
    STORAGE_WATCH_QUEUE = os.getenv('STORAGE_WATCH_QUEUE', 'df-storage-events')
    STORAGE_HOLD_QUEUE = os.getenv('STORAGE_HOLD_QUEUE', 'df-storage-events-hold')
    STORAGE_FAIL_QUEUE = os.getenv('STORAGE_FAIL_QUEUE', 'df-storage-events-fail')
    STORAGE_FAIL_QUEUE_PERS=os.getenv('STORAGE_FAIL_QUEUE_PERS', 'df-storage-events-fail-persistent')
    EVENT_TYPES                         = os.getenv('EVENT_TYPES', 'vi,24h,12h,irp').split(',')
    PENDING_EVENT_STATUSES = os.getenv('PENDING_EVENT_STATUSES', 'pending,retrying').split(',')

    DB_HOST = os.environ.get('DB_HOST', 'db')
    DB_USER = os.environ.get('DB_USER', 'testuser')
    DB_PASS = os.environ.get('DB_PASS', 'pass')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    DB_NAME = os.environ.get('DB_NAME', 'test')
    DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY', '12345')
    LOGGERS_IN_USE = os.getenv('LOGGERS_IN_USE', 'console').split()
    LOG_FORMAT = "[DF_FORM_HANDLER] %(asctime)s::%(levelname)s::%(name)s::%(message)s"
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG').upper()
    SYSTEM_RECORD_MAX_RETRIES = int(os.environ.get('SYSTEM_RECORD_MAX_RETRIES', 2))
    SYSTEM_RECORD_MAX_TRANSIENT_RETRIES = int(os.environ.get('SYSTEM_RECORD_MAX_TRANSIENT_RETRIES', 2))

    STORAGE_HOST = os.environ.get('STORAGE_HOST', 'localhost')
    STORAGE_PORT = os.environ.get('STORAGE_PORT', 9000)
    STORAGE_ACCESS_KEY = os.environ.get('STORAGE_ACCESS_KEY', 'vEful9aJZRjNCP3dQwQ9')
    STORAGE_SECRET_KEY= os.environ.get('STORAGE_SECRET_KEY', 'KWCldKNT4zbirer12GA290MJBjTNAXIZMEmNXkY8')

    RABBITMQ_URL                        = os.getenv('RABBITMQ_URL', 'localhost')
    RABBITMQ_USER                       = os.getenv('RABBITMQ_USER')
    RABBITMQ_PASS                       = os.getenv('RABBITMQ_PASS')
    RABBITMQ_PORT                       = os.getenv('RABBITMQ_PORT', '5672')
    RABBITMQ_EXCHANGE                   = os.getenv('RABBITMQ_EXCHANGE', '')
    MAX_CONNECTION_RETRIES              = os.getenv('MAX_CONNECTION_RETRIES', 25)
    RETRY_DELAY                         = os.getenv('RETRY_DELAY', 30)
    RABBITMQ_MESSAGE_ENCODE             = os.getenv('RABBITMQ_MESSAGE_ENCODE', 'utf-8')
    ENCRYPT_KEY                         = os.getenv('ENCRYPT_KEY','secret')
    ENCRYPT_KEY_SALT = os.getenv('ENCRYPT_KEY_SALT', 'aaaa')


    ICBC_API_ROOT = os.getenv('ICBC_API_ROOT', 'http://localhost:5003')
    ICBC_API_USERNAME = os.getenv('ICBC_API_USERNAME', 'user')
    ICBC_API_PASSWORD = os.getenv('ICBC_API_PASSWORD', 'password')
    ICBC_API_SUBMIT_ROOT = os.getenv('ICBC_API_SUBMIT_ROOT', 'http://localhost:5003')
    ICBC_API_SUBMIT_USERNAME = os.getenv('ICBC_API_SUBMIT_USERNAME', 'user')
    ICBC_API_SUBMIT_PASSWORD = os.getenv('ICBC_API_SUBMIT_PASSWORD', 'password')


    VIPS_ROOT = os.getenv('VIPS_ROOT', 'http://localhost:5003')
    VIPS_API_USERNAME = os.getenv('VIPS_API_USERNAME', 'user')
    VIPS_API_PASSWORD = os.getenv('VIPS_API_PASSWORD', 'password')

    COMM_SERV_AUTH_URL = os.getenv('COMM_SERV_AUTH_URL', 'http://localhost')
    COMM_SERV_API_ROOT_URL = os.getenv('COMM_SERV_API_ROOT_URL', 'http://localhost')
    COMM_SERV_REALM = os.getenv('COMM_SERV_REALM', 'realm')
    COMM_SERV_CLIENT_ID = os.getenv('COMM_SERV_CLIENT_ID', '')
    COMM_SERV_CLIENT_SECRET = os.getenv('COMM_SERV_CLIENT_SECRET', '')

    RSIOPS_EMAIL_ADDRESS = os.getenv('RSIOPS_EMAIL_ADDRESS')
    REPLY_EMAIL_ADDRESS = os.getenv('REPLY_EMAIL_ADDRESS', 'do-not-reply-rsi@gov.bc.ca')
    BCC_EMAIL_ADDRESSES = os.getenv('BCC_EMAIL_ADDRESSES')
    VIPS_BCC_EMAIL_ADDRESSES = os.getenv('VIPS_BCC_EMAIL_ADDRESSES', '')
    TMP_STORAGE_LOCAL=os.getenv('TMP_STORAGE_LOCAL')

    MINIO_SECURE                        = os.environ.get("MINIO_SECURE", False)
    MINIO_CERT_FILE                     = os.environ.get("MINIO_CERT_FILE", "/opt/app-root/src/ca.crt")

    VIPS_DPS_EMAIL = os.getenv('VIPS_DPS_EMAIL', 'do-not-reply-rsi@gov.bc.ca')

    # Geocoding service details
    GEOCODING_API_URL = os.getenv('GEOCODING_API_URL', 'http://localhost:8000')
    GEOCODING_API_KEY = os.getenv('GEOCODING_API_KEY', 'TEST')

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'json': {
                '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
                'format': '[DF_FORM_HANDLER] %(asctime)s %(filename)s %(funcName)s %(levelname)s %(lineno)d %(module)s %(message)s %(pathname)s'
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
            },
        'pika': {
            'handlers': LOGGERS_IN_USE,
            'level': 'WARNING'
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
