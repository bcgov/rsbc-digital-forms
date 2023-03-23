module.exports = {
  env: {
    browser: true,
    es6: true
  },
  extends: ['eslint:recommended', 'plugin:react/recommended', 'plugin:storybook/recommended'],
  settings: {
    "react": {
      "version": "^17.0.0"
    }
  },
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly'
  },
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaFeatures: {
      jsx: true
    },
    ecmaVersion: 2018,
    sourceType: 'module'
  },
  plugins: ['react', '@typescript-eslint'],
  rules: {
    'react/jsx-props-no-spreading': [0],
    'react/jsx-filename-extension': [1, {
      'extensions': ['.js', '.jsx']
    }],
    'react/jsx-one-expression-per-line': 'off',
    'no-plusplus': [2, {
      'allowForLoopAfterthoughts': true
    }]
  }
};