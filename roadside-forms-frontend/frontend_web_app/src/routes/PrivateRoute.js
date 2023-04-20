import { Route, Navigate } from 'react-router-dom';
import { useKeycloak } from "@react-keycloak/web";

function PrivateRoute({ children, ...rest }) {
    const { keycloak } = useKeycloak();
    return (
        <Route
        {...rest}
        render={
            ({ location }) => (
            keycloak.authenticated
                ? (
                children
                ) : (
                <Navigate
                    to={{
                    pathname: '/login',
                    state: { from: location }
                    }}
                />
                ))
        }
        />
    );
}
  
export default PrivateRoute;