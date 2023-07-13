import React from 'react';
import { render, cleanup } from '@testing-library/react';
import { Header } from '../components/common/Header/Header';
import { useKeycloak } from '@react-keycloak/web';

jest.mock('@react-keycloak/web');

describe('Keycloak test', () => {
  beforeEach(cleanup);

  test('renders without crashing', async () => {
    useKeycloak.mockReturnValue({
      keycloak: { authenticated: false },
      initialized: true,
    });

    const { getByTestId } = render(<Header />);
    expect(getByTestId('roadsafety-header')).toBeInTheDocument();
  });
});
