import { api} from '../../api/config/axiosConfig'
import {createRequestHeader} from '../../utils/requestHeaders'
import { cleanup } from '@testing-library/react';
import { FormIDApi } from '../../api/formIDApi';

jest.mock('../../utils/requestHeaders', () => ({
  createRequestHeader: jest.fn()
}));

describe('formIDApi', () => {
    beforeEach(() => {
      cleanup();
      createRequestHeader.mockReturnValue({ 'Authorization': 'Bearer token' });
    });

    test('should post data on successful request', async () => {
      // Arrange
      const expectedData = {'VI': '1234'};
      const expectedStatus = 200;
      const mockResponse = { status: expectedStatus, data: expectedData };
      const data = {'12Hour':0,'24Hour':0,'VI':1};

      // Mock the request
      api.request = jest.fn().mockResolvedValue(mockResponse);
  
      // Act
      const result = await FormIDApi.post(data);
  
      // Assert
      expect(api.request).toHaveBeenCalledWith({
        url: `/api/v1/forms`,
        method: 'POST',
        headers: await createRequestHeader(),
        data: JSON.stringify(data),
      });
      expect(result).toEqual(expectedData);
    });

    test('should return error data on failed post request', async () => {
      const postData = {'12Hour':0,'24Hour':0,'VI':1};
      const expectedErrorData = { message: 'Example error' };
      const expectedErrorStatus = 500;
      const mockError = {
        status: expectedErrorStatus,
        response: expectedErrorData,
      };
  
      api.request = jest.fn().mockRejectedValue(mockError);
      const result = await FormIDApi.post(postData);
  
      expect(api.request).toHaveBeenCalledWith({
        url: `/api/v1/forms`,
        method: 'POST',
        headers: await createRequestHeader(),
        data: JSON.stringify(postData),
      });
      expect(result).toEqual(null);
    });

    test('should return data on successful request', async () => {
      // Arrange
      const expectedData = [{formId: '1234', type: 'VI'}];
      const expectedStatus = 200;
      const mockResponse = { status: expectedStatus, data: expectedData };
  
      // Mock the request
      api.request = jest.fn().mockResolvedValue(mockResponse);
  
      // Act
      const result = await FormIDApi.get();
  
      // Assert
      expect(api.request).toHaveBeenCalledWith({
        url: `/api/v1/forms`,
        method: 'GET',
        headers: await createRequestHeader(),
      });
      expect(result).toEqual(expectedData);
    });
  
    test('should return error data on failed request', async () => {
      const resource = 'agencies';
      const expectedErrorData = { message: 'Example error' };
      const expectedErrorStatus = 500;
      const mockError = {
        status: expectedErrorStatus,
        response: expectedErrorData,
      };
  
      api.request = jest.fn().mockRejectedValue(mockError);
      const result = await FormIDApi.get(resource);
  
      expect(api.request).toHaveBeenCalledWith({
        url: `/api/v1/forms`,
        method: 'GET',
        headers: await createRequestHeader(),
      });
      expect(result).toEqual({
        status: expectedErrorStatus,
        data: expectedErrorData,
      });
    });

    test('should patch data on successful request', async () => {
      // Arrange
      const expectedStatus = 200;
      const mockResponse = { status: expectedStatus };
      const data = {'forms': {'VI_number': 123},'printed_timestamp':'2024-07-09'};

      // Mock the request
      api.request = jest.fn().mockResolvedValue(mockResponse);
  
      // Act
      const result = await FormIDApi.patch(data);
  
      // Assert
      expect(api.request).toHaveBeenCalledWith({
        url: `/api/v1/forms`,
        method: 'PATCH',
        headers: await createRequestHeader(),
        data: { ...data },
      });
      expect(result).toEqual(undefined);
    });

    test('should return error data on failed patch request', async () => {
      const data = {'forms': {'VI_number': 123},'printed_timestamp':'2024-07-09'};
      const expectedErrorData = { message: 'Example error' };
      const expectedErrorStatus = 500;
      const mockError = {
        status: expectedErrorStatus,
        response: expectedErrorData,
      };
  
      api.request = jest.fn().mockRejectedValue(mockError);
      const result = await FormIDApi.patch(data);
  
      expect(api.request).toHaveBeenCalledWith({
        url: `/api/v1/forms`,
        method: 'PATCH',
        headers: await createRequestHeader(),
        data: { ...data },
      });
      expect(result).toEqual({
        status: expectedErrorStatus,
        data: expectedErrorData,
      });
    });    
  });
  