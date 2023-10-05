import os
from python.common.config import Config as BaseConfig

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(BaseConfig):
    FLASK_SECRET_KEY                    = os.getenv('FLASK_SECRET_KEY')

    FLASK_BASIC_AUTH_USER               = os.getenv('FLASK_BASIC_AUTH_USER')
    FLASK_BASIC_AUTH_PASS               = os.getenv('FLASK_BASIC_AUTH_PASS')

    ICBC_API_ROOT                       = os.getenv('ICBC_API_ROOT', "http://localhost:8080/api")
    ICBC_API_USERNAME                   = os.getenv('ICBC_API_USERNAME', 'user1')
    ICBC_API_PASSWORD                   = os.getenv('ICBC_API_PASSWORD', 'secret')

    # URL of requesting resource
    ACCESS_CONTROL_ALLOW_ORIGIN         = os.getenv('ACCESS_CONTROL_ALLOW_ORIGIN', '*')
    
    DB_HOST = os.environ.get('DB_HOST', 'db')
    DB_USER = os.environ.get('DB_USER', 'testuser')
    DB_PASS = os.environ.get('DB_PASS', 'pass')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    DB_NAME = os.environ.get('DB_NAME', 'test')
    DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # This user has the ability to add, edit and delete other users
    ADMIN_USERNAME                      = os.getenv('ADMIN_USERNAME')

    KEYCLOAK_REALM                      = os.getenv("KEYCLOAK_REALM", "some-realm")
    KEYCLOAK_AUTH_URL                   = os.getenv("KEYCLOAK_AUTH_URL", "http://localhost/auth/")
    KEYCLOAK_CLIENT_ID                  = os.getenv("KEYCLOAK_CLIENT_ID", 'my-client')
    KEYCLOAK_ALGORITHM                  = os.getenv("KEYCLOAK_ALGORITHM", "RS256")

    KEYCLOAK_CERTS_URL = "{}realms/{}/protocol/openid-connect/certs".format(KEYCLOAK_AUTH_URL, KEYCLOAK_REALM)

    URL_PREFIX                          = os.getenv('URL_PREFIX', '')  # no trailing slash!

    MAX_RECORDS_RETURNED                = 1000
    VANCOUVER_TIMEZONE                  = 'America/Vancouver'
    
    MINIO_AK                            = os.environ.get("MINIO_AK", "test")
    MINIO_SK                            = os.environ.get("MINIO_SK", "test")
    MINIO_BUCKET_URL                    = os.environ.get("MINIO_BUCKET_URL", 'minio:9000')
    MINIO_SECURE                        = os.environ.get("MINIO_SECURE", False)
    STORAGE_BUCKET_NAME                 = os.environ.get("STORAGE_BUCKET_NAME", "test")

    ENCRYPT_KEY = os.environ.get('ENCRYPT_KEY')
    ENCRYPT_KEY_SALT = os.environ.get('ENCRYPT_KEY_SALT')

