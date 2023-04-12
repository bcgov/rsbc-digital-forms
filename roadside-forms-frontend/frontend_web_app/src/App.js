import React from 'react';
import { ReactKeycloakProvider } from "@react-keycloak/web";
import Router from './utils/router';
import keycloak, { keycloakInitConfig } from './keycloak';
import { library } from '@fortawesome/fontawesome-svg-core';
import { fab } from '@fortawesome/free-brands-svg-icons';
import { far } from '@fortawesome/free-regular-svg-icons';
import { fas } from '@fortawesome/free-solid-svg-icons';

library.add(fab, far, fas);

function App() {
  console.log(process)
  return (
    <div className="App">    
      <ReactKeycloakProvider authClient={keycloak} initOptions={keycloakInitConfig}>
        <Router/>
      </ReactKeycloakProvider>
    </div>
  );
}

export default App;
