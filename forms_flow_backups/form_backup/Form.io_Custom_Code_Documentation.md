# RoadSaftey Digital Forms - Form.io Custom JavaScript Documentation

This document provides a comprehensive guide to all custom JavaScript code found in the LatestFromDF.json form configuration file. It is intended for developers who are editing this form in the Form.io platform.

## Table of Contents
1. [Introduction to Custom Code in Form.io](#introduction-to-custom-code-in-formio)
2. [Form Logic](#form-logic)
3. [Custom Action Scripts](#custom-action-scripts)
4. [Error Handling](#error-handling)
5. [Custom Conditionals](#custom-conditionals)
6. [Calculated Values](#calculated-values)
7. [Best Practices for Editing](#best-practices-for-editing)

## Introduction to Custom Code in Form.io

Form.io allows custom JavaScript in several places within the form configuration:

1. **Custom Action Buttons**: JavaScript executed when a button is clicked
2. **Custom Conditional Logic**: JavaScript to determine if a component should be shown
3. **Calculated Values**: JavaScript to calculate a field's value based on other fields
4. **Custom Validation**: JavaScript to validate field inputs
5. **Logic Arrays**: Complex logic with triggers and actions

This form uses all of these features to create a dynamic, interactive experience.

## Form Logic

### Page Navigation Logic
The form contains logic to control page navigation based on certain conditions. This logic is defined in the `logic` array of a component:

```javascript
// Logic to jump to Print Preview page if already printed
{
  "name": "Don not show officer input if already printed",
  "trigger": {
    "type": "advanced",
    "showAdvanced": true,
    "whenAndOr": "&&",
    "advanced": [
      {
        "name": "Check if Print Response is YES",
        "whenAdvanced": "printResponse",
        "operatorAdvanced": "isEqual",
        "eqAdvanced": "YES"
      }
    ]
  },
  "actions": [
    {
      "name": "Jump to Print Preview page",
      "type": "customAction",
      "customAction": "console.log(\"Page switcher\")\nif(instance.root.page === 0){\n  instance.root.setPage(1);\n}"
    }
  ]
}
```

**How it works**: 
- The trigger checks if the field `printResponse` equals "YES"
- If true, the custom action executes JavaScript that checks if the current page is 0
- If the current page is 0, it navigates to page 1 (the Print Preview page)

**Form.io Context**: 
- `instance.root.page` refers to the current page index in a wizard form
- `instance.root.setPage(1)` is a Form.io API method to navigate to a specific page

## Custom Action Scripts

### Form ID Management
The form includes functionality to manage form IDs for different form types. This is implemented in the `calculateValue` property of a hidden field:

```javascript
// Calculate form IDs and mark as leased
async function markFormAsLeased(formId, formType) {
  try {
    // Call the function to update the formID table
    await window.markFormAsLeased(formId, formType);
  } catch (error) {
    console.error("Error marking form as leased:", error);
    return false;
  }
}

async function getAndSaveFormId(formType = "24Hour", maxRetries = 5, retryDelay = 1000) {
  let retries = 0;
  let value = null;
  while (retries < maxRetries) {
    try {
      value = await window.getNextAvailableFormId(formType);
      console.log(`Retrieved form ID ${formType}:`, value);
      if (value !== null) {
        return value; // Success! Return the value
      } else {
        console.log(`No available form ID found on attempt ${retries + 1}. Retrying...`);
        retries++;
        // Wait before retrying
        await new Promise(resolve => setTimeout(resolve, retryDelay));
      }
    } catch (error) {
      console.error(`Error getting form ID (attempt ${retries + 1}):`, error);
      retries++;
      // Wait before retrying
      await new Promise(resolve => setTimeout(resolve, retryDelay));
    }
  }
  console.error(`Failed to get form ID after ${maxRetries} attempts`);
  return null;
}

// Checksum calculation for form numbers
const formNumberChecksum = (formNumber) => {
  const timesTwo = (num) => {
    let newNum = num * 2;
    if (newNum > 9) {
      newNum = 1;
    }
    return newNum;
  };
  let [calc1, calc2, calc3, calc4, calc5, calc6, calc7, calc8] = formNumber
    .toString()
    .split("")
    .map(Number);

  calc4 = timesTwo(calc4);
  calc6 = timesTwo(calc6);
  calc8 = timesTwo(calc8);

  const digit = (calc3 + calc4 + calc5 + calc6 + calc7 + calc8) % 10;

  return +(formNumber + digit);
};

// Main function to get and set form IDs
async function main(formType, apiKey) {
  const numberinstance = instance.root.getComponent(apiKey);
  if(numberinstance.getValue()){
    return;
  }
  value = await getAndSaveFormId(formType); // Wait for the function to complete
  if (value) {
    console.log("Successfully retrieved form ID:", value);
    // if VI form do the checksum
    const form_id = formType === "VI" ? formNumberChecksum(value) : value
    instance.root.getComponent(apiKey).setValue(form_id);
    // mark the form as leased in indexedDB
    // TODO : Enable leasing logic
    await markFormAsLeased(value, formType);
    // Do something with the value
  } else {
    console.log("Could not retrieve a valid form ID");
  }
}
```

**How it works**:
- The code manages form IDs for three different form types: "VI", "12Hour", and "24Hour"
- It retrieves available form IDs from a database, applies checksums for VI forms, and marks them as "leased"
- It uses retry logic to handle potential failures when retrieving form IDs

**Form.io Context**:
- `instance.root.getComponent(apiKey)` retrieves a form component by its key
- `component.setValue()` sets the value of a form component
- This code interacts with external functions (`window.getNextAvailableFormId`, `window.markFormAsLeased`) that are defined outside the form

### Form Module Initialization
The form uses a module pattern to prevent duplicate initialization:

```javascript
// Use a more specific variable name or namespace
if (typeof window.myFormModule === 'undefined' || !window.myFormModule.formRenderedSuccess) {
  window.myFormModule = {
    formRenderedSuccess: false
  };
  
  // Check if instance exists before accessing its properties
  if (instance && instance.root) {
    // Delete the flag if user navigates away
    window.addEventListener('popstate', (event) => {
      console.log('URL changed');
      if (window.myFormModule) {
        window.myFormModule.formRenderedSuccess = false;
        console.log("Reset formRenderedSuccess flag");
      }
    });
    
    Promise.all([
      instance.root.formReady,
      instance.root.ready
    ]).then(() => {
      console.log("Form ready and in submission", (instance.options && instance.options.readOnly ? true : false));
      const isSubmission = (instance.options && instance.options.readOnly ? true : false);
      
      if (!isSubmission && !window.myFormModule.formRenderedSuccess) {
        main("24Hour", "twenty_four_hour_number");
        main("12Hour", "twelve_hour_number");
        main("VI", "VI_number");
        window.myFormModule.formRenderedSuccess = true;
        console.log("Set formRenderedSuccess to true after processing");
      }
    }).catch(error => {
      console.error("Error during form initialization:", error);
      if (window.myFormModule) {
        window.myFormModule.formRenderedSuccess = false;
      }
    });
  } else {
    console.warn("Instance or instance.root is not defined");
  }
} else {
  console.log("myFormModule already exists, skipping initialization");
}
```

**How it works**:
- Creates a global module (`window.myFormModule`) to track form initialization state
- Listens for navigation events to reset the initialization flag
- Waits for the form to be fully ready before initializing form IDs
- Checks if the form is in submission mode (read-only) to avoid unnecessary initialization

**Form.io Context**:
- `instance.root.formReady` and `instance.root.ready` are Form.io promises that resolve when the form is ready
- `instance.options.readOnly` indicates if the form is in read-only mode (submission view)

### Generate Form IDs Button
Custom script for generating form IDs, attached to a button's `custom` property:

```javascript
console.log("generate formids")
if (window.myFormModule) {
  window.myFormModule.formRenderedSuccess = false;
}

/**
 * This is a script for temporary use by admin/designer when form IDs are not available in dev backend
 * It will only execute for users with the designer role and will only insert new form IDs if none are available
 */

// Main function to check and insert records if needed
async function checkAndInsertFormIds() {
  try {
    // // First check if user has designer role
    // const userDetails = JSON.parse(localStorage.getItem('USER_DETAILS') || '{}');
    // const userGroups = userDetails.groups || [];
    
    // // Check if user has designer role
    // const hasDesignerRole = userGroups.some(group => 
    //   group === "/digitalforms/digitalform-designer" || 
    //   group.includes("digitalform-designer")
    // );
    
    // if (!hasDesignerRole) {
    //   console.warn("Script execution halted: User does not have designer role");
    //   return;
    // }
    
    console.log("User has designer role. Proceeding with form ID check...");
    
    // Define the form types
    const formTypes = ['VI', '12Hour', '24Hour'];
    
    // Open the database
    const dbOpenRequest = indexedDB.open("digitalForms");
    
    dbOpenRequest.onerror = (event) => {
      console.error("Error opening database:", event.target.error);
    };
    
    dbOpenRequest.onsuccess = async (event) => {
      const db = event.target.result;
      console.log("Database opened successfully");
      
      let needToInsert = false;
      const formTypesNeedingIds = [];
      
      // Check if each form type has available IDs
      for (const formType of formTypes) {
        const transaction = db.transaction("formID", "readonly");
        const formIDStore = transaction.objectStore("formID");
        
        // Get all records for this form type
        const index = formIDStore.index("form_type");
        const request = index.getAll(formType);
        
        await new Promise((resolve) => {
          request.onsuccess = (event) => {
            const forms = event.target.result;
            const availableForms = forms.filter(form => form.leased === false);
            
            if (availableForms.length === 0) {
              console.log(`No available forms for type ${formType}. Will need to insert new ones.`);
              formTypesNeedingIds.push(formType);
              needToInsert = true;
            } else {
              console.log(`Found ${availableForms.length} available forms for type ${formType}.`);
            }
            resolve();
          };
          
          request.onerror = (event) => {
            console.error(`Error checking forms for type ${formType}:`, event.target.error);
            resolve();
          };
        });
      }
      
      if (!needToInsert) {
        console.log("All form types have available IDs. No insertion needed.");
        db.close();
        return;
      }
      
      console.log(`Need to insert IDs for form types: ${formTypesNeedingIds.join(', ')}`);
      
      // Start insertion for types that need it
      const insertTransaction = db.transaction("formID", "readwrite");
      const formIDStore = insertTransaction.objectStore("formID");
      
      let insertCounter = 0;
      let errorCounter = 0;
      const totalToInsert = formTypesNeedingIds.length * 5;
      
      formTypesNeedingIds.forEach(formType => {
        for (let i = 0; i < 5; i++) {
          const record = createFormIdRecord(formType);
          const request = formIDStore.add(record);
          
          request.onsuccess = () => {
            insertCounter++;
            console.log(`Successfully inserted ${formType} record: ${record.id}`);
            
            // Check if all operations completed
            if (insertCounter + errorCounter === totalToInsert) {
              console.log(`Insertion complete. ${insertCounter} records inserted, ${errorCounter} errors.`);
            }
          };
          
          request.onerror = (event) => {
            errorCounter++;
            console.error(`Error inserting ${formType} record:`, event.target.error);
            
            // Check if all operations completed
            if (insertCounter + errorCounter === totalToInsert) {
              console.log(`Insertion complete. ${insertCounter} records inserted, ${errorCounter} errors.`);
            }
          };
        }
      });
      
      insertTransaction.oncomplete = () => {
        console.log("Transaction completed successfully");
        db.close();
      };
      
      insertTransaction.onerror = (event) => {
        console.error("Transaction error:", event.target.error);
        db.close();
      };
    };
  } catch (error) {
    console.error("Error in checkAndInsertFormIds:", error);
  }
}

// Helper function to create a form ID record
function createFormIdRecord(formType) {
  // Generate a random ID between 10000000 and 99999999
  const id = Math.floor(10000000 + Math.random() * 90000000);
  
  return {
    id: id,
    form_type: formType,
    leased: false,
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString()
  };
}

// Call the main function
checkAndInsertFormIds();
```

**How it works**:
- This is an administrative tool for generating new form IDs when none are available
- It checks the IndexedDB database for available form IDs of each type
- If no IDs are available, it generates new ones with random numbers
- It's designed to be used by users with the designer role

**Form.io Context**:
- This script is attached to a button's `custom` property and executes when the button is clicked
- It interacts with the browser's IndexedDB API, which is outside of Form.io's scope

### Sample Data Fill
Script for filling the form with sample data, attached to a button's `custom` property:

```javascript
sample = {
    "VI": true,
    "TwentyFourHour": true,
    "TwelveHour": false,
    "driver_address": "1910 Westpark Ln",
    "driver_prov_state": {"value": 'CA_BC', "label": 'BRITISH COLUMBIA'},
    "driver_phone": "(787) 979-7797",
    "driver_city": "Victoria",
    "driver_postal": "V9B3R7",
    // ... (extensive sample data)
}
```

**How it works**:
- This is a simple object containing sample data for testing the form
- When the button is clicked, this data is used to populate the form fields

**Form.io Context**:
- In Form.io, this data would be assigned to the `data` object to populate form fields

## Error Handling

### Error Display and Navigation
Custom error handling to display and navigate to form errors, implemented in a component's `customConditional` property:

```javascript
function displayErrors(errorsArray, instanceObj) {
  // Get the errors container div
  const errorsContainer = document.getElementById('errorsContainer');
  
  if (!errorsArray || errorsArray.length === 0) {
    // No errors, empty and hide the container
    errorsContainer.innerHTML = '';
    errorsContainer.style.display = 'none';
    return;
  }
  
  // Make the container visible
  errorsContainer.style.display = 'block';
  
  // Create an unordered list element with a unique ID
  let errorsList = '<ul id="errorsList" style="color: #dc3545; padding-left: 20px; margin-bottom: 10px;">';
  
  // Loop through the errors array and add each error message to the list
  errorsArray.forEach((error, index) => {
    // Extract the error message and component label
    const errorMessage = error.message || 'Unknown error';
    const componentLabel = error.component && error.component.label 
      ? error.component.label.trim() 
      : 'Unknown field';
    
    // Get component ID
    const componentId = error.component ? 'l-' + error.component.id + '-' + error.component.key : '';
    
    // Add both the component label and error message with a data attribute
    if (componentId) {
      errorsList += `<li style="cursor: pointer;" data-component-id="${componentId}" data-error-index="${index}"><strong>${componentLabel}:</strong> ${errorMessage}</li>`;
    } else {
      errorsList += `<li><strong>${componentLabel}:</strong> ${errorMessage}</li>`;
    }
  });
  
  // Close the unordered list
  errorsList += '</ul>';
  
  // Set the HTML content of the errors container
  errorsContainer.innerHTML = errorsList;
  
  // Get the errors list element
  const errorsListElement = document.getElementById('errorsList');
  if (errorsListElement) {
    // Instead of trying to remove previous listeners (which won't work with a new function),
    // use the simpler approach of just setting a new handler
    errorsListElement.onclick = function(event) {
      // Check if a list item was clicked
      let target = event.target;
      
      // If the click was on a child element of the li (like the strong tag),
      // traverse up to find the li element
      while (target !== this && !target.hasAttribute('data-component-id')) {
        target = target.parentNode;
        if (!target) return; // Handle case where no matching parent is found
      }
      
      // If we found an li with a data-component-id attribute
      if (target !== this && target.hasAttribute('data-component-id')) {
        const componentId = target.getAttribute('data-component-id');
        focusComponent(componentId, instanceObj);
      }
    };
  }
}

// Define the focusComponent function in the same scope
function focusComponent(componentId, instanceObj) {
  const element = document.getElementById(componentId);
  if (element) {
    // Scroll to the element
    element.scrollIntoView({
      behavior: 'smooth',
      block: 'center'
    });
    
    // Try to focus on the element or its input
    const input = element.querySelector('input, select, textarea');
    if (input) {
      input.focus();
    } else {
      element.focus();
    }
    
    // Add a temporary highlight effect
    element.style.transition = 'background-color 0.5s';
    const originalBackgroundColor = element.style.backgroundColor;
    element.style.backgroundColor = '#fff3cd';
    
    setTimeout(() => {
      element.style.backgroundColor = originalBackgroundColor;
    }, 2000);
  }
}

// Function to reset everything
function resetErrorDisplay() {
  const errorsContainer = document.getElementById('errorsContainer');
  if (errorsContainer) {
    errorsContainer.innerHTML = '';
    errorsContainer.style.display = 'none';
  }
}

// Make sure instance is defined before using it
if (typeof instance !== 'undefined' && instance) {
  if (instance.root?.errors?.length) {
    console.log("Displaying errors");
    displayErrors(instance.root.errors, instance);
  } else {
    console.log("No errors, resetting display");
    resetErrorDisplay();
  }
} else {
  console.error("Instance object is not ready or not available");
}
```

**How it works**:
- This code creates a user-friendly error display that shows all validation errors in the form
- Users can click on an error message to navigate directly to the field with the error
- It highlights the field temporarily to make it easier to locate

**Form.io Context**:
- `instance.root.errors` contains all validation errors in the form
- The code uses DOM manipulation to create and manage the error display
- It's attached to an HTML element component's `customConditional` property to run when the form state changes

## Custom Conditionals

### Form Selection Conditional
Conditional logic to show/hide form sections based on selections, implemented in a component's `customConditional` property:

```javascript
// Driver's Information panel conditional
try {
  show = false;
  if(data?.VI || data?.TwentyFourHour || data?.TwelveHour){
    show = true
  } else {
    show = false;
  }
} catch (error) {
  console.error(error);
}
```

**How it works**:
- This conditional checks if any of the form types (VI, TwentyFourHour, or TwelveHour) are selected
- If at least one is selected, it shows the component; otherwise, it hides it
- It's wrapped in a try-catch block to prevent errors from breaking the form

**Form.io Context**:
- In Form.io's `customConditional` property, the variable `show` determines if the component is visible
- `data` refers to the current form data object

### Form Data Logging
Simple conditional to log form data:

```javascript
console.log("data from first panel", data)
```

**How it works**:
- This simple line logs the current form data to the console
- It's useful for debugging and development purposes

**Form.io Context**:
- This is used in a `customConditional` property to execute when the component is evaluated

## Calculated Values

Various calculated values used in the form:

```javascript
// Calculate if any form is selected
value = (data?.VI || data?.TwentyFourHour || data?.TwelveHour)
```

**How it works**:
- This expression calculates a boolean value based on whether any form type is selected
- The result is stored in the field's value

**Form.io Context**:
- In Form.io's `calculateValue` property, the variable `value` represents the calculated value to be assigned to the field
- This is used to drive conditional logic elsewhere in the form

## Best Practices for Editing

When editing custom JavaScript in this form, please follow these best practices:

1. **Understand the Form.io Context**:
   - Custom JavaScript runs in specific contexts within Form.io
   - Variables like `data`, `value`, `show`, and `instance` have special meanings
   - Be careful not to overwrite these built-in variables

2. **Test Thoroughly**:
   - Always test your changes in a development environment before deploying to production
   - Check both the happy path and error scenarios
   - Verify that your changes don't break existing functionality

3. **Error Handling**:
   - Always include try-catch blocks in custom conditionals and calculated values
   - Log errors to help with debugging
   - Provide fallback values when operations might fail

4. **Code Organization**:
   - Keep functions small and focused on a single task
   - Use meaningful variable and function names
   - Add comments to explain complex logic

5. **Performance Considerations**:
   - Avoid expensive operations in frequently evaluated code (like conditionals)
   - Be cautious with async operations that might delay form rendering
   - Consider the impact on form loading time

6. **Security Best Practices**:
   - Never store sensitive information in client-side code
   - Validate all data on the server side, not just in the client
   - Be cautious with external API calls

7. **Form.io Specific**:
   - Use `instance.root.getComponent()` to get references to other components
   - Use `component.setValue()` to update component values programmatically
   - Be aware of the form lifecycle (when components are created, rendered, and destroyed)

By following these guidelines, you'll help maintain the stability and performance of the form while making your changes.
