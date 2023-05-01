import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const StaticDataApi = {

      get: async function (resource) {
        const headers = {
          ...createRequestHeader(),
        };
        return await api.request({
          url: `/static/${resource}`,
          method: "GET",
          headers:{...headers},
        }).then ( (response) => {
          console.log(response)
          return {
              status: response.status,
              data: response.data
          }
      }).catch((error) =>{
          console.log(error)
          return {
              status: error.status,
              data: error.response
          }
      })
      },
};
