import * as staticData from "../atoms/staticData"

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

const fieldsToSplit = {"VEHICLE_MAKE":0,"VEHICLE_MODEL":1,}

export const printFormatHelper = (values, data, key) => {
    let val = "";
    if(key in fieldsToSplit){
        val = values[data["field_name"][fieldsToSplit[key]]]
        return val
    } 
    if(data["field_name"].isArray()){
        for(var field in data["field_name"]){
            val += values[field] + " "
        }
        return val
    }
    val = values[data["field_name"]]

    return val
}
  