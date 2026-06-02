import os


class Config():
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG').upper()
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'dev').upper()

    # Postgres settings
    DB_HOST = os.environ.get('DB_HOST', 'db')
    DB_USER = os.environ.get('DB_USER', 'testuser')
    DB_PASS = os.environ.get('DB_PASS', 'pass')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    DB_NAME_DF = os.environ.get('DB_NAME_DF', 'test')

    # Keycloak settings
    KEYCLOAK_AUTH_URL = os.environ.get('KEYCLOAK_AUTH_URL', 'http://keycloak:8080/auth/')
    KEYCLOAK_REALM = os.environ.get('KEYCLOAK_REALM', 'master')
    KEYCLOAK_CLIENT_ID = os.environ.get('KEYCLOAK_CLIENT_ID', 'test-client')
    KEYCLOAK_CLIENT_SECRET = os.environ.get('KEYCLOAK_CLIENT_SECRET', 'secret')

    # Splunk settings
    SPLUNK_HOST = os.environ.get('SPLUNK_HOST', 'localhost')
    SPLUNK_PORT = int(os.environ.get('SPLUNK_PORT', 8088))
    SPLUNK_TOKEN = os.environ.get('SPLUNK_TOKEN', 'your-splunk-token')
    OPENSHIFT_PLATE = os.environ.get('OPENSHIFT_PLATE', 'irp_rts_notification_job')

    # Email settings
    COMM_SERV_AUTH_URL = os.getenv('COMM_SERV_AUTH_URL', 'http://localhost')
    COMM_SERV_API_ROOT_URL = os.getenv('COMM_SERV_API_ROOT_URL', 'http://localhost')
    COMM_SERV_REALM = os.getenv('COMM_SERV_REALM', 'realm')
    COMM_SERV_CLIENT_ID = os.getenv('COMM_SERV_CLIENT_ID', '')
    COMM_SERV_CLIENT_SECRET = os.getenv('COMM_SERV_CLIENT_SECRET', '')

    REPLY_EMAIL_ADDRESS = os.getenv('REPLY_EMAIL_ADDRESS', 'do-not-reply-rsi@gov.bc.ca')
    BCC_EMAIL_ADDRESSES = os.getenv('BCC_EMAIL_ADDRESSES')
    SUPERINTENDENT_EMAIL = os.getenv('SUPERINTENDENT_EMAIL', 'VIPSFAXP@gov.bc.ca')

    JINJA2_TEMPLATE_PATH = os.getenv('JINJA2_TEMPLATE_PATH', '/src/python/common/templates')