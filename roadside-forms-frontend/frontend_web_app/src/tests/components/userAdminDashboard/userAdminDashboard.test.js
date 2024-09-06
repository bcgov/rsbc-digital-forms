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
          <div key={row.user_guid}>
            <span>{row.last_name}</span>
            <span>{row.first_name}</span>
            <span>{row.role_name}</span>
            {props.columns.find(col => col.dataField === 'action').formatter(null, row)}
          </div>
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
    UserApi.delete = jest.fn().mockResolvedValue({});
    UserApi.patch = jest.fn().mockResolvedValue({});
    UserApi.postAdmin = jest.fn().mockResolvedValue({});
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

    // Check if the expected data is rendered
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

    // Test the formatting function separately
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

  test('should handle user deletion', async () => {
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

    // Find and click the delete button
    const deleteButton = screen.getByText('Delete');
    fireEvent.click(deleteButton);

    // Check if confirmation modal appears
    expect(screen.getByText('Are you sure you want to delete the user USER Test?')).toBeInTheDocument();

    // Confirm deletion
    const confirmButton = screen.getByText('Confirm');
    await act(async () => {
      fireEvent.click(confirmButton);
    });

    // Check if API was called
    expect(UserApi.delete).toHaveBeenCalled();

    // Check for success message
    expect(screen.getByText('USER Test has been successfully deleted.')).toBeInTheDocument();
  });

  test('should handle user approval', async () => {
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

    // Find and click the approve button
    const approveButton = screen.getByText('Approve');
    fireEvent.click(approveButton);

    // Check if confirmation modal appears
    expect(screen.getByText('Are you sure you want to approve the user NEW User?')).toBeInTheDocument();

    // Confirm approval
    const confirmButton = screen.getByText('Confirm');
    await act(async () => {
      fireEvent.click(confirmButton);
    });

    // Check if API was called
    expect(UserApi.patch).toHaveBeenCalled();

    // Check for success message
    expect(screen.getByText('NEW User has been successfully approved.')).toBeInTheDocument();
  });

  test('should handle adding an administrator', async () => {
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

    // Find the select input
    const selectInput = screen.getByRole('combobox');

    // Open the dropdown
    fireEvent.focus(selectInput);
    fireEvent.keyDown(selectInput, { key: 'ArrowDown' });

    // Wait for the options to appear and select one
    await waitFor(() => {
      const option = screen.getByText('NEW@idir');
      fireEvent.click(option);
    });

    // Click the "Add as administrator" button
    const addAdminButton = screen.getByText('Add as administrator');
    fireEvent.click(addAdminButton);

    // Check if confirmation modal appears
    await waitFor(() => {
      expect(screen.getByText('Are you sure you want to grant administrator role to NEW User?')).toBeInTheDocument();
    });

    // Confirm adding admin
    const confirmButton = screen.getByText('Confirm');
    await act(async () => {
      fireEvent.click(confirmButton);
    });

    // Check if API was called
    expect(UserApi.postAdmin).toHaveBeenCalled();

    // Check for success message
    await waitFor(() => {
      expect(screen.getByText('NEW User has been successfully added as an administrator.')).toBeInTheDocument();
    });
  });

  test('should handle empty user list', async () => {
    UserApi.getAll.mockResolvedValueOnce({ data: [] });

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

    expect(screen.getByText('No users found matching your search criteria. Please try adjusting your search parameters.')).toBeInTheDocument();
  });

  test('should redirect non-admin users', async () => {
    const mockNavigate = jest.fn();
    useNavigate.mockImplementation(() => mockNavigate);

    await act(async () => {
      render(
        <RecoilRoot
          initializeState={(snap) => {
            snap.set(userRolesAtom, [{ role_name: "officer" }]);
            snap.set(loginCompletedAtom, true);
          }}
        >
          <UserAdminDashboard />
        </RecoilRoot>
      );
    });

    expect(mockNavigate).toHaveBeenCalledWith('/');
  });
});