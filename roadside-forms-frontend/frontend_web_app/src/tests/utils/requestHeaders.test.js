import {createRequestHeader} from '../../utils/requestHeaders';

describe('requestHeaders', () => {
  test('should return the header with authentication token if success', async () => {
    const now = Date.now() / 1000;
    const auth = { 
      user: {
        access_token: 'token',
        expires_at: now + 3600
      }
    }
    const header =  await createRequestHeader({}, auth);

    expect(header).toEqual({
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
      credentials: "same-origin",
      Authorization: 'Bearer token'
    });
  });

  test('should return base header if token refresh fails', async () => {
    const now = Date.now() / 1000;
    const auth = { 
      user: {
        access_token: 'token',
        expires_at: now - 3600
      },
      signinSilent: jest.fn().mockRejectedValue(new Error('Token refresh failed'))
    }
    const header =  await createRequestHeader({}, auth);

    expect(header).toEqual({
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
      credentials: "same-origin"
    });
  })
});