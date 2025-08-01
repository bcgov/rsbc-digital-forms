import React from 'react';
import { render, act } from '@testing-library/react';
import { RecoilRoot } from 'recoil';
import { MemoryRouter } from 'react-router-dom';
import { Header } from "../../../components/common/Header/Header";
import { UserApi } from "../../../api/userApi";
import { UserRolesApi } from "../../../api/userRolesApi";
import { useAuth } from "react-oidc-context";
import * as connectivity from "../../../utils/connectivity";
import * as axiosConfig from "../../../api/config/axiosConfig";

jest.mock('react-oidc-context', () => ({
  useAuth: jest.fn(),
}));

jest.mock('../../../api/userApi', () => ({
  UserApi: {
    get: jest.fn(),
    updateLastActive: jest.fn(),
  },
}));

jest.mock('../../../api/userRolesApi', () => ({
  UserRolesApi: {
    get: jest.fn(),
  },
}));

jest.mock('../../../utils/connectivity', () => ({
  useSharedIsOnline: jest.fn(),
}));

jest.mock('react-router-dom', () => ({
  ...jest.requireActual('react-router-dom'),
  useNavigate: jest.fn(),
}));

jest.mock('../../../api/config/axiosConfig', () => ({
  api: {
    request: jest.fn(),
  },
}));

const HeaderWrapper = () => (
  <RecoilRoot>
    <MemoryRouter>
      <Header />
    </MemoryRouter>
  </RecoilRoot>
);

describe('Header Component - UpdateLastActive', () => {
  beforeAll(() => {
    jest.useFakeTimers();
    jest.setSystemTime(new Date("2024-01-01T00:00"));
  });

  afterAll(() => {
    jest.useRealTimers();
  });

  beforeEach(() => {
    useAuth.mockReturnValue({
      isAuthenticated: true,
      user: {
        profile: {
          identity_provider: 'idir',
          idir_user_guid: 'test-user-id'
        }
      },
      isLoading: false
    });

    UserApi.get.mockResolvedValue({
      status: 200,
      data: {
        login: 'testuser',
        agency: 'testagency'
      }
    });

    UserApi.updateLastActive.mockResolvedValue({});

    UserRolesApi.get.mockResolvedValue({
      status: 200,
      data: [{ role_name: 'officer' }]
    });

    axiosConfig.api.request.mockImplementation(({ method, url }) => {
      if (method === 'GET' && url === '/api/v1/user_roles') {
        return Promise.resolve({ status: 200, data: [{ role_name: 'officer' }] });
      }
      return Promise.resolve({ status: 200, data: {} });
    });

    connectivity.useSharedIsOnline.mockReturnValue({ isConnected: true });

    console.error = jest.fn();
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  test('calls updateLastActive immediately when userId is available', async () => {
    await act(async () => {
      render(<HeaderWrapper />);
    });

    expect(UserApi.updateLastActive).toHaveBeenCalledTimes(1);
    expect(UserApi.updateLastActive).toHaveBeenCalledWith('test-user-id');
  });

  test('calls updateLastActive every 5 minutes', async () => {
    await act(async () => {
      render(<HeaderWrapper />);
    });

    expect(UserApi.updateLastActive).toHaveBeenCalledTimes(1);

    await act(async () => {
      jest.advanceTimersByTime(5 * 60 * 1000);
    });

    expect(UserApi.updateLastActive).toHaveBeenCalledTimes(2);

    await act(async () => {
      jest.advanceTimersByTime(5 * 60 * 1000);
    });

    expect(UserApi.updateLastActive).toHaveBeenCalledTimes(3);
  });

  test('handles error when updateLastActive fails', async () => {
    UserApi.updateLastActive.mockRejectedValueOnce(new Error('API error'));

    await act(async () => {
      render(<HeaderWrapper />);
    });

    expect(console.error).toHaveBeenCalledWith(
      'Failed to update last active time:',
      expect.any(Error)
    );
  });

  test('clears interval on component unmount', async () => {
    let unmount;
    await act(async () => {
      const { unmount: componentUnmount } = render(<HeaderWrapper />);
      unmount = componentUnmount;
    });

    const clearIntervalSpy = jest.spyOn(global, 'clearInterval');

    act(() => {
      unmount();
    });

    expect(clearIntervalSpy).toHaveBeenCalledTimes(2); // Once for each interval
  });
});