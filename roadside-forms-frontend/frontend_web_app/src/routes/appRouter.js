import React, { Component } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Login } from '../components/Login/login';
import {Dashboard} from '../components/Dashboard/Dashboard';
import { PrivateRoutes } from './PrivateRoutes';
import { RequestAccess } from '../components/RequestAccess/requestAccess';
import { UserAdminDashboard } from '../components/userAdminDashboard/userAdminDashboard';
import { Header } from '../components/common/Header/Header';
import { CreateEvent } from '../components/Event/createEvent';
import { SVGprint } from '../components/Forms/Print/svgPrint';

class AppRouter extends Component {
    render() {
    return (
        <Router basename="/roadside-forms">
            <Header/>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/requestAccess" element={<RequestAccess/>} />
                <Route element={<PrivateRoutes/> } >
                    <Route path="/createEvent" element={<CreateEvent/>} />
                    <Route path="/" element={<Dashboard/>} exact/>
                    <Route path="/admin-console" element={<UserAdminDashboard />} exact />
                    <Route path="/svg-preview" element={<SVGprint />} exact />
                </Route>
            </Routes>
        </Router>
    );
  }
}

Router.propTypes = {};
  
export default AppRouter;