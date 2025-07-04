import moment from "moment-timezone";

import * as staticData from "../atoms/staticData";

import { pstDate } from "./dateTime";
import { genderDropdown } from "./constants";
import twentyFourHourDriverform from "../assets/MV2634E_082023_driver.png";
import twentyFourHourILOform from "../assets/MV2634E_082023_ilo.png";
import twentyFourHourPoliceform from "../assets/MV2634E_082023_icbc.png";
import viDriverForm from "../assets/MV2721_20250630.png";
import viIncidentDetails from "../assets/MV2722_20250630_Incident_Details.png";
import appealsForm from "../assets/MV2721_20250630_appeal.png";
import viReportForm from "../assets/MV2722_20250630.png";
import twelveHourDriverForm from "../assets/MV2906E_082023_driver.png";
import twelveHourICBCForm from "../assets/MV2906E_082023_icbc.png";
import { db } from "../db";
import { FormIDApi } from "../api/formIDApi";

const eventValueKeys = [
  "event_id",
  "icbc_sent_status",
  "driver_licence_no",
  "drivers_licence_jurisdiction",
  "driver_last_name",
  "driver_given_name",
  "driver_dob",
  "driver_address",
  "driver_city",
  "driver_prov_state",
  "driver_postal",
  "driver_phone",
  "vehicle_jurisdiction",
  "vehicle_plate_no",
  "vehicle_registration_no",
  "vehicle_year",
  "vehicle_mk_md",
  "vehicle_style",
  "vehicle_colour",
  "vehicle_vin_no",
  "nsc_prov_state",
  "nsc_no",
  "owned_by_corp",
  "corporation_name",
  "regist_owner_last_name",
  "regist_owner_first_name",
  "regist_owner_address",
  "regist_owner_dob",
  "regist_owner_city",
  "regist_owner_prov_state",
  "regist_owner_postal",
  "regist_owner_phone",
  "printed",
  "sync_status",
  "created_dt",
  "updated_dt",
  "created_by",
  "updated_by",
  "vehicle_impounded",
  "reason_for_not_impounding",
  "vehicle_released_to",
  "date_released",
  "time_released",
  "location_of_keys",
  "impound_lot_operator",
  "type_of_prohibition",
  "intersection_or_address_of_offence",
  "offence_city",
  "agency_file_no",
  "date_of_driving",
  "time_of_driving",
  "reasonable_ground",
  "reasonable_ground_other",
  "prescribed_test_used",
  "date_of_test",
  "time_of_test",
  "reason_for_not_using_prescribed_test",
  "test_used_alcohol",
  "asd_expiry_date",
  "result_alcohol",
  "bac_result_mg",
  "test_used_drugs",
  "test_result_drugs",
  "IRP",
  "VI",
  "TwentyFourHour",
  "TwelveHour",
];

export const staticResources = {
  agencies: staticData.agencies,
  cities: staticData.cities,
  countries: staticData.countries,
  impound_lot_operators: staticData.impoundLotOperators,
  jurisdictions: staticData.jurisdictions,
  permissions: staticData.permissions,
  provinces: staticData.provinces,
  vehicle_styles: staticData.vehicleStyles,
  vehicle_types: staticData.vehicleTypes,
  vehicle_colours: staticData.vehicleColours,
  vehicles: staticData.vehicles,
  nscPuj: staticData.nscPuj,
  jurisdictionCountry: staticData.jurisdictionCountry,
};

export const getEventDataToSave = (formValues) => {
  const eventValues = {};
  eventValueKeys.forEach((item) => {
    if (formValues[item] === null || formValues[item] === "") {
      eventValues[item] = "";
    } else {
      eventValues[item] =
        typeof formValues[item] === "object"
          ? formValues[item]["value"].includes("_")
            ? formValues[item]["value"].split("_")[1]
            : formValues[item]["value"]
          : formValues[item];
    }
  });

  // eventValueKeys.forEach(
  //   (item) =>
  //     (eventValues[item] =
  //       typeof formValues[item] === "object"
  //         ? formValues[item]["value"]
  //         : formValues[item])
  // );
  return eventValues;
};

export const getTwentyFourHourDataToSave = (formValues, event_id) => {
  const twentyFourHourFormValues = {};
  // twentyFourHourValueKeys.forEach((item) => twentyFourHourFormValues[item] = typeof formValues[item] === 'object' ? formValues[item]["value"] : formValues[item])
  twentyFourHourFormValues["event_id"] = event_id;
  return twentyFourHourFormValues;
};

