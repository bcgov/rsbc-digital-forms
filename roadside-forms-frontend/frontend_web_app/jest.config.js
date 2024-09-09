module.exports = {
    // Other Jest configuration options...
    moduleFileExtensions: ["js", "jsx", "json", "node"],
    transform: {
      "^.+\\.js$": "babel-jest",
    },
    "setupFiles": [
      "fake-indexeddb/auto",
      "./src/setupTests.js"
  ]
  };