import "./commonForm.scss";
import PropTypes from "prop-types";
import React, { useState, useEffect } from "react";
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
          console.log(resp.data);
          //       setFieldValue("driver_last_name", party.lastName);
          //       setFieldValue("driver_given_name", party.firstName);
          //       setFieldValue("driver_dob", new Date(party.birthDate));
          //       setFieldValue("driver_address", address.addressLine1);
          //       setFieldValue("driver_city", address.city);
          //       setFieldValue("driver_postal", address.postalCode);
        }
      });
    }
  };

  return (
    <div className="vehicle-info border-design-form left">
      <h3>Vehicle Information</h3>
      <div>
        <div className="row" style={{ minHeight: "85px" }}>
          <div className="col-sm-5">
            <SearchableSelect
              className="field-height field-width"
              label="Jurisdiction"
              name="vehicle_jurisdiction"
              options={jurisdictions}
            />
          </div>
          <div className=" col-sm-5">
            <Input
              className="field-height field-width"
              label="Plate Number"
              name="vehicle_plate_no"
              type="text"
            />
          </div>
          <div className=" col-sm-1 mt-4">
            <Button
              className="slim-button"
              variant="primary"
              disabled={disableBtn}
              onClick={() => fetchICBCVehicleInfo()}
            >
              ICBC Prefill
            </Button>
          </div>
        </div>
        {(values["TwentyFourHour"] || values["VI"]) && (
          <div className="row" style={{ minHeight: "85px" }}>
            <div className=" col-sm-5">
              <Input
                label="Registration Number"
                name="vehicle_registration_no"
                className="field-height field-width"
                type="text"
              />
            </div>
          </div>
        )}
        <div className="row" style={{ minHeight: "85px" }}>
          <div className=" col-sm-3">
            <SearchableSelect
              className="field-height field-width"
              label="Vehicle Year"
              name="vehicle_year"
              options={years}
            />
          </div>
          <div className=" col-sm-3">
            <SearchableSelect
              className="field-height field-width"
              label="Vehicle Make and Model"
              name="vehicle_mk_md"
              options={vehicles}
            />
          </div>
          <div className=" col-sm-3">
            <SearchableSelect
              className="field-height field-width"
              label="Vehicle Style"
              name="vehicle_style"
              options={vehicleStyles}
            />
          </div>
          <div className=" col-sm-3">
            <MultiSelectField
              className="field-width"
              label="Vehicle Colour(s)"
              name="vehicle_colour"
              options={vehicleColours}
            />
          </div>
        </div>
        <div className="row" style={{ minHeight: "85px" }}>
          {(values["TwentyFourHour"] || values["VI"]) && (
            <div className=" col-sm-5">
              <Input
                label="VIN Number"
                name="vehicle_vin_no"
                className="field-height field-width"
                type="text"
              />
            </div>
          )}
          <div className=" col-sm-3">
            <SearchableSelect
              className="field-height field-width"
              label="NSC Prov / State"
              name="nsc_prov_state"
              options={provinces}
            />
          </div>
          <div className=" col-sm-4">
            <Input
              label="NSC Number"
              name="nsc_no"
              className="field-height field-width"
              type="text"
            />
          </div>
        </div>
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
