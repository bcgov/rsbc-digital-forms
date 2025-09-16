import {createRequestHeader} from '../../utils/requestHeaders';
import keycloak from '../../keycloak';

jest.mock('../../keycloak', () => ({
  updateToken: jest.fn(),
  token: 'token'
}));

describe('requestHeaders', () => {
  test('should return the header with authentication token if success', async () => {
    const header =  await createRequestHeader();

    expect(header).toEqual({
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
      credentials: "same-origin",
      Authorization: 'Bearer token'
    });
  });

  test('should return base header if token refresh fails', async () => {
    keycloak.updateToken.mockRejectedValue(false);

    const header =  await createRequestHeader();

    expect(header).toEqual({
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
      credentials: "same-origin"
    });
  })
});