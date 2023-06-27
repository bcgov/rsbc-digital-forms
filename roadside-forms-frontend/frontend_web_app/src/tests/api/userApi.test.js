
import { UserApi } from '../../api/userApi';
import { api} from "../../api/config/axiosConfig"
import { cleanup } from '@testing-library/react';
import {createRequestHeader} from '../../utils/requestHeaders'

jest.mock('../../utils/requestHeaders', () => ({
    createRequestHeader: jest.fn()
  }));
describe('UserApi Testing', () => {
  beforeEach(() => {
    // Reset the mock for createRequestHeader before each test
    createRequestHeader.mockClear();
  });
  beforeEach(cleanup);
  test('should fetch user info based on userId', async () => {
    const userApiData = [
      {
        agency: "BCHP Burnaby",
        badge_number: "222222",
        display_name: "Test, user",
        first_name: "USER",
        last_name: "Test",
        login: "TEST@idir",
        user_guid: "91D388D1339C41388E622F5",
        username: "91d388d1339c41388e622f5@idir",
      },
    ];

    const resp = { data: userApiData };
    api.request = jest.fn().mockResolvedValueOnce(resp); 

    const result = await UserApi.get('91D388D1889C41388E622F5');

    expect(result).toEqual({
      data: userApiData
    });
  });

  test('should fetch user list', async () => {
      const userApiData = [
        {
          agency: "BCHP Burnaby",
          approved_dt: "Thu, 22 Jun 2023 16:51:39 GMT",
          badge_number: "222222",
          display_name: "Test, user",
          first_name: "USER",
          last_name: "Test",
          login: "TEST@idir",
          role_name: "administrator",
          submitted_dt: "Thu, 22 Jun 2023 16:51:39 GMT",
          user_guid: "91D388D1339C41388E622F5",
          username: "91d388d1339c41388e622f5@idir",
        },
        {
          agency: "BCHP Burnaby",
          approved_dt: "Thu, 22 Jun 2023 16:51:39 GMT",
          badge_number: "222222",
          display_name: "Test, user",
          first_name: "USER",
          last_name: "Test",
          login: "TEST@idir",
          role_name: "officer",
          submitted_dt: "Thu, 22 Jun 2023 16:51:39 GMT",
          user_guid: "91D388D1339C41388E622F5",
          username: "91d388d1339c41388e622f5@idir",
        }
      ];
    
      const resp = { data: userApiData };
      api.request = jest.fn().mockResolvedValueOnce(resp); 
    
      const result = await UserApi.getAll();
    
      expect(result).toEqual({
        data: userApiData
      });
    });

  test('should return successful response', async () => {
      // Mock the createRequestHeader function
      createRequestHeader.mockReturnValueOnce({ 'Authorization': 'Bearer token' });

      // Mock the response
      const mockResponse = {
        status: 200,
        data: { message: 'Success' }
      };
      const mockRequest = jest.fn().mockResolvedValueOnce(mockResponse);
      api.request = mockRequest;

      // Call the post function with sample data
      const data = {
                  last_name: 'Test',
                  first_name: 'Test',
                  agency:'police',
                  badge_number:'123456'
                };
      const result = await UserApi.post(data);

      // Assert the expected behavior
      expect(createRequestHeader).toHaveBeenCalledTimes(1);
      expect(api.request).toHaveBeenCalledTimes(1);
      expect(api.request).toHaveBeenCalledWith({
        url: '/api/v1/users',
        method: 'POST',
        headers: { 'Authorization': 'Bearer token' },
        data: data,
      });
      expect(result).toEqual({
        status: 200,
        data: { message: 'Success' }
      });
    });

    test('should return error response for POST call', async () => {
      createRequestHeader.mockReturnValueOnce({ 'Authorization': 'Bearer token' });

      const mockErrorResponse = {
        status: 404,
        response: { message: 'Not found' }
      };
      const mockRequest = jest.fn().mockRejectedValueOnce(mockErrorResponse);
      api.request = mockRequest;

      const data = { 
          last_name: 'Test',
          first_name: 'Test',
          agency:'police',
          badge_number:'123456'
      };
      const result = await UserApi.post(data);

      expect(createRequestHeader).toHaveBeenCalledTimes(1);
      expect(api.request).toHaveBeenCalledTimes(1);
      expect(api.request).toHaveBeenCalledWith({
        url: '/api/v1/users',
        method: 'POST',
        headers: { 'Authorization': 'Bearer token' },
        data: data,
      });
      expect(result).toEqual({
        status: 404,
        data: { message: 'Not found' }
      });
    });

    test('should return successful response for DELETE call', async () => {
      createRequestHeader.mockReturnValueOnce({ 'Authorization': 'Bearer token' });

      const mockResponse = {
        status: 204,
        data: null
      };
      const mockRequest = jest.fn().mockResolvedValueOnce(mockResponse);
      api.request = mockRequest;

      const data = {
        user_guid: 'user-guid',
        role_name: 'role-name'
      };
      const result = await UserApi.delete(data);

      expect(createRequestHeader).toHaveBeenCalledTimes(1);
      expect(api.request).toHaveBeenCalledTimes(1);
      expect(api.request).toHaveBeenCalledWith({
        url: '/api/v1/admin/users/user-guid/roles/role-name',
        method: 'DELETE',
        headers: { 'Authorization': 'Bearer token' },
      });
      expect(result).toEqual({
        status: 204,
        data: null
      });
    });
});


