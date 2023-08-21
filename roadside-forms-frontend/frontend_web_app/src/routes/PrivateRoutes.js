import React, { useEffect, useRef, useState } from 'react';
import { Navigate, Outlet} from 'react-router-dom';
import { userRolesAtom } from '../atoms/userRoles';
import { useKeycloak } from '@react-keycloak/web';
import { useRecoilValueLoadable } from 'recoil';

export const PrivateRoutes = () => {
  const { keycloak, initialized } = useKeycloak();
  const [userRoleDataLoaded, setUserRoleDataLoaded] = useState(false);
  const userHasRoleRef = useRef(false);
  const userRolesLoadable = useRecoilValueLoadable(userRolesAtom);

  useEffect(() => {
    if (initialized && keycloak.authenticated) {
      if (userRolesLoadable.state === 'hasValue') {
        const userRoles = userRolesLoadable.contents;
        userHasRoleRef.current = userRoles.length !== 0;
      }
      setUserRoleDataLoaded(true);
    }
  }, [initialized, keycloak.authenticated, userRolesLoadable]);

  if (!initialized) {
    return <div>Loading...</div>;
  }

  if (!keycloak.authenticated) {
    return <Navigate to="/login" />;
  }

  if (!userRoleDataLoaded) {
    return <div>Loading...</div>;
  }

  if (userHasRoleRef.current) {
    return <Outlet />;
  }

  return <Navigate to="/requestAccess" />;
};