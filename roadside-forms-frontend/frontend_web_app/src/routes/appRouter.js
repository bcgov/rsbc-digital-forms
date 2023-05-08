import React, { Component } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Login } from '../components/Login/login';
import {Dashboard} from '../components/Dashboard/Dashboard';
import PrivateRoutes from './PrivateRoutes';
import { RequestAccess } from '../components/RequestAccess/requestAccess';

class AppRouter extends Component {
    render() {
    return (
        <Router>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route element={<PrivateRoutes/> } >
                    <Route path="/requestAccess" element={<RequestAccess/>} />
                    <Route path="/" element={<Dashboard/>} exact/>
                </Route>
            </Routes>
        </Router>
    );
  }
}

Router.propTypes = {};
  
export default AppRouter;