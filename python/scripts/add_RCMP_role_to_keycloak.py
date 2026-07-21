import datetime
import os
import requests
import logging

from keycloak_auth import KeycloakAuth
from sqlalchemy import create_engine, text

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Set up file handler for logging
file_handler = logging.FileHandler('add_RCMP_role_to_keycloak.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger = logging.getLogger()
logger.addHandler(file_handler)

logger.info("Starting the script to add users to Keycloak")

keycloak_auth = KeycloakAuth(logger)
expires_in = -1000
expiration = datetime.datetime.now() + datetime.timedelta(seconds=expires_in)
access_token = None

# Database configuration
# ostgresql://localhost:5434/rsi_df_db
DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://testuser:pass@db:5432/test')

# Create an engine and a metadata object
engine = create_engine(DATABASE_URI)

# Connect to the database
with engine.connect() as connection:
  # Execute a raw SQL query to fetch all RCMP officers
  # result = connection.execute(text('''
  #   select * from "user" u
  #   where u.user_guid = '31A21CA7406E4AA9A3037E416DE241B6';
  # '''))
  result = connection.execute(text('''
    select * from "user" u
    where u.agency_id in (
      select a.id
      from agency a
      where a.agency_name like 'RCMP%'
         or a.agency_name like 'BCHP%'
    )
  '''))

  # Print the users
  for row in result:
    logger.info(f"Processing user: {row.user_guid}")

    if expiration < datetime.datetime.now() or access_token is None:
      logger.info("Access token expired or not available, authenticating...")
      authSession = keycloak_auth.authenticate()
      expires_in = authSession.get('expires_in', 0)
      expiration = datetime.datetime.now() + datetime.timedelta(seconds=expires_in)
      logger.info(f"Access token will expire in {expires_in} seconds.")
      access_token = authSession.get('access_token')

    url = f"{keycloak_auth.KEYCLOAK_URL}/admin/realms/{keycloak_auth.KEYCLOAK_REALM}/users"
    headers = {
      'Content-Type': 'application/json',
      'Authorization': f"Bearer {access_token}"
    }

    get_user_response = requests.get(
      url,
      headers=headers,
      params={'username': row.username, 'exact': True}
    )

    if get_user_response.status_code != 200:
      logger.error(
        f"Failed to look up Keycloak user for {row.username}. Status code: {get_user_response.status_code}, Response: {get_user_response.text}"
      )
      continue

    user_matches = get_user_response.json()
    if not user_matches:
      logger.warning(f"No Keycloak user found for {row.username}; skipping group assignment.")
      continue

    # Add RCMP group
    update_response = requests.put(
      f"{keycloak_auth.keycloak_admin_url}/users/{user_matches[0]['id']}/groups/{keycloak_auth.RCMP_GROUP_ID}", 
      headers=keycloak_auth.get_header())
    if update_response.status_code == 204:
      logger.info("RCMP group added successfully.")
    else:
      logger.error(f"Failed to add RCMP group. Status code: {update_response.status_code}, Response: {update_response.text}")


logger.info("Script finished.")