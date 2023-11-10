import "./commonForm.scss";
import PropTypes from "prop-types";
import React, { useState, useEffect } from "react";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import _ from "lodash";
import { Input } from "../common/Input/Input";
import { SearchableSelect } from "../common/Select/SearchableSelect";
import { useFormikContext } from "formik";
import Button from "react-bootstrap/Button";
import { MultiSelectField } from "../common/Select/MultiSelectField";
import { ICBCVehicleDataApi } from "../../api/icbcVehicleDataApi";

export const VehicleInfo = (props) => {
  const {
    vehicles,
    years,
    vehicleStyles,
    vehicleColours,
    jurisdictions,
    provinces,
    vehicleTypes,
  } = props;
  const { values, setFieldValue } = useFormikContext();
  const [disableBtn, setdisableBtn] = useState(true);
  const driversLicenceJurisdiction = values["vehicle_jurisdiction"];

  useEffect(() => {
    if (
      driversLicenceJurisdiction &&
      driversLicenceJurisdiction.value === "BC"
    ) {
      setdisableBtn(false);
    } else {
      setdisableBtn(true);
    }
  }, [driversLicenceJurisdiction]);

  const fetchICBCVehicleInfo = () => {
    if (values["vehicle_plate_no"]) {
      ICBCVehicleDataApi.get(values["vehicle_plate_no"]).then((resp) => {
        if (!_.isEmpty(resp.data)) {
          return;
        }
      });
    }
  };

  return (
    <div className="vehicle-info border-design-form left">
      <h3>Vehicle Information</h3>
      <div>
        <Row style={{ minHeight: "85px" }}>
          <Col sm={5}>
            <SearchableSelect
              className="field-height field-width"
              label="Jurisdiction"
              name="vehicle_jurisdiction"
              options={jurisdictions}
            />
          </Col>
          <Col sm={5}>
            <Input
              className="field-height field-width"
              label="Plate Number"
              name="vehicle_plate_no"
              type="text"
            />
          </Col>
          <Col sm={1} className="mt-4">
            <Button
              className="slim-button"
              variant="primary"
              disabled={disableBtn}
              onClick={() => fetchICBCVehicleInfo()}
            >
              ICBC Prefill
            </Button>
          </Col>
        </Row>

        <Row style={{ minHeight: "85px" }}>
          {(values["TwentyFourHour"] || values["VI"]) && (
            <Col sm={5}>
              <Input
                label="Registration Number"
                name="vehicle_registration_no"
                className="field-height field-width"
                type="text"
              />
            </Col>
          )}
          <Col sm={5}>
            <SearchableSelect
              className="field-height field-width"
              label="Vehicle Type"
              name="vehicle_type"
              options={vehicleTypes}
            />
          </Col>
        </Row>

        <Row style={{ minHeight: "85px" }}>
          <Col sm={3}>
            <SearchableSelect
              className="field-height field-width"
              label="Vehicle Year"
              name="vehicle_year"
              options={years}
            />
          </Col>
          <Col sm={3}>
            <SearchableSelect
              className="field-height field-width"
              label="Vehicle Make and Model"
              name="vehicle_mk_md"
              options={vehicles}
            />
          </Col>
          <Col sm={3}>
            <SearchableSelect
              className="field-height field-width"
              label="Vehicle Style"
              name="vehicle_style"
              options={vehicleStyles}
            />
          </Col>
          <Col sm={3}>
            <MultiSelectField
              className="field-width"
              label="Vehicle Colour(s)"
              name="vehicle_colour"
              options={vehicleColours}
            />
          </Col>
        </Row>
        <Row style={{ minHeight: "85px" }}>
          {(values["TwentyFourHour"] || values["VI"]) && (
            <Col sm={5}>
              <Input
                label="VIN Number"
                name="vehicle_vin_no"
                className="field-height field-width"
                type="text"
              />
            </Col>
          )}
          <Col sm={3}>
            <SearchableSelect
              className="field-height field-width"
              label="NSC Prov / State"
              name="nsc_prov_state"
              options={provinces}
            />
          </Col>
          <Col sm={4}>
            <Input
              label="NSC Number"
              name="nsc_no"
              className="field-height field-width"
              type="text"
            />
          </Col>
        </Row>
      </div>
    </div>
  );
};

VehicleInfo.propTypes = {
  vehicles: PropTypes.array.isRequired,
  vehicleStyles: PropTypes.array.isRequired,
  vehicleColours: PropTypes.array.isRequired,
  jurisdictions: PropTypes.array.isRequired,
  provinces: PropTypes.array.isRequired,
  years: PropTypes.array.isRequired,
};
