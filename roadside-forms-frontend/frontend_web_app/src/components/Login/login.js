import React from "react";
import { Navigate } from "react-router-dom";
import { useAuth } from "react-oidc-context";
import { Button } from "../common/Button/Button";
import "./login.scss";

export const Login = () => {
  const auth = useAuth();
  // const redirectUri = `${process.env.REACT_APP_BASE_URL}/requestAccess`;
  const redirectUri = `${process.env.REACT_APP_BASE_URL}/`;

  const handleClick = async () => {
    await auth.signinRedirect();
  };

  if (auth.isLoading) {
    return <div>Loading...</div>;
  }
  if (auth.isAuthenticated) {
    return <Navigate to="/requestAccess" />;
  }

  return (
    <div className="wrapper">
      {!auth.isAuthenticated && (
        <div className="border-design text-font">
          <span className="fw-bold">Welcome!</span>&nbsp; Please log in to get
          started.&nbsp;
          <Button primary size="large" onClick={handleClick} label="Login" />
        </div>
      )}
    </div>
  );
};

Login.propTypes = {};

Login.defaultProps = {};
