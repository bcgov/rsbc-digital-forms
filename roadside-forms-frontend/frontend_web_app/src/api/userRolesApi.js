import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const UserRolesApi = {
  get: async function () {
    const headers = {
      ...await createRequestHeader(),
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

  post: async function (data) {
    const headers = {
      ...await createRequestHeader(),
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
