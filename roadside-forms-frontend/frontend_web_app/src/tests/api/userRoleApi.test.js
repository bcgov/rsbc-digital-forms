import { UserRolesApi } from '../../api/userRolesApi';
import { api} from "../../api/config/axiosConfig"

test('should fetch user role info ', async () => {
  const userRolesApiData = [
    {
        approved_dt : "Thu, 22 Jun 2023 16:51:39 GMT",
        role_name: "administrator",
        submitted_dt: "Thu, 22 Jun 2023 16:51:39 GMT",
        user_guid: "91D388D1889HHGFGFHG6TF777FF7F7F7"
    },
    {
        approved_dt : "Thu, 22 Jun 2023 16:51:39 GMT",
        role_name: "officer",
        submitted_dt: "Thu, 22 Jun 2023 16:51:39 GMT",
        user_guid: "91D388D1889HHGFGFHG6TF777FF7F7F7"
    },
  ];

  const resp = { data: userRolesApiData };
  api.request = jest.fn().mockResolvedValueOnce(resp); 

  const result = await UserRolesApi.get();

  expect(result).toEqual({
    data: userRolesApiData
  });
});