import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const UserRolesApi = {

    getAll: async function () {
      const headers = {
        ...createRequestHeader(),
      };
        const response = await api.request({
          url: "/user_roles",
          method: "GET",
          headers,
        })
    
        return response.json()
      },

    post: async function (data) {
      const headers = {
        ...createRequestHeader(),
      };
        const response = await api.request({
          url: "/user_roles",
          method: "POST",
          headers,
          data: {...data},
        })
    
        return response.json()
      },
};