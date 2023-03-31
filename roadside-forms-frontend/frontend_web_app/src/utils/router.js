import React, { Component } from 'react';
import { Route, BrowserRouter, Routes} from 'react-router-dom';
import { Login } from '../components/Login/login';
import PrivateRoute from '../routes/PrivateRoute';

class Router extends Component {

  render() {

    return (
        <BrowserRouter>
                <Routes>
                    <Route 
                      path="/" 
                      element={<Login />}  />
                </Routes>
        </BrowserRouter>
    );
  }

}

Router.propTypes = {};

export default Router;