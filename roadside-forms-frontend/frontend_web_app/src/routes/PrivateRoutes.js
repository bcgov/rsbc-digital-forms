import React from 'react';
import { Outlet, Navigate } from 'react-router-dom';
import { useKeycloak } from '@react-keycloak/web';

const PrivateRoutes = () => {
  const { keycloak, initialized } = useKeycloak();

  if (!initialized) {
    return <div>Loading...</div>;
  }

  return (
    keycloak.authenticated ? <Outlet/> : <Navigate to="/login" />
  )
}

export default PrivateRoutes;