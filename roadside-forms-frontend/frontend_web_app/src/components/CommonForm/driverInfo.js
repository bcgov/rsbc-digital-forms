import { Input } from "../common/Input/Input";
import React, { useState, useEffect } from "react";
import { SearchableSelect } from "../common/Select/SearchableSelect";
import PropTypes from "prop-types";
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

export const DriverInfo = (props) => {
  const { jurisdictions, provinces } = props;
  const { values } = useFormikContext();
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
    //TODO: CONFIRM THIS NEXT LISTENER WORKS
    scanner.addEventListener("inputreport", handleScannedBarcode);
    setScannerOpened(!!scannerOpened);
  };

  const cancelDlScan = () => {
    setModalShow(false);
  };

  //TODO: FILL DRIVER INFO FROM SCAN
  const populateDriverFromBarCode = async (dl_data) => {
    console.log("dl_data: ", dl_data);
  };

  //TODO: LOOKUP PROVINCE FROM BARCODE
  const lookupDriverProvince = async (provinceArray) => {
    console.log("provincearray: ", provinceArray);
  };

  //TODO: VERIFY THIS WORKS
  const handleScannedBarcode = (event) => {
    console.log("EVENT: ", event);
    const { data, device, reportId } = event;
    dlScanner
      .readFromScanner(device, reportId, data)
      .then((dl_data) => {
        populateDriverFromBarCode(dl_data);
        return dl_data["address"]["province"];
      })
      .then((provinceCode) => {
        lookupDriverProvince([this.path, provinceCode]);
      })
      .then(() => {
        setModalShow(false);
      });
  };

  // Create conditional check for 12h
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
            <div>Please scan BC Driver's License.</div>
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
                type="text"
              />
            </Col>
            <Col sm={1} className="mt-4 pr-2">
              <Button
                className="slim-button"
                variant="primary"
                disabled={disableBtn}
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
                required
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
                required
              />
            </Col>
            <Col sm={4}>
              <SearchableSelect
                className="field-height field-width"
                label="Province / State"
                name="driver_prov_state"
                options={provinces}
                required
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
