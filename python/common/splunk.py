import requests

from python.common.logging_utils import get_logger

logger = get_logger(__name__)

def log_to_splunk(**kwargs) -> tuple:
    """
    We always return True regardless of whether the Splunk message is
    received successfully or not. We don't want the failure of Splunk logging
    call to disrupt the business flow where this function was called.
    """
    splunk_data = kwargs.get('splunk_data')
    if splunk_data is not None:
        config = kwargs.get('config')
        splunk_payload = dict({})
        # From DF-2908: Need to ensure that splunk_data is not None
        splunk_payload['event'] = splunk_data if splunk_data is not None else {}
        splunk_payload['source'] = config.OPENSHIFT_PLATE
        _post_to_splunk(splunk_payload, **kwargs)
        kwargs['splunk_data'] = None
    return True, kwargs


def _post_to_splunk(splunk_payload: dict, **args) -> bool:
    logger.verbose(f"inside _post_to_splunk()")
    config = args.get('config')
    endpoint = "{}:{}/services/collector".format(config.SPLUNK_HOST, config.SPLUNK_PORT)
    headers = {"Authorization": "Splunk " + config.SPLUNK_TOKEN}
    logger.debug(f"Splunk endpoint: {endpoint}")
    logger.debug(f"Splunk headers: {headers}")
    logger.debug(f"Splunk payload: {splunk_payload}")
    try:
        response = requests.post(endpoint, headers=headers, json=splunk_payload, verify=False)
    except requests.ConnectionError as error:
        logger.warning(f"No response from the Splunk API: {error}")
        return False
    logger.debug(f"response from Splunk: {response.status_code}")
    if response.status_code != 200:
        logger.warning(f"response from Splunk was not successful: {response.status_code}: {response.text}")
        return False
    return True