export const formTypes = (form) => {
  const formTypeList = [
    ...(form["IRP"] ? ["IRP"] : []),
    ...(form["VI"] ? ["VI"] : []),
    ...(form["TwentyFourHour"] ? ["24H"] : []),
    ...(form["TwelveHour"] ? ["12H"] : []),
  ];

  return formTypeList.join(", ");
};

export const formNumbers = (data) => {
  let formNums = [];
  if (data["VI_number"]) {
    formNums.push(data["VI_number"]);
  }
  if (data["IRP_number"]) {
    formNums.push(data["IRP_number"]);
  }
  if (data["twelve_hour_number"]) {
    formNums.push(data["twelve_hour_number"]);
  }
  if (data["twenty_four_hour_number"]) {
    formNums.push(data["twenty_four_hour_number"]);
  }
  return formNums.join(", ");
};

export const formsPNG = {
  stageOne: {
    TwentyFourHour: {
      DRIVER: { png: twentyFourHourDriverform, aspectClass: "--landscape" },
      ILO: { png: twentyFourHourILOform, aspectClass: "--landscape" },
    },
    TwelveHour: {
      DRIVER: { png: twelveHourDriverForm, aspectClass: "--landscape" },
    },
    VI: {
      DRIVER: { png: viDriverForm, aspectClass: "--portrait" },
      APPEAL: { png: appealsForm, aspectClass: "--portrait" },
      ILO: { png: viDriverForm, aspectClass: "--portrait" },
    },
  },
  stageTwo: {
    TwentyFourHour: {
      POLICE: { png: twentyFourHourPoliceform, aspectClass: "--landscape" },
    },
    TwelveHour: {
      POLICE: { png: twelveHourICBCForm, aspectClass: "--landscape" },
    },
    VI: {
      POLICE: { png: viDriverForm, aspectClass: "--portrait" },
      REPORT: { png: viReportForm, aspectClass: "--portrait" },
      DETAILS: { png: viIncidentDetails, aspectClass: "--portrait" },
    },
  },
};

const fieldsToSplit = { VEHICLE_MAKE: 0, VEHICLE_MODEL: 1 };
const dateFieldSplit = ["date_of_driving", "driver_licence_expiry"];

