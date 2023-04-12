import React from 'react';
import PropTypes from 'prop-types';
import { UserRolesApi } from '../../api/userRolesApi';
import { useKeycloak } from '@react-keycloak/web';
import { Button } from '../Button/Button';
import { Header } from '../Header/Header';

export const Login = () => {
    const { keycloak, initialized } = useKeycloak();
    console.log(keycloak)
    return(    
        <div className="wrapper">
            <Header></Header>
            <div>
                <h1>Login</h1>
                <Button primary size="small" onClick={() => keycloak.login()} label="Log in" />
            </div>
            {/* for testing purposes */}
            {keycloak.authenticated  && 
            <Button primary size="small" onClick={() => UserRolesApi.getAll() } label="test" />  
            }
        </div>
    );
  };
  
  Login.propTypes = {
    
  };
  
  Login.defaultProps = {
    
  };