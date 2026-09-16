import jwt
import ssl
from python.common.logging_utils import get_logger
from python.prohibition_web_svc.config import Config

logger = get_logger(__name__)

ssl_context=ssl.create_default_context()
ssl_context.check_hostname=False
ssl_context.verify_mode=ssl.CERT_NONE
jwks_client = jwt.PyJWKClient(Config.KEYCLOAK_CERTS_URL, ssl_context=ssl_context)
def get_authorization_header_from_request(**kwargs) -> tuple:
    request = kwargs.get('request')
    try:
        kwargs['auth_header'] = request.headers.get('Authorization').split(" ")
    except Exception as e:
        return False, kwargs
    return len(kwargs.get('auth_header')) == 2, kwargs


def get_token_from_authorization_header(**kwargs) -> tuple:
    auth_header = kwargs.get('auth_header')
    try:
        kwargs['access_token'] = auth_header[1]
    except Exception as e:
        kwargs['error'] = "keycloak authorization header is not valid: " + str(e)
        return False, kwargs
    return auth_header[0] == 'Bearer' and kwargs['access_token'] is not None, kwargs


def get_keycloak_certificates(**kwargs) -> tuple:
    try:        
        logger.verbose("getting keycloak certificates")
        kwargs['signing_key'] = jwks_client.get_signing_key_from_jwt(kwargs.get('access_token')).key
        logger.info("got keycloak certificates")
        logger.debug("signing key: " + str(kwargs.get('signing_key')))
    except Exception as e:
        kwargs['error'] = str(e)
        logger.error("error while getting keycloak certificates: " + str(e))
        return False, kwargs
    return True, kwargs


def decode_keycloak_access_token(**kwargs) -> tuple:
    access_token = kwargs.get('access_token')
    signing_key = kwargs.get('signing_key')
    try:
        kwargs['decoded_access_token'] = jwt.decode(access_token,
                                                    signing_key,
                                                    algorithms=[Config.KEYCLOAK_ALGORITHM],
                                                    audience=Config.KEYCLOAK_CLIENT_ID)
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs


def get_username_from_decoded_access_token(**kwargs) -> tuple:
    decoded_access_token = kwargs.get('decoded_access_token')
    try:
        kwargs['username'] = decoded_access_token['preferred_username']
        kwargs['display_name'] = decoded_access_token['display_name']
        kwargs['identity_provider'] = decoded_access_token['identity_provider']
        logger.debug("username and identity_provider from access token: " +  kwargs.get('username') + kwargs.get('identity_provider'))
        if decoded_access_token.get('bceid_user_guid'):
            logger.verbose('BCeID user')
            kwargs['bceid_username'] = decoded_access_token['bceid_username']
            kwargs['login'] = str(kwargs.get('bceid_username', '')) + '@' + str(kwargs.get('identity_provider', ''))
        if decoded_access_token.get('idir_user_guid'):
            logger.verbose('IDIR user')
            kwargs['idir_username'] = decoded_access_token['idir_username']
            kwargs['login'] = str(kwargs.get('idir_username', '')) + '@' + str(kwargs.get('identity_provider', ''))
        if decoded_access_token.get('identity_provider') == 'service_account':
            logger.verbose('service account user')
            kwargs['identity_provider'] = 'service_account'
            kwargs['login'] = str(kwargs.get('preferred_username', '')) + '@' + str(kwargs.get('identity_provider', ''))    
        logger.info("login id from access token: " +  kwargs.get('login'))
    except Exception as e:
        kwargs['error'] = "preferred_username or login not present in decoded access token: " + str(e)
        return False, kwargs
    return True, kwargs


def get_user_guid_from_decoded_access_token(**kwargs) -> tuple:
    decoded_access_token = kwargs.get('decoded_access_token')
    if decoded_access_token.get('bceid_user_guid'):
        logger.verbose('BCeID user')
        kwargs['business_guid'] = decoded_access_token.get('bceid_business_guid')
        kwargs['user_guid'] = decoded_access_token.get('bceid_user_guid')
        return True, kwargs
    if decoded_access_token.get('idir_user_guid'):
        logger.verbose('IDIR user')
        kwargs['user_guid'] = decoded_access_token.get('idir_user_guid')
        return True, kwargs
    if decoded_access_token.get('identity_provider') == 'service_account':
        logger.verbose('Service account user')
        kwargs['user_guid'] = decoded_access_token.get('preferred_username')
        return True, kwargs
    logger.verbose('Github user? - no user GUID')
    kwargs['user_guid'] = kwargs.get('username')
    if kwargs['user_guid']:
        return True, kwargs
    return False, kwargs

def get_user_roles_from_decoded_access_token(**kwargs) -> tuple:
    decoded_access_token = kwargs.get('decoded_access_token')
    try:
        kwargs['user_roles'] = decoded_access_token['role']
    except Exception as e:
        logger.error(e)
        return False, kwargs
    return True, kwargs


def check_user_is_authorized(**kwargs) -> tuple:
    username = kwargs.get('username')
    required_permission = kwargs.get('required_permission', None)
    required_permissions = required_permission.split(',') if required_permission else []
    user_roles = kwargs.get('user_roles')
    logger.verbose("inside check_user_is_authorized() {} {} {}".format(username, required_permission, "|".join(user_roles)))
    for role in user_roles:
        if any(rp in role for rp in required_permissions):
            return True, kwargs
    logger.warning("user {} does not have required permission {}".format(username, required_permission))
    return False, kwargs