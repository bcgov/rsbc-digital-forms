import moment from "moment-timezone"

import * as staticData from "../atoms/staticData"
import twentyFourHourDriverform from '../assets/MV2634_102018_driver.png';
import appealsForm from '../assets/MV2721_201502_appeal.png'
import twentyFourHourOfficerform from '../assets/MV2634_102018_police.png';

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

export const formsPNG = {"TwentyFourHour":{"driver":{"png":twentyFourHourDriverform, "aspectClass":'--landscape'},"APPEAL": {"png":appealsForm, "aspectClass":"--portrait"}, "ILO":{"png":twentyFourHourDriverform, "aspectClass":"--landscape"}}}

const fieldsToSplit = {"VEHICLE_MAKE":0, "VEHICLE_MODEL":1}
const dateFieldSplit = ["date-of-driving"]


export const printFormatHelper = (values, data, key) => {
    let val = values[data["field_name"]]
    // if the value needs to be split into to fields
    if(key in fieldsToSplit){
        const splitData = typeof values[data["field_name"]] === 'object' ? values[data["field_name"]]["value"].split(data["delimeter"]) : values[data["field_name"]].split(data["delimeter"])
        // if the value only needs the first part split off then rejoin the rest
        val = typeof fieldsToSplit[key] === "number" ?  splitData[fieldsToSplit[key]] : splitData.splice(1).join(data["delimeter"])
        return val
    } 
    //if the field on the form is expecting more than one value join them together
    if(Array.isArray(data["field_name"])){
        val = ""
        for(var field in data["field_name"]){
            val += typeof values[data["field_name"][field]] === 'object' ? values[data["field_name"][field]]["value"] : values[data["field_name"][field]]
            val += " "
        }
        return val
    }
    //if the value is a date
    if (Object.prototype.toString.call(values[data["field_name"]]) === "[object Date]"){
        if (dateFieldSplit.includes(data["field_name"])){
            val = moment(values[data["field_name"]]).format(data["date_val"]); 
        }else{
            val = moment(values[data["field_name"]]).format('YYYYMMDD'); 
        }
        return val
    }
    //if the value is a list join them into a single string
    if(Array.isArray(values[data["field_name"]])){
        val = values[data["field_name"]].join("")
        return val
    }
    //temp: if the value is an object then take its value
    if (typeof values[data["field_name"]] === 'object'){
        val = values[data["field_name"]]["value"]
        return val
    }
    return val
}


export const printCheckHelper = (values, data, key) => {
    //if value is boolean just return it
    if (typeof values[data["field_name"]] === "boolean"){
        return values[data["field_name"]]
    }
    //if value is a string check to see that it matches what is expected
    if (values[data["field_name"]] === data["field_val"]){
        return true
    }
    return false
}

  