# Roadside forms automation browser extension
*A minimal browser extension to make filling out roadside digital forms easier.*

## Description
When you install this extension in your browser and go to the Digital Forms DEV or TEST environment, a "Fill" button will be added to the top-left corner of the page. After you have selected a 24-hour form, click the Fill button to fill out the fields quickly.

## Installation
To install this extension, you must be using a Chromium-based browser like Edge or Chrome. Go to Settings > Extensions and enable developer mode. After enabling developer mode, you should see the option "Load Unpacked" appear. Click "Load Unpacked" and select the folder where this file is located. 

You may wish to pin the extension so it is always visible. The icon will show in colour and the Fill button will appear only when the DEV or TEST environments are loaded.

Steps:
 1. Go to Extensions.
 2. Enable developer mode.
 3. Select "Load Unpacked" on the extensions page.
 4. Enable the extension.

![Steps to install this extension](images/installation.png)

## Usage

When in the DEV or TEST environment, click the "Fill" button in the top-left corner of the page:

![This is what the button looks like](images/usage.png)

Example of the form after clicking the "Fill" button:

![Filled form](example.png)

## Making changes to this extension
If you want to modify this project, here is a description of what each file does:

- icons/: folder for icon images shown in the extension bar.
- chance.min.js: copy of the open-source chance.js library, for generating field values.
- content.js: the primary script, which gets called when the Fill button is pressed.
- helper-functions.js: helper functions called from content.js.
- tables.js: data used from content.js (e.g. a table of towns and cities in BC).
- manifest.json: the file that the browser uses to get information about this extension
- README.md: this file

## Notes
This extension works by injecting JavaScript onto pages that load from the DEV and TEST environment. The JavaScript accesses the form elements (fields, buttons, checkboxes) and adds values to the fields. The custom React fields may not work as expected until you click on the selected values. This should be fixable in the near future if we can figure out how these custom elements work.

The extension should work in any Chromium-based browser. It will not work in Firefox unless you change the manifest to v2.