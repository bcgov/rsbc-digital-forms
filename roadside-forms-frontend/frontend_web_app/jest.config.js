const { transform } = require("lodash");

module.exports = {
    // Other Jest configuration options...
    moduleFileExtensions: ["js", "jsx", "json", "node"],
    transform: {
      "^.+\\.js$": "babel-jest",
    },
    transformIgnorePatterns: [
      "/node_modules/(?!@react-keycloak)/",
      "/node_modules/(?!(.*.css|.*.mjs$|keycloak.js)/)",
    ],
    "setupFiles": [
      "fake-indexeddb/auto",
      "./src/setupTests.js"
  ]
  };