export const printFormatHelper = (values, data, key, impoundLotOperators) => {
  let val = values[data["field_name"]];

  // if the value needs to be split into to fields

  if (key in fieldsToSplit) {
    const splitData =
      typeof values[data["field_name"]] === "object"
        ? values[data["field_name"]]["value"].split(data["delimeter"])
        : values[data["field_name"]].split(data["delimeter"]);
    // if the value only needs the first part split off then rejoin the rest
    val =
      typeof fieldsToSplit[key] === "number"
        ? splitData[fieldsToSplit[key]]
        : splitData.splice(1).join(data["delimeter"]);
    return val;
  }

  //if the field on the form is expecting more than one value join them together
  if (Array.isArray(data["field_name"])) {
    val = "";
    data["field_name"].forEach((value, index) => {
      if (values[data["field_name"][index]]) {
        if (typeof values[data["field_name"][index]] === "object") {
          if (value === "offence_city") {
            val += values[data["field_name"][index]]["label"];
          } else if (value === "driver_prov_state") {
            if (values[data["field_name"][index]]["value"].includes("_")) {
              val += values[data["field_name"][index]]["value"].split("_")[1];
            } else {
              val += values[data["field_name"][index]]["value"];
            }
          } else {
            val += values[data["field_name"][index]]["value"];
          }
        } else {
          val += values[data["field_name"][index]];
        }
        if (data["field_name"].length > index + 1) {
          val += ", ";
        }
      }
    });

    // Add province to location of DL surrender
    if (key === "DL_SURRENDER_LOCATION") {
      val = val + ", BC";
    }

    // For registered owner, if owned by corp, display corp name instead of owner name
    if (key === "OWNER_NAME") {
      if (values["owned_by_corp"]) {
        val = values["corporation_name"];
      }
    }

    return val;
  }

  // If the value is a barcode
  if (data["barcode"]) {
    // Strip the prefix characters
    val = "*" + val.toString().slice(2) + "*";
  }

  //if the value is a date
  if (
    Object.prototype.toString.call(values[data["field_name"]]) ===
    "[object Date]"
  ) {
    if (data["date_val"]) {
      val = moment(values[data["field_name"]]).format(data["date_val"]);
    } else {
      val = moment(values[data["field_name"]]).format("YYYY-MM-DD");
    }
    return val;
  }
  //if the value is a list join them into a single string
  if (Array.isArray(values[data["field_name"]])) {
    val = values[data["field_name"]].join("");
    return val;
  }

  if (key === "DRIVER_DL_EXPIRY") {
    if (values["driver_licence_expiry"]) {
      val = moment(values["driver_licence_expiry"]).format("YYYY");
      return val;
    }
  }

  if (key === "REPORT_DRIVER_DL_EXPIRY") {
    if (values["out_of_province_dl_expiry"]) {
      val = moment(values["out_of_province_dl_expiry"]).format("YYYY");
      return val;
    }
  }

  //temp: if the value is an object then take its value
  if (
    values[data["field_name"]] &&
    typeof values[data["field_name"]] === "object"
  ) {
    if (key === "LOCATION_CITY") {
      val = val["label"];
    } else {
      val = values[data["field_name"]]["value"];
      String(val).includes("_")
        ? (val = values[data["field_name"]]["value"].split("_")[1])
        : (val = values[data["field_name"]]["value"]);
    }
    return val;
  }
  let released_val = "";
  if (values["TwelveHour"]) {
    released_val = "vehicle_location";
  } else if (values["TwentyFourHour"]) {
    released_val = "reason_for_not_impounding";
  }
  if (key === "NOT_IMPOUNDED_REASON") {
    switch (values[released_val]) {
      case "released":
        val = "RELEASED TO OTHER DRIVER";
        break;
      case "private":
        val = "PRIVATE TOW";
        break;
      case "roadside":
        val = "LEFT AT ROADSIDE";
        break;
      case "investigation":
        val = "SEIZED FOR INVESTIGATION";
        break;
      default:
        val = "";
    }
  }

  if (key === "RELEASE_LOCATION_VEHICLE") {
    if (
      values["VI"] ||
      (values["TwentyFourHour"] && values["vehicle_impounded"] === "YES")
    ) {
      val = "IMPOUNDED";
    } else {
      switch (values[released_val]) {
        case "released":
          val = "RELEASED TO OTHER DRIVER";
          break;
        case "private":
          val = "PRIVATE TOW";
          break;
        case "roadside":
          val = "LEFT AT ROADSIDE";
          break;
        case "investigation":
          val = "SEIZED FOR INVESTIGATION";
          break;
        default:
          val = "";
      }
    }
  }

  if (key === "RELEASE_LOCATION_KEYS") {
    if (
      values["VI"] ||
      (values["TwentyFourHour"] && values["vehicle_impounded"] === "YES")
    ) {
      val = values["location_of_keys"];
    } else {
      switch (values[released_val]) {
        case "released":
          val = "WITH OTHER DRIVER";
          break;
        case "private":
          val = values["location_of_keys"];
          break;
        case "roadside":
          val = values["location_of_keys"];
          break;
        default:
          val = "";
      }
    }
  }

  if (key === "RELEASE_PERSON") {
    if (
      values["VI"] ||
      (values["TwentyFourHour"] && values["vehicle_impounded"] === "YES")
    ) {
      val = "";
    } else {
      switch (values[released_val]) {
        case "released":
          val = values["vehicle_released_to"];
          break;
        case "private":
          val = values["ILO-name"];
          break;
        case "roadside":
          val = "";
          break;
        default:
          val = "";
      }
    }
  }

  if (key === "RELEASE_DATE") {
    if (values["VI"]) {
      // val = moment(values["date_of_impound"]).format("YYYY-MM-DD");
    }
  }

  if (values["incident_details"] && values["incident_details"].length > 0) {
    values["incident_details_explained_below"] = true;
  }

  // Split into two fields
  if (key === "REPORT_INCIDENT_DETAILS") {
    if (values["incident_details"] && values["incident_details"].length > 500) {
      val = values["incident_details"].substring(0, 500);
      // values["extra_page_flag"] = true;
      // console.log("extra page flag", values["extra_page_flag"]);
    }
  }

  if (key === "DETAILS_INCIDENT_DETAILS") {
    if (values["incident_details"] && values["incident_details"].length > 500) {
      val = values["incident_details"].substring(500);
      // values["extra_page_flag"] = true;
      // console.log("extra page flag", values["extra_page_flag"]);
    }
  }

  if (
    key === "IMPOUND_LOT_NAME" ||
    key === "IMPOUNDED_LOT" ||
    (key === "RELEASE_PERSON" &&
      values["TwelveHour"] &&
      !values["VI"] &&
      values["vehicle_location"] === "private")
  ) {
    const tmp = impoundLotOperators.filter(
      (x) => x["name"] === values["ILO-name"]
    )[0];
    if (tmp && tmp.name_print) {
      val = tmp.name_print;
    } else {
      val = values["ILO-name"];
    }
  }

  return val;
};

