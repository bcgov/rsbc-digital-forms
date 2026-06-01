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
