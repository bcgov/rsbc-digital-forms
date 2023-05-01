import React from 'react';
import { Navigate} from 'react-router-dom';
import { useKeycloak } from '@react-keycloak/web';
import { Button } from '../common/Button/Button';
import './login.scss';

export const Login = () => {
    const { keycloak, initialized} = useKeycloak();
    const redirectUri = `${process.env.REACT_APP_BASE_URL}/requestAccess`;

    const handleClick = async () => {
        await keycloak.login({redirectUri: redirectUri});
      };
    
    if (!initialized) {
      return <div>Loading...</div>;
    
    }
    if (keycloak.authenticated) {
      return <Navigate to='/requestAccess' />;
    }
    
    return(    
        <div className="wrapper">
            {!keycloak.authenticated  && (<div className='border-design text-font'>
                <span className="fw-bold">Welcome!</span>&nbsp;
                Please log in to get started.&nbsp;
                <Button primary size="large" onClick={handleClick} label="Login" />
            </div>
            )}
        </div>
    );
  };
  
  Login.propTypes = {
    
  };
  
  Login.defaultProps = {
    
  };