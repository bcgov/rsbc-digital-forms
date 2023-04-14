import React from 'react';
import { ReactKeycloakProvider } from "@react-keycloak/web";
import Router from './utils/router';
import keycloak, { keycloakInitConfig } from './keycloak';
import '../src/utils/commonStyles.scss';
import { library } from '@fortawesome/fontawesome-svg-core';
import { fab } from '@fortawesome/free-brands-svg-icons';
import { far } from '@fortawesome/free-regular-svg-icons';
import { fas } from '@fortawesome/free-solid-svg-icons';
import { Header } from './components/Header/Header';
import { Footer } from './components/Footer/footer';

library.add(fab, far, fas);

function App() {
  return (
    <div className="App">
      <ReactKeycloakProvider authClient={keycloak} initOptions={keycloakInitConfig}>
        <Header/>
        <Router/>
        <Footer/>
      </ReactKeycloakProvider>
    </div>
  );
}

export default App;
