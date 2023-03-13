import React from 'react';
import { expect, test } from 'jest';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import App from './App';

test('renders hello message', () => {
  render(<App />);
  const textElement = screen.getByText(/Hello, world!/i);
  expect(textElement).toBeInTheDocument();
});
