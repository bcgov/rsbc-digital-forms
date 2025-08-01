// WebStorageStateStore class for userStore
class WebStorageStateStore {
  constructor({ store = window.localStorage, prefix = 'oidc' } = {}) {
    this._store = store;
    this._prefix = prefix;
  }

  set(key, value) {
    const prefixedKey = `${this._prefix}.${key}`;
    return Promise.resolve(this._store.setItem(prefixedKey, value));
  }

  get(key) {
    const prefixedKey = `${this._prefix}.${key}`;
    const value = this._store.getItem(prefixedKey);
    return Promise.resolve(value);
  }

  remove(key) {
    const prefixedKey = `${this._prefix}.${key}`;
    const value = this._store.getItem(prefixedKey);
    this._store.removeItem(prefixedKey);
    return Promise.resolve(value);
  }

  getAllKeys() {
    const keys = [];
    for (let i = 0; i < this._store.length; i++) {
      const key = this._store.key(i);
      if (key && key.startsWith(`${this._prefix}.`)) {
        keys.push(key.substring(this._prefix.length + 1));
      }
    }
    return Promise.resolve(keys);
  }
}

// OIDC Configuration for react-oidc-context
export const oidcConfig = {
  authority: `${process.env.REACT_APP_KEYCLOAK_URL}realms/${process.env.REACT_APP_KEYCLOAK_REALM}`,
  client_id: process.env.REACT_APP_KEYCLOAK_CLIENT_ID,
  redirect_uri: process.env.REACT_APP_BASE_URL,
  post_logout_redirect_uri: process.env.REACT_APP_BASE_URL,
  response_type: 'code',
  scope: 'openid profile email offline_access',
  automaticSilentRenew: true,
  includeIdTokenInSilentRenew: true,
  revokeTokensOnSignout: true,
  userStore: new WebStorageStateStore({ store: window.localStorage }),
  // monitorSession: false,
  checkSessionInterval: 10000,
  onSigninCallback: () => {
    // Clean up the URL after successful sign-in
    window.history.replaceState({}, document.title, window.location.pathname);
  },
  onSignoutCallback: () => {
    // Clean up after sign-out
    window.history.replaceState({}, document.title, window.location.pathname);
  },
};

// Additional helper function to get user info
export const getUserInfo = (user) => {
  if (!user) return null;
  
  return {
    id: user.profile?.sub,
    username: user.profile?.preferred_username,
    email: user.profile?.email,
    firstName: user.profile?.given_name,
    lastName: user.profile?.family_name,
    fullName: user.profile?.name,
    roles: user.profile?.realm_access?.roles || []
  };
};
