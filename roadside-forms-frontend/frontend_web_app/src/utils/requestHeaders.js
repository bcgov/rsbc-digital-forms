import keycloak from "../keycloak";
/**
 * Utility class for various request Headers.
 */

// This file is anticipated to have multiple exports
// eslint-disable-next-line import/prefer-default-export
export const createRequestHeader = async (customHeaders = {}) => {
  const baseHeader = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    credentials: "same-origin",
    ...customHeaders,
  };
  try {
    await keycloak.updateToken(30);
    return {
      ...baseHeader,
      Authorization: `Bearer ${keycloak.token}`,
    }
  } catch (error) {
    console.log(error)
    return baseHeader;
  }
}
