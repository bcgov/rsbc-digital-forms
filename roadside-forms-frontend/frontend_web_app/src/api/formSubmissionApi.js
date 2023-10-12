import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const FormSubmissionApi = {
  post: async function (data) {
    const headers = {
      ...createRequestHeader(),
    };
    const response = await api.request({
      url: "/api/v1/event",
      method: "POST",
      headers: { ...headers },
      data: { ...data },
    });
    console.log(response);
    return response;
  },

  get: async function () {
    const headers = {
      ...createRequestHeader(),
    };
    const response = await api.request({
      url: "/api/v1/event",
      method: "GET",
      headers: { ...headers },
    });
    console.log(response);
    return response;
  },
};
