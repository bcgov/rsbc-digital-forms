import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const ICBCVehicleDataApi = {
  get: async function (licencePlate) {
    const headers = {
      ...createRequestHeader(),
    };
    return await api
      .request({
        url: `/api/v1/icbc/vehicles/${licencePlate}`,
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
