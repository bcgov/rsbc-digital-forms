import React, { useState, useEffect } from "react";
import { Formik, Form } from "formik";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import Spinner from "react-bootstrap/Spinner";
import { toPng, toBlob } from "html-to-image";
import { Checkbox } from "../common/Checkbox/checkbox";
import { validationSchema } from "./validationSchema";
import { DriverInfo } from "../CommonForm/driverInfo";
import { InitialValues } from "./initialValues";
import { VehicleInfo } from "../CommonForm/vehicleInfo";
import { OfficerInfo } from "../CommonForm/officerInfo";
import { VehicleImpoundment } from "../Forms/TwentyFourHourForm/vehicleImpoundment";
import { Disposition } from "../Forms/TwelveHourForm/dispositionOfVehicle";
import { Prohibition } from "../Forms/TwentyFourHourForm/prohibition";
import { ReasonableGrounds } from "../Forms/TwentyFourHourForm/reasonableGrounds";
import { TestAdministered } from "../Forms/TwentyFourHourForm/testAdministered";
import { VehicleImpoundmentIRP } from "../Forms/VehicleImpoundment/vehicleImpoundmentIRP";
import { VehicleImpoundmentReason } from "../Forms/VehicleImpoundment/vehicleImpoundmentReason";
import { Excessive } from "../Forms/VehicleImpoundment/excessive";
import { Unlicensed } from "../Forms/VehicleImpoundment/unlicensed";
import { LinkageFactors } from "../Forms/VehicleImpoundment/linkageFactors";
import { IncidentDetails } from "../Forms/VehicleImpoundment/incidentDetails";
import { RegisteredOwnerInfo } from "../CommonForm/registeredOwnerInfo";
import { useRecoilValue } from "recoil";
import { useNavigate } from "react-router-dom";
import { ConfirmationStep } from "./ConfirmationStep/confirmationStep";
import { PoliceDetails } from "../Forms/TwentyFourHourForm/policeDetails";
import {
  staticResources,
  getEventDataToSave,
  formsPNG,
  formNumberChecksum,
} from "../../utils/helpers";
import { FormSubmissionApi } from "../../api/formSubmissionApi";
import { SVGprint } from "../Forms/Print/svgPrint";
import { db } from "../../db";
import "./createEvent.scss";
import { FormIDApi } from "../../api/formIDApi";
import { Alert } from "react-bootstrap";
const { v4: uuidv4 } = require("uuid");

