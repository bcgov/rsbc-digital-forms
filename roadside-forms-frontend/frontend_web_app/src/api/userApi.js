import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const UserApi = {

    getAll: async function () {
        const headers = {
          ...createRequestHeader(),
        };
        return await api.request({
          url: "/users",
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
      get: async function (userId) {
        const headers = {
          ...createRequestHeader(),
        };
        return await api.request({
          url: `/users/${userId}`,
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
    post: async function (data) {
      const headers = createRequestHeader();
        return await api.request({
          url: "/users",
          method: "POST",
          headers:{...headers},
          data: {...data},
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
