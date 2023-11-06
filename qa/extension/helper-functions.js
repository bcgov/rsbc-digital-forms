// Tweak this if it's taking too long to load drop-downs to populate
const secondsToWaitForDropdownsToAppear = 25;

// Helper to call all the sections to be filled
function FillAllSections() {
    FillDriverSection();
    FillVehicleSection();
    FillOwnerSection();
    FillDispositionOfVehicleSection();
    FillVehicleImpoundmentSection();
    FillProhibitionSection();
    FillImpoundmentForIrpSection();
    FillImpoundmentForDrivingBehavhiour();
    FillUnlicencedDriverSection();
    FillExcessiveSpeedSection();
    FillLinkageFactorsSection();
    FillIncidentDetailsSection();
    FillReasonableGroundsSection();
    FillTestAdministeredSection();
    //FillOfficerSection();
}

function FillDriverSection() {
    SetField('driver_licence_no', GenerateDL());
    SetField('driver_last_name', chance.last());
    SetField('driver_given_name', GenerateGivenNames());
    SetField('driver_dob', GenerateDateOfBirth());
    SetField('driver_address', GenerateStreetAddress());
    SetField('driver_phone', GeneratePhoneNumber());
    SetField('driver_city', GenerateCity())
    SetField('driver_postal', GeneratePostalCode());
    SetField('gender', RandomGender());
    SetField('driver_licence_expiry', GenerateDLExpiryDate());
    SetField('driver_licence_class', GenerateRandomDlClass());
}

function FillVehicleSection(){
    SetField('vehicle_plate_no', GenerateLicencePlate());
    SetField('vehicle_registration_no', GenerateRegistrationNumber());
    SetField('vehicle_vin_no', GenerateVIN());
    SetField('nsc_no', GenerateNSC());

    //SetMultiSelect('vehicle_year-select', "1979");
    SelectRandomVehicleYear('vehicle_year-select');
    //SetMultiSelect('vehicle_mk_md-select', "CHEVROLET - CHEVETTE");
    SelectRandomVehicle('vehicle_mk_md-select');
    //SetMultiSelect('vehicle_style-select', "5-DOOR HATCH");
    SelectRandomVehicleStyle('vehicle_style-select');
    //SetMultiSelect('vehicle_colour', "YELLOW");
    SelectRandomVehicleColour('vehicle_colour');
}

function FillOwnerSection() {
    RandomlySelectRadioButton('owned_by_corp');
    var ownerLastName = chance.last();
    var ownerFirstNames = GenerateGivenNames();
    SetField('regist_owner_last_name', ownerLastName);
    SetField('corporation_name', GenerateCompanyName());
    SetField('regist_owner_first_name', ownerFirstNames);
    SetField('regist_owner_email', GenerateEmailAddress(ownerFirstNames));
    SetField('regist_owner_address', GenerateStreetAddress());
    SetField('regist_owner_phone', GeneratePhoneNumber());
    SetField('regist_owner_city', GenerateCity());
    SetCustomSelect('regist_owner_prov_state-select', "BRITISH COLUMBIA");
    SetSelect('regist_owner_postal', GeneratePostalCode());
}

function FillDispositionOfVehicleSection() {
    RandomlyChooseRadio('vehicle_location-released', 'vehicle_location-roadside', 'vehicle_location-private');
    SetField('vehicle_released_to', chance.name());
    SetField('date_released', GetCurrentDate());
    SetField('time_released', GetTimeFiveMinutesAgo());
    RandomlyChooseRadio('location_of_keys-WITH VEHICLE', 'location_of_keys-WITH DRIVER');
}

function FillVehicleImpoundmentSection() {
    // Radio button vehicle-impounded-YES
    SetField('date_of_impound', GetCurrentDate())
    //SelectRadioButton('vehicle-impounded-YES');
    RandomlyChooseRadio('location_of_keys-WITH VEHICLE', 'location_of_keys-WITH DRIVER');
    //SetMultiSelect('ILO-options-select', 'COLD COUNTRY TOWING (CRANBROOK), 3584 COLLINSON RD, CRANBROOK, 250-426-3680');
    SelectRandomIlo('ILO-options-select');
}

