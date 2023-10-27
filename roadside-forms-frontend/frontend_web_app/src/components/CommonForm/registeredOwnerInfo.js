import { Checkbox } from "../common/Checkbox/checkbox";
import { Input } from "../common/Input/Input";
import Button from "react-bootstrap/Button";
import { PhoneField } from "../common/Input/phoneField";
import { useEffect } from "react";
import PropTypes from "prop-types";
import { SearchableSelect } from "../common/Select/SearchableSelect";
import { useFormikContext } from "formik";
import "./commonForm.scss";
import { Row, Col } from "react-bootstrap";
import { DateOfBirthField } from "../common/DateField/dateOfBirthField";

export const RegisteredOwnerInfo = (props) => {
  const { provinces } = props;
  const { values, setValues } = useFormikContext();
  const ownedByCorp = values["owned_by_corp"];

  useEffect(() => {
    // If user autofill owner info from driver info and then click owned by corp checkbox, this logic will remove autofilled owner info
    if (
      ownedByCorp &&
      (values["regist_owner_last_name"] !== "" ||
        values["regist_owner_first_name"] !== "")
    ) {
      const updatedValues = {
        ...values,
        regist_owner_last_name: "",
        regist_owner_first_name: "",
      };

      setValues(updatedValues);
    }
  }, [ownedByCorp, setValues, values]);

  // TODO: Clear driver first + last name + DOB when corporate ownership checked

  const handlePopulateFields = () => {
    // Get the driver information and populate registered owner fields when prefill button is clicked
    const driverInfo = {
      regist_owner_last_name: ownedByCorp ? "" : values["driver_last_name"],
      regist_owner_first_name: ownedByCorp ? "" : values["driver_given_name"],
      regist_owner_address: values["driver_address"],
      regist_owner_phone: values["driver_phone"],
      regist_owner_city: values["driver_city"],
      regist_owner_prov_state: values["driver_prov_state"],
      regist_owner_postal: values["driver_postal"],
      regist_owner_dob: values["driver_dob"],
      driver_is_regist_owner: true,
      owned_by_corp: false,
      corporation_name: "",
    };
    setValues({
      ...values,
      ...driverInfo,
    });
  };

  return (
    <div className="registered-owner-info border-design-form left">
      <Row style={{ minHeight: "40px" }}>
        <Col sm={10}>
          <h3>Registered Owner</h3>
        </Col>
        <Col sm={2}>
          <Button
            className="slim-button"
            variant="primary"
            onClick={handlePopulateFields}
          >
            Fill from driver
          </Button>
        </Col>
      </Row>
      <Row style={{ minHeight: "85px", marginTop: "20px" }}>
        <Col sm={6}>
          <Checkbox name="owned_by_corp">Owned by Corporate Entity</Checkbox>
        </Col>
        {values["VI"] && (
          <Col sm={6}>
            <Checkbox name="driver_is_regist_owner">
              The driver is the registered owner
            </Checkbox>
          </Col>
        )}
      </Row>
      {ownedByCorp ? (
        <Row className="row" style={{ minHeight: "85px" }}>
          <Col className="col-sm-12">
            <Input
              className="field-height field-width"
              name="corporation_name"
              label="Corporation Name"
            />
          </Col>
        </Row>
      ) : (
        <Row className="row" style={{ minHeight: "85px" }}>
          <Col className="col-sm-5">
            <Input
              className="field-height field-width"
              name="regist_owner_last_name"
              label="Owner's Last Name"
            />
          </Col>
          <Col className="col-sm-5">
            <Input
              className="field-height field-width"
              name="regist_owner_first_name"
              label="Owner's First Name"
            />
          </Col>
          <Col className="col-sm-2">
            <DateOfBirthField
              className="field-height field-width"
              name="regist_owner_dob"
              label="Owner's Date of Birth"
            />
          </Col>
        </Row>
      )}
      <Row className="row" style={{ minHeight: "85px" }}>
        <Col className="col-sm-4">
          <Input
            label="Address"
            name="regist_owner_address"
            className="field-height field-width"
            type="text"
          />
        </Col>
        <Col className=" col-sm-4">
          <PhoneField
            className="field-height field-width"
            label="Phone Number"
            name="regist_owner_phone"
          />
        </Col>
        <Col className="col-sm-4">
          <Input
            label="Email Address"
            name="regist_owner_email"
            className="field-height field-width"
            type="text"
          />
        </Col>
      </Row>
      <Row className="row" style={{ minHeight: "85px" }}>
        <Col className=" col-sm-4">
          <Input
            label="City"
            name="regist_owner_city"
            className="field-height field-width"
            type="text"
          />
        </Col>
        <Col className=" col-sm-4">
          <SearchableSelect
            className="field-height field-width"
            label="Province / State"
            name="regist_owner_prov_state"
            options={provinces}
          />
        </Col>
        <Col className=" col-sm-4">
          <Input
            className="field-height field-width"
            label="Postal / Zip"
            name="regist_owner_postal"
          />
        </Col>
      </Row>
    </div>
  );
};

RegisteredOwnerInfo.propTypes = {
  provinces: PropTypes.array.isRequired,
};
