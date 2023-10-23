import { Checkbox } from "../common/Checkbox/checkbox";
import { Input } from "../common/Input/Input";
import Button from "react-bootstrap/Button";
import { PhoneField } from "../common/Input/phoneField";
import { useEffect } from "react";
import PropTypes from "prop-types";
import { SearchableSelect } from "../common/Select/SearchableSelect";
import { useFormikContext } from "formik";
import "./commonForm.scss";

export const RegisteredOwnerInfo = (props) => {
  const { provinces } = props;
  const { values, setValues } = useFormikContext();
  const ownedByCorp = values["owned-by-corp"];

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
    };
    setValues({
      ...values,
      ...driverInfo,
    });
  };

  return (
    <div className="registered-owner-info border-design-form left">
      <div className="row" style={{ minHeight: "40px" }}>
        <div className="col-sm-10">
          <h3>Registered Owner</h3>
        </div>
        <div className="col-sm-2 right">
          <Button
            className="slim-button"
            variant="primary"
            onClick={handlePopulateFields}
          >
            Fill from driver
          </Button>
        </div>
      </div>
      <div className="row" style={{ minHeight: "85px" }}>
        <div className="col-sm-12 mt-4">
          <Checkbox name="owned_by_corp">Owned by Corporate Entity</Checkbox>
        </div>
      </div>
      {ownedByCorp ? (
        <div className="row" style={{ minHeight: "85px" }}>
          <div className="col-sm-12">
            <Input
              className="field-height field-width"
              name="corporation_name"
              label="Corporation Name"
            />
          </div>
        </div>
      ) : (
        <div className="row" style={{ minHeight: "85px" }}>
          <div className="col-sm-6">
            <Input
              className="field-height field-width"
              name="regist_owner_last_name"
              label="Owner's Last Name"
            />
          </div>
          <div className="col-sm-6">
            <Input
              className="field-height field-width"
              name="regist_owner_first_name"
              label="Owner's First Name"
            />
          </div>
        </div>
      )}
      <div className="row" style={{ minHeight: "85px" }}>
        <div className=" col-sm-9">
          <Input
            label="Address"
            name="regist_owner_address"
            className="field-height field-width"
            type="text"
          />
        </div>
        <div className=" col-sm-3">
          <PhoneField
            className="field-height field-width"
            label="Phone number"
            name="regist_owner_phone"
          />
        </div>
      </div>
      <div className="row" style={{ minHeight: "85px" }}>
        <div className=" col-sm-4">
          <Input
            label="City"
            name="regist_owner_city"
            className="field-height field-width"
            type="text"
          />
        </div>
        <div className=" col-sm-4">
          <SearchableSelect
            className="field-height field-width"
            label="Province / State"
            name="regist_owner_prov_state"
            options={provinces}
          />
        </div>
        <div className=" col-sm-4">
          <Input
            className="field-height field-width"
            label="Postal / Zip"
            name="regist_owner_postal"
          />
        </div>
      </div>
    </div>
  );
};

RegisteredOwnerInfo.propTypes = {
  provinces: PropTypes.array.isRequired,
};