export const printCheckHelper = (values, data, key) => {
  //if value is boolean just return it
  if (typeof values[data["field_name"]] === "boolean") {
    if (data["field_val"] === "false") {
      return !values[data["field_name"]];
    }
    return values[data["field_name"]];
  }

  if (Array.isArray(data["field_val"])) {
    if (data["field_val"].includes(values[data["field_name"]])) {
      return true;
    }
  }
  //if value is a string check to see that it matches what is expected
  if (values[data["field_name"]] === data["field_val"]) {
    return true;
  }
  return false;
};

export const eventObjectFlatener = (data) => {
  const eventData = [];
  for (const item in data) {
    const event = data[item];
    const viForm = event["vi_form"];
    const twentyFourHourForm = event["twenty_four_hour_form"];
    const twelveHourForm = event["twelve_hour_form"];
    const irpForm = event["irp_form"];
    event["vehicle_colour"] = event["vehicle_colour"]
      .substring(1, event["vehicle_colour"].length - 1)
      .split(",");
    delete event["irp_form"];
    delete event["twelve_hour_form"];
    delete event["twenty_four_hour_form"];
    delete event["vi_form"];
    eventData.push({
      ...event,
      ...viForm,
      VI: !(JSON.stringify(viForm) === "{}"),
      ...twelveHourForm,
      TwelveHour: !(JSON.stringify(twelveHourForm) === "{}"),
      ...irpForm,
      IRP: !(JSON.stringify(irpForm) === "{}"),
      ...twentyFourHourForm,
      TwentyFourHour: !(JSON.stringify(twentyFourHourForm) === "{}"),
    });
  }
  return eventData;
};

