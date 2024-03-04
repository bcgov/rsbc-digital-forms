import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const ICBCVehicleDataApi = {
  get: async function (registrationNumber) {
    const headers = {
      ...createRequestHeader(),
    };
    return await api
      .request({
        url: `/api/v1/icbc/vehicles/${registrationNumber}`,
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
