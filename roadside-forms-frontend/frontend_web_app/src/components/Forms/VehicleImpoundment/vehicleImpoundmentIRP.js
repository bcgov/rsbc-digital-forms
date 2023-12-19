import React, { useEffect } from "react";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { useFormikContext } from "formik";
import PropTypes from "prop-types";
import { Radio } from "../../common/Radio/radio";
import { Input } from "../../common/Input/Input";

export const VehicleImpoundmentIRP = (props) => {
  const { values } = useFormikContext();

  useEffect(() => {
    if (values["irp_impound"] === "NO") {
      values["irp_impound_duration"] = "";
      values["IRP_number"] = "";
      values["VI_number"] = "";
    }
  }, [values["irp_impound"]]);

  return (
    <div className="border-design-form left text-font">
      <h3>Impoundment for Immediate Roadside Prohibition</h3>

      <Row>
        <Col>
          <Radio
            label="Was an IRP issued as a part of this vehicular impound?"
            lightLabel=" In accordance with section 215.46 and 253 of the Motor VehicleAct"
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
                    label: "3-Day IRP (Warn)",
                    value: "BACWARN3",
                  },
                  {
                    label: "7-Day IRP (Warn)",
                    value: "BACWARN7",
                  },
                  {
                    label: "30-day IRP (Warn)",
                    value: "BACWARN30",
                  },
                  {
                    label: "90-day IRP (Fail or Refusal)",
                    value: "BACFAIL",
                  },
                ]}
                required
              />
            </Col>
          </Row>
          {(values["irp_impound_duration"] === "BACWARN3" ||
            values["irp_impound_duration"] === "BACWARN7") && (
            <p style={{ color: "gray" }}>
              Vehicle <strong>could</strong> be impounded for:{" "}
              {values["irp_impound_duration"][7]} days
            </p>
          )}
          {(values["irp_impound_duration"] === "BACWARN30" ||
            values["irp_impound_duration"] === "BACFAIL") && (
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
