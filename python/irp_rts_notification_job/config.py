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
