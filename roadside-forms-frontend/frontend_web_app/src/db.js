import Dexie from "dexie";

export const db = new Dexie("digitalForms");
//if you need to change any of these definitions add a new version below instead of changing the current one. If there is a change that
//requires a migration you need to add a .upgrade(() => {}) to the end of the version to handle how the data is migrated.
db.version(3).stores({
  user: "user_guid, business_guid, username, agency, badge_number, last_name, first_name, display_name, login",
  userRoles:
    "[user_guid+role_name], user_guid, role_name, submitted_dt, approved_dt",
  vehicles: "id, mk, search, md",
  vehicleStyles: "code, name",
  vehicleColours: "code, display_name, colour_class",
  provinces: "id, objectCd, objectDsc",
  jurisdictions: "id, objectCd, objectDsc",
  impoundLotOperators: "id, name, lot_address, city, phone, name_print",
  countries: "id, objectCd, objectDsc",
  cities: "id, objectCd, objectDsc",
  agencies: "id, vjur, agency_name",
  event:
    "event_id++,[driver_licence_no+date_of_driving], icbc_sent_status, driver_licence_no, driver_jurisdiction, driver_last_name, driver_given_name, driver_dob, driver_address, driver_city, driver_prov, driver_postal, driver_phone, vehicle_jurisdiction, vehicle_plate_no, vehicle_registration_no, vehicle_year, vehicle_mk_md, vehicle_style, vehicle_colour, vehicle_vin_no, nsc_prov_state, nsc_no, owned_by_corp, corporation_name, regist_owner_last_name, regist_owner_first_name, regist_owner_address, regist_owner_dob, regist_owner_city, regist_owner_prov, regist_owner_postal, regist_owner_phone, printed, sync_status, created_dt, updated_dt, created_by, updated_by , vehicle_impounded, reason_for_not_impounding, vehicle_released_to, date_released, time_released, location_of_keys, impound_lot_operator, type_of_prohibition, intersection_or_address_of_offence, offence_city, agency_file_no, date_of_driving, time_of_driving, reasonable_ground, reasonable_ground_other, prescribed_test_used, date_of_test, time_of_test, reason_for_not_using_prescribed_test, test_used_alcohol, asd_expiry_date, result_alcohol, bac_result_mg, test_used_drugs, test_result_drugs, IRP, VI, TwentyFourHour, TwelveHour, requested_prescribed_test, requested_test_used, time_of_requested_test, requested_ASD_expiry_date, requested_alcohol_test_result, requested_BAC_result, requested_approved_instrument_used, gender, driver_licence_expiry, driver_licence_class, unlicenced_prohibition_number, belief_driver_bc_resident, out_of_province_dl, out_of_province_dl_number, date_of_impound, irp_impound, irp_impound_duration, IRP_number, VI_number, excessive_speed, prohibited, suspended, street_racing, stunt_driving, motorcycle_seating, motorcycle_restrictions, unlicensed, linkage_location_of_keys, linkage_location_of_keys_explanation, linkage_driver_principal, linkage_owner_in_vehicle, linkage_owner_aware_possesion, linkage_vehicle_transfer_notice, linkage_other, speed_limit, vehicle_speed, speed_estimation_technique, speed_confirmation_technique",
  formID: "id, form_type, user_guid, leased, [form_type+leased]",
  vehicleTypes: "type_cd, description",
});

db.version(4).stores({
  nscPuj: "id, objectCd, objectDsc",
  jurisdictionCountry: "id, objectCd, objectDsc",
});

const initDB = async () => {
  await db.open();
};

initDB()
  .then(() => {
    console.log("Idexed DB is open");
  })
  .catch(function (e) {
    console.error("Open failed: " + e);
  });
