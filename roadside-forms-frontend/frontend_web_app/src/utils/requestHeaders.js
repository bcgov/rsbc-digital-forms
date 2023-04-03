import keycloak from "../keycloak"
/**
 * Utility class for various request Headers.
 */

// This file is anticipated to have multiple exports
// eslint-disable-next-line import/prefer-default-export
export const createRequestHeader = (customHeaders = {}) => ({
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${keycloak.token}`,
    ...customHeaders,
  },
});