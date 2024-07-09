import React from 'react';
import { render, cleanup, screen } from '@testing-library/react';
import { Header } from '../components/common/Header/Header';
import { useKeycloak } from '@react-keycloak/web';
import { BrowserRouter } from 'react-router-dom';

jest.mock('@react-keycloak/web');

describe('Keycloak test', () => {
  beforeEach(cleanup);

  test('renders without crashing', async () => {
    useKeycloak.mockReturnValue({
      keycloak: { authenticated: false },
      initialized: true,
    });

    render(<BrowserRouter><Header /></BrowserRouter>);
    expect(screen.getByTestId('roadsafety-header')).toBeInTheDocument();
  });
});
