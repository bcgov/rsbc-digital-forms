import React, { useEffect, useState } from "react";
import { ReactKeycloakProvider } from "@react-keycloak/web";
import keycloak, { keycloakInitConfig } from "./keycloak";
import "../src/utils/commonStyles.scss";
import { library } from "@fortawesome/fontawesome-svg-core";
import { fab } from "@fortawesome/free-brands-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { RouterProvider } from "react-router-dom";
import { useSelector } from "react-redux";

import { appRouter } from "./routes/appRouter";
import { Modal } from "react-bootstrap";

library.add(fab, far, fas);

function App() {
  const isServiceWorkerUpdated = useSelector(
    (state) => state.serviceWorkerUpdated
  );
  const serviceWorkerRegistration = useSelector(
    (state) => state.serviceWorkerRegistration
  );

  const [initOptions, setInitOptions] = useState(keycloakInitConfig);
  const [loadedStoredTokens, setLoadedStoredTokens] = useState(false);

  useEffect(() => {
    if (isServiceWorkerUpdated) {
      updateServiceWorker();
    }
  }, [isServiceWorkerUpdated, serviceWorkerRegistration]);

  const storedToken = sessionStorage.getItem('keycloak-token');
  const storedRefreshToken = sessionStorage.getItem('keycloak-refresh-token');
  if (storedToken && storedRefreshToken && !loadedStoredTokens) {
    console.log('[Keycloak] Loading stored tokens from sessionStorage');
    setLoadedStoredTokens(true);
    setInitOptions({
      ...keycloakInitConfig,
      token: storedToken,
      refreshToken: storedRefreshToken,
      checkLoginIframe: false, // Disable iframe check when using stored tokens
    });
  }

  const updateServiceWorker = () => {
    if (!serviceWorkerRegistration) return;
    const registrationWaiting = serviceWorkerRegistration.waiting;

    if (registrationWaiting) {
      registrationWaiting.postMessage({ type: "SKIP_WAITING" });

      registrationWaiting.addEventListener("statechange", (e) => {
        if (e.target.state === "activated") {
          window.location.reload();
        }
      });
    }
  };

  // Keycloak event handler for logging auth events
  const onKeycloakEvent = (eventType, error) => {
    console.log(`[Keycloak Event] ${eventType}`, {
      timestamp: new Date().toISOString(),
      eventType,
      error: error ? error.message || error : null,
      realm: keycloak.realm || "unknown",
    });

    if (error) {
      console.error(`[Keycloak Error] ${eventType}:`, error);
    }

    // Clear sessionStorage on logout
    if (eventType === 'onAuthLogout') {
      console.log('[Keycloak] Clearing stored tokens from sessionStorage');
      sessionStorage.removeItem('keycloak-token');
      sessionStorage.removeItem('keycloak-refresh-token');
    }
  };

  // Keycloak tokens handler for logging and storing token updates
  const onKeycloakTokens = (tokens) => {
    console.log("[Keycloak Tokens] Updated", {
      timestamp: new Date().toISOString(),
      hasAccessToken: !!tokens.token,
      hasRefreshToken: !!tokens.refreshToken
    });

    // Store tokens in sessionStorage
    if (tokens.token) {
      sessionStorage.setItem('keycloak-token', tokens.token);
      console.log('[Keycloak] Stored access token in sessionStorage');
    }
    if (tokens.refreshToken) {
      sessionStorage.setItem('keycloak-refresh-token', tokens.refreshToken);
      console.log('[Keycloak] Stored refresh token in sessionStorage');
    }
  };

  return (
    <div className="App">
      {/* <Modal show={isServiceWorkerUpdated}>
        <Modal.Header>
          <h3>A new version of this app is available!</h3>
        </Modal.Header>
        <Modal.Body>
          Click below to refresh the application and start using the latest
          version.
        </Modal.Body>
        <Modal.Footer>
          <button
            className="btn btn-primary"
            onClick={() => updateServiceWorker()}
          >
            Refresh
          </button>
        </Modal.Footer>
      </Modal> */}
      <ReactKeycloakProvider
        authClient={keycloak}
        initOptions={initOptions}
        onEvent={onKeycloakEvent}
        onTokens={onKeycloakTokens}
      >
        <RouterProvider router={appRouter} />
      </ReactKeycloakProvider>
    </div>
  );
}

export default App;
