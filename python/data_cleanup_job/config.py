import os


class Config():
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG').upper()
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'dev').upper()

    # Retention settings
    RETENTION_DAYS = int(os.environ.get('RETENTION_DAYS', 90))
    DRY_RUN = os.environ.get('DRY_RUN', 'TRUE').upper() == 'TRUE'

    # Postgres settings
    DB_HOST = os.environ.get('DB_HOST', 'db')
    DB_USER = os.environ.get('DB_USER', 'testuser')
    DB_PASS = os.environ.get('DB_PASS', 'pass')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    DB_NAME_DF = os.environ.get('DB_NAME_DF', 'test')

    # MongoDB settings
    MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
    MONGO_PORT = int(os.environ.get('MONGO_PORT', 27017))
    MONGO_USER = os.environ.get('MONGO_USER', '')
    MONGO_PASS = os.environ.get('MONGO_PASS', '')
    MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME', 'formio')
