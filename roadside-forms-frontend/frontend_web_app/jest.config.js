module.exports = {
    // Other Jest configuration options...
    "jest": {
    "moduleFileExtensions": ["js", "jsx", "json", "node"]
  },
    transform: {
      "^.+\\.js$": "babel-jest",
    },
    "setupFiles": [
      "fake-indexeddb/auto",
      "./src/setupTests.js"
  ]
  };