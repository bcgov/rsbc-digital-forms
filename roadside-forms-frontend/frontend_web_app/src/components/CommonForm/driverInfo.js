import { Input } from "../common/Input/Input";
import React, { useState, useEffect } from "react";
import { SearchableSelect } from "../common/Select/SearchableSelect";
import PropTypes from "prop-types";
import _ from "lodash";
import Button from "react-bootstrap/Button";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { DateOfBirthField } from "../common/DateField/dateOfBirthField";
import { DatePickerField } from "../common/DateField/DatePicker";
import { PhoneField } from "../common/Input/phoneField";
import { useFormikContext } from "formik";
import "./commonForm.scss";
import Modal from "react-bootstrap/Modal";
import { dlScanner } from "../../utils/dlScanner";
import { ICBCDriverDataApi } from "../../api/icbcDriverDataAPI";
import { formatBCDL } from "../../utils/formatBCDL";

export const DriverInfo = (props) => {
  const { jurisdictions, provinces } = props;
  const { values, setFieldValue } = useFormikContext();
  const [disableBtn, setdisableBtn] = useState(true);
  const [modalShow, setModalShow] = useState(false);
  const [scannerOpened, setScannerOpened] = useState(false);
  const driversLicenceJurisdiction = values["drivers_licence_jurisdiction"];

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

  const launchDlScanner = async () => {
    setModalShow(true);
    let scanner = await dlScanner.openScanner();
    scanner.addEventListener("inputreport", handleScannedBarcode);
    setScannerOpened(true);
  };

  const cancelDlScan = () => {
    setModalShow(false);
  };

  const populateDriverFromBarCode = async (dl_data) => {
    const dob_year = dl_data["dob"].slice(0, 4);
    const dob_month = dl_data["dob"].slice(4, 6);
    const dob_day = dl_data["dob"].slice(6, 8);

    values["driver_licence_no"] = dl_data["number"];
    values["driver_last_name"] = dl_data["name"]["surname"];
    values["driver_given_name"] = dl_data["name"]["given"];
    values["driver_dob"] = new Date(dob_year, dob_month - 1, dob_day);
    values["drivers_licence_jurisdiction"] = jurisdictions.filter(
      (jurisdiction) => jurisdiction.value === dl_data["province"]
    );
    values["driver_address"] = dl_data["address"]["street"];
    values["driver_city"] = dl_data["address"]["city"];
    values["driver_prov_state"] = provinces.filter(
      (province) => province.value === dl_data["address"]["province"]
    );
    values["driver_postal"] = dl_data["address"]["postalCode"];
  };

  const handleScannedBarcode = (event) => {
    const { data, device, reportId } = event;
    dlScanner
      .readFromScanner(device, reportId, data)
      .then((dl_data) => {
        populateDriverFromBarCode(dl_data);
      })
      .then(() => {
        setModalShow(false);
      })
      .catch((err) => {
        console.error(
          "! An error occurred reading data from the scanner: ",
          err
        );
      });
  };

  const fetchICBCDriverInfo = () => {
    if (values["driver_licence_no"]) {
      ICBCDriverDataApi.get(values["driver_licence_no"]).then((resp) => {
        if (!_.isEmpty(resp.data)) {
          const party = resp.data.party;
          const address = party.addresses[0];
          setFieldValue("driver_last_name", party.lastName);
          setFieldValue("driver_given_name", party.firstName);
          setFieldValue("driver_dob", new Date(party.birthDate));
          setFieldValue("driver_address", address.addressLine1);
          setFieldValue("driver_city", address.city);
          setFieldValue("driver_postal", address.postalCode);
        }
      });
    }
  };

  return (
    <>
      <Modal
        aria-labelledby="contained-modal-title-vcenter"
        centered
        show={modalShow}
        onHide={() => setModalShow(false)}
      >
        <Modal.Header closeButton>
          <Modal.Title>Scan Driver's License</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          {scannerOpened ? (
            <div>Please scan BC Driver's License now.</div>
          ) : (
            <div> Requesting access to the DL scanner...</div>
          )}
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={cancelDlScan}>
            Cancel
          </Button>
        </Modal.Footer>
      </Modal>
      <div className="driver-info border-design-form left">
        <h3>Driver's Information</h3>
        <div>
          <Row style={{ minHeight: "85px" }}>
            <Col sm={4}>
              <Input
                className="field-height field-width"
                label="Driver's Licence Number"
                name="driver_licence_no"
                onBlur={(event) => {
                  event.target.value = formatBCDL(event, values);
                  values["driver_licence_no"] = event.target.value;
                }}
                type="text"
              />
            </Col>
            <Col sm={1} className="mt-4 pr-2">
              <Button
                className="slim-button"
                variant="primary"
                disabled={disableBtn}
                onClick={() => fetchICBCDriverInfo()}
              >
                ICBC Prefill
              </Button>
            </Col>
            <Col sm={1} className="mt-4 left">
              <Button
                className="slim-button"
                variant="primary"
                disabled={disableBtn}
                onClick={launchDlScanner}
              >
                Scan DL
              </Button>
            </Col>
            {!values["TwelveHour"] && (
              <Col sm={6}>
                <SearchableSelect
                  className="field-height field-width"
                  label="Province / State/ International"
                  name="drivers_licence_jurisdiction"
                  options={jurisdictions}
                />
              </Col>
            )}
          </Row>
          <Row style={{ minHeight: "85px" }}>
            <Col sm={4}>
              <Input
                label="Last Name"
                name="driver_last_name"
                className="field-height field-width"
                type="text"
                required
              />
            </Col>
            <Col sm={4}>
              <Input
                label="Given Name"
                name="driver_given_name"
                className="field-height field-width"
                type="text"
              />
            </Col>
            <Col sm={4}>
              <DateOfBirthField
                className="field-height field-width"
                label="Date Of Birth"
                name="driver_dob"
              />
            </Col>
          </Row>
          <Row style={{ minHeight: "85px" }}>
            <Col sm={9}>
              <Input
                label="Address"
                name="driver_address"
                className="field-height field-width"
                type="text"
              />
            </Col>
            <Col sm={3}>
              <PhoneField
                className="field-height field-width"
                label="Phone number"
                name="driver_phone"
              />
            </Col>
          </Row>
          <Row style={{ minHeight: "85px" }}>
            <Col sm={4}>
              <Input
                label="City"
                name="driver_city"
                className="field-height field-width"
                type="text"
              />
            </Col>
            <Col sm={4}>
              <SearchableSelect
                className="field-height field-width"
                label="Province / State"
                name="driver_prov_state"
                options={provinces}
              />
            </Col>
            <Col sm={4}>
              <Input
                className="field-height field-width"
                label="Postal / Zip"
                name="driver_postal"
              />
            </Col>
          </Row>
          {values["VI"] && (
            <Row style={{ minHeight: "85px" }}>
              <Col sm={4}>
                <Input
                  label="Gender"
                  name="gender"
                  className="field-height field-width"
                  type="text"
                />
              </Col>
              <Col sm={4}>
                <DatePickerField
                  className="field-height field-width"
                  label="Licence Expiry Date"
                  name="driver_licence_expiry"
                />
              </Col>
              <Col sm={4}>
                <Input
                  className="field-height field-width"
                  label="BCDL Class"
                  name="driver_licence_class"
                />
              </Col>
            </Row>
          )}
        </div>
      </div>
    </>
  );
};

DriverInfo.propTypes = {
  jurisdictions: PropTypes.array.isRequired,
  provinces: PropTypes.array.isRequired,
};
