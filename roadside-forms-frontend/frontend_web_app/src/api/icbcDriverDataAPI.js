import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const ICBCDriverDataApi = {
  get: async function (driver_licence_no) {
    const headers = {
      ...await createRequestHeader(),
    };
    return await api
      .request({
        url: `/api/v1/icbc/drivers/${driver_licence_no}`,
        method: "GET",
        headers: { ...headers },
      })
      .then((response) => {
        return {
          status: "success",
          data: response.data,
        };
      })
      .catch((error) => {
        return {
          status: "error",
          data: error.response,
        };
      });
  },
};
