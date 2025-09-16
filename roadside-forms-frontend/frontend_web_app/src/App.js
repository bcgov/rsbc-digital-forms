import React, { useEffect } from "react";
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

  useEffect(() => {
    if (isServiceWorkerUpdated) {
      updateServiceWorker();
    }
  }, [isServiceWorkerUpdated, serviceWorkerRegistration]);

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
        initOptions={keycloakInitConfig}
      >
        <RouterProvider router={appRouter} />
      </ReactKeycloakProvider>
    </div>
  );
}

export default App;
