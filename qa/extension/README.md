# Roadside forms automation browser extension
*A minimal extension to make filling out roadside digital forms easier.*

## Description
When you install this extension in your browser and go to the Digital Forms DEV, TEST, or localhost environments, a "Fill" button appar in the top-left corner of the page. Click it to fill out the fields quickly with random data.

## Installation
To install this extension, you must be using a Chromium-based browser like Edge or Chrome. Go to **Settings** > **Extensions** and enable **Developer Mode**. You should then see the option **Load Unpacked** appear. Click it and select the folder where this file is checked out. 

You may wish to pin the extension so its icon always visible. Or, not. The icon will show in colour and the Fill button will appear only when the DEV, TEST, or localhost environments are loaded.

Steps to sideload this extension:
 1. Go to **Extensions** in the browser settings.
 2. Enable the **Developer Mode** toggle (this allows you to side-load the extension).
 3. Select the **Load Unpacked** link on the Extensions page.
 4. Enable the extension, if needed.
 5. Browse to the DEV or TEST environment.

This screenshot illustrates the steps:
![Steps to install this extension](images/installation.png)

## Usage

When in the DEV, TEST, or local environments, click the "Fill" button in the top-left corner of the page:

![This is what the button looks like](images/usage.png)

Example of the form after clicking the "Fill" button:

<img src="images/example.gif">


## Also see

If you want to learn more about how this extension works, and how to update it, see [DEVELOPER.md](DEVELOPER.md).