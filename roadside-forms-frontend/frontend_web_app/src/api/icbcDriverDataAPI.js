import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const ICBCDriverDataApi = {
  get: async function (driver_licence_no) {
    const headers = {
      ...createRequestHeader(),
    };
    return await api
      .request({
        url: `/api/v1/icbc/drivers/${driver_licence_no}`,
        method: "GET",
        headers: { ...headers },
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
};
