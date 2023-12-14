import React from "react";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { useFormikContext } from "formik";
import PropTypes from "prop-types";
import { Radio } from "../../common/Radio/radio";
import { Input } from "../../common/Input/Input";

export const VehicleImpoundmentIRP = (props) => {
  const { values } = useFormikContext();

  return (
    <div className="border-design-form left text-font">
      <h3>Impoundment for Immediate Roadside Prohibition</h3>

      <Row>
        <Col>
          <Radio
            label="Was an IRP issued as a part of this vehicular impound?"
            name="irp_impound"
            options={[
              { label: "Yes", value: "YES" },
              { label: "No", value: "NO" },
            ]}
            required
          />
        </Col>
      </Row>

      {values["irp_impound"] === "YES" && (
        <>
          <Row>
            <Col>
              <Radio
                label="IRP Duration"
                name="irp_impound_duration"
                options={[
                  {
                    label: "3 Day IRP",
                    value: "3DAY",
                  },
                  {
                    label: "7 Day IRP",
                    value: "7DAY",
                  },
                  {
                    label: "30 day IRP",
                    value: "30DAY",
                  },
                  {
                    label: "90 day IRP",
                    value: "90DAY",
                  },
                ]}
                required
              />
            </Col>
          </Row>
          {(values["irp_impound_duration"] === "3DAY" ||
            values["irp_impound_duration"] === "7DAY") && (
            <p style={{ color: "gray" }}>
              Vehicle <strong>could</strong> be impounded for:{" "}
              {values["irp_impound_duration"][0]} days
            </p>
          )}
          {(values["irp_impound_duration"] === "30DAY" ||
            values["irp_impound_duration"] === "90DAY") && (
            <p style={{ color: "gray" }}>
              Vehicle <strong>must</strong> be impounded for: 30 days
            </p>
          )}
          <Row>
            <Col sm={6}>
              <Input
                label="IRP Number"
                name="IRP_number"
                className="field-height field-width"
                type="text"
                required
              ></Input>
            </Col>
            <Col sm={6}>
              <Input
                label="This VI Number"
                name="VI_number"
                className="field-height field-width"
                type="text"
                required
              ></Input>
            </Col>
          </Row>
        </>
      )}
    </div>
  );
};

VehicleImpoundmentIRP.propTypes = {};
