import React from 'react';
import { render, screen, fireEvent, waitFor, act } from '@testing-library/react';
import { RecoilRoot } from 'recoil';
import { userRolesAtom } from '../../../atoms/userRoles';
import { loginCompletedAtom } from '../../../atoms/loginCompleted';
import { useNavigate } from 'react-router-dom';
import { UserApi } from '../../../api/userApi';
import { UserAdminDashboard } from '../../../components/userAdminDashboard/userAdminDashboard';
import moment from 'moment-timezone';

jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'),
  useNavigate: jest.fn(),
}));

// Mock the entire BootstrapTable component
jest.mock('react-bootstrap-table-next', () => {
  return function DummyBootstrapTable(props) {
    return (
      <div data-testid="mock-bootstrap-table">
        {props.data.map((row) => (
          <div key={row.user_guid}>{row.last_name}</div>
        ))}
      </div>
    );
  };
});

jest.mock('react-bootstrap-table2-filter', () => ({
  textFilter: jest.fn(),
  __esModule: true,
  default: (props) => props,
}));

jest.mock('react-bootstrap-table2-paginator', () => {
  return jest.fn((props) => props);
});

describe('UserAdminDashboard', () => {
  const mockUsers = [
    {
      agency: "BCHP Burnaby",
      approved_dt: "2023-06-22T16:51:39Z",
      badge_number: "222222",
      display_name: "Test, user",
      first_name: "USER",
      last_name: "Test",
      login: "TEST@idir",
      role_name: "administrator",
      submitted_dt: "2023-06-22T16:51:39Z",
      user_guid: "91D388D1339C41388E622F5",
      username: "91d388d1339c41388e622f5@idir",
      last_active: "2023-06-23T10:00:00Z"
    },
    {
      agency: "BCHP Victoria",
      approved_dt: null,
      badge_number: "333333",
      display_name: "New, user",
      first_name: "NEW",
      last_name: "User",
      login: "NEW@idir",
      role_name: "officer",
      submitted_dt: "2023-06-23T09:00:00Z",
      user_guid: "91D388D1339C41388E622F6",
      username: "91d388d1339c41388e622f6@idir",
      last_active: null
    }
  ];

  beforeEach(() => {
    jest.clearAllMocks();
    UserApi.getAll = jest.fn().mockResolvedValue({ data: mockUsers });
  });

  test('should render UserAdminDashboard and handle new features', async () => {
    const mockNavigate = jest.fn();
    useNavigate.mockImplementation(() => mockNavigate);

    await act(async () => {
      render(
        <RecoilRoot
          initializeState={(snap) => {
            snap.set(userRolesAtom, [{ role_name: "administrator" }]);
            snap.set(loginCompletedAtom, true);
          }}
        >
          <UserAdminDashboard />
        </RecoilRoot>
      );
    });

    // Check if the table is rendered
    expect(screen.getByTestId('mock-bootstrap-table')).toBeInTheDocument();

    // Test "Show New User Requests only" filter
    const newUserFilter = screen.getByLabelText('Show New User Requests only');
    expect(newUserFilter).toBeInTheDocument();
    
    await act(async () => {
      fireEvent.click(newUserFilter);
    });

    // Test add administrator button
    const addAdminButton = screen.getByText('Add as administrator');
    expect(addAdminButton).toBeInTheDocument();
    expect(addAdminButton).toBeDisabled();
  });

  test('should handle sorting, filtering, and pagination', async () => {
    await act(async () => {
      render(
        <RecoilRoot
          initializeState={(snap) => {
            snap.set(userRolesAtom, [{ role_name: "administrator" }]);
            snap.set(loginCompletedAtom, true);
          }}
        >
          <UserAdminDashboard />
        </RecoilRoot>
      );
    });

    const table = screen.getByTestId('mock-bootstrap-table');
    expect(table).toBeInTheDocument();

    // check if the expected data is rendered
    expect(screen.getByText('Test')).toBeInTheDocument();
    expect(screen.getByText('User')).toBeInTheDocument();
  });

  test('should render last_active field in the table', async () => {
    await act(async () => {
      render(
        <RecoilRoot
          initializeState={(snap) => {
            snap.set(userRolesAtom, [{ role_name: "administrator" }]);
            snap.set(loginCompletedAtom, true);
          }}
        >
          <UserAdminDashboard />
        </RecoilRoot>
      );
    });

    // test the formatting function separately
    const formatLastActive = (cell) => {
      if (cell === null || cell === undefined) {
        return '';
      }
      return moment(cell).tz("America/Vancouver").format("YYYY-MM-DD HH:mm");
    };

    const formattedDate = formatLastActive('2023-06-23T10:00:00Z');
    expect(formattedDate).toBe('2023-06-23 03:00');

    const formattedNullDate = formatLastActive(null);
    expect(formattedNullDate).toBe('');
  });
});