import React, { Component } from 'react';
import { BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';
import { Login } from '../components/Login/login';
// import PrivateRoute from '../routes/PrivateRoute';
import { RequestAccess } from '../components/RequestAccess/requestAccess';

class Router extends Component {
    render() {
    return (
        <BrowserRouter>
                <Routes>
                    <Route path="/login" element={<Login/>} />
                    <Route path="/requestAccess" element={<RequestAccess/>}  />
                    <Route path="/" element={<Navigate to="/login" />} />
                </Routes>
        </BrowserRouter>
    );
  }
}

Router.propTypes = {};
  
export default Router;