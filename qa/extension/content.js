/*
Form-filler automation for DF 2.0 roadside forms.
This code runs when a page from the RSF DEV or TEST server is loaded.
*/

// Element id to use for the automation menu and buttons div
let automationId = "qa-automation";

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

// Helper function to overlay an ugly Fill button on the form
function AddButton(buttonName, topLocation, leftLocation, zIndex, fieldStructure) 
{
    let btn = document.createElement("button");
    btn.innerHTML = buttonName;
    buttonStyle = "top:" + topLocation + " !important;left:" + leftLocation + " !important;position:fixed;z-index: " + zIndex;
    buttonStyle += ";background-color: #ffff00 !important;";
    btn.style = buttonStyle;

    btn.addEventListener('click', () => {
        FillDriverSection();
        FillVehicleSection();
        FillOwnerSection();
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
        FillOfficerSection();
     })

    // Add the button to the page
    document.getElementById("qa-automation").appendChild(btn);
}

function FillDriverSection() {
    SetField('drivers_licence_no', GenerateDL());
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
    SetField('regist_owner_last_name', chance.last());
    SetField('regist_owner_first_name', GenerateGivenNames());
    SetField('regist_owner_address', GenerateStreetAddress());
    SetField('regist_owner_phone', GeneratePhoneNumber());
    SetField('regist_owner_city', GenerateCity());
    SetCustomSelect('regist_owner_prov_state-select', "BRITISH COLUMBIA");
    SetSelect('regist_owner_postal', GeneratePostalCode());
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
    SetField('linkage_location_of_keys_explanation', chance.paragraph({ sentences: 1 }));
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
    SetField('other-reason', chance.paragraph({ sentences: 1 }));
    RandomlyChooseRadio('prescribed_test_used-YES', 'prescribed_test_used-NO');
    SetField('date_of_test', GetCurrentDate());
    SetField('time_of_test', GetTimeOneMinuteAgo());
    RandomlyChooseRadio('reason_for_not_using_prescribed_test-refused', 'reason_for_not_using_prescribed_test-opinion')
}

function FillTestAdministeredSection() {
    // Test administered (alcohol)
    RandomlyChooseRadio('test_used_alcohol-alco-sensor', 'test_used_alcohol-instrument', 'test_used_alcohol-physical-cordination-test');
    SetField('asd_expiry_date', GetDateInFiveFiveDays());
    RandomlyChooseRadio('result_alcohol-51-99 mg%', 'result_alcohol-51-99 mg%');
    SetField('bac_result_mg', Math.floor(Math.random() * 1000));

    // Test administered (drugs)
    RandomlyChooseRadio('test_used_drugs-approved-drug', // test_used_drugs-approved-drug
        'test_used_drugs-physical-cordination-test-sfts', // test_used_drugs-physical-cordination-test-sfts
        'test_used_drugs-physical-cordination-test-dre'); // test_used_drugs-physical-cordination-test-dre
    RandomlySelectRadioButton('THC');
    RandomlySelectRadioButton('Cocaine');
}

function FillOfficerSection() {
    SetField('officer-lastname', chance.last());
    SetField('officer-prime-id', "QA" + GenerateRandomNumberLength(4));
    SetField('officer-agency', GenerateCity() + " COPS");        
    SetField('date-of-test', GetCurrentDate());
    SetField('time-of-test', GetTimeFiveMinutesAgo());
    SelectRadioButton('test-used-alcohol-physical-cordination-test')
}
