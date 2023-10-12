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
AddHotKeys();




// Overlay an ugly yellow Fill button on the form
function AddButton(buttonName, topLocation, leftLocation, zIndex, fieldStructure) 
{
    let btn = document.createElement("button");
    btn.innerHTML = buttonName;
    buttonStyle = "top:" + topLocation + " !important;left:" + leftLocation + " !important;position:fixed;z-index: " + zIndex;
    buttonStyle += ";background-color: #ffff00 !important;";
    btn.style = buttonStyle;
    btn.title = "Alt-I: inject values in all sections\nAlt-H: hide/show  button";
    btn.addEventListener('click', () => {
        FillAllSections();
     })

    // Add the button to the page
    document.getElementById("qa-automation").appendChild(btn);
}

// Show and hide the "Fill" button on the form
// (Otherwise, it might get printed)
function ToggleShowHideMenu() {
    console.log("ToggleShowHideMenu")
    qae = document.getElementById("qa-automation");
    if (qae.style.display === "none" ) {
        qae.style.display = "block";
        document.getElementById('app').style.paddingLeft = sidebarWidth
    } else {
        qae.style.display = "none";
    }
}

// Hotkeys:
// Alt-H: Show/Hide menu
// Alt-I: Fill all sections
function AddHotKeys() {
    document.onkeyup = function () {
        var e = e || window.event; // for IE to cover IEs window event-object

        if (e.altKey && e.which === "H".charCodeAt(0)) {
            ToggleShowHideMenu()
            return false;
        } 
        else if (e.altKey && e.which === "I".charCodeAt(0)) {
            FillAllSections();
            return false;
        } 
    }
}
