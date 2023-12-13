import React, { useEffect } from "react";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { useFormikContext } from "formik";
import PropTypes from "prop-types";
import { Radio } from "../../common/Radio/radio";
import { Input } from "../../common/Input/Input";
import { DatePickerField } from "../../common/DateField/DatePicker";
import { TimeInputField } from "../../common/Input/TimeInputField";
import { PhoneField } from "../../common/Input/phoneField";
import { SearchableSelect } from "../../common/Select/SearchableSelect";

export const VehicleImpoundment = (props) => {
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
    if (values["VI"]) {
      setFieldValue("vehicle_impounded", "YES");
    }
    if (values["vehicle_impounded"] === "NO") {
      setFieldValue("key-location", "");
      setFieldValue("ILO-name", "");
      setFieldValue("ILO-address", "");
      setFieldValue("ILO-city", "");
      setFieldValue("ILO-phone", "");
      setFieldValue("ILO-options", {});
      setFieldValue("ILO-name-print", "");
    } else if (values["vehicle_impounded"] === "YES") {
      setFieldValue("reason_for_not_impounding", "");
      setFieldValue("date_released", null);
      setFieldValue("time_released", "");
      setFieldValue("vehicle_released_to", "");
    }
  }, [values["vehicle_impounded"], values["VI"], setFieldValue]);

  const reasonForNotImpounding = [
    { label: "Released to other driver", value: "released" },
    { label: "Left at roadside", value: "roadside" },
    { label: "Private tow", value: "private" },
    { label: "Seized for investigation", value: "investigation" },
  ];
  return (
    <div className="border-design-form left text-font">
      <h3>Vehicle Impoundment or Disposition</h3>
      {!values["VI"] && (
        <Row>
          <Col>
            <Radio
              label="Vehicle Impounded?"
              name="vehicle_impounded"
              options={[
                { label: "Yes", value: "YES" },
                { label: "No", value: "NO" },
              ]}
              required
            />
          </Col>
        </Row>
      )}
      {values["VI"] && (
        <Row>
          <Col>
            <DatePickerField
              name="date_of_impound"
              label="Date of vehicle impound"
              className="field-height field-width"
              required
            />
          </Col>
        </Row>
      )}
      {(values["TwentyFourHour"] || values["TwelveHour"]) &&
        values["vehicle_impounded"] === "YES" && (
          <>
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
          </>
        )}
      {(((values["TwentyFourHour"] || values["TwelveHour"]) &&
        values["vehicle_impounded"] === "YES") ||
        values["VI"]) && (
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
              <Row>
                <Col sm={4}>
                  <Input
                    value={values["ILO-address"]}
                    label="Public Lot Address"
                    name="ILO-address"
                    className="field-height field-width"
                    type="text"
                    required
                  />
                </Col>
                <Col sm={4}>
                  <Input
                    value={values["ILO-city"]}
                    label="City"
                    name="ILO-city"
                    className="field-height field-width"
                    type="text"
                    required
                  />
                </Col>
                <Col sm={4}>
                  <PhoneField
                    value={values["ILO-phone"]}
                    className="field-height field-width"
                    label="Public Phone Number"
                    name="ILO-phone"
                    required
                  />
                </Col>
              </Row>
            </div>
          </div>
        </>
      )}
      {values["vehicle_impounded"] === "NO" && (
        <>
          <Row style={{ minHeight: "85px" }}>
            <Col>
              <Radio
                label="Reason for not impounding?"
                name="reason_for_not_impounding"
                options={reasonForNotImpounding}
                required
              />
            </Col>
          </Row>
          {values["reason_for_not_impounding"] === "released" && (
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
        </>
      )}
    </div>
  );
};

VehicleImpoundment.propTypes = {
  impoundLotOperators: PropTypes.array.isRequired,
};
