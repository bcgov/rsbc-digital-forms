import React from 'react';
import PropTypes from 'prop-types';
import { UserRolesApi } from '../../api/userRolesApi';
import { useKeycloak } from '@react-keycloak/web';
import { useNavigate } from 'react-router-dom';
import { Button } from '../Button/Button';
import './login.scss';

export const Login = () => {
    const { keycloak, initialized } = useKeycloak();
    const navigate = useNavigate();
    console.log(keycloak)

    const handleClick = async () => {
        await keycloak.login();
        navigate('/requestAccess');
      };
    
    return(    
        <div className="wrapper">
            <div className='border-design text-font'>
                <span className="fw-bold">Welcome!</span>&nbsp;
                Please log in to get started.&nbsp;
                <Button primary size="large" onClick={handleClick} label="Login" />
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