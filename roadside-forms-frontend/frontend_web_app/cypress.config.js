const { defineConfig } = require("cypress");
const { initPlugin } = require('cypress-plugin-snapshots/plugin');

module.exports = defineConfig({
  e2e: {
    baseUrl: 'http://localhost:3000',
    setupNodeEvents(on, config) {
      initPlugin(on, config);
    }
  },
});
