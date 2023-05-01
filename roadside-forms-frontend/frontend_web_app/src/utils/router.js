import React, { Component } from 'react';
import { BrowserRouter, Routes, Route} from 'react-router-dom';
import { Login } from '../components/Login/login';
import { Dashboard } from '../components/Dashboard/Dashboard';
import PrivateRoute from '../routes/PrivateRoute';
import { RequestAccess } from '../components/RequestAccess/requestAccess';

class Router extends Component {
    render() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/" element={<PrivateRoute element={<Dashboard />} />} />
                <Route path="/requestAccess" element={  <PrivateRoute> <RequestAccess/> </PrivateRoute> } />
            </Routes>
        </BrowserRouter>
    );
  }
}

Router.propTypes = {};
  
export default Router;