function FillProhibitionSection() {
    RandomlyChooseRadio('type_of_prohibition-alcohol','type_of_prohibition-drugs');
    SetField('intersection_or_address_of_offence', GenerateStreetAddress());
    SetCustomSelect('offence_city-select', GenerateCity())
    SetField('agency_file_no', "RSI" + GenerateRandomNumberLength(4));
    SetField('date_of_driving', GetCurrentDate());
    SetField('time_of_driving', GetTimeFiveMinutesAgo());
}

function FillImpoundmentForIrpSection() {
    RandomlyChooseRadio('irp_impound-YES', 'irp_impound-NO');
    RandomlyChooseRadio('irp_impound_duration-3DAY', 'irp_impound_duration-7DAY', 'irp_impound_duration-30DAY');
    SetField('IRP_number', "01-000001");
}

function FillImpoundmentForDrivingBehavhiour() {
    RandomlySelectRadioButton('excessive_speed');
    RandomlySelectRadioButton('prohibited');
    RandomlySelectRadioButton('suspended');
    RandomlySelectRadioButton('street_racing');
    RandomlySelectRadioButton('stunt_driving');
    RandomlySelectRadioButton('motorcycle_seating');
    RandomlySelectRadioButton('unlicensed');
}

function FillUnlicencedDriverSection() {
    SetField('unlicenced_prohibition_number', "02-000002");
    RandomlyChooseRadio('belief_driver_bc_resident-YES', 'belief_driver_bc_resident-NO');
    RandomlyChooseRadio('out_of_province_dl-YES', 'out_of_province_dl-NO');
    SetField('out_of_province_dl_number', GenerateDL())
}

function FillExcessiveSpeedSection() {
    var speedLimit = RandomlySpeedLimit();
    SetField('speed_limit', speedLimit);
    SetField('vehicle_speed', parseInt(speedLimit) + 45);
    RandomlyChooseRadio('speed_estimation_technique-VISUAL', 'speed_estimation_technique-PACING')
    RandomlyChooseRadio('speed_confirmation_technique-LASER', 'speed_confirmation_technique-RADAR', 'speed_confirmation_technique-OTHER');
}

function FillLinkageFactorsSection() {
    RandomlySelectRadioButton('linkage_location_of_keys');
    RandomlySelectRadioButton('linkage_driver_principal');
    RandomlySelectRadioButton('linkage_owner_in_vehicle');
    RandomlySelectRadioButton('linkage_owner_aware_possesion');
    RandomlySelectRadioButton('linkage_vehicle_transfer_notice');
    RandomlySelectRadioButton('linkage_other');
    SetField('linkage_location_of_keys_explanation', chance.sentence({ words: 4 }));
}

function FillIncidentDetailsSection() {
    RandomlySelectRadioButton('incident_details_extra_page');
    var numberOfSentences = Math.floor(Math.random() * 10) + 10;
    SetField('incident_details', chance.paragraph({ sentences: numberOfSentences }));
}

function FillReasonableGroundsSection() {
    RandomlySelectRadioButton('witnessed-by-officer');
    RandomlySelectRadioButton('admission-by-driver');
    RandomlySelectRadioButton('independent-witness');
    RandomlySelectRadioButton('video-surveillance');
    RandomlySelectRadioButton('reasonable_ground_other');
    SetField('reasonable_ground_other_reason', chance.sentence({ words: 12 }));
    RandomlyChooseRadio('prescribed_test_used-YES', 'prescribed_test_used-NO');
    SetField('reasonable_date_of_test', GetCurrentDate());
    SetField('reasonable_time_of_test', GetTimeOneMinuteAgo());
    RandomlyChooseRadio('reason_for_not_using_prescribed_test-refused', 'reason_for_not_using_prescribed_test-opinion')
}

