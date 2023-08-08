import * as staticData from "../atoms/staticData"

const eventValueKeys = ["event_id", "icbc_sent_status", "drivers_licence_no", "drivers_licence_jurisdiction",
 "driver_last_name", "driver_given_name", "driver_dob", "driver_address", "driver_city", "driver_prov_state",
 "driver_postal", "driver_phone", "vehicle_jurisdiction", "vehicle_plate_no", "vehicle_registration_no",
 "vehicle_year", "vehicle_mk_md", "vehicle_style", "vehicle_colour", "vehicle_vin_no", "nsc_prov_state", "nsc_no",
 "owned_by_corp", "corporation_name", "regist_owner_last_name", "regist_owner_first_name", "regist_owner_address",
 "regist_owner_dob", "regist_owner_city", "regist_owner_prov_state", "regist_owner_postal", "regist_owner_phone",
 "printed", "sync_status", "created_dt", "updated_dt", "created_by", "updated_by", 'vehicle_impounded', 'reason_for_not_impounding',
 'vehicle_released_to', 'date_released', 'time_released', 'location_of_keys', 'impound_lot_operator', 'type_of_prohibition',
 'intersection_or_address_of_offence', 'offence_city', 'agency_file_no', 'date_of_driving', 'time_of_driving', 'reasonable_ground',
 'reasonable_ground_other', 'prescribed_test_used', 'date_of_test', 'time_of_test', 'reason_for_not_using_prescribed_test',
 'test_used_alcohol', 'asd_expiry_date', 'result_alcohol', 'bac_result_mg', 'test_used_drugs', 'test_result_drugs', 'IRP', 'VI', '24Hour', '12Hour']

export const staticResources = {
    "agencies": staticData.agencies,
    "cities": staticData.cities,
    "countries": staticData.countries,
    "impound_lot_operators": staticData.impoundLotOperators,
    "jurisdictions": staticData.jurisdictions,
    "permissions": staticData.permissions,
    "provinces": staticData.provinces,
    "vehicle_styles": staticData.vehicleStyles,
    "vehicle_colours": staticData.vehicleColours,
    "vehicles": staticData.vehicles

}
  
export const getEventDataToSave = (formValues) => {
    const eventValues = {}
    eventValueKeys.forEach((item) => eventValues[item] = typeof formValues[item] === 'object' ? formValues[item]["value"] : formValues[item])        
    return eventValues
}

export const getTwentyFourHourDataToSave = (formValues, event_id) => {
    const twentyFourHourFormValues = {}
    // twentyFourHourValueKeys.forEach((item) => twentyFourHourFormValues[item] = typeof formValues[item] === 'object' ? formValues[item]["value"] : formValues[item])        
    twentyFourHourFormValues["event_id"] = event_id
    return twentyFourHourFormValues
}

export const formTypes = (form) => {
    const forms = (form['IRP'] ? 'IRP,': " ") + (form['VI'] ? 'VI,': " ") + (form['24Hour'] ? '24Hour,': " ") + (form['12Hour'] ? '12Hour': " ");
    return (forms)   
}