import React from 'react';
import PropTypes from 'prop-types';
import { useState, useEffect } from 'react';
import { useKeycloak } from '@react-keycloak/web';
import './header.scss';
import { getCurrentDateTime } from '../../../utils/dateTime';
import CloudOutlinedIcon from '@mui/icons-material/CloudOutlined';
import CloudOffOutlinedIcon from '@mui/icons-material/CloudOffOutlined';

export const Header = ({user}) => {
  const [isConnected, setIsConnected] = useState(navigator.onLine);
  const [isLoading, setIsLoading] = useState(true);
  const { keycloak} = useKeycloak();
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
      setIsLoading(false);
    }, 1000);

    return () => {
      clearInterval(interval);
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    }
  }, []);

  return (
  <header>
    <div id="roadsafety-header" className='container text-font'>
      <div className='row'> 
        <div className="col-sm-3" >
          <div className='brand-logo'></div>
        </div>
         {/* added keycloak.authenticated for testing purposes only*/}
        { keycloak.authenticated && !isLoading && (<div className='col-sm-9'>
        <div className="row">
          <div className=" col-sm-4 time fw-bold mt-4">
            &nbsp;<span className="text-light d-block large">{time}</span>
            <span className="text-light d-block large">{day} {date}</span>
          </div>
          <div className=" col-sm-2 icon mt-4">
            {isConnected ? (
              <CloudOutlinedIcon sx={{ color: "white" , fontSize: 80}}></CloudOutlinedIcon>
            ) : (
              <CloudOffOutlinedIcon sx={{ color: "white" , fontSize: 80}}></CloudOffOutlinedIcon>
            )}
          </div>
          <div className=" col-sm-4 user-info fw-bold col-right">
            &nbsp;<span className="text-light d-block large">John SMITH</span>
            <span className="text-light d-block large">Vancouver Police Dept.</span>
          </div>
          <div className=" col-sm-2 links fw-bold col-right">
            &nbsp;<a className="d-block text-light" href="https://example.com">Settings</a>
            <a className="d-block text-light" href="/" onClick={() => keycloak.logout()}>Logout</a>
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
};

Header.defaultProps = {
  user: null,
};