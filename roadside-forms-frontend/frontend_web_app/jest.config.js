const { transform } = require("lodash");

module.exports = {
    // Other Jest configuration options...
    moduleFileExtensions: ["js", "jsx", "json", "node"],
    transform: {
      "^.+\\.js$": "babel-jest",
    },
    transformIgnorePatterns: [
      "node_modules/(?!(.*.mjs$|keycloak.js))",
      "node_modules/(?!(react|@react-keycloak|@react-keycloak/web)/)"
    ],
    "setupFiles": [
      "fake-indexeddb/auto",
      "./src/setupTests.js"
  ]
  };