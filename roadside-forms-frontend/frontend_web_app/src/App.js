import React from 'react';
import { ReactKeycloakProvider } from "@react-keycloak/web";
import Router from './utils/router';
import keycloak, { keycloakInitConfig } from './keycloak';

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
