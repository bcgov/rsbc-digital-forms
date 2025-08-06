import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const UserRolesApi = {
  get: async function (auth = null) {
    const headers = {
      ...await createRequestHeader({}, auth),
    };
    return await api
      .request({
        url: "/api/v1/user_roles",
        method: "GET",
        headers: { ...headers },
      })
      .then((response) => {
        return {
          status: response.status,
          data: response.data,
        };
      })
      .catch((error) => {
        return {
          status: error.status,
          data: error.response,
        };
      });
  },

  post: async function (data, auth = null) {
    const headers = {
      ...await createRequestHeader({}, auth),
    };
    const response = await api.request({
      url: "/api/v1/user_roles",
      method: "POST",
      headers: { ...headers },
      data: { ...data },
    });

    return response.json();
  },
};