export const eventDataFormatter = (
  data,
  user,
  provinces,
  vehicles,
  vehicleStyles,
  jurisdictions,
  cities,
  impoundLots,
  jurisdictionCountry,
  nscPuj
) => {
  const eventData = [];
  const date_fields = [
    "driver_licence_expiry",
    "date_of_driving",
    "date_of_impound",
    "driver_dob",
    "regist_owner_dob",
    "confirmation_of_service_date",
    "created_dt",
    "updated_dt",
    "date_released",
    "requested_ASD_expiry_date",
  ];
  for (const item in data) {
    const event = data[item];
    let driverJurisdiction = jurisdictions.filter(
      (x) => x["objectCd"] === event["driver_jurisdiction"]
    )[0];
    if (driverJurisdiction === undefined) {
      driverJurisdiction = jurisdictionCountry.filter(
        (x) => x["objectCd"] === event["driver_jurisdiction"]
      )[0];
    }
    event["drivers_licence_jurisdiction"] = {
      value: driverJurisdiction.objectCd,
      label: driverJurisdiction.objectDsc,
    };
    delete event["drivers_jurisdiction"];
    let driverProvState = jurisdictions.filter(
      (x) => x["objectCd"] === event["driver_prov"]
    )[0];
    if (driverProvState === undefined) {
      driverProvState = jurisdictionCountry.filter(
        (x) => x["objectCd"] === event["driver_prov"]
      )[0];
    }
    event["driver_prov_state"] = {
      value: driverProvState.objectCd,
      label: driverProvState.objectDsc,
    };
    delete event["driver_prov"];
    let vehicleJurisdiction = jurisdictions.filter(
      (x) => x["objectCd"] === event["vehicle_jurisdiction"]
    )[0];
    if (vehicleJurisdiction === undefined) {
      vehicleJurisdiction = jurisdictionCountry.filter(
        (x) => x["objectCd"] === event["vehicle_jurisdiction"]
      )[0];
    }
    event["vehicle_jurisdiction"] = {
      value: vehicleJurisdiction.objectCd,
      label: vehicleJurisdiction.objectDsc,
    };
    if (event["out_of_province_dl_jurisdiction"]) {
      const outOfProvinceDlJurisdiction = jurisdictions.filter(
        (x) => x["objectCd"] === event["out_of_province_dl_jurisdiction"]
      )[0];

      event["out_of_province_dl_jurisdiction"] = {
        value: outOfProvinceDlJurisdiction.objectCd,
        label: outOfProvinceDlJurisdiction.objectDsc,
      };
    }
    if (event["nsc_prov_state"]) {
      const nscProvState = nscPuj.filter(
        (x) => x["objectCd"] === event["nsc_prov_state"]
      )[0];
      event["nsc_prov_state"] = {
        value: nscProvState.objectCd,
        label: nscProvState.objectDsc,
      };
    }

    if (!event["TwelveHour"] || (event["TwelveHour"] && event["VI"])) {
      let registOwnerProvState = jurisdictions.filter(
        (x) => x["objectCd"] === event["regist_owner_prov"]
      )[0];
      if (registOwnerProvState === undefined) {
        registOwnerProvState = jurisdictionCountry.filter(
          (x) => x["objectCd"] === event["regist_owner_prov"]
        )[0];
      }
      event["regist_owner_prov_state"] = {
        value: registOwnerProvState.objectCd,
        label: registOwnerProvState.objectDsc,
      };
    }
    delete event["regist_owner_prov"];
    const offenceCity = cities.filter(
      (x) => x["objectCd"] === event["offence_city"]
    )[0];
    event["offence_city"] = {
      value: offenceCity.objectCd,
      label: offenceCity.objectDsc,
    };
    const mk_md_split = event["vehicle_mk_md"].split("-");
    const vehicle = vehicles.filter(
      (x) => x["mk"] === mk_md_split[0] && x["md"] === mk_md_split[1]
    )[0];
    event["vehicle_mk_md"] = {
      value: vehicle?.mk + "-" + vehicle?.md,
      label: vehicle?.search,
    };

    event["officer-lastname"] = user.last_name;
    event["officer-prime-id"] = user.badge_number;
    event["officer-agency"] = user.agency;

    if (event["VI"]) {
      event["nsc_no"] === ""
        ? (event["is_nsc"] = false)
        : (event["is_nsc"] = true);

      const gender = genderDropdown.filter(
        (x) => x["value"] === event["gender"]
      )[0];
      event["gender"] = {
        value: gender?.value,
        label: gender?.label,
      };
    }

    const vehicleStyl = vehicleStyles.filter(
      (x) => x["code"] === event["vehicle_style"]
    )[0];
    event["vehicle_style"] = {
      value: vehicleStyl.code,
      label: vehicleStyl.name,
    };
    if (event["impound_lot_operator"]) {
      const impound = impoundLots.filter(
        (x) => x["id"] === event["impound_lot_operator"]
      )[0];
      event["ILO-options"] = {
        label:
          impound.name +
          ", " +
          impound.lot_address +
          ", " +
          impound.city +
          ", " +
          impound.phone,
        value: impound.id,
      };
      event["ILO-name"] = impound.name;
      event["ILO-address"] = impound.lot_address;
      event["ILO-city"] = impound.city;
      event["ILO-phone"] = impound.phone;
    }
    for (const field of date_fields) {
      if (event[field]) {
        event[field] = pstDate(event[field]);
      } else {
        event[field] = "";
      }
    }
    eventData.push(event);
  }
  return eventData;
};

export const formNumberChecksum = (formNumber) => {
  const timesTwo = (num) => {
    let newNum = num * 2;
    if (newNum > 9) {
      newNum = 1;
    }
    return newNum;
  };
  let [calc1, calc2, calc3, calc4, calc5, calc6, calc7, calc8] = formNumber
    .toString()
    .split("")
    .map(Number);

  calc4 = timesTwo(calc4);
  calc6 = timesTwo(calc6);
  calc8 = timesTwo(calc8);

  const digit = (calc3 + calc4 + calc5 + calc6 + calc7 + calc8) % 10;

  return +("" + formNumber + digit);
};

export const deleteIncompleteEvent = async (incEventID) => {
  try {
    db.incompleteEvent.where("inc_event_id").equals(incEventID).delete();
  } catch (error) {
    console.log(error);
  }
  return;
};

export const spoilForm = async (incEventID) => {
  await db.incompleteEvent
    .where("inc_event_id")
    .equals(incEventID)
    .first()
    .then((value) => {
      const idsToDelete = {};
      const forms = {
        TwentyFourHour: "twenty_four_hour_number",
        TwelveHour: "twelve_hour_number",
        VI: "VI_number",
      };
      for (const form in forms) {
        if (value[forms[form]]) {
          idsToDelete[forms[form]] = value[forms[form]];
        }
      }
      FormIDApi.patch({
        forms: { ...idsToDelete },
        spoiled_timestamp: new Date(),
      }).then(() => deleteIncompleteEvent(incEventID));
    });
};