function FillTestAdministeredSection() {
    // ALCOHOL
    RandomlyChooseRadio('resonable_test_used_alcohol-alco-sensor', 'resonable_test_used_alcohol-instrument', 'resonable_test_used_alcohol-PPCT');
    // When Alco-Sensor FST(ASD) is selected:
    SetField('reasonable_asd_expiry_date', GetDateInFiveFiveDays());
    RandomlyChooseRadio('reasonable_result_alcohol-51-59', 'reasonable_result_alcohol-WARN', 'reasonable_result_alcohol-FAIL');
    // When Approved Instrument option is selected:
    SetField('reasonable_bac_result_mg', Math.floor(Math.random() * 1000));
    SetField('resonable_approved_instrument_used', 'Instrument 1');
    // When Prescribed Pyhsical Coordination Test option is selected:
    RandomlySelectRadioButton('reasonable_can_drive_alcohol');

    // DRUGS
    RandomlyChooseRadio('reasonable_test_used_drugs-approved-drug',
        'reasonable_test_used_drugs-screening-equipment',
        'reasonable_test_used_drugs-PPCT'); 
    RandomlySelectRadioButton('THC');
    RandomlySelectRadioButton('Cocaine');
    RandomlySelectRadioButton('reasonable_can_drive_drug');
}

function FillOfficerSection() {
    SetField('officer-lastname', chance.last());
    SetField('officer-prime-id', "QA" + GenerateRandomNumberLength(4));
    SetField('officer-agency', GenerateCity() + " TEST");        
    SetField('date-of-test', GetCurrentDate());
    SetField('time-of-test', GetTimeFiveMinutesAgo());
    SelectRadioButton('test-used-alcohol-physical-cordination-test')
}

// Helper function to set the value of a text field 
function SetField(id, value) {
    const inputElement = document.getElementById(id);
    if (inputElement !== null) {
        inputElement.value = value;
        const event = new Event('input', {bubbles: true});
        inputElement.dispatchEvent(event);
    }
}

// Helper function to set the value of a drop-down field
function SetSelect(id, value) {
    const inputElement = document.getElementById(id);
    if (inputElement !== null) {
        inputElement.value = value;
        const enterKeyEvent = new KeyboardEvent('keydown', { key: 'Enter' });
        const event = new Event('input', {bubbles: true});
        inputElement.dispatchEvent(enterKeyEvent);
        inputElement.dispatchEvent(event);
    }
}

function SelectRandomVehicleStyle(id) {
    // Select a random vehicle style
    const vehicleStyle = vehicleStyles[Math.floor(Math.random() * vehicleStyles.length)];
    SetCustomSelect(id, vehicleStyle);
}

function SelectRandomVehicleColour(id) {
    // Select a random vehicle style
    const vehicleColour = vehicleColours[Math.floor(Math.random() * vehicleColours.length)];
    SetCustomSelect(id, vehicleColour);
}

function SelectRandomVehicle(id) {
    // Select a random vehicle style
    const vehicle = worstVehicles[Math.floor(Math.random() * worstVehicles.length)];
    SetCustomSelect(id, vehicle);
}

function SelectRandomVehicleYear(id){
    // Pick a year any time between the current year plus one and 100 years ago
    const currentYear = new Date().getFullYear();
    const min = currentYear - 100;
    const max = currentYear + 1;
    const randomYear = Math.floor(Math.random() * (max - min + 1)) + min;
    SetCustomSelect(id, randomYear.toString());
}

function SelectRandomIlo(id){
    // Select a random ILO
    const ilo = ilos[Math.floor(Math.random() * ilos.length)];
    SetCustomSelect(id, ilo);
}

// Helper function to randomly select a value from a populated custom drop-down)
function SetCustomSelect(id, value) {
    SetSelect(id, value);
    const inputElement = document.getElementById(id);
    if (inputElement !== null) {

        // Now we have to send a click event to confirm the selected value
        //el.parentElement.parentElement.parentElement.parentElement.getElementsByTagName('div')[7].click()
        
        // Wait 'secondsToWaitForDropdownsToAppear' seconds for the drop-down to populate. It can be slow.
        let count = 0;
        let interval = setInterval(function() {
            count++;
            if (count >= secondsToWaitForDropdownsToAppear) {
                clearInterval(interval);
            }
            else {
                var arrayOfDivs = inputElement.parentElement.parentElement.parentElement.parentElement.getElementsByTagName('div');
                var div = arrayOfDivs[arrayOfDivs.length - 1];
        
                if (div.innerText === value) {
                    clearInterval(interval);
                    // Now we can click the child element
                    div.click();
                }
            }
        }, 1000);
    }
}

