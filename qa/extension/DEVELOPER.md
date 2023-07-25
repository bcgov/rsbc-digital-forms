# How to update this extension

## Making changes to this extension
If you want to modify this project, here is a description of what each file does:

- **icons/**: folder for icon images shown in the extension bar.
- **chance.min.js**: copy of the open-source chance.js library, for generating field values.
- **content.js**: the primary script, which gets called when the Fill button is pressed.
- **helper-functions.js**: helper functions called from content.js.
- **tables.js**: data used from content.js (e.g. a table of towns and cities in BC).
- **manifest.json**: the file that the browser uses to get information about this extension.
- **DEVELOPER.MD**: this page, with tips on how to update the extension.
- **README.md**: instructions for usage.

## Notes
This extension works by injecting JavaScript onto pages that load from the DEV and TEST environment. The JavaScript accesses the form elements (fields, buttons, checkboxes) and adds values to the fields. The custom React fields may not work as expected until you click on the selected values. This should be fixable in the near future if we can figure out how these custom elements work.

The extension should work in any Chromium-based browser. It will not work in Firefox unless you change the manifest to v2.