import requests

from python.common.config import Config
from python.common.logging_utils import get_logger

logger = get_logger(__name__)

def get_charge_types(config: Config) -> list:
    endpoint = f"{config.ETK_ISSUANCE_SVC_URL}/chargetypes"
    logger.debug(f"Fetching charge types from {endpoint}")
    
    try:
        response = requests.get(endpoint)
        logger.debug(f"Response status code: {response.status_code}")
        response.raise_for_status()
        etk_charge_types = response.json()
        charge_types = [{
            'id': ct['cmnChargeId'],
            'statuteCode': ct['cmnStatuteCode'],
            'code': ct['cmnChargeCode'], 
            'description': ct['cmnChargeDesc']
          } for ct in etk_charge_types]
        logger.debug(f"Received charge types count: {len(charge_types)}")
        return charge_types
    except Exception as error:
        logger.error(f"Error fetching charge types from {endpoint}: {error}")
        return []