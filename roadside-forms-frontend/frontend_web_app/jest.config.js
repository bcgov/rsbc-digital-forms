module.exports = {
    // Other Jest configuration options...
  
    transform: {
      "^.+\\.js$": "babel-jest",
    },
    "setupFiles": [
      "fake-indexeddb/auto",
      "./src/setupTests.js"
  ]
  };