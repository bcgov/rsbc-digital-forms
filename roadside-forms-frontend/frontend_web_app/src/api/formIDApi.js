import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const FormIDApi = {
  post: async function (data) {
    const headers = {
      ...createRequestHeader(),
    };

    const response = await api
      .request({
        url: "/api/v1/forms",
        method: "POST",
        headers: { ...headers },
        data: JSON.stringify(data),
      })
      .catch(function (error) {
        console.log(error.toJSON());
      });

    return response.data;
  },

  get: async function () {
    const headers = {
      ...createRequestHeader(),
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
      ...createRequestHeader(),
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
