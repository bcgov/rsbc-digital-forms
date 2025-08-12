import React, { useState, useEffect } from "react";
import Button from "react-bootstrap/Button";
import { Formik, Form } from "formik";
import { validate } from "./validate";
import WarningIcon from "@mui/icons-material/Warning";
import { Input } from "../common/Input/Input";
import { SearchableSelect } from "../common/Select/SearchableSelect";
import { UserApi } from "../../api/userApi";
import { staticResources } from "../../utils/helpers";
import { useRecoilState } from "recoil";
import { StaticDataApi } from "../../api/staticDataApi";
import { useRecoilValue } from "recoil";
import { userRolesAtom } from "../../atoms/userRoles";
import { loginCompletedAtom } from "../../atoms/loginCompleted";
import { useNavigate } from "react-router-dom";
import { useAuth } from "react-oidc-context";

export const RequestAccess = () => {
  const auth = useAuth();
  const [showApplication, setShowApplication] = useState(false);
  const [options, setOptions] = useState([]);
  const [showApplicationReceived, setShowApplicationReceived] = useState(false);
  const [agencies, setAgency] = useRecoilState(staticResources["agencies"]);
  const userRoles = useRecoilValue(userRolesAtom);
  const loginComplete = useRecoilValue(loginCompletedAtom);
  const navigate = useNavigate();

  const initialValues = {
    last_name: "",
    first_name: "",
    agency: null,
    badge_number: "",
  };

  const onSubmit = (values, { setSubmitting }) => {
    const data = {
      agency: values.agency.value,
      badge_number: values.badge_number,
      first_name: values.first_name,
      last_name: values.last_name,
    };
    UserApi.post(data, auth)
      .then((data) => {
        setSubmitting(false);
        setShowApplication(false);
        setShowApplicationReceived(true);
      })
      .catch((error) => {
        console.log("Error", error);
      });
  };

  const handleClick = () => {
    setShowApplication(true);
    if (agencies === undefined || (agencies && agencies.length === 0)) {
      StaticDataApi.get("agencies", auth).then((resp) => {
        setAgency(resp.data);
        setOptions(
          resp.data.map((item) => {
            return { label: item.agency_name, value: item };
          })
        );
      });
    } else {
      setOptions(
        agencies.map((item) => {
          return { label: item.agency_name, value: item };
        })
      );
    }
  };

  useEffect(() => {
    if (userRoles && userRoles.length !== 0) {
      navigate("/");
    }
  }, [userRoles, navigate]);

  return (
    <>
      {userRoles && userRoles.length === 0 && loginComplete && (
        <div className="border-design text-font">
          {!showApplicationReceived && (
            <div>
              <p>
                <span className="fw-bold">
                  Welcome to the Digital Forms system
                </span>
              </p>
              <p>
                <em>
                  WARNING: This system is for use by authorized law enforcement
                  officers only.
                </em>
              </p>
              <p>
                You currently do not have access to the Digital Forms system.
              </p>
              <p>
                Please apply for access after completing the training course and
                with the approval of your unit commander.
              </p>
            </div>
          )}
          {!showApplication && !showApplicationReceived && (
            <Button variant="primary" onClick={handleClick}>
              Apply for Access
            </Button>
          )}
          {showApplication && (
            <div>
              <div className=" d-flex justify-content-center mt-2">
                <Formik
                  initialValues={initialValues}
                  validate={validate}
                  onSubmit={onSubmit}
                >
                  {({ isSubmitting }) => (
                    <Form>
                      <div className="row">
                        <div className="col-sm-3">
                          <Input
                            label="SURNAME"
                            name="last_name"
                            className="field-width field-height"
                            type="text"
                          ></Input>
                        </div>
                        <div className="col-sm-3">
                          <Input
                            label="Given"
                            name="first_name"
                            className="field-width field-height"
                            type="text"
                          ></Input>
                        </div>
                        <div className="col-sm-4">
                          <SearchableSelect
                            label="Agency or RCMP Detachment"
                            className="field-width field-height"
                            name="agency"
                            options={options}
                          />
                        </div>
                        <div className="col-sm-2">
                          <Input
                            label="PRIME ID"
                            name="badge_number"
                            className="field-width field-height"
                            type="text"
                            maxLength={6}
                          ></Input>
                        </div>
                      </div>
                      <div className="info-container">
                        <div className="row">
                          <div className="col" />
                          <div
                            className="col-9 left-align"
                            style={{ textAlign: "center" }}
                          >
                            <p>
                              <WarningIcon className="text-warning" />{" "}
                              <span className="fw-bold">PRIME ID</span> is the
                              username you use to log into the MDT (CAD) and the
                              MRE.
                              <br />
                            </p>
                            <ul
                              className="ml-10"
                              style={{
                                listStylePosition: "inside",
                                textAlign: "center",
                              }}
                            >
                              <li>
                                For independents, this is your agency's
                                two-letter abbreviation followed by 2 to 4
                                numbers.
                              </li>
                              <br />
                              <li>
                                For RCMP members, this will be your 6 digit
                                HRMIS.
                              </li>
                            </ul>
                          </div>
                          <div className="col" />
                        </div>
                      </div>
                      <Button
                        variant="primary"
                        type="submit"
                        disabled={isSubmitting}
                      >
                        Apply for Access
                      </Button>
                    </Form>
                  )}
                </Formik>
              </div>
            </div>
          )}
          {showApplicationReceived && (
            <div>
              <p>
                <span className="fw-bold">Application received.</span>{" "}
                Thank-you!
              </p>
              <p>
                Your application will be reviewed and approved within 24
                business hours.
              </p>
            </div>
          )}
        </div>
      )}
    </>
  );
};