export const CreateEvent = () => {
  const vehicleStylesAtom = useRecoilValue(staticResources["vehicle_styles"]);
  const vehicleTypesAtom = useRecoilValue(staticResources["vehicle_types"]);
  const vehicleColoursAtom = useRecoilValue(staticResources["vehicle_colours"]);
  const jurisdictionsAtom = useRecoilValue(staticResources["jurisdictions"]);
  const provincesAtom = useRecoilValue(staticResources["provinces"]);
  const cityAtom = useRecoilValue(staticResources["cities"]);
  const vehiclesAtom = useRecoilValue(staticResources["vehicles"]);
  const impoundAtom = useRecoilValue(staticResources["impound_lot_operators"]);
  const [formValues, setFormValues] = useState([]);
  const [formIDs, setFormIDs] = useState({
    VI: "",
    IRP: "",
    TwentyFourHour: "",
    TwelveHour: "",
  });
  const [formIDsFetched, setFormIDsFetched] = useState(false);
  const [jurisdictions, setJurisdictions] = useState([]);
  const [provinces, setProvinces] = useState([]);
  const [vehicleStyles, setVehicleStyles] = useState([]);
  const [vehicleTypes, setVehicleTypes] = useState([]);
  const [vehicles, setVehicles] = useState([]);
  const [vehicleColours, setVehicleColours] = useState([]);
  const [cities, setCities] = useState([]);
  const [impoundLotOperators, setImpoundLotOperators] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);
  const [show, setShow] = useState(false);
  const [modalTitle, setModalTitle] = useState("");
  const [modalBody, setModalBody] = useState("");
  const [modalButtonOneText, setModalButtonOneText] = useState("");
  const [modalButtonTwoText, setModalButtonTwoText] = useState("");
  const [isPrinted, setIsPrinted] = useState(false);
  const [modalCloseFunc, setmodalCloseFunc] = useState(() => () => null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [formHasErrors, setFormHasErrors] = useState(false);
  const [formErrors, setFormErrors] = useState([]);

  const navigate = useNavigate();

  useEffect(() => {
    const fetchOneOfEachID = async () => {
      const VINum = await db.formID
        .where("[form_type+leased]")
        .anyOf([["VI", 0]])
        .first();
      console.log("VINum: ", VINum);

      const IRPNum = await db.formID
        .where("[form_type+leased]")
        .anyOf([["IRP", 0]])
        .first();
      const twentyFourNum = await db.formID
        .where("[form_type+leased]")
        .anyOf([["24Hour", 0]])
        .first();
      const twelveNum = await db.formID
        .where("[form_type+leased]")
        .anyOf([["12Hour", 0]])
        .first();

      await setFormIDs({
        VI: VINum.id,
        IRP: IRPNum.id,
        TwentyFourHour: twentyFourNum.id,
        TwelveHour: twelveNum.id,
      });

      // Go into indexedDB and mark all form IDs we are leasing for this form as "leased"
      await db.formID.where("id").equals(VINum.id).modify({ leased: 1 });
      await db.formID.where("id").equals(IRPNum.id).modify({ leased: 1 });
      await db.formID
        .where("id")
        .equals(twentyFourNum.id)
        .modify({ leased: 1 });
      await db.formID.where("id").equals(twelveNum.id).modify({ leased: 1 });
      await setFormIDsFetched(true);
    };
    setJurisdictions(
      jurisdictionsAtom.map((each) => ({
        label: each.objectDsc,
        value: each.objectCd,
      }))
    );
    setImpoundLotOperators(
      impoundAtom.map((each) => ({
        label:
          each.name +
          ", " +
          each.lot_address +
          ", " +
          each.city +
          ", " +
          each.phone,
        value: each.id,
      }))
    );
    setProvinces(
      provincesAtom.map((each) => ({
        label: each.objectDsc,
        value: each.objectCd,
      }))
    );
    setVehicleStyles(
      vehicleStylesAtom.map((each) => ({ label: each.name, value: each.code }))
    );
    setVehicleTypes(
      vehicleTypesAtom.map((each) => ({
        label: each.description,
        value: each.type_cd,
      }))
    );
    setVehicleColours(
      vehicleColoursAtom.map((each) => ({
        label: each.display_name,
        value: each.code,
      }))
    );
    setVehicles(
      vehiclesAtom.map((each) => ({
        label: each.search,
        value: each.mk + "-" + each.md,
      }))
    );
    setCities(
      cityAtom.map((each) => ({ label: each.objectDsc, value: each.objectCd }))
    );
    if (!formIDsFetched) {
      fetchOneOfEachID();
    }
  }, [
    vehicleStylesAtom,
    jurisdictionsAtom,
    provincesAtom,
    vehiclesAtom,
    vehicleColoursAtom,
    cityAtom,
    impoundAtom,
    vehicleTypesAtom,
    formIDsFetched,
  ]);

  const handleClose = async () => {
    setShow(false);
    modalCloseFunc();
    setmodalCloseFunc(() => () => null);
    setModalBody("");
    setModalTitle("");
    setModalButtonOneText("");
    setModalButtonTwoText("");
  };

  const handleModalClose = async () => {
    setShow(false);
    setmodalCloseFunc(() => () => null);
    setModalBody("");
    setModalTitle("");
    setModalButtonOneText("");
    setModalButtonTwoText("");
  };

  const handleShow = (title, body, buttonOneText, buttonTwoText, func) => {
    setModalTitle(title);
    setModalBody(body);
    setModalButtonOneText(buttonOneText);
    setModalButtonTwoText(buttonTwoText);
    setmodalCloseFunc(() => func);
    setShow(true);
  };

  const generateYearOptions = () => {
    const currentYear = new Date().getFullYear();
    const startYear = 1900;
    const years = [];

    for (let year = startYear; year <= currentYear; year++) {
      years.push({ value: year, label: year.toString() });
    }

    return years;
  };

  const setNSCVI = (values) => {
    const nscNumber = values["nsc_no"];
    nscNumber === "" ? (values["is_nsc"] = false) : (values["is_nsc"] = true);
  };

  const onSubmit = async (values) => {
    setIsSubmitting(true);
    if (values["VI"]) {
      const element = document.getElementById("VI");
      const base64_png = await toPng(element);
      values["VI_form_png"] = base64_png;
    }
    if (values["TwentyFourHour"]) {
      const element = document.getElementById("TwentyFourHour");
      const base64_png = await toPng(element);
      values["TwentyFourHour_form_png"] = base64_png;
    }
    if (values["IRP"]) {
      const element = document.getElementById("IRP");
      const base64_png = await toPng(element);
      values["IRP_form_png"] = base64_png;
    }
    if (values["TwelveHour"]) {
      const element = document.getElementById("TwelveHour");
      const base64_png = await toPng(element);
      values["TwelveHour_form_png"] = base64_png;
    }
    if (values["date_of_impound"] && values["vehicle_impounded"] === "NO") {
      values["date_released"] = values["date_of_impound"];
    }
    // console.log('here are the values before api call')
    // console.log(values);
    // db.event
    //       .put(values)
    //       .then(() => {
    //         // setIsSubmitting(false);
    //         // navigate("/");
    //       })
    //       .catch((err) => {
    //         // console.error(err);
    //         // setIsSubmitting(false);
    //       });
    FormSubmissionApi.post(values)
      .then((resp) => {
        values["event_id"] = resp.data["event_id"];
        // console.log('here are the values')
        // console.log(values);
        db.event
          .put(values)
          .then(() => {
            setIsSubmitting(false);
            navigate("/");
          })
          .catch((err) => {
            console.error(err);
            setIsSubmitting(false);
          });
      })
      .catch((err) => {
        console.error(err);
        setIsSubmitting(false);
      });
  };

  const handleGoBackandSave = (values) => {
    // console.log('this is value before saveing impound even before')
    // console.log(values)
    // copy values to another variable
    // let valuesCopy = JSON.parse(JSON.stringify(values));
    let valuesCopy = { ...values };
    // console.log('this is value of valuesCopy before saveing impound even before')
    // console.log(valuesCopy)
    if (
      valuesCopy["date_of_impound"] &&
      valuesCopy["vehicle_impounded"] === "NO"
    ) {
      valuesCopy["date_released"] = valuesCopy["date_of_impound"];
    }
    const eventData = getEventDataToSave(valuesCopy);
    // console.log('this is value of event data before saving impound')
    // console.log(eventData)
    if (eventData["event_id"] === undefined) {
      // need a beter solution to this--DONE
      // eventData["event_id"] = 1;
      eventData["event_id"] = uuidv4();
    }
    // console.log('this is value before saveing impound')
    // console.log(eventData)

    db.event
      .put(eventData, eventData["event_id"])
      .then(() => {
        navigate("/");
      })
      .catch((err) => {
        console.error(err);
      });
  };

  const printForms = async (values) => {
    handleShow(
      "Print Form",
      "If you print this form you cannot go back and edit it, please confirm you wish to proceed.",
      "Close",
      "Print",
      () => handlePrintForms(values)
    );
  };

  const handleWithdraw = () => {
    navigate("/");
  };

  const handlePrintForms = async (values) => {
    window.print();
  };

  const handleSuccessfulPrint = async (values) => {
    nextPage(values);
  };

  // Step 0: data entry
  // Step 1: driver copy preview / print
  // Step 2: eCOS (12 & 24h only)
  // Step 3: Police details (24h only)
  // Step 4: Police copy preview / print
  const nextPage = (values) => {
    // Need to check if schema is valid before proceeding to next page
    // Once form has printed successfully, need to set values["form_printed_successfully"] to true and then proceed to next page, but after validating the schema for the same reason as below
    // If 24h and we are on step 2 and in this function, we need to set values["ecos_confirmed"] to true before proceeding to the next page but after validating the schema
    // Otherwise the schema will throw an error as a field on the next page is required if values["ecos_confirmed"] is true

    if (validationSchema.isValidSync(values)) {
      // Clear errors
      setFormHasErrors(false);
      setFormErrors([]);
      // Once we know the form schema so far is valid, we can alter values based on the step we are on
      if (currentStep === 1) {
        // By this point the user has confirmed the form has printed successfully
        values["form_printed_successfully"] = true;
      }
      if (
        currentStep === 2 &&
        (values["TwentyFourHour"] || values["TwelveHour"])
      ) {
        // By this point the user has certified the eCOS and confirmed the form has printed successfully
        values["ecos_confirmed"] = true;
      }
      if (
        currentStep === 3 &&
        values["TwentyFourHour"] &&
        values["prescribed_test_used"] === "NO"
      ) {
        // By this point the police details have been completed if applicable, we can navigate to the police copy
        values["police_details_complete"] = true;
      }

      // Page navigation
      if (values["TwentyFourHour"]) {
        if (currentStep === 2 && values["prescribed_test_used"] === "YES") {
          setCurrentStep(currentStep + 2);
        } else {
          setCurrentStep(currentStep + 1);
        }
      } else if (values["TwelveHour"]) {
        if (currentStep === 2) {
          setCurrentStep(currentStep + 2);
        } else {
          setCurrentStep(currentStep + 1);
        }
      } else {
        if (currentStep === 0) {
          setCurrentStep(currentStep + 1);
        } else {
          setCurrentStep(4);
        }
      }
    } else {
      // Schema not valid, display errors
      validationSchema.validate(values, { abortEarly: false }).catch((err) => {
        console.log("Validation Errors: ", err.errors);
        setFormHasErrors(true);
        setFormErrors(err.errors);
        // scroll to the top of the page
        window.scrollTo(0, 0);
      });
    }
  };

  const prevPage = () => {
    setCurrentStep(currentStep - 1);
  };

  const setFormNumbers = (e, setFieldValue, form) => {
    const formFieldNames = {
      TwelveHour: "twelve_hour_number",
      TwentyFourHour: "twenty_four_hour_number",
      IRP: "IRP_number",
      VI: "VI_number",
    };
    setFieldValue(
      formFieldNames[form],
      e.target.checked
        ? form === "VI" || form === "IRP"
          ? formNumberChecksum(formIDs[form])
          : formIDs[form]
        : ""
    );
  };

  const withdrawProhibition = () => {
    handleShow(
      "Confirm Withdraw Prohibition",
      "Are you sure you want to withdraw this prohibition.",
      "Withdraw",
      () => handleWithdraw()
    );
  };

  const renderSVGForm = (values, renderStage) => {
    const forms = {
      TwentyFourHour: values["TwentyFourHour"],
      TwelveHour: values["TwelveHour"],
      IRP: values["IRP"],
      VI: values["VI"],
    };
    const valuesCopy = { ...values };
    if (values["vehicle_impounded"] === "YES") {
      console.log(values["date_released"]);
      valuesCopy["date_released"] = null;
      valuesCopy["time_released"] = null;
      // break;
    }
    const componentsToRender = [];
    let components = [];
    for (const item in forms) {
      if (forms[item]) {
        for (const form in formsPNG[renderStage][item]) {
          if (form === "ILO" && values["vehicle_impounded"] === "NO") {
            break;
          }
          // if (form === "ILO" && values["vehicle_impounded"] === "YES") {
          //   values['date_released']=null
          //   values['time_released']=null
          //   break;
          // }

          if (form === "DETAILS" && !values["incident_details_extra_page"]) {
            break;
          }

          components.push(
            <SVGprint
              key={item + form}
              form={formsPNG[renderStage][item][form]["png"]}
              formAspect={formsPNG[renderStage][item][form]["aspectClass"]}
              formLayout={item}
              formType={form}
              values={valuesCopy}
            />
          );
        }
        componentsToRender.push(<div id={item}>{components}</div>);
        components = [];
      }
    }
    return componentsToRender;
  };

  const renderPage = (currentStep, values, setFieldValue) => {
    // console.log("FORM IDS: ", formIDs);
    // console.log(values);
    window.onafterprint = async () => {
      console.log("Done printing");
      setIsPrinted(true);
      const forms = {
        TwentyFourHour: "twenty_four_hour_number",
        TwelveHour: "twelve_hour_number",
        // IRP: "IRP_number",
        VI: "VI_number",
      };
      const idsToDelete = {};
      for (const form in forms) {
        console.log("Form: ", form);
        if (values[forms[form]]) {
          await db.formID.delete(
            forms[form] === "VI_number" || forms[form] === "IRP_number"
              ? values[forms[form]].toString().slice(0, -1)
              : values[forms[form]]
          );
          idsToDelete[forms[form]] = values[forms[form]];
        }
      }
      if (!values["TwentyFourHour"]) {
        // unlease the TwentyFourHour ID
        await db.formID
          .where("id")
          .equals(formIDs["TwentyFourHour"])
          .modify({ leased: 0 });
      }
      if (!values["TwelveHour"]) {
        // unlease the TwelveHour ID
        await db.formID
          .where("id")
          .equals(formIDs["TwelveHour"])
          .modify({ leased: 0 });
      }
      if (!values["IRP"]) {
        // unlease the IRP ID
        await db.formID
          .where("id")
          .equals(formIDs["IRP"])
          .modify({ leased: 0 });
      }
      if (!values["VI"]) {
        // unlease the VI ID
        await db.formID.where("id").equals(formIDs["VI"]).modify({ leased: 0 });
      }

      await FormIDApi.patch({
        forms: { ...idsToDelete },
        printed_timestamp: new Date(),
      });
      handleShow(
        "Print Form",
        "Did the form print correctly?",
        "No",
        "Yes",
        () => handleSuccessfulPrint(values)
      );
    };

    switch (currentStep) {
      case 0:
        return (
          <>
            <div className="row mt-2">
              <div className="col-sm-4 left checkboxs">
                <h4>Documents to Generate</h4>
                <Checkbox
                  name="IRP"
                  disabled={
                    true || values["TwentyFourHour"] || values["TwelveHour"]
                  }
                  onClick={(e) => setFormNumbers(e, setFieldValue, "IRP")}
                >
                  Immediate Roadside Prohibition
                </Checkbox>
                <Checkbox
                  name="VI"
                  onClick={(e) => setFormNumbers(e, setFieldValue, "VI")}
                >
                  Vehicle Impound
                </Checkbox>
                <Checkbox
                  name="TwentyFourHour"
                  disabled={values["IRP"] || values["TwelveHour"]}
                  onClick={(e) =>
                    setFormNumbers(e, setFieldValue, "TwentyFourHour")
                  }
                >
                  24-hour Driving Prohibition
                </Checkbox>
                <Checkbox
                  name="TwelveHour"
                  disabled={values["TwentyFourHour"] || values["IRP"]}
                  onClick={(e) =>
                    setFormNumbers(e, setFieldValue, "TwelveHour")
                  }
                >
                  12-hour Driving Prohibition
                </Checkbox>
              </div>
              <div className="col-sm-4 form-id-border">
                {values["IRP"] && <h5>IRP Number: {values["IRP_number"]}</h5>}
                {values["VI"] && <h5>VI Number: {values["VI_number"]}</h5>}
                {values["TwentyFourHour"] && (
                  <h5>24 Hour Number: {values["twenty_four_hour_number"]}</h5>
                )}
                {values["TwelveHour"] && (
                  <h5>12 Hour Number: {values["twelve_hour_number"]}</h5>
                )}
              </div>
              <div className="col-sm-4 time-of-completion center mt-5">
                <span>Estimated time to complete:</span>
                <h5>12 minutes</h5>
              </div>
            </div>
            <div className="common-fields">
              <DriverInfo jurisdictions={jurisdictions} provinces={provinces} />
              <VehicleInfo
                vehicleColours={vehicleColours}
                years={generateYearOptions()}
                provinces={provinces}
                jurisdictions={jurisdictions}
                vehicles={vehicles}
                vehicleStyles={vehicleStyles}
                vehicleTypes={vehicleTypes}
              />
              {(values["TwentyFourHour"] || values["VI"]) && (
                <RegisteredOwnerInfo provinces={provinces} />
              )}
            </div>
            {(values["TwentyFourHour"] || values["VI"]) && (
              <>
                <VehicleImpoundment impoundLotOperators={impoundLotOperators} />
                <Prohibition cities={cities} />
              </>
            )}
            {values["TwelveHour"] && !values["VI"] && (
              <>
                <Disposition impoundLotOperators={impoundLotOperators} />
                <Prohibition cities={cities} />
              </>
            )}
            {values["VI"] && (
              <>
                <VehicleImpoundmentIRP />
                <VehicleImpoundmentReason />
                {values["excessive_speed"] && <Excessive />}
                {values["unlicensed"] && (
                  <Unlicensed jurisdictions={jurisdictions} />
                )}
                <LinkageFactors />
                <IncidentDetails />
              </>
            )}
            {values["TwentyFourHour"] && (
              <>
                <ReasonableGrounds />
                <TestAdministered />
              </>
            )}
            <OfficerInfo />
          </>
        );
      case 1:
        if (values["VI"]) {
          setNSCVI(values);
        }
        return <div>{renderSVGForm(values, "stageOne")}</div>;
      case 2:
        return <ConfirmationStep />;
      case 3:
        return <PoliceDetails />;
      case 4:
        return renderSVGForm(values, "stageTwo");
      // Add more cases for each page
      default:
        return null;
    }
  };

  return (
    <div id="event-container" className="text-font">
      <Modal
        id="spinner-modal"
        show={isSubmitting}
        aria-labelledby="contained-modal-title-vcenter"
        centered
      >
        <Modal.Body>
          <div className="center">
            <h5>Submitting...</h5>
            <Spinner style={{ marginTop: "10px" }} animation="border" />
          </div>
        </Modal.Body>
      </Modal>
      <div id="button-container" className="m-4">
        <Button
          variant="primary"
          onClick={() => handleGoBackandSave(formValues)}
        >
          Save & Return to Main Menu
        </Button>
      </div>
      <div className="outline">
        <Formik
          innerRef={(formikActions) =>
            formikActions
              ? setFormValues(formikActions.values)
              : setFormValues({})
          }
          initialValues={InitialValues()}
          validationSchema={validationSchema}
        >
          {({ values, errors, setFieldValue }) => (
            <Form>
              {/* TODO: Fix race condition with modal on print */}
              <Modal
                id="popconfirm-modal"
                show={show}
                onHide={handleModalClose}
              >
                <Modal.Header closeButton>
                  <Modal.Title>{modalTitle}</Modal.Title>
                </Modal.Header>
                <Modal.Body>{modalBody}</Modal.Body>
                <Modal.Footer>
                  <Button variant="secondary" onClick={handleModalClose}>
                    {modalButtonOneText}
                  </Button>
                  <Button variant="primary" onClick={handleClose}>
                    {modalButtonTwoText}
                  </Button>
                </Modal.Footer>
              </Modal>
              <Alert
                variant="danger"
                show={formHasErrors}
                style={{ alignItems: "left" }}
              >
                <div className="left">
                  <Alert.Heading>
                    This form has errors preventing you from proceeding.
                  </Alert.Heading>
                  <p>Please address them before continuing.</p>
                  <hr />
                  <ul>
                    {formErrors.map((error) => (
                      <li>{error}</li>
                    ))}
                  </ul>
                </div>
              </Alert>
              {renderPage(currentStep, values, setFieldValue)}
              <div id="button-container" className="flex">
                {((currentStep > 0 && !isPrinted) ||
                  values["prescribed_device"] === "YES") && (
                  <div className="left">
                    <Button type="button" onClick={() => prevPage()}>
                      Previous
                    </Button>
                  </div>
                )}
                {currentStep === 3 && values["prescribed_device"] === "NO" && (
                  <div className="left">
                    <Button type="button" onClick={() => withdrawProhibition()}>
                      Withdraw Prohibition
                    </Button>
                  </div>
                )}
                <div className="right">
                  {currentStep < 4 ? (
                    currentStep === 1 ? (
                      <Button type="button" onClick={() => printForms(values)}>
                        Print
                      </Button>
                    ) : (
                      <Button type="button" onClick={() => nextPage(values)}>
                        Next
                      </Button>
                    )
                  ) : (
                    <Button
                      variant="primary"
                      onClick={() => {
                        console.log(errors);
                        onSubmit(values);
                      }}
                      disabled={isSubmitting}
                    >
                      Submit
                    </Button>
                  )}
                </div>
              </div>
            </Form>
          )}
        </Formik>
      </div>
    </div>
  );
};
