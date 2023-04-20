import { Route, Navigate } from 'react-router-dom';
import React from 'react';
import { useKeycloak } from "@react-keycloak/web";

function PrivateRoute({ element: Element,...rest }) {
    const [authenticated, setAuthenticated] = React.useState(false);
    const { keycloak } = useKeycloak();

    React.useEffect(() => {
        let isMounted = true;
        
        const checkAuth = async () => {
          const isAuthenticated = await keycloak.authenticated;
          if (isMounted) {
            setAuthenticated(isAuthenticated);
          }
        };
    
        checkAuth();
    
        return () => {
          isMounted = false;
        };
    }, [keycloak.authenticated]);

    console.log( keycloak )
    if (!authenticated) {
        return <Navigate to="/login" />;
      }
    
    return <Element {...rest} />;
}
  
export default React.memo(PrivateRoute);