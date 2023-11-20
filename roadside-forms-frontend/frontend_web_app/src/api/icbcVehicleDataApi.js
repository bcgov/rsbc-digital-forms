import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const ICBCVehicleDataApi = {
  get: async function (licencePlate) {
    const headers = {
      ...createRequestHeader(),
    };
    const response = await api.request({
      url: `/api/v1/icbc/vehicles/${licencePlate}`,
      method: "GET",
      headers: { ...headers },
    });
    console.log(response);
    return response.data;
  },
};
