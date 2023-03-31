import React from 'react';
import PropTypes from 'prop-types';
import { useState, useEffect } from 'react';
import './header.css';
import { getCurrentDateTime } from '../../utils/dateTime';

export const Header = ({ user, onLogin, onLogout}) => {
  const [isConnected, setIsConnected] = useState(navigator.onLine);
  const [time, setTime] = useState('');
  const [date, setDate] = useState('');
  const [day, setDay] = useState('');

  useEffect(() => {
    const handleOnline = () => setIsConnected(true);
    const handleOffline = () => setIsConnected(false);

    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);

    const interval = setInterval(() => {
      const {dateString, dayString, timeString} = getCurrentDateTime();
      setDate(dateString);
      setDay(dayString + ',');
      setTime(timeString);
    }, 1000);

    return () => {
      clearInterval(interval);
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    }
  }, []);

  return (
  <header>
    <div id="roadsafety-header" className='container'>
      <div className='row'> 
        <div className="col-sm-3" >
          <div className='brand-logo'></div>
        </div>
        { user && (<div className='col-sm-9'>
        <div className="row">
          <div className=" col-sm-4 time font-weight-bold mt-4">
            &nbsp;<span className="text-light d-block large">{time}</span>
            <span className="text-light d-block large">{day} {date}</span>
          </div>
          <div className=" col-sm-2 icon font-weight-bold mt-4">
            {isConnected ? (
              <div className='connected'></div>
            ) : (
              <div className='disconnected'></div>
            )}
          </div>
          <div className=" col-sm-4 user-info font-weight-bold col-right">
            &nbsp;<span className="text-light d-block large">John SMITH</span>
            <span className="text-light d-block large">Vancouver Police Dept.</span>
          </div>
          <div className=" col-sm-2 links font-weight-bold col-right">
            &nbsp;<a className="d-block text-light" href="https://example.com">Settings</a>
            <a className="d-block text-light" href="https://example.com">Logout</a>
          </div>
         </div>
         </div>
         )}
      </div>
    </div>
  </header>
);
}

Header.propTypes = {
  user: PropTypes.shape({}),
  onLogin: PropTypes.func.isRequired,
  onLogout: PropTypes.func.isRequired,
  onCreateAccount: PropTypes.func.isRequired,
};

Header.defaultProps = {
  user: null,
};
