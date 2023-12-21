import React, { useEffect } from "react";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { useFormikContext } from "formik";
import PropTypes from "prop-types";
import { Radio } from "../../common/Radio/radio";
import { Input } from "../../common/Input/Input";
import { DatePickerField } from "../../common/DateField/DatePicker";
import { TimeInputField } from "../../common/Input/TimeInputField";
import { SearchableSelect } from "../../common/Select/SearchableSelect";

export const Disposition = (props) => {
  const { impoundLotOperators, allILOs } = props;
  const { values, setFieldValue } = useFormikContext();

  const handleILOChange = (selectedOption) => {
    if (selectedOption) {
      const [name, address, city, phone] = selectedOption.label.split(", ");
      setFieldValue("ILO-name", name);
      setFieldValue("ILO-address", address);
      setFieldValue("ILO-city", city);
      setFieldValue("ILO-phone", phone);
      setFieldValue(
        "ILO-name-print",
        allILOs.find((operator) => operator.name === name).name_print
      );
    } else {
      setFieldValue("ILO-name", "");
      setFieldValue("ILO-address", "");
      setFieldValue("ILO-city", "");
      setFieldValue("ILO-phone", "");
      setFieldValue("ILO-name-print", "");
    }
  };

  useEffect(() => {
    if (values["vehicle_location"] !== "private") {
      setFieldValue("key-location", "");
      setFieldValue("ILO-name", "");
      setFieldValue("ILO-address", "");
      setFieldValue("ILO-city", "");
      setFieldValue("ILO-phone", "");
      setFieldValue("ILO-options", {});
      setFieldValue("ILO-name-print", "");
    }
  }, [values["vehicle_location"], setFieldValue]);

  const dispositionOptions = [
    { label: "Released to other driver", value: "released" },
    { label: "Left at roadside", value: "roadside" },
    { label: "Private tow", value: "private" },
  ];
  return (
    <div className="border-design-form left text-font">
      <h3>Disposition of Vehicle</h3>
      <Row style={{ minHeight: "85px" }}>
        <Col>
          <Radio
            label="Location of the vehicle?"
            name="vehicle_location"
            options={dispositionOptions}
            required
          />
        </Col>
      </Row>
      {values["vehicle_location"] === "released" && (
        <Row style={{ minHeight: "85px" }}>
          <Col sm={4}>
            <Input
              label="Vehicle Released To"
              name="vehicle_released_to"
              className="field-height field-width"
              type="text"
              required
            />
          </Col>
          <Col sm={4}>
            <DatePickerField
              name="date_released"
              label="Date Released"
              className="field-height field-width"
              required
            />
          </Col>
          <Col sm={4}>
            <TimeInputField
              label="Time"
              className="field-height field-width"
              name="time_released"
              required
            />
          </Col>
        </Row>
      )}
      {(values["vehicle_location"] === "roadside" ||
        values["vehicle_location"] === "private") && (
        <Row>
          <Col>
            <Radio
              label="Location of Keys?"
              name="location_of_keys"
              options={[
                { value: "WITH VEHICLE", label: "With vehicle" },
                { value: "WITH DRIVER", label: "With driver" },
              ]}
              required
            />
          </Col>
        </Row>
      )}

      {values["vehicle_location"] === "private" && (
        <>
          <div className="impound-lot-operator">
            <Row>
              <Col sm={12}>
                <SearchableSelect
                  onChange={handleILOChange}
                  className="field-height field-width"
                  label="Search for Impound Lot Operator"
                  name="ILO-options"
                  options={impoundLotOperators}
                />
              </Col>
            </Row>
            <div
              className="impoud-lot-fields"
              style={{ backgroundColor: "lightgray" }}
            >
              <Row>
                <Col sm={12}>
                  <Input
                    value={values["ILO-name"]}
                    label="Impound Lot Operator Name"
                    name="ILO-name"
                    className="field-height field-width"
                    type="text"
                    required
                  />
                </Col>
              </Row>
            </div>
            <Row>
              <Col sm={4}>
                <DatePickerField
                  name="date_released"
                  label="Date Released"
                  className="field-height field-width"
                  required
                />
              </Col>
              <Col sm={4}>
                <TimeInputField
                  label="Time Released"
                  className="field-height field-width"
                  name="time_released"
                  required
                />
              </Col>
            </Row>
          </div>
        </>
      )}
    </div>
  );
};

Disposition.propTypes = {
  impoundLotOperators: PropTypes.array.isRequired,
};
