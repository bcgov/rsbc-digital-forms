import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const ICBCVehicleDataApi = {
  get: async function (licencePlate) {
    const headers = {
      ...await createRequestHeader(),
    };
    return await api
      .request({
        url: `/api/v1/icbc/vehicles/${licencePlate}`,
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
