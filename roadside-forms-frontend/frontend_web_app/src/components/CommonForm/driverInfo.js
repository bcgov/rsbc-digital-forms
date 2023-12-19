import React, { useState, useEffect } from "react";
import PropTypes from "prop-types";
import _ from "lodash";
import { useFormikContext } from "formik";
import Modal from "react-bootstrap/Modal";
import Button from "react-bootstrap/Button";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import moment from "moment-timezone";
import { toast } from "react-toastify";

import { Input } from "../common/Input/Input";
import { SearchableSelect } from "../common/Select/SearchableSelect";
import { DateOfBirthField } from "../common/DateField/dateOfBirthField";
import { DatePickerField } from "../common/DateField/DatePicker";
import { PhoneField } from "../common/Input/phoneField";
import { dlScanner } from "../../utils/dlScanner";
import { ICBCDriverDataApi } from "../../api/icbcDriverDataAPI";
import { formatBCDL } from "../../utils/formatBCDL";
import { genderDropdown } from "../../utils/constants";
import "./commonForm.scss";
import { OverlayTrigger, Tooltip } from "react-bootstrap";

export const DriverInfo = (props) => {
  const { jurisdictions, provinces, jurisdictionCountry } = props;
  const { values, setFieldValue } = useFormikContext();
  const [disableBtn, setdisableBtn] = useState(true);
  const [modalShow, setModalShow] = useState(false);
  const [scannerOpened, setScannerOpened] = useState(false);
  const [dlJurisdictionOptions, setDlJurisdictionOptions] =
    useState(jurisdictions);
  const [driverJurisdictionOptions, setDriverJurisdictionOptions] =
    useState(jurisdictions);
  const driversLicenceJurisdiction = values["drivers_licence_jurisdiction"];

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

  useEffect(() => {
    if (values["TwelveHour"]) {
      values["driver_prov_state"] = jurisdictions.filter(
        (province) => province.value === "CA_BC"
      )[0];
    }
  }, [values["TwelveHour"]]);

  const renderTooltip = (props) => {
    if (values["TwelveHour"]) {
      return (
        <Tooltip id="button-tooltip" {...props}>
          Driver must be a BC resident for 12 hour Driving Prohibition
        </Tooltip>
      );
    } else {
      return <></>;
    }
  };

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

    values["driver_licence_no"] = formatBCDL(dl_data["number"], values);
    values["driver_last_name"] = dl_data["name"]["surname"];
    values["driver_given_name"] = dl_data["name"]["given"];
    values["driver_dob"] = new Date(dob_year, dob_month - 1, dob_day);
    values["drivers_licence_jurisdiction"] = jurisdictions.filter(
      (jurisdiction) => jurisdiction.value === dl_data["province"]
    )[0];
    values["driver_address"] = dl_data["address"]["street"];
    values["driver_city"] = dl_data["address"]["city"];
    values["driver_prov_state"] = provinces.filter(
      (province) => province.value === dl_data["address"]["province"]
    )[0];
    values["driver_postal"] = dl_data["address"]["postalCode"];

    const dl_expiry_year = "20" + dl_data["expiration"].slice(0, 2);
    const dl_expiry_month = dl_data["dob"].slice(4, 6);
    const dl_expiry_day = dl_data["dob"].slice(6, 8);
    values["driver_licence_expiry"] = new Date(
      dl_expiry_year + "/" + dl_expiry_month + "/" + dl_expiry_day
    );

    if (dl_data["gender"] === "M") {
      values["gender"] = genderDropdown[0];
    }
    if (dl_data["gender"] === "F") {
      values["gender"] = genderDropdown[1];
    }
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
        toast.error("An error occured while trying to read the DL.", {
          position: toast.POSITION.TOP_RIGHT,
        });
      });
  };

  const fetchICBCDriverInfo = () => {
    values["driver_licence_no"] = formatBCDL(
      values["driver_licence_no"],
      values
    );
    if (values["driver_licence_no"]) {
      ICBCDriverDataApi.get(values["driver_licence_no"]).then((resp) => {
        console.log(resp);
        if (!_.isEmpty(resp.data) && resp.status === "success") {
          const party = resp.data.party;
          const address = party.addresses[0];
          setFieldValue("driver_last_name", party.lastName);
          setFieldValue("driver_given_name", party.firstName);
          setFieldValue(
            "driver_dob",
            moment(party.birthDate).tz("America/Vancouver").toDate()
          );
          setFieldValue("driver_address", address.addressLine1);
          setFieldValue("driver_city", address.city);
          setFieldValue("driver_postal", address.postalCode);
        } else {
          toast.error("No driver was found using this DL number.", {
            position: toast.POSITION.TOP_RIGHT,
          });
        }
      });
    }
  };

  const handleJurisdictionChange = (event, setter) => {
    const newValue = event.value;
    // Update options based on the selected value
    if (newValue === "XX") {
      setter(jurisdictionCountry);
    } else if (newValue === "XZ") {
      setter(jurisdictions);
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
                  event.target.value = formatBCDL(event.target.value, values);
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
                  label="Province / State / International"
                  name="drivers_licence_jurisdiction"
                  onChange={(event) =>
                    handleJurisdictionChange(event, setDlJurisdictionOptions)
                  }
                  options={dlJurisdictionOptions}
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
              <OverlayTrigger placement="top" overlay={renderTooltip}>
                <div>
                  <SearchableSelect
                    className="field-height field-width"
                    label="Province / State / International"
                    name="driver_prov_state"
                    onChange={(event) =>
                      handleJurisdictionChange(
                        event,
                        setDriverJurisdictionOptions
                      )
                    }
                    options={driverJurisdictionOptions}
                  />
                </div>
              </OverlayTrigger>
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
                <SearchableSelect
                  className="field-height field-width"
                  label="Gender"
                  name="gender"
                  options={genderDropdown}
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
