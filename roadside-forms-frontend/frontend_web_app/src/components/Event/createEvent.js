import React, { useState, useEffect } from "react";
import { Formik, Form } from "formik";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import Spinner from "react-bootstrap/Spinner";
import { toPng } from "html-to-image";
import { useRecoilValue } from "recoil";
import {
  useBeforeUnload,
  useBlocker,
  useNavigate,
  useLocation,
} from "react-router-dom";
import { ToastContainer } from "react-toastify";
import { Alert } from "react-bootstrap";
import Warning from "@mui/icons-material/Warning";
import { ArrowBack, Error, Refresh } from "@mui/icons-material";
import { useKeycloak } from "@react-keycloak/web";

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
import { ConfirmationStep } from "./ConfirmationStep/confirmationStep";
import { PoliceDetails } from "../Forms/TwentyFourHourForm/policeDetails";
import {
  staticResources,
  formsPNG,
  formNumberChecksum,
  deleteIncompleteEvent,
  spoilForm,
} from "../../utils/helpers";
import { FormSubmissionApi } from "../../api/formSubmissionApi";
import { SVGprint } from "../Forms/Print/svgPrint";
import { db } from "../../db";
import "./createEvent.scss";
import "react-toastify/dist/ReactToastify.css";
import { FormIDApi } from "../../api/formIDApi";
import { userAtom } from "../../atoms/users";
import moment from "moment";
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
  const nscPujAtom = useRecoilValue(staticResources["nscPuj"]);
  const jurisdictionCountryAtom = useRecoilValue(
    staticResources["jurisdictionCountry"]
  );
  const userData = useRecoilValue(userAtom);
  const [formValues, setFormValues] = useState([]);
  const [formIDs, setFormIDs] = useState({
    VI: "",
    // IRP: "",
    TwentyFourHour: "",
    TwelveHour: "",
  });
  const [formIDsFetched, setFormIDsFetched] = useState(false);
  const [jurisdictions, setJurisdictions] = useState([]);
  const [jurisdictionCountry, setJurisdictionCountry] = useState([]);
  const [nscPuj, setNscPuj] = useState([]);
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
  const [modalButtonTwoClass, setModalButtonTwoClass] = useState("primary");
  const [isPrinted, setIsPrinted] = useState(false);
  const [modalCloseFunc, setmodalCloseFunc] = useState(() => () => null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isBlockerActive, setisBlockerActive] = useState(true);
  const [formHasErrors, setFormHasErrors] = useState(false);
  const [formErrors, setFormErrors] = useState([]);
  const [exitWindowModalOpen, setExitWindowModalOpen] = useState(false);
  const [eventCreationFailedModalOpen, setEventCreationFailedModalOpen] =
    useState(false);
  const [criticalErrorModalOpen, setCriticalErrorModelOpen] = useState(false);
  const [incompleteEvent, setIncompleteEvent] = useState(null);
  const [incompleteEventID, setIncompleteEventID] = useState(null);

  const navigate = useNavigate();
  const { keycloak } = useKeycloak();

  // Blocker
  const blocker = useBlocker(({ currentLocation, nextLocation }) => {
    return (
      currentLocation.pathname !== nextLocation.pathname &&
      currentLocation.pathname === "/createEvent" &&
      isBlockerActive
    );
  });

  const { state } = useLocation();

  useBeforeUnload((event) => {
    event.preventDefault();
  });

  useEffect(() => {
    if (blocker.state === "blocked") {
      setExitWindowModalOpen(true);
    }
  }, [blocker.state]);

  useEffect(() => {
    const getIncompleteEvent = async () => {
      try {
        await db.incompleteEvent
          .where("inc_event_id")
          .equals(state?.incEventId)
          .first()
          .then((value) => {
            setIncompleteEvent(value);
            setCurrentStep(value["step"]);
            setIsPrinted(true);
            return;
          });
        setIncompleteEventID(state?.incEventId);
      } catch (error) {
        console.log(error);
      }
    };
    if (state) {
      getIncompleteEvent();
    } else {
      console.log("No incomplete event.");
    }
  }, [setIncompleteEvent, setCurrentStep, state]);

  useEffect(() => {
    const fetchOneOfEachID = async () => {
      const VINum = await db.formID
        .where("[form_type+leased]")
        .anyOf([["VI", 0]])
        .first();
      // const IRPNum = await db.formID
      //   .where("[form_type+leased]")
      //   .anyOf([["IRP", 0]])
      //   .first();
      const twentyFourNum = await db.formID
        .where("[form_type+leased]")
        .anyOf([["24Hour", 0]])
        .first();
      const twelveNum = await db.formID
        .where("[form_type+leased]")
        .anyOf([["12Hour", 0]])
        .first();

      if (
        !VINum ||
        !twentyFourNum ||
        !twelveNum ||
        !VINum.id ||
        !twentyFourNum.id ||
        !twelveNum.id
      ) {
        // If we could not get IDs, show critical error modal
        setCriticalErrorModelOpen(true);
      } else {
        await setFormIDs({
          VI: VINum.id,
          // IRP: IRPNum.id,
          TwentyFourHour: twentyFourNum.id,
          TwelveHour: twelveNum.id,
        });

        // Go into indexedDB and mark all form IDs we are leasing for this form as "leased"
        await db.formID.where("id").equals(VINum.id).modify({ leased: 1 });
        // await db.formID.where("id").equals(IRPNum.id).modify({ leased: 1 });
        await db.formID
          .where("id")
          .equals(twentyFourNum.id)
          .modify({ leased: 1 });
        await db.formID.where("id").equals(twelveNum.id).modify({ leased: 1 });
        await setFormIDsFetched(true);
      }
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
    setJurisdictionCountry(
      jurisdictionCountryAtom.map((each) => ({
        label: each.objectDsc,
        value: each.objectCd,
      }))
    );
    setNscPuj(
      nscPujAtom.map((each) => ({
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
    if (!formIDsFetched && !state) {
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
    jurisdictionCountryAtom,
    nscPujAtom,
    formIDsFetched,
    state,
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

  const handleShow = (title, body, buttonOneText, buttonTwoText, func, buttonTwoClass) => {
    setModalTitle(title);
    setModalBody(body);
    setModalButtonOneText(buttonOneText);
    setModalButtonTwoText(buttonTwoText);
    setmodalCloseFunc(() => func);
    setModalButtonTwoClass(buttonTwoClass||"primary");
    setShow(true);
  };

  const generateYearOptions = () => {
    const currentYear = new Date().getFullYear() + 1;
    const startYear = 1900;
    const years = [];

    for (let year = startYear; year <= currentYear; year++) {
      years.push({ value: year, label: year.toString() });
    }

    return years.sort((a, b) => b.value - a.value);
  };

  const setNSCVI = (values) => {
    const nscNumber = values["nsc_no"];
    nscNumber === "" ? (values["is_nsc"] = false) : (values["is_nsc"] = true);
  };

  const onSubmit = async (values) => {
    try {
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
  
      await FormSubmissionApi.post(values)
        .then((resp) => {
          console.log("response: ", resp);
          if (resp.status === 201) {
            setIsSubmitting(false);
            setisBlockerActive(false);
            navigate("/");
            if (incompleteEventID) {
              deleteIncompleteEvent(incompleteEventID);
            }
          } else {
            // The form did not submit correctly. Cancel submit and display error message.
            setIsSubmitting(false);
            setEventCreationFailedModalOpen(true);
          }
        })
      
    } catch (error) {
      console.error("An error occurred submitting the event: ", error);
      setIsSubmitting(false);
      setEventCreationFailedModalOpen(true);
    }
  }
  const handleSpoilForm = async () => {
    await spoilForm(incompleteEventID);
    await setisBlockerActive(false);
    navigate("/");
  };

  const cancelForm = () => {
    handleShow(
      "Confirm Spoil Form",
      "Are you sure you want to spoil this form?",
      "Cancel",
      "Spoil",
      () => handleSpoilForm(),
      "danger"
    );
  };
  const fetchIDsToDelete = async (values) => {
    const forms = {
      TwentyFourHour: "twenty_four_hour_number",
      TwelveHour: "twelve_hour_number",
      // IRP: "IRP_number",
      VI: "VI_number",
    };
    const idsToDelete = {};
    for (const form in forms) {
      if (values[forms[form]]) {
        await db.formID.delete(
          forms[form] === "VI_number" || forms[form] === "IRP_number"
            ? values[forms[form]].toString().slice(0, -1)
            : values[forms[form]]
        );
        idsToDelete[forms[form]] = values[forms[form]];
      }
    }
    return idsToDelete;
  };

  const unleaseIDs = async (values) => {
    // unlease the TwentyFourHour ID
    await db.formID
      .where("id")
      .equals(formIDs["TwentyFourHour"])
      .modify({ leased: 0 });

    // unlease the TwelveHour ID
    await db.formID
      .where("id")
      .equals(formIDs["TwelveHour"])
      .modify({ leased: 0 });

    // unlease the IRP ID
    // await db.formID.where("id").equals(formIDs["IRP"]).modify({ leased: 0 });

    // unlease the VI ID
    await db.formID.where("id").equals(formIDs["VI"]).modify({ leased: 0 });
  };

  const renderNextButton = (values, errors) => {
    if (currentStep < 4) {
      // We are not on the submit step
      if (currentStep === 1) {
        // We are on the driver copy print preview page
        return (
          <Button type="button" onClick={() => printForms(values)}>
            Print
          </Button>
        );
      } else if (currentStep === 2 && values["document_served"] === "NO") {
        // Prompt user to exit form if the document was not served
        return (
          <Button type="button" onClick={() => navigate("/")}>
            Exit Form
          </Button>
        );
      } else {
        return (
          <Button type="button" onClick={() => nextPage(values)}>
            Next
          </Button>
        );
      }
    } else {
      return (
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
      );
    }
  };

  // Should we account for when the user presses the back button in their browser?
  // If not, can just call handleExitForm() and then programatically navigate to main menu after user confirms
  // If so, need to block navigation away from the page and prompt user to confirm they want to exit the form
  const handleExitForm = async (values) => {
    // We need to unlease the IDs used for this form
    await unleaseIDs(values);

    // Finally, unblock the user from changing routes.
    if (blocker.state === "blocked") {
      blocker.proceed();
    }
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
    await handleModalClose();
    if (!incompleteEventID) {
      try {
        await db.incompleteEvent
          .put({
            ...values,
            form_printed_successfully: true,
            created_by: userData.user_guid,
            step: values["TwentyFourHour"] || values["TwelveHour"] ? 2 : 4,
          })
          .then((val) => {
            setIncompleteEventID(val);
          });
      } catch (error) {
        console.log(error);
      }
    }
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
      // IRP: "IRP_number",
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
      // IRP: values["IRP"],
      VI: values["VI"],
    };
    const valuesCopy = { ...values };
    if (values["vehicle_impounded"] === "YES") {
      valuesCopy["date_released"] = null;
      valuesCopy["time_released"] = null;
      // break;
    }
    const componentsToRender = [];
    let components = [];
    for (const item in forms) {
      if (forms[item]) {
        for (const form in formsPNG[renderStage][item]) {
          if (
            form === "ILO" &&
            values["VI"] &&
            values["TwentyFourHour"] &&
            item === "TwentyFourHour"
          ) {
            break;
          }
          if (form === "ILO" && values["vehicle_impounded"] === "NO") {
            break;
          }
          // if (form === "ILO" && values["vehicle_impounded"] === "YES") {
          //   values['date_released']=null
          //   values['time_released']=null
          //   break;
          // }

          // We don't need an extra page if our incident details will fit on the first.
          if (form === "DETAILS" && values["incident_details"].length < 500) {
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
              impoundLotOperators={impoundAtom}
              renderStage={renderStage}
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
    window.onbeforeunload = async () => {
      await handleExitForm(values);
    };

    window.onafterprint = async () => {
      if (currentStep === 1) {
        try {
          setIsPrinted(true);
          const idsToDelete = await fetchIDsToDelete(values);
          await FormIDApi.patch({
            forms: { ...idsToDelete },
            printed_timestamp: new Date(),
          });
          await unleaseIDs(values);
          handleShow(
            "Print Form",
            "Did the form print correctly?",
            "No",
            "Yes",
            () => handleSuccessfulPrint(values)
          );
        } catch (e) {
          handleShow(
            "Error",
            "An error occurred while printing the form.",
            "Close",
            () => handleModalClose()
          );
        }
      }
    };

    if (values["VI"] && (values["TwelveHour"] || values["TwentyFourHour"])) {
      values["irp_impound"] = "";
      values["irp_impound_duration"] = "";
      values["IRP_number"] = "";
    }

    switch (currentStep) {
      case 0:
        return (
          <>
            <div className="row mt-2">
              <div className="col-sm-4 left checkboxs">
                <h3>Please select one or more forms:</h3>
                {/* <Checkbox
                  name="IRP"
                  disabled={
                    true || values["TwentyFourHour"] || values["TwelveHour"]
                  }
                  onClick={(e) => setFormNumbers(e, setFieldValue, "IRP")}
                >
                  Immediate Roadside Prohibition
                </Checkbox> */}
                <h5>
                  <Checkbox
                    name="VI"
                    onClick={(e) => setFormNumbers(e, setFieldValue, "VI")}
                  >
                    Vehicle Impound
                  </Checkbox>
                </h5>
                <h5>
                  <Checkbox
                    name="TwentyFourHour"
                    disabled={values["IRP"] || values["TwelveHour"]}
                    onClick={(e) =>
                      setFormNumbers(e, setFieldValue, "TwentyFourHour")
                    }
                  >
                    24-hour Driving Prohibition
                  </Checkbox>
                </h5>
                <h5>
                  <Checkbox
                    name="TwelveHour"
                    disabled={values["TwentyFourHour"] || values["IRP"]}
                    onClick={(e) =>
                      setFormNumbers(e, setFieldValue, "TwelveHour")
                    }
                  >
                    12-hour Driving Suspension
                  </Checkbox>
                </h5>
              </div>
              <div className="col-sm-4 form-id-border">
                {/* {values["IRP"] && <h5>IRP Number: {values["IRP_number"]}</h5>} */}
                {values["VI"] && <h5>VI Number: {values["VI_number"]}</h5>}
                {values["TwentyFourHour"] && (
                  <h5>24 Hour Number: {values["twenty_four_hour_number"]}</h5>
                )}
                {values["TwelveHour"] && (
                  <h5>12 Hour Number: {values["twelve_hour_number"]}</h5>
                )}
              </div>
              {/* {(values["IRP"] ||
                values["VI"] ||
                values["TwentyFourHour"] ||
                values["TwelveHour"]) && (
                <div className="col-sm-4 time-of-completion center mt-5">
                  <span>Estimated time to complete:</span>
                  <h5>12 minutes</h5>
                </div>
              )} */}
            </div>
            {(values["IRP"] ||
              values["VI"] ||
              values["TwentyFourHour"] ||
              values["TwelveHour"]) && (
              <div>
                <div className="common-fields">
                  <DriverInfo
                    jurisdictions={jurisdictions}
                    jurisdictionCountry={jurisdictionCountry}
                    provinces={provinces}
                  />
                  <VehicleInfo
                    vehicleColours={vehicleColours}
                    years={generateYearOptions()}
                    nscPuj={nscPuj}
                    jurisdictions={jurisdictions}
                    jurisdictionCountry={jurisdictionCountry}
                    vehicles={vehicles}
                    vehicleStyles={vehicleStyles}
                    vehicleTypes={vehicleTypes}
                  />
                  {(values["TwentyFourHour"] || values["VI"]) && (
                    <RegisteredOwnerInfo
                      jurisdictions={jurisdictions}
                      jurisdictionCountry={jurisdictionCountry}
                    />
                  )}
                </div>
                {(values["TwentyFourHour"] || values["VI"]) && (
                  <>
                    <VehicleImpoundment
                      impoundLotOperators={impoundLotOperators}
                      allILOs={impoundAtom}
                    />
                    <Prohibition cities={cities} />
                  </>
                )}
                {values["TwelveHour"] && !values["VI"] && (
                  <>
                    <Disposition
                      impoundLotOperators={impoundLotOperators}
                      allILOs={impoundAtom}
                    />
                    <Prohibition cities={cities} />
                  </>
                )}
                {values["VI"] && (
                  <>
                    {!values["TwelveHour"] && !values["TwentyFourHour"] && (
                      <VehicleImpoundmentIRP />
                    )}
                    <VehicleImpoundmentReason values={values} />
                    {values["excessive_speed"] && <Excessive />}
                    {values["unlicensed"] && (
                      <Unlicensed
                        jurisdictions={jurisdictions}
                        jurisdictionCountry={jurisdictionCountry}
                      />
                    )}
                    <LinkageFactors />
                  </>
                )}
                {values["TwentyFourHour"] && (
                  <>
                    <ReasonableGrounds />
                    <TestAdministered />
                  </>
                )}
                {values["VI"] && <IncidentDetails values={values} />}
                <OfficerInfo />
              </div>
            )}
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
        return <div style={{ minWidth: "1640px" }}>{renderSVGForm(values, "stageTwo")}</div>;
      // Add more cases for each page
      default:
        return null;
    }
  };

  const getFormNames = (values) => {
    const forms = [];
    if (values["VI"]) {
      forms.push("VI");
    }
    if (values["TwentyFourHour"]) {
      forms.push("24-hour");
    }
    if (values["TwelveHour"]) {
      forms.push("12-hour");
    }
    let formNames = forms.join(" and ");
    if (forms.length > 1) {
      formNames += " forms";
    } else {
      formNames += " form";
    }

    return formNames;
  };

  if (!incompleteEvent && state) {
    return <div>Loading...</div>;
  }
  return (
    <div id="event-container" className="text-font">
      <ToastContainer />
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
      {blocker && (
        <Modal show={exitWindowModalOpen} centred>
          <Modal.Header>
            <h3>Are you sure you want to leave this page?</h3>
          </Modal.Header>
          <Modal.Body>
            {isPrinted
              ? "Your form is not completed. You can continue it from the events in progress table on the dashboard."
              : "All progress will be lost."}
          </Modal.Body>
          <Modal.Footer>
            <Button
              variant="secondary"
              onClick={() => {
                if (blocker.state === "blocked") {
                  blocker.reset();
                }
                setExitWindowModalOpen(false);
              }}
            >
              Cancel
            </Button>
            <Button variant="danger" onClick={() => handleExitForm(formValues)}>
              <Warning />
              Proceed
            </Button>
          </Modal.Footer>
        </Modal>
      )}
      <div className="flex">
        <div id="button-container" className="m-4">
          <Button variant="primary" onClick={() => navigate("/")}>
            <ArrowBack />
            &nbsp; Return to Main Menu
          </Button>
        </div>

        {isPrinted && (
          <div id="button-container" className="m-4">
            <Button
              variant="danger"
              onClick={async () => {
                cancelForm();
              }}
            >
              <Warning />
              &nbsp;
              {"Spoil Form"}
            </Button>
          </div>
        )}
      </div>

      <div className="outline">
        <Formik
          innerRef={(formikActions) =>
            formikActions
              ? setFormValues(formikActions.values)
              : setFormValues({})
          }
          initialValues={incompleteEvent ? incompleteEvent : InitialValues()}
          validationSchema={validationSchema}
        >
          {({ values, errors, setFieldValue }) => (
            <Form>
              <Modal
                size={"md"}
                show={criticalErrorModalOpen}
                backdrop="static"
                centered
              >
                <Modal.Header
                  style={{
                    background: "#D8292F",
                    justifyContent: "flex-start",
                  }}
                >
                  <Error
                    style={{
                      color: "white",
                      marginRight: "10px",
                      marginBottom: "5px",
                    }}
                  />
                  <h3 style={{ color: "white" }}>Form Numbers Not Available</h3>
                </Modal.Header>
                <Modal.Body>
                  <p>
                    A fatal technical issue has occurred. One or more form
                    number types could be retrieved. Please try logging out and
                    logging back in again.
                  </p>
                </Modal.Body>
                <Modal.Footer>
                  <Button
                    variant="secondary"
                    onClick={async () => {
                      await setisBlockerActive(false);
                      navigate("/");
                    }}
                  >
                    Return to Dashboard
                  </Button>
                  <Button
                    variant="danger"
                    onClick={async () => {
                      await setisBlockerActive(false);
                      keycloak.logout();
                    }}
                  >
                    Log Out of Digital Forms
                  </Button>
                </Modal.Footer>
              </Modal>
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
                  <Button variant={modalButtonTwoClass} onClick={handleClose}>
                    {modalButtonTwoText}
                  </Button>
                </Modal.Footer>
              </Modal>
              <Modal
                show={eventCreationFailedModalOpen}
                backdrop="static"
                size="lg"
                centered
              >
                <Modal.Header
                  style={{
                    background: "#D8292F",
                    justifyContent: "flex-start",
                  }}
                >
                  <Error
                    style={{
                      color: "white",
                      marginRight: "10px",
                      marginBottom: "5px",
                    }}
                  />
                  <h3 style={{ color: "white" }}>Unable to Submit Form</h3>
                </Modal.Header>
                <Modal.Body>
                  <p>
                    <div>
                      The form could not be submitted or electronically
                      delivered to ICBC due to a fatal network error.
                    </div>
                    <div>
                      Options:
                      <ul>
                        <li>
                          Try moving this computer to an area with better
                          network reception; <i>or</i>
                        </li>
                        <li>
                          Abandon the Digital Forms process and re-serve the
                          document (including DRIVER and ILO copies) using a
                          handwritten paper form.
                        </li>
                      </ul>
                    </div>
                    <strong>
                      Important! ICBC is no longer accepting printed copies of
                      12-hour and 24-hour forms. The forms MUST be handwritten
                      to be submitted via the existing paper process.
                    </strong>
                  </p>
                </Modal.Body>
                <Modal.Footer>
                  <Button
                    variant="danger"
                    onClick={async () => {
                      await setisBlockerActive(false);
                      navigate("/");
                    }}
                  >
                    <Warning />
                    &nbsp; Abandon Document and Return to Dashboard
                  </Button>
                  <Button
                    variant="primary"
                    onClick={async () => {
                      await setEventCreationFailedModalOpen(false);
                      await onSubmit(values);
                    }}
                  >
                    <Refresh />
                    &nbsp; Retry Submission
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
                {(values["IRP"] ||
                  values["VI"] ||
                  values["TwentyFourHour"] ||
                  values["TwelveHour"]) &&
                  renderNextButton(values, errors)}
              </div>
            </Form>
          )}
        </Formik>
      </div>
    </div>
  );
};
