/**
 * Utility class for various request Headers.
 */

// This file is anticipated to have multiple exports
// eslint-disable-next-line import/prefer-default-export
export const createRequestHeader = async (customHeaders = {}, auth = null) => {
  const baseHeader = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    credentials: "same-origin",
    ...customHeaders,
  };
  
  try {
    if (auth && auth.user?.access_token) {
      // Check if token needs refresh (5 minutes before expiry)
      const now = Date.now() / 1000;
      const tokenExpiry = auth.user.expires_at;
      
      if (tokenExpiry && (tokenExpiry - now) < 30) {
        await auth.signinSilent();
      }
      
      return {
        ...baseHeader,
        Authorization: `Bearer ${auth.user.access_token}`,
      };
    }
    return baseHeader;
  } catch (error) {
    console.log('Error refreshing token:', error);
    return baseHeader;
  }
};
