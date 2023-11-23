import React from "react";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { Radio } from "../../common/Radio/radio";
import { Input } from "../../common/Input/Input";

export const Excessive = (props) => {
  return (
    <div className="border-design-form left text-font">
      <h3>Excessive Speed</h3>
      <Row>
        <Col sm={6}>
          <Input
            label="Speed Limit(KM/H)"
            name="speed_limit"
            className="field-height field-width"
            type="number"
            required
          ></Input>
        </Col>
        <Col sm={6}>
          <Input
            label="Vehicle Speed(KM/H)"
            name="vehicle_speed"
            className="field-height field-width"
            type="number"
            required
          ></Input>
        </Col>
      </Row>

      <Row>
        <Col>
          <Radio
            label="Vehicle speed estimated by:"
            name="speed_estimation_technique"
            options={[
              { label: "Visual", value: "VISUAL" },
              { label: "Pacing", value: "PACING" },
            ]}
            required
          />
        </Col>
      </Row>
      <Row>
        <Col>
          <Radio
            label="Vehicle speed confirmed by:"
            name="speed_confirmation_technique"
            options={[
              { label: "Laser", value: "LASER" },
              { label: "Radar", value: "RADAR" },
              { label: "Other(explain in incident details)", value: "OTHER" },
            ]}
            required
          />
        </Col>
      </Row>
    </div>
  );
};

Excessive.propTypes = {};
