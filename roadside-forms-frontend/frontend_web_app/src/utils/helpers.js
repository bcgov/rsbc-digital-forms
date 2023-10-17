import moment from "moment-timezone";

import * as staticData from "../atoms/staticData";

import { pstDate } from "./dateTime";
import twentyFourHourDriverform from "../assets/MV2634E_101223_driver.png";
import twentyFourHourILOform from "../assets/MV2634E_101223_ilo.png";
import twentyFourHourPoliceform from "../assets/MV2634E_101223_police.png";
import viDriverForm from "../assets/MV2721_201502.png";
import appealsForm from "../assets/MV2721_201502_appeal.png";
import viReportForm from "../assets/MV2722_201502.png";
import twelveHourDriverForm from "../assets/TwelveHourDriverCopy.png";
import twelveHourICBCForm from "../assets/TwelveHourICBCCopy.png";

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
  vehicle_colours: staticData.vehicleColours,
  vehicles: staticData.vehicles,
};

export const getEventDataToSave = (formValues) => {
  const eventValues = {};
  eventValueKeys.forEach(
    (item) =>
      (eventValues[item] =
        typeof formValues[item] === "object"
          ? formValues[item]["value"]
          : formValues[item])
  );
  return eventValues;
};

export const getTwentyFourHourDataToSave = (formValues, event_id) => {
  const twentyFourHourFormValues = {};
  // twentyFourHourValueKeys.forEach((item) => twentyFourHourFormValues[item] = typeof formValues[item] === 'object' ? formValues[item]["value"] : formValues[item])
  twentyFourHourFormValues["event_id"] = event_id;
  return twentyFourHourFormValues;
};

export const formTypes = (form) => {
  const forms =
    (form["IRP"] ? "IRP," : " ") +
    (form["VI"] ? "VI," : " ") +
    (form["TwentyFourHour"] ? "TwentyFourHour," : " ") +
    (form["TwelveHour"] ? "TwelveHour" : " ");
  return forms;
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
      DRIVER: { png: twentyFourHourPoliceform, aspectClass: "--landscape" },
    },
    TwelveHour: {
      POLICE: { png: twelveHourICBCForm, aspectClass: "--landscape" },
    },
    VI: {
      POLICE: { png: viDriverForm, aspectClass: "--portrait" },
      REPORT: { png: viReportForm, aspectClass: "--portrait" },
    },
  },
};

const fieldsToSplit = { VEHICLE_MAKE: 0, VEHICLE_MODEL: 1 };
const dateFieldSplit = ["date_of_driving", "driver_licence_expiry"];

export const printFormatHelper = (values, data, key) => {
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
      val +=
        typeof values[data["field_name"][index]] === "object"
          ? values[data["field_name"][index]]["value"]
          : values[data["field_name"][index]];
      if (data["field_name"].length > index + 1) {
        val += ", ";
      }
    });
    return val;
  }
  //if the value is a date
  if (
    Object.prototype.toString.call(values[data["field_name"]]) ===
    "[object Date]"
  ) {
    if (dateFieldSplit.includes(data["field_name"])) {
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
  //temp: if the value is an object then take its value
  if (typeof values[data["field_name"]] === "object") {
    val = values[data["field_name"]]["value"];
    return val;
  }

  if (key === "RELEASE_LOCATION_VEHICLE") {
    if (values["VI"]) {
      val = values["ILO-name"];
    } else {
      switch (values["vehicle_location"]) {
        case "released":
          val = "RELEASED TO OTHER DRIVER";
          break;
        case "private":
          val = "PRIVATE TOW";
          break;
        case "roadside":
          val = "LEFT AT ROADSIDE";
          break;
        default:
          val = "";
      }
    }
  }

  if (key === "RELEASE_LOCATION_KEYS") {
    if (values["VI"]) {
      val = values["location_of_keys"];
    } else {
      switch (values["vehicle_location"]) {
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
    if (values["VI"]) {
      val = values["ILO-name"];
    } else {
      switch (values["vehicle_location"]) {
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
      val = moment(values["date_of_impound"]).format("YYYY-MM-DD");
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
  provinces,
  vehicles,
  vehicleStyles,
  jurisdictions,
  cities,
  impoundLots
) => {
  const eventData = [];
  const date_fields = [
    "driver_licence_expiry",
    "date_of_driving",
    "date_of_impound",
    "driver_dob",
    "regist_owner_dob",
  ];
  for (const item in data) {
    const event = data[item];
    const driverJurisdiction = jurisdictions.filter(
      (x) => x["objectCd"] === event["driver_jurisdiction"]
    )[0];
    event["drivers_licence_jurisdiction"] = {
      value: driverJurisdiction.objectCd,
      label: driverJurisdiction.objectDsc,
    };
    delete event["drivers_jurisdiction"];
    const driverProvState = provinces.filter(
      (x) => x["objectCd"] === event["driver_prov"]
    )[0];
    event["driver_prov_state"] = {
      value: driverProvState.objectCd,
      label: driverProvState.objectDsc,
    };
    delete event["driver_prov"];
    const vehicleJurisdiction = jurisdictions.filter(
      (x) => x["objectCd"] === event["vehicle_jurisdiction"]
    )[0];
    event["vehicle_jurisdiction"] = {
      value: vehicleJurisdiction.objectCd,
      label: vehicleJurisdiction.objectDsc,
    };
    if (event["nsc_prov_state"]) {
      const nscProvState = provinces.filter(
        (x) => x["objectCd"] === event["nsc_prov_state"]
      )[0];
      event["nsc_prov_state"] = {
        value: nscProvState.objectCd,
        label: nscProvState.objectDsc,
      };
    }
    const registOwnerProvState = provinces.filter(
      (x) => x["objectCd"] === event["regist_owner_prov"]
    )[0];
    event["regist_owner_prov_state"] = {
      value: registOwnerProvState.objectCd,
      label: registOwnerProvState.objectDsc,
    };
    delete event["regist_owner_prov"];
    const offenceCity = cities.filter(
      (x) => x["objectCd"] === event["offence_city"]
    )[0];
    event["offence_city"] = {
      value: offenceCity.objectCd,
      label: offenceCity.objectDsc,
    };
    const vehicle = vehicles.filter(
      (x) => x["search"] === event["vehicle_mk_md"]
    )[0];
    event["vehicle_mk_md"] = {
      value: vehicle.search,
      label: vehicle.search,
    };
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
      for (const field of date_fields) {
        event[field] = pstDate(event[field]);
      }
      event["ILO-name"] = impound.name;
      event["ILO-address"] = impound.lot_address;
      event["ILO-city"] = impound.city;
      event["ILO-phone"] = impound.phone;
    }
    eventData.push(event);
  }
  return eventData;

};
