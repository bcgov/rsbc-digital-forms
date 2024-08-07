import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const FormSubmissionApi = {
  post: async function (data) {
    const headers = {
      ...await createRequestHeader(),
    };
    return await api
      .request({
        url: "/api/v1/event",
        method: "POST",
        headers: { ...headers },
        data: { ...data },
      })
      .then((response) => {
        return response;
      })
      .catch((error) => {
        return {
          status: error.status,
          data: error.response,
        };
      });
  },

  get: async function () {
    const headers = {
      ...await createRequestHeader(),
    };
    return await api
      .request({
        url: "/api/v1/event",
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
};
