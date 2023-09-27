// Tweak this if it's taking too long to load drop-downs to populate
const secondsToWaitForDropdownsToAppear = 25;

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
    const genders = ["M", "F", "X", "U"];
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