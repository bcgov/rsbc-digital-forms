import React, { useEffect, useRef, useState } from "react";
import { Navigate, Outlet } from "react-router-dom";
import { userRolesAtom } from "../atoms/userRoles";
import { useAuth } from "react-oidc-context";
import { useRecoilValueLoadable } from "recoil";

export const PrivateRoutes = () => {
  const auth = useAuth();
  const [userRoleDataLoaded, setUserRoleDataLoaded] = useState(false);
  const userHasRoleRef = useRef(false);
  const userRolesLoadable = useRecoilValueLoadable(userRolesAtom);

  useEffect(() => {
    if (!auth.isLoading && auth.isAuthenticated) {
      if (userRolesLoadable.state === "hasValue") {
        const userRoles = userRolesLoadable.contents;
        userHasRoleRef.current = userRoles.length !== 0;
      }
      setUserRoleDataLoaded(true);
    }
  }, [auth.isLoading, auth.isAuthenticated, userRolesLoadable]);

  if (auth.isLoading) {
    return <div>Loading...</div>;
  }

  if (!auth.isAuthenticated) {
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
