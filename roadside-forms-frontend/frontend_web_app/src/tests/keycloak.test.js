import React from 'react';
import { render, cleanup, screen } from '@testing-library/react';
import { Header } from '../components/common/Header/Header';
import { useAuth } from 'react-oidc-context';
import { BrowserRouter } from 'react-router-dom';

jest.mock('react-oidc-context');

describe('OIDC Auth test', () => {
  beforeEach(cleanup);

  test('renders without crashing', async () => {
    useAuth.mockReturnValue({
      isAuthenticated: false,
      isLoading: false,
    });

    render(<BrowserRouter><Header /></BrowserRouter>);
    expect(screen.getByTestId('roadsafety-header')).toBeInTheDocument();
  });
});
