import React, { useEffect } from "react";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { Checkbox } from "../../common/Checkbox/checkbox";
import "./vehicleImpound.scss";
import { OverlayTrigger, Tooltip } from "react-bootstrap";

export const VehicleImpoundmentReason = (props) => {
  const { values } = props;
  const renderTooltip = (props) => (
    <Tooltip id="button-tooltip" {...props}>
      This impound reason is currently under review by RSBC policy and is
      currently unenforceable under the MVA until changes are enacted.{" "}
    </Tooltip>
  );

  useEffect(() => {
    if (values["excessive_speed"] === false) {
      values["speed_limit"] = null;
      values["vehicle_speed"] = null;
      values["speed_estimation_technique"] = "";
      values["speed_confirmation_technique"] = "";
    }
  }, [values["excessive_speed"]]);

  useEffect(() => {
    if (values["out_of_province_dl"] === "NO") {
      values["out_of_province_dl_number"] = "";
      values["out_of_province_dl_jurisdiction"] = null;
      values["out_of_province_dl_expiry"] = null;
    }
  }, [values["out_of_province_dl"]]);

  useEffect(() => {
    if (!values["unlicensed"]) {
      values["unlicenced_prohibition_number"] = "";
      values["belief_driver_bc_resident"] = "";
      values["out_of_province_dl"] = "";
      values["out_of_province_dl_number"] = "";
      values["out_of_province_dl_jurisdiction"] = null;
      values["out_of_province_dl_expiry"] = null;
    }
  }, [values["unlicensed"]]);

  return (
    <div className="border-design-form left text-font">
      <h3>Impoundment for Driving Behaviour</h3>
      <p>7-Day Impoundment for the following reason(s):</p>
      <Row>
        <Col className="left checkboxs">
          <Checkbox name="excessive_speed">
            Excessive Speed
            <span className="light-text">
              - Committing an offence under section 148 of the Motor Vehicle
              Act.
            </span>
          </Checkbox>
          <Checkbox name="prohibited">
            Prohibited
            <span className="light-text">
              - Driving while prohibited under the Motor Vehicle Act, Criminal
              Code, Youth Justice Act or Youth Criminal Justice Act (Canada).
            </span>
          </Checkbox>
          <Checkbox name="suspended">
            Suspended
            <span className="light-text">
              - Driving while suspended under section 89 or section 232 of the
              Motor Vehicle Act.
            </span>
          </Checkbox>
          <Checkbox name="street_racing">
            Street Racing
            <span className="light-text">
              - Driving or operating a motor vehicle in a race as defined in the
              Motor Vehicle Act and the officer inteds to charge with an
              offence.
            </span>
          </Checkbox>
          <Checkbox name="stunt_driving">
            Stunt Driving
            <span className="light-text">
              - Driving or operating a motor vehicle in a stunt as defined in
              the Motor Vehicle Act and the officer inteds to charge with an
              offence.
            </span>
          </Checkbox>
          <Checkbox name="motorcycle_seating">
            Motorcycle (seating)
            <span className="light-text">
              - Committing an offence under section 194 (1) or (2) of the Motor
              Vehicle Act.
            </span>
          </Checkbox>
          <Checkbox name="unlicensed">
            Unlicensed (UL)
            <span className="light-text">
              - Driving without a valid driver's licence and with a notice on
              the driving record indicating a previous conviction for driving
              while unlicensed
            </span>
          </Checkbox>
        </Col>
      </Row>
    </div>
  );
};

VehicleImpoundmentReason.propTypes = {};
