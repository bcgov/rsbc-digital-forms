/*
This code runs when a page from the RSF DEV or TEST server is loaded.
*/
// Element id to use for the automation menu and buttons div
let automationId = "qa-automation";


// Helper function to put a button on the form, so you can click it to fill the form
function AddButton(buttonName, topLocation, leftLocation, zIndex, fieldStructure) 
{
    let btn = document.createElement("button");
    btn.innerHTML = buttonName;
    buttonStyle = "top:" + topLocation + " !important;left:" + leftLocation + " !important;position:fixed;z-index: " + zIndex;
    console.log("Adding button " + buttonName + ": " + buttonStyle);
    btn.style = buttonStyle;

    btn.addEventListener('click', () => {
        // Driver's information section
        SetField('drivers-number', GenerateDL());
        //let licenceJurisdictions = ValuesFromDropdownField('react-select-2-input');
        //SetField('react-select-2-input', licenceJurisdictions[Math.floor(Math.random() * licenceJurisdictions.length)]);
        SetField('last-name', chance.last());
        SetField('given-name', GenerateGivenNames());
        SetField('dob', GenerateDateOfBirth());
        SetField('address', GenerateStreetAddress());
        SetField('phone', GeneratePhoneNumber());
        SetField('city', GenerateCity())
        //let provinces = ValuesFromDropdownField('react-select-3-input');
        //SetField('react-select-3-input', provinces[Math.floor(Math.random() * provinces.length)]);
        SetField('postal-code', GeneratePostalCode());

        // Vehicle information section
        //let vehicleJurisdictions = ValuesFromDropdownField('react-select-2-input');
        //SetField('react-select-4-input', licenceJurisdictions[Math.floor(Math.random() * vehicleJurisdictions.length)]);
        SetField('plate-number', GenerateLicencePlate());
        SetField('registration-number', GenerateRegistrationNumber());
        SetField('vin-number', GenerateVIN());
        SetField('nsc-number', GenerateNSC());
        
        // Registered owner section
        SetField('owner-last-name', chance.last());
        SetField('owner-first-name', GenerateGivenNames());
        SetField('registered-owner-address', GenerateStreetAddress());
        SetField('registered-owner-phone', GeneratePhoneNumber());
        SetField('registered-owner-city', GenerateCity());
        SetSelect('registered-owner-prov-state-select', "BRITISH COLUMBIA");
        SetSelect('vehicle-year-select', "1979");
        SetSelect('vehicle-make-model-select', "CHEVROLET - CHEVETTE");
        SetSelect('vehicle-style-select', "5-DOOR HATCH");
        SetSelect('vehicle-colour', "YELLOW");
        
        // Vehicle impoundment or disposition
        // Radio button vehicle-impounded-YES
        SelectRadioButton('vehicle-impounded-YES');
        SelectRadioButton('key-location-WITH VEHICLE');
        SetField('ILO-options-select', 'COLD COUNTRY TOWING (CRANBROOK), 3584 COLLINSON RD, CRANBROOK, 250-426-3680');
        
        // Prohibition
        SelectRadioButton('type-of-prohibition-alcohol');
        SetField('offence-address', GenerateStreetAddress());
        SetField('offence-city-select', GenerateCity())
        SetField('offence-agency-file', "RSI" + GenerateRandomNumberLength(4));

        SetField('registered-owner-postal', GeneratePostalCode());
        SetField('date-of-driving', GetCurrentDate());
        SetField('time-of-driving', GetTimeFiveMinutesAgo())

        // Reasonable grounds
        SelectRadioButton('witnessed-by-officer');
        SelectRadioButton('independent-witness');
        SelectRadioButton('prescribed-device-YES');

        // Officer section
        SetField('officer-lastname', chance.last());
        SetField('officer-prime-id', "QA" + GenerateRandomNumberLength(4));
        SetField('officer-agency', GenerateCity() + " COPS");        
        SetField('date-of-test', GetCurrentDate());
        SetField('time-of-test', GetTimeFiveMinutesAgo());
        SelectRadioButton('test-used-alcohol-physical-cordination-test')
     })
    //document.body.insertAdjacentElement("afterbegin", btn);
    document.getElementById("qa-automation").appendChild(btn);
}


// Select the entire DOM for observing:
const target = document.querySelector('body');

// Create a new observer instance to update the app container when it appears
const observer = new MutationObserver(function ()
{
    // Trigger when the 'app' element loads. Will be called multiple times
    if (document.getElementById('root'))
    {
        // Move page content over
        //document.getElementsByClassName('App')[0].style.paddingLeft = "50px"

        // Add new UI div if it doesn't already exist
        if (!document.getElementById(automationId))
        {
            // Create a div to put all the UI in
            let testDiv = document.createElement("div");
            testDiv.id = automationId;
            document.body.insertAdjacentElement("afterbegin", testDiv);

            // UI
            AddButton("Fill", "10px", "8px", "999", "1");
        }
    }
});

// Set configuration object:
const config = {childList: true};

// Start the observer
observer.observe(target, config);
