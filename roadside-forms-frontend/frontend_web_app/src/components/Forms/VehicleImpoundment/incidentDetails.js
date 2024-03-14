import React, { useState } from "react";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { Checkbox } from "../../common/Checkbox/checkbox";
import { TextAreaInput } from "../../common/Input/TextAreaInput";

export const IncidentDetails = (props) => {
  const { values } = props;
  const [input, setInput] = useState(values["incident_details"]);
  const handleChange = (event) => {
    setInput(event.target.value);
  };

  return (
    <div className="border-design-form left text-font">
      <h3>Incident Details</h3>
      <Row>
        <Col className="left checkboxs">
          {/* <Checkbox name="incident_details_extra_page">
            Will a separate document be attached?
          </Checkbox> */}
          <span>{input.length + "/3000"}</span>
          <TextAreaInput
            name="incident_details"
            className="text-area-height field-width"
            maxLength="3000"
            onChange={handleChange}
            value={input}
            placeholder="Enter details here..."
          />
        </Col>
      </Row>
    </div>
  );
};

IncidentDetails.propTypes = {};
