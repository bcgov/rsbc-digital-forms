import React, { useState, useEffect } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

import { Radio } from "../../common/Radio/radio";
import { useFormikContext } from "formik";
import { useRecoilValue } from "recoil";
import { userAtom } from "../../../atoms/users";
import { Checkbox } from "../../common/Checkbox/checkbox";
import "./confirmationStep.scss";
import { pstDate } from "../../../utils/dateTime";

export const ConfirmationStep = () => {
  const { values, setFieldValue } = useFormikContext();
  const userData = useRecoilValue(userAtom);
  const documentServed = values["document-served"];
  const certifyNoticeDelivery = values["confirmation_of_service"];
  const twentyFourHourForm = values["TwentyFourHour"];
  const twelveHourForm = values["TwelveHour"];
  const vi = values["VI"];
  const driverGivenName = values["driver_given_name"];
  const driverLastName = values["driver_last_name"];
  const dateOfDriving = values["date_of_driving"];
  const timeOfDriving = values["time_of_driving"];

  useEffect(() => {
    if (values["confirmation_of_service"]) {
      setFieldValue("confirmation_of_service_date", pstDate(new Date()));
    }
    console.log("set value");
  }, [values["confirmation_of_service"], setFieldValue]);

  const generateLabel = () => {
    let formNames = [];
    if (vi) formNames.push("Vehicle Impound");
    if (twentyFourHourForm) formNames.push("24-hour Driving Prohibition");
    if (twelveHourForm) formNames.push("12-hour Driving Prohibition");

    let formNamesString = formNames.join(" and ");

    return `Did you serve the ${formNamesString} document${
      formNames.length > 1 ? "s" : ""
    } to ${driverLastName}, ${driverGivenName}?`;
  };
  const generateCertifyNotice = () => {
    const currentDate = new Date();

    const pacificDate = new Date(
      currentDate.toLocaleString("en-US", { timeZone: "America/Los_Angeles" })
    );

    const year = pacificDate.getFullYear();
    const month = String(pacificDate.getMonth() + 1).padStart(2, "0"); // months are 0-indexed in JS
    const day = String(pacificDate.getDate()).padStart(2, "0");

    const formattedPacificDate = `${year}-${month}-${day}`; // returns date in 'YYYY-MM-DD' format

    const formSubmittedDate = formattedPacificDate;
    const noticeNumber = "mock-232323";

    return `I, the peace officer identified below, certify that on ${formSubmittedDate} I served a printout under the Motor Vehicle Act or the Motor Vehicle Act Regulations, of notice number ${noticeNumber} on ${driverLastName}, ${driverGivenName} by personal delivery.`;
  };

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, "0");
    const day = String(date.getDate()).padStart(2, "0");
    return `${year}-${month}-${day}`;
  };

  const formatTime = (timeString) => {
    const date = new Date(timeString);
    const hours = String(date.getHours()).padStart(2, "0");
    const minutes = String(date.getMinutes()).padStart(2, "0");
    return `${hours}:${minutes}`;
  };

  let label = generateLabel();
  let certifyNoticeText = generateCertifyNotice();

  return (
    <div className="border-design-form left text-font">
      <h3>Confirmation</h3>
      <div className="row">
        <div className="col">
          <Radio
            label={label}
            name="document-served"
            options={[
              { label: "Yes", value: "YES" },
              { label: "No", value: "NO", disabled: true },
            ]}
            required
          />
        </div>
      </div>
      {documentServed === "YES" && (
        <div className="row">
          <div className="col">
            <Checkbox name="confirmation_of_service">
              {certifyNoticeText}
            </Checkbox>
          </div>
          {certifyNoticeDelivery === true && (
            <div>
              <br />
              <Container className="ecos-container">
                <Row>
                  <Col>
                    {"Enforcment Officers Name"}
                    <br />
                    {userData.last_name + ", " + userData.first_name}
                  </Col>
                  <Col>
                    {"Officers Number"}
                    <br />
                    {userData.badge_number}
                  </Col>
                </Row>
                <Row>
                  <Col>
                    {"Oranization/Detachment/Location of Officer"}
                    <br />
                    {userData.agency}
                  </Col>
                </Row>
                <Row>
                  <Col>
                    {"Date Certified (YYYY-MM-DD)"}
                    <br />
                    {formatDate(new Date())}
                  </Col>
                </Row>
              </Container>
              <span className="mt-4">
                The individual is prohibited under section 215 of the Motor
                Vehicle Act from driving a motor vehicle for
                {values["TwelveHour"] ? "12" : "24"} hours, commencing at
                {dateOfDriving ? formatDate(dateOfDriving) : "N/A"},
                {timeOfDriving ? formatTime(timeOfDriving) : "N/A"}
              </span>
            </div>
          )}
        </div>
      )}
    </div>
  );
};
