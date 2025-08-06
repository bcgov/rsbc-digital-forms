import React, { useState, useEffect } from "react";
import { useAuth } from "react-oidc-context";
import { getUserInfo } from "../../../auth";
import CloudOutlinedIcon from "@mui/icons-material/CloudOutlined";
import CloudOffOutlinedIcon from "@mui/icons-material/CloudOffOutlined";
import AccountCircle from "@mui/icons-material/AccountCircle";
import ArrowDropDownIcon from "@mui/icons-material/ArrowDropDown";
import { useSetRecoilState } from "recoil";
import { Link } from "react-router-dom";
import { Dropdown } from "react-bootstrap";

import { userAtom } from "../../../atoms/users";
import { userRolesAtom } from "../../../atoms/userRoles";
import { loginCompletedAtom } from "../../../atoms/loginCompleted";
import { getCurrentDateTime } from "../../../utils/dateTime";
import { UserApi } from "../../../api/userApi";
import { UserRolesApi } from "../../../api/userRolesApi";
import { db } from "../../../db";
import "./header.scss";
import { useSharedIsOnline } from "../../../utils/connectivity";
import { Col, Row } from "react-bootstrap";

export const Header = () => {
  const { isConnected } = useSharedIsOnline();
  const [isLoading, setIsLoading] = useState(true);
  const [userInfo, setUserInfo] = useState({ username: null, agency: null });
  const [userAdminInfo, setuserAdminInfo] = useState(false);
  const auth = useAuth();
  const [time, setTime] = useState("");
  const [date, setDate] = useState("");
  const [day, setDay] = useState("");
  const [userId, setUserId] = useState(null);
  const setUserData = useSetRecoilState(userAtom);
  const setUserRoleData = useSetRecoilState(userRolesAtom);
  const setLoginCompleted = useSetRecoilState(loginCompletedAtom);

  useEffect(() => {
    // Get the userId based on identity_provider from auth user
    if (auth.isAuthenticated && auth.user) {
      if (auth.user.profile?.identity_provider === "idir") {
        setUserId(auth.user.profile?.idir_user_guid);
      } else if (auth.user.profile?.identity_provider === "bceid") {
        setUserId(auth.user.profile?.bceid_user_guid);
      } else {
        setUserId(auth.user.profile?.bceid_user_guid);
      }
    }

    // Based on userId, get user information from the DB
    if (userId !== null && userId !== undefined) {
      UserApi.get(userId, auth)
        .then((response) => {
          if (
            response &&
            (response.status === 201 || response.status === 200)
          ) {
            const data = response.data;
            setUserData(data);
            if (data) {
              db.user.put(data);
            }
            setUserInfo({ username: data.login, agency: data.agency });
          } else {
            setUserData([]);
          }
        })
        .catch((error) => {
          setUserData([]);
        });
      UserRolesApi.get(auth).then((resp) => {
        if (resp && (resp.status === 201 || resp.status === 200)) {
          const data = resp.data;
          if (data) {
            db.userRoles.bulkPut(data);
          }
          setUserRoleData(data);
          setuserAdminInfo(
            data.some((role) => role["role_name"] === "administrator")
          );
          setLoginCompleted(true);
        } else {
          setUserRoleData([]);
          setLoginCompleted(true);
        }
      });
    }

    const interval = setInterval(() => {
      const { dateString, dayString, timeString } = getCurrentDateTime();
      setDate(dateString);
      setDay(dayString + ",");
      setTime(timeString);
      setIsLoading(false);
    }, 1000);

    // Function to update last active time
    const updateLastActive = async () => {
      if (userId) {
        try {
          await UserApi.updateLastActive(userId, auth);
        } catch (error) {
          console.error("Failed to update last active time:", error);
        }
      }
    };
    // Call updateLastActive immediately when userId is available
    if (userId) {
      updateLastActive();
    }

    // Set up interval to update last active time every 5 minutes
    const lastActiveInterval = setInterval(() => {
      if (userId) {
        updateLastActive();
      }
    }, 5 * 60 * 1000); // 5 minutes in milliseconds

    return () => {
      clearInterval(interval);
      clearInterval(lastActiveInterval);
    };
  }, [
    auth,
    setUserData,
    setUserRoleData,
    setLoginCompleted,
    userId,
  ]);

  return (
    <header>
      <div
        id="roadsafety-header"
        data-testid="roadsafety-header"
        className="header-container text-font"
        style={{ maxWidth: "100%" }}
      >
        <Row className="header">
          <Col sm={3}>
            <Link to="/">
              <div className="brand-logo"></div>
            </Link>
          </Col>
          {auth.isAuthenticated && !isLoading && (
            <Col sm={9}>
              <Row>
                <Col sm={4} className="time fw-bold mt-4">
                  &nbsp;<span className="text-light d-block large">{time}</span>
                  <span className="text-light d-block large">
                    {day} {date}
                  </span>
                </Col>
                <Col sm={2} className="icon mt-4">
                  {isConnected ? (
                    <CloudOutlinedIcon
                      sx={{ color: "white", fontSize: 80 }}
                    ></CloudOutlinedIcon>
                  ) : (
                    <CloudOffOutlinedIcon
                      sx={{ color: "white", fontSize: 80 }}
                    ></CloudOffOutlinedIcon>
                  )}
                </Col>
                <Col sm={6} className="user-info fw-bold col-right">
                  <Dropdown align="end">
                    <Dropdown.Toggle variant="link" id="dropdown-basic" className="text-white text-decoration-none p-0">
                      <div className="d-flex align-items-center">
                        <AccountCircle sx={{ fontSize: 40, marginRight: 1 }} />
                        <div className="text-start me-2">
                          <div>{userInfo.username}</div>
                          <div>{userInfo.agency}</div>
                        </div>
                        <ArrowDropDownIcon sx={{ fontSize: 24 }} />
                      </div>
                    </Dropdown.Toggle>

                    <Dropdown.Menu>
                      {userAdminInfo && (
                        <>
                          <Dropdown.Item as={Link} to="/admin-console">
                            Admin Console
                          </Dropdown.Item>
                          <Dropdown.Item as={Link} to="/admin-console/form-inventory">
                            Form Inventory
                          </Dropdown.Item>
                        </>
                      )}
                      <Dropdown.Item onClick={() => auth.signoutRedirect()}>Logout</Dropdown.Item>
                    </Dropdown.Menu>
                  </Dropdown>
                </Col>
              </Row>
            </Col>
          )}
        </Row>
      </div>
    </header>
  );

};