// Helper function to generate an eight-digit drivers licence number
function GenerateDL() {
    const min = 0;  
    const max = 99999999;
    const eightDigitNumber = Math.floor(Math.random() * (max - min + 1)) + min;
    const eightDigitNumberPadded = eightDigitNumber.toString().padStart(8, '0');
    return eightDigitNumberPadded;
}

// Helper function to generate a surname
function GenerateLastName() {
    return chance.last();
}

// Helper function to generate a male or female given name
function GenerateGivenName(gender) {
    if (gender === 'male') {
        return chance.first({gender: 'male'});
    }
    else if (gender === 'female'){
        return chance.first({gender: 'female'});
    }
    // Could be male or female
    return chance.first();
}

// Helper function to generate a 1-5 given names. Male, female, or either.
function GenerateGivenNames(gender) {
    let names = [];
    let numNames = chance.integer({min: 1, max: 5});

    for (let i = 0; i < numNames; i++) {
        if (gender === 'male') {
            names.push(chance.first({gender: 'male'}));
        }
        else if (gender === 'female'){
            names.push(chance.first({gender: 'female'}));
        }
        else{
            names.push(chance.first());
        }
        
    }
    return names.join(" ");
}

// Helper function to convert a date to YYYYMMDD format
function dateToYMD(date) {
    var d = date.getDate();
    var m = date.getMonth() + 1; //Month from 0 to 11
    var y = date.getFullYear();
    return '' + y + (m<=9 ? '0' + m : m) + (d <= 9 ? '0' + d : d);
}

// Helper function to generate a random adult birth date
function GenerateDateOfBirth() {
    return dateToYMD(chance.birthday({type: "adult"}));
}

function GenerateDLExpiryDate() {
    const date = new Date();

    // pick a number from 1 to 4
    const randomNum = Math.floor(Math.random() * 4) + 1;

    date.setFullYear(date.getFullYear() + randomNum);
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const day = date.getDate().toString().padStart(2, '0');
    const formattedDate = `${year}${month}${day}`;
    return formattedDate;
}

function RandomGender() {
    const genders = ["Male", "Female", "Gender Diverse", "Unknown"];
    return genders[Math.floor(Math.random() * genders.length)];
}

function GenerateRandomDlClass()
{
    const dlClasses = ["1", "2", "3", "4", "5", "6", "7", "8", "5L", "5N", "5 + 7L", "5 + 8N", "4 + 7N"];
    return dlClasses[Math.floor(Math.random() * dlClasses.length)];
}

// Helper function to generate a street address at random
function GenerateStreetAddress() {
    return chance.address({ short_suffix: false });
}

// Helper function to generate a random Canadian postal code
function GeneratePostalCode() {
    return chance.postal();
}

// Helper function to generate a random BC area phone number
function GeneratePhoneNumber() {
    const areaCodes = [250, 604, 778 , 236 ]; // Also valid in BC: 672
    const randomAreaCode = areaCodes[Math.floor(Math.random() * areaCodes.length)];
    const phoneNumber = randomAreaCode + GenerateRandomNumberLength(7);
    return phoneNumber;
}

// Helper function to generate a number of random digits for a length
function GenerateRandomNumberLength(length) {
    const min = 0;
    const max = Math.pow(10, length) - 1;
    const randomNumber = Math.floor(Math.random() * (max - min + 1)) + min;
    const randomNumberPadded = randomNumber.toString().padStart(length, '0');
    return randomNumberPadded;
}

// Constant values for BC towns and cities
function GenerateCity() {
    
    const randomValue = city_values[Math.floor(Math.random() * city_values.length)];
    return randomValue;
}

// Helper function to get values from a drop-down field
function ValuesFromDropdownField(id) {
    let field = document.getElementById(id);
    if (field !== null) {

        let values = [];
        for (const option of field.options) {
            values.push(option.value);
        }
        return values;
    }
    return [];
}

