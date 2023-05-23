import React, { useState, useEffect } from 'react';
import { useKeycloak } from '@react-keycloak/web';
import CloudOutlinedIcon from '@mui/icons-material/CloudOutlined';
import CloudOffOutlinedIcon from '@mui/icons-material/CloudOffOutlined';
import { useSetRecoilState} from 'recoil';
import { Link } from 'react-router-dom';

import { userAtom } from '../../../atoms/users';
import { userRolesAtom } from '../../../atoms/userRoles';
import { getCurrentDateTime } from '../../../utils/dateTime';
import { UserApi } from '../../../api/userApi';
import { UserRolesApi } from '../../../api/userRolesApi';
import {db} from '../../../db'
import './header.scss';

export const Header = () => {
  const [isConnected, setIsConnected] = useState(navigator.onLine);
  const [isLoading, setIsLoading] = useState(true);
  const [userInfo, setUserInfo] = useState({username: null, agency: null });
  const [userAdminInfo, setuserAdminInfo] = useState(false);
  const { keycloak, initialized} = useKeycloak();
  const [time, setTime] = useState('');
  const [date, setDate] = useState('');
  const [day, setDay] = useState('');
  const [userId, setUserId] = useState(null);
  const setUserData = useSetRecoilState(userAtom);
  const setUserRoleData = useSetRecoilState(userRolesAtom);


  useEffect(() => {
    // Get the userId based on identity_provider from keycloak
    if (keycloak.authenticated && initialized && keycloak.tokenParsed) {
      if (keycloak.tokenParsed.identity_provider === 'idir') {
        setUserId(keycloak.tokenParsed.idir_user_guid);
      } else  if(keycloak.tokenParsed.identity_provider === 'bceid') {
        setUserId(keycloak.tokenParsed.bceid_user_guid);
      }
    }

    // Based on userId, get user information from the DB
    if (userId !== null && userId !== undefined) {
      UserApi.get(userId)
        .then((response) => {
          if (response && (response.status === 201 || response.status === 200)) {
            const data = response.data
            setUserData(data);
            if(data){
              db.user.put(data);
            }
            setUserInfo({"username":data.login,"agency":data.agency})
          }
          else {
            setUserData([]);
            console.log(response.data.error);
          }
        })
        .catch((error) => {
          setUserData([]);
          console.log("Error", error.response.data.error);
        })
        UserRolesApi.get().then((resp) =>{
          if (resp && (resp.status === 201 || resp.status === 200)) {
            const data = resp.data
            if(data){
              db.userRoles.bulkPut(data);
            }
            setUserRoleData(data);
            setuserAdminInfo(data.some( role => role['role_name'] === 'administrator' ))
          }
          else {
            setUserRoleData([]);
            console.log(resp.data.error);
          }
        })
     }
    
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
  }, [keycloak.authenticated, 
      initialized, 
      setUserData,
      setUserRoleData, 
      keycloak.tokenParsed, 
      userId]);

  return (
  <header>
    <div id="roadsafety-header" className='container text-font'>
      <div className='row'> 
        <div className="col-sm-3" >
          <div className='brand-logo'></div>
        </div>
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
            &nbsp;<span className="text-light d-block large">{userInfo.username}</span>
            <span className="text-light d-block large">{userInfo.agency}</span>
          </div>
          <div className=" col-sm-2 links fw-bold col-right">
            &nbsp; {userAdminInfo ? <div><Link className="d-block text-light" to="/admin-console">Admin</Link></div> :<div><a className="d-block text-light" href="https://example.com">Settings</a></div>}
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

Header.propTypes = {};

Header.defaultProps = {};