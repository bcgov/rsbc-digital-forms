import { api} from "../../api/config/axiosConfig"
import {createRequestHeader} from '../../utils/requestHeaders'
import { cleanup } from '@testing-library/react';
import { StaticDataApi } from "../../api/staticDataApi"

jest.mock('react-oidc-context', () => ({
  ...jest.requireActual('react-oidc-context'),
  useAuth: jest.fn()
}));

jest.mock('../../utils/requestHeaders', () => ({
  createRequestHeader: jest.fn()
}));

describe("staticDataApi", () => {
    beforeEach(() => {
      cleanup();
      createRequestHeader.mockReturnValue({ 'Authorization': 'Bearer token' });
    });
    test("should return data on successful request", async () => {
      // Arrange
      const resource = "agencies";
      const expectedData = [{ 
        "vjur": "AB",
        "agency_name": "Test ag."
     },
     { 
        "vjur": "ABC",
        "agency_name": "Test ag 1."
     }];
      const expectedStatus = 200;
      const mockResponse = { status: expectedStatus, data: expectedData };
  
      // Mock the request
      api.request = jest.fn().mockResolvedValue(mockResponse);
  
      // Act
      const result = await StaticDataApi.get(resource);
  
      // Assert
      expect(api.request).toHaveBeenCalledWith({
        url: `/api/v1/static/${resource}`,
        method: "GET",
        headers: await createRequestHeader(),
      });
      expect(result).toEqual({ status: expectedStatus, data: expectedData });
    });
  
    test("should return error data on failed request", async () => {
      const resource = "agencies";
      const expectedErrorData = { message: "Example error" };
      const expectedErrorStatus = 500;
      const mockError = {
        status: expectedErrorStatus,
        response: expectedErrorData,
      };
  
      api.request = jest.fn().mockRejectedValue(mockError);
      const result = await StaticDataApi.get(resource);
  
      expect(api.request).toHaveBeenCalledWith({
        url: `/api/v1/static/${resource}`,
        method: "GET",
        headers: await createRequestHeader(),
      });
      expect(result).toEqual({
        status: expectedErrorStatus,
        data: expectedErrorData,
      });
    });
  });
  