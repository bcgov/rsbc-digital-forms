import React, { Component } from 'react';
import { Route, BrowserRouter, Routes} from 'react-router-dom';

class Router extends Component {

  render() {

    return (
        <BrowserRouter>
                <Routes>
                    <Route 
                         path="/" 
                         element={<h1>Hello, world!</h1>}  />
                </Routes>
        </BrowserRouter>
    );
  }

}

Router.propTypes = {};

export default Router;