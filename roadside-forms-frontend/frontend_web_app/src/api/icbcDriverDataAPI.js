import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const ICBCDriverDataApi = {
  get: async function (driver_licence_no) {
    const headers = {
      ...createRequestHeader(),
    };
    const response = await api.request({
      url: `/api/v1/icbc/drivers/${driver_licence_no}`,
      method: "GET",
      headers: { ...headers },
    });
    console.log(response);
    return response;
  },
};
