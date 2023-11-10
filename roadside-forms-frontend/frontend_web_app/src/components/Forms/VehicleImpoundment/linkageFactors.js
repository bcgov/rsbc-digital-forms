import React from "react";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { useFormikContext } from "formik";
import { Checkbox } from "../../common/Checkbox/checkbox";
import { Input } from "../../common/Input/Input";

export const LinkageFactors = (props) => {
  const { values } = useFormikContext();
  return (
    <div className="border-design-form left text-font">
      <h3>Linkage Factors</h3>
      <p>
        The officer determined the following: (relationship between driver,
        owner, and the vehicle)
      </p>
      <Row>
        <Col className="left checkboxs">
          <Checkbox name="linkage_location_of_keys">
            Location of vehicle key(s) (explain below or in incident details)
          </Checkbox>
          {values["linkage_location_of_keys"] && (
            <Input
              label="Where are the keys located?"
              name="linkage_location_of_keys_explanation"
              className="field-height field-width"
              type="text"
            ></Input>
          )}
          <Checkbox name="linkage_driver_principal">
            The driver is a principal operator
          </Checkbox>
          <Checkbox name="linkage_owner_in_vehicle">
            The owner was in the vehicle
          </Checkbox>
          <Checkbox name="linkage_owner_aware_possesion">
            The owner was aware the driver was in possession of the vehicle
            (explain in incident details)
          </Checkbox>
          <Checkbox name="linkage_vehicle_transfer_notice">
            Vehicle subject to a transfer notice (explain in incident details)
          </Checkbox>
          <Checkbox name="linkage_other">
            Other (explain in incident details)
          </Checkbox>
        </Col>
      </Row>
    </div>
  );
};

LinkageFactors.propTypes = {};
