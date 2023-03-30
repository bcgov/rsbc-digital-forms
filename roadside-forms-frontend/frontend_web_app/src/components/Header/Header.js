import React from 'react';
import PropTypes from 'prop-types';

import { Button } from '../Button/Button';
import './header.css';

export const Header = ({ user, onLogin, onLogout}) => (
  <header>
    <div id="roadsafety-header" className='container'>
      <div className='row'> 
        <div className="col-sm-4" >
          <div className='brand-logo'></div>
        </div>
        <div className="col-sm-8 col-right">
          <div className="font-weight-bold text-warning mb-4">
            Version&nbsp;<span className="text-light small" id="app-version">-&nbsp;0.1</span>
          </div>
          { user &&  ( 
          <div className="mt-auto">
            &nbsp;<span className="text-light large">Navpreet Sidhu</span>
            &nbsp;&nbsp;&nbsp;
            <Button  size='small' primary label="Sign Out"/>
          </div>
          )}
        </div>
      </div>
    </div>
  </header>
);

Header.propTypes = {
  user: PropTypes.shape({}),
  onLogin: PropTypes.func.isRequired,
  onLogout: PropTypes.func.isRequired,
  onCreateAccount: PropTypes.func.isRequired,
};

Header.defaultProps = {
  user: null,
};
