import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const StaticDataApi = {
  get: async function (resource) {
    const headers = {
      ...await createRequestHeader(),
    };
    return await api
      .request({
        url: `/api/v1/static/${resource}`,
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
};
