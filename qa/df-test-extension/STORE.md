# Store listing

This extension is available in the Chrome Web Store, but is not listed in the public directory. Here is a direct link to the store listing so you can install it in your browser:

[RSBC Roadside Forms auto-fill extension](https://chromewebstore.google.com/detail/rsbc-roadside-forms-auto/fjmiihmammcnhbkijhdnbjlklejdcgee?authuser=0&hl=en&pli=1)


## Update the store listing

The store listing is configured from a Chrome Web Extension developer account. Use this URL to access and update the listing:

[Chrome Web Store Developer page](https://chrome.google.com/webstore/devconsole/741cffb5-4b89-410d-b746-281caac5968e/fjmiihmammcnhbkijhdnbjlklejdcgee/edit/listing)


## Publish a new version of the extension

Be sure to update the version number for each new release of the extension. The version number is in [manifest.json](manifest.json).

When you are ready to publish a new version to the store, run the PowerShell script [build.ps1](build.ps1). This will package up the extension into a zip file with the version number in the file.

Note: You can't load the zip file directly into your web browser, even in developer mode. The zip file is only for submission to the Chrome Web Store. If you look at build.ps1, you will see that it follows these steps:

1. Extract the version number from [manifest.json](manifest.json).
2. Copy `df-test-extension/` to a temporary folder.
3. Update [manifest.json](manifest.json) in the temporary folder to remove localhost and loopback hosts (these are not allowed in the Chrome store, but are required when working locally as a developer).
4. Create a zip archive. The archive will have the build number in the file name, and the zip file will not include images, to keep the archive small.
5. Lists the zip file contents, to verify that the zip file is valid.

Once complete, you can submit the zip file to the Chrome Web Store. It may take hours or days to gain approval.
