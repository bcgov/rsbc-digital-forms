import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const FormIDApi = {
  post: async function (data) {
    const headers = {
      ...await createRequestHeader(),
    };

    try {
      const response = await api
        .request({
          url: "/api/v1/forms",
          method: "POST",
          headers: { ...headers },
          data: JSON.stringify(data),
        });
      return response.data;      
    } catch (error) {
      console.log(error);
    }
    return null;
  },

  get: async function () {
    const headers = {
      ...await createRequestHeader(),
    };
    return await api
      .request({
        url: "/api/v1/forms",
        method: "GET",
        headers: { ...headers },
      })
      .then((response) => {
        return response.data;
      })
      .catch((error) => {
        return {
          status: error.status,
          data: error.response,
        };
      });
  },
  patch: async function (data) {
    const headers = {
      ...await createRequestHeader(),
    };
    return await api
      .request({
        url: "/api/v1/forms",
        method: "PATCH",
        headers: { ...headers },
        data: { ...data },
      })
      .then((response) => {
        return response.data;
      })
      .catch((error) => {
        return {
          status: error.status,
          data: error.response,
        };
      });
  },
};
