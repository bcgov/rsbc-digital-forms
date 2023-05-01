import { Navigate } from 'react-router-dom';
import React from 'react';
import { useKeycloak } from "@react-keycloak/web";

function PrivateRoute(children){
    const { keycloak } = useKeycloak();
    if (!keycloak.authenticated) {
      return <Navigate to="/" replace />
    }
    return children
}

export default PrivateRoute
