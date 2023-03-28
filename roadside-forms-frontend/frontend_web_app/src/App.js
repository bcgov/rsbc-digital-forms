import React from 'react';
import { ReactKeycloakProvider } from "@react-keycloak/web";
import Router from './utils/router';
import keycloak from './keycloak';

function App() {
  return (
    <div className="App">    
      {/* <ReactKeycloakProvider authClient={keycloak}> */}
        <Router/>
      {/* </ReactKeycloakProvider> */}
    </div>
  );
}

export default App;
