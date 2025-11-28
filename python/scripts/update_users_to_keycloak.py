import datetime
import os
from sqlalchemy import create_engine, Table, MetaData
import requests
import logging
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Set up file handler for logging
file_handler = logging.FileHandler('update_users_to_keycloak.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger = logging.getLogger()
logger.addHandler(file_handler)

logger.info("Starting the script to add users to Keycloak")

# Database configuration
# ostgresql://localhost:5434/rsi_df_db
DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://testuser:pass@db:5432/test')
KEYCLOAK_URL = os.getenv('KEYCLOAK_URL', 'https://loginproxy.gov.bc.ca/auth')
KEYCLOAK_REALM = os.getenv('KEYCLOAK_REALM', 'rsbc-digital-forms')
KEYCLOAK_CLIENT_ID = os.getenv('KEYCLOAK_CLIENT_ID', 'roadsafety-digital-forms-backend')
KEYCLOAK_CLIENT_SECRET = os.getenv('KEYCLOAK_CLIENT_SECRET', 'test-secret')
GUEST_GROUP_ID = os.getenv('GUEST_GROUP_ID', '699f7ab2-6068-4fa2-9e77-0d9110b6395c')
OFFICER_GROUP_ID = os.getenv('OFFICER_GROUP_ID', 'd1f1e8b3-5c4a-4e2d-9e2f-5f6e6e6e6e6e')

# Create an engine and a metadata object
engine = create_engine(DATABASE_URI)
metadata = MetaData(schema='public')

# Reflect the user table
# user_table = Table('user', metadata, autoload_with=engine)
user_role_table = Table('user_role', metadata, autoload_with=engine)

def authenticate():
  url = f"{KEYCLOAK_URL}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/token"
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  data = {
    'grant_type': 'client_credentials',
    'client_id': KEYCLOAK_CLIENT_ID,
    'client_secret': KEYCLOAK_CLIENT_SECRET
  }
  response = requests.post(url, headers=headers, data=data)
  if response.status_code == 200:
    return response.json()
  else:
    logger.error(f"Failed to retrieve access token. Status code: {response.status_code}, Response: {response.text}")
    raise Exception(f"Failed to retrieve access token. Status code: {response.status_code}, Response: {response.text}")

def get_identity_provider(username):
  if username.endswith('@idir'):
    return 'azureidir'
  else:
    return 'bceidbusiness'

expires_in = -1000
expiration = datetime.datetime.now() + datetime.timedelta(seconds=expires_in)
access_token = None
keycloak_admin_url = f"{KEYCLOAK_URL}/admin/realms/{KEYCLOAK_REALM}"

# Connect to the database
with engine.connect() as connection:
    authSession = authenticate()
    expires_in = authSession.get('expires_in', 0)
    expiration = datetime.datetime.now() + datetime.timedelta(seconds=expires_in)
    logger.info(f"Access token will expire in {expires_in} seconds.")
    access_token = authSession.get('access_token')

    # Retrieve all members of the guest group
    get_guests_members_response = requests.get(f"{keycloak_admin_url}/groups/{GUEST_GROUP_ID}/members", headers={
      'Content-Type': 'application/json',
      'Authorization': f"Bearer {access_token}"
    })

    if get_guests_members_response.status_code != 200:
      logger.error(f"Failed to retrieve guest group members. Status code: {get_guests_members_response.status_code}, Response: {get_guests_members_response.text}")
      raise Exception(f"Failed to retrieve guest group members. Status code: {get_guests_members_response.status_code}, Response: {get_guests_members_response.text}")

    for member in get_guests_members_response.json():
      logger.info(f"Processing Keycloak user: {member['id']} with username {member['username']}")

      if (member.get('attributes') is None) or (member['attributes'].get('bceid_user_guid') is None):
        logger.info(f"User {member['username']} does not have bceid_user_guid attribute, skipping.")
        continue
      query_user_role = connection.execute(
        user_role_table.select().where(
          (user_role_table.columns.user_guid == member['attributes']['bceid_user_guid'][0])
        )
      )
      user_role = query_user_role.fetchone()
      if user_role and user_role.approved_dt != None:
        logger.info(f"User {member['username']} is approved in database, updating Keycloak groups.")

        if expiration < datetime.datetime.now() or access_token is None:
            logger.info("Access token expired or not available, authenticating...")
            authSession = authenticate()
            expires_in = authSession.get('expires_in', 0)
            expiration = datetime.datetime.now() + datetime.timedelta(seconds=expires_in)
            logger.info(f"Access token will expire in {expires_in} seconds.")
            access_token = authSession.get('access_token')

        headers = {
          'Content-Type': 'application/json',
          'Authorization': f"Bearer {access_token}"
        }

        # Add officer group
        update_response = requests.put(f"{keycloak_admin_url}/users/{member['id']}/groups/{OFFICER_GROUP_ID}", headers=headers)
        if update_response.status_code == 204:
          logger.info("Officer group added successfully.")

          # Remove guest group
          delete_response = requests.delete(f"{keycloak_admin_url}/users/{member['id']}/groups/{GUEST_GROUP_ID}", headers=headers)
          if delete_response.status_code == 204:
            logger.info("Guest group removed successfully.")
          else:
            logger.error(f"Failed to remove guest group. Status code: {delete_response.status_code}, Response: {delete_response.text}")
        else:
          logger.error(f"Failed to add officer group. Status code: {update_response.status_code}, Response: {update_response.text}")
      else:
        logger.info(f"User {member['username']} does not have officer role in database, skipping.")
  
  
logger.info("Script finished.")