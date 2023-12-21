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
import { toast } from "react-toastify";

export const VehicleInfo = (props) => {
  const {
    vehicles,
    years,
    vehicleStyles,
    vehicleColours,
    jurisdictions,
    jurisdictionCountry,
    vehicleTypes,
    nscPuj,
  } = props;
  const { values, setFieldValue } = useFormikContext();
  const [disableBtn, setdisableBtn] = useState(true);
  const [vehicleJurisdictionOptions, setVehicleJurisdictionOptions] =
    useState(jurisdictions);
  const driversLicenceJurisdiction = values["vehicle_jurisdiction"];
  if (nscPuj[0].value !== "") {
    nscPuj.unshift({ value: "", label: "---" });
  }

  useEffect(() => {
    if (
      driversLicenceJurisdiction &&
      driversLicenceJurisdiction.value === "CA_BC"
    ) {
      setdisableBtn(false);
    } else {
      setdisableBtn(true);
    }
  }, [driversLicenceJurisdiction]);

  const fetchICBCVehicleInfo = async () => {
    if (values["vehicle_plate_no"]) {
      await ICBCVehicleDataApi.get(values["vehicle_plate_no"]).then((resp) => {
        //ICBC sends back different responses based on sucess and fail and only real way to check is if it is an array
        if (resp.status === "success") {
          const vehicle = resp.data[0];
          const party = vehicle.vehicleParties[0].party;
          const address = party.addresses[0];
          setFieldValue("nsc_no", vehicle.nscNumber);
          setFieldValue("vehicle_registration_no", vehicle.registrationNumber);
          const colour = vehicleColours.filter(
            (item) => item.label === vehicle.vehicleColour.toUpperCase()
          )[0].value;
          setFieldValue("vehicle_colour", [colour]);
          setFieldValue("vehicle_mk_md", vehicle.vehicleMake + " - ");
          setFieldValue("vehicle_vin_no", vehicle.vehicleIdNumber);
          setFieldValue(
            "vehicle_year",
            years.filter((item) => item.label === vehicle.vehicleModelYear)
          );
          setFieldValue(
            "vehicle_type",
            vehicleTypes.filter(
              (item) => item.label === vehicle.vehicleType.toUpperCase()
            )
          );
          setFieldValue("vehicle_jurisdiction", {
            value: "CA_BC",
            label: "BRITISH COLUMBIA",
          });
          setFieldValue("regist_owner_last_name", party.lastName);
          setFieldValue("regist_owner_first_name", party.firstName);
          setFieldValue("regist_owner_dob", new Date(party.birthDate));
          setFieldValue("regist_owner_address", address.addressLine1);
          setFieldValue("regist_owner_city", address.city);
          setFieldValue("regist_owner_postal", address.postalCode);
          setFieldValue("regist_owner_prov_state", {
            value: "CA_BC",
            label: "BRITISH COLUMBIA",
          });
          return;
        } else {
          toast.error("No vehicle was found using this plate number.", {
            position: toast.POSITION.TOP_RIGHT,
          });
        }
      });
    }
  };

  const handleJurisdictionChange = (event) => {
    const newValue = event.value;
    // Update options based on the selected value
    if (newValue === "XX") {
      setVehicleJurisdictionOptions(jurisdictionCountry);
    } else if (newValue === "XZ") {
      setVehicleJurisdictionOptions(jurisdictions);
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
              onChange={handleJurisdictionChange}
              options={vehicleJurisdictionOptions}
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
              required
            />
          </Col>
          <Col sm={3}>
            <SearchableSelect
              className="field-height field-width"
              label="Vehicle Make and Model"
              name="vehicle_mk_md"
              options={vehicles}
              required
            />
          </Col>
          <Col sm={3}>
            <SearchableSelect
              className="field-height field-width"
              label="Vehicle Style"
              name="vehicle_style"
              options={vehicleStyles}
              required
            />
          </Col>
          <Col sm={3}>
            <MultiSelectField
              className="field-width"
              label="Vehicle Colour(s)"
              name="vehicle_colour"
              options={vehicleColours}
              required
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
                required
              />
            </Col>
          )}
          <Col sm={3}>
            <SearchableSelect
              className="field-height field-width"
              label="NSC Prov / State"
              name="nsc_prov_state"
              options={nscPuj}
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
  jurisdictionCountry: PropTypes.array.isRequired,
  nscPuj: PropTypes.array.isRequired,
  years: PropTypes.array.isRequired,
};
