import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const FormIDApi = {
  post: async function (data) {
    const headers = {
      ...createRequestHeader(),
    };

    const response = await api.request({
      url: "/api/v1/forms",
      method: "POST",
      headers: { ...headers },
      data: JSON.stringify(data),
    });

    return response.data;
  },

  get: async function () {
    const headers = {
      ...createRequestHeader(),
    };
    const response = await api.request({
      url: "/api/v1/forms",
      method: "GET",
      headers: { ...headers },
    });
    return response.data;
  },
  patch: async function (data) {
    const headers = {
      ...createRequestHeader(),
    };
    const response = await api.request({
      url: "/api/v1/forms",
      method: "PATCH",
      headers: { ...headers },
      data: { ...data },
    });
    return response.data;
  },
};
