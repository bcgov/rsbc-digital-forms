import keycloak from "../keycloak"
/**
 * Utility class for various request Headers.
 */

// This file is anticipated to have multiple exports
// eslint-disable-next-line import/prefer-default-export
export const createRequestHeader = (customHeaders = {}) => ({
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Authorization': `Bearer ${keycloak.token}`,
    'credentials': 'same-origin',
    ...customHeaders,
});