// Helper function to generate a BC licence plate
function GenerateLicencePlate() {
    let characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    let numbers = '0123456789';
    let plate= '';

    for (let i = 0; i < 3; i++) {
        plate += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    plate += ' ';
    for (let i = 0; i < 3; i++) {
        plate += numbers.charAt(Math.floor(Math.random() * numbers.length));
    }
    return plate;
}

// Helper function to generate a vehicle registration number
function GenerateRegistrationNumber() {
    return "REG" + GenerateRandomNumberLength(10);
}

// Helper function to generate a vehicle identification number
function GenerateVIN() {
    return "VIN" + GenerateRandomNumberLength(12);
}

// Helper function to generate a vehicle NSC number
function GenerateNSC() {
    return "NSC" + GenerateRandomNumberLength(11);
}

// Helper function to randomly select a value from a populated drop-down
function setSelectValue(className, value) {
    const selectElement = document.querySelector(`.${className}`);
    if (selectElement !== null) {
        console.log("Setting value of " + className + " to " + value);

        //selectElement.dispatchEvent(new Event("onClick", { bubbles: true }));
        //selectElement.value = value;
        const event = new Event('onChange', {bubbles: true});
        selectElement.dispatchEvent(event);
    }
}

function SelectRadioButton(id) {
    var el = document.getElementById(id);
    if (el !== null) {
        el.click();
    }
}

function RandomlySelectRadioButton(id) {
    // 50% chance of clicking the button
    if (Math.floor(Math.random() * 100) + 1 > 50) {
        var el = document.getElementById(id);
        if (el !== null) {
            el.click();
        }
    }
}

function RandomlyChooseRadio(...params) {
    // randomly select one of the values in params
    var randomIndex = Math.floor(Math.random() * params.length);
    var id = params[randomIndex];
    el = document.getElementById(id);
    if (el !== null) {
        el.click();
    }
}

function GenerateRandomText(length) {
    return chance.string({length: length});
}

function RandomlySpeedLimit(){
    const speedLimits = ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "110"];
    return speedLimits[Math.floor(Math.random() * speedLimits.length)];
}

function GetDateFiveMinutesAgo() {
    const date = new Date();
    date.setMinutes(date.getMinutes() - 5);
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const day = date.getDate().toString().padStart(2, '0');
    const formattedDate = `${year}${month}${day}`;
    return formattedDate;
}

function GetCurrentDate() {
    const date = new Date();
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const day = date.getDate().toString().padStart(2, '0');
    const formattedDate = `${year}${month}${day}`;
    return formattedDate;
}

function GetDateInFiveFiveDays() {
    // Add five days to the current date
    let date = new Date();  // Get the current date
    date.setDate(date.getDate() + 5);  // Add five days to the current date
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const day = date.getDate().toString().padStart(2, '0');
    const formattedDate = `${year}${month}${day}`;
    return formattedDate;
}

function GetTimeFiveMinutesAgo() {
    const date = new Date();
    date.setMinutes(date.getMinutes() - 5);
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');
    const formattedTime = `${hours}${minutes}`;
    return formattedTime;
}

function GetTimeOneMinuteAgo() {
    const date = new Date();
    date.setMinutes(date.getMinutes() - 1);
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');
    const formattedTime = `${hours}${minutes}`;
    return formattedTime;
}

function GenerateCompanyName() {
    var companysuffixes = ["Inc.", "Ltd.", "Corp.", "Co.", "Company", "Foundation", "GmbH", "AG", "e.V."];
    var name = chance.last() + " TEST " + companysuffixes[Math.floor(Math.random() * companysuffixes.length)];
    return name;
}

function GenerateEmailAddress(firstnames) {
      var emaildomains = [
        "yahoo.com",
        "hotmail.com",
        "gmx.de",
        "aol.com",
        "gov.bc.ca",
        "vehicle-ownership-4u.com",
        "eml.cc",
        "thisisaverylongdomainname.co.uk"
    ]

    var firstname = "";
    // Split the first name into parts
    if (firstnames === undefined) {
        firstname = chance.first();
    }
    else {
        firstname = firstnames.split(" ")[0];
    }
    return firstname + "@" + emaildomains[Math.floor(Math.random() * emaildomains.length)];
}