# Store listing

This extension is published to the Chrome Web Store, but is not listed in the public extension directory, which may keep it from being discovered by non RSI people. Here is a direct link to the store listing:

https://chrome.google.com/webstore/

## Update the store listing

Use this URL to update the listing:

https://chrome.google.com/webstore/devconsole/741cffb5-4b89-410d-b746-281caac5968e/fjmiihmammcnhbkijhdnbjlklejdcgee/edit/listing

## Publish a new version of the extension

Be sure to update the version number for each new release of the extension. The version number is in the manifest.json file.

When you are ready to publish the new version to the store, run the PowerShell script build.ps1. This will package up the extension into a zip file with the version number in the file.

You can't load the zip file into your web browser: the zip file is only for submission to the Chrome Web Store. If you look at build.ps1, you will see that it follows these steps:

1. Extracts the version number from the manifest.json file.
2. Copy the df-test-extension folder to a temporary location.
3. Updates manifest.json in the temporary folder to remove localhost and loopback hosts (these are not allowed in the Chrome store).
4. Creates a zip file, ignoring some files to keep the archive small.
5. Lists the zip file contents, to verify that the zip file is valid.

Once complete, you can submit the zip file to the Chrome Web Store. It may take days to weeks to gain approval.
