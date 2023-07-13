import React from 'react';
import { render, cleanup } from '@testing-library/react';
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

    const { getByTestId } = render(<BrowserRouter><Header /></BrowserRouter>);
    expect(getByTestId('roadsafety-header')).toBeInTheDocument();
  });
});
