import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const FormStatisticsApi = {
  getStatistics: async function () {
    const headers = {
      ...await createRequestHeader(),
    };
    return await api
      .request({
        url: "/api/v1/forms/statistics", // Adjust this to match your API endpoint
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