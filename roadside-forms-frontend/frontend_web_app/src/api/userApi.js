import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const UserApi = {

    getAll: async function () {
        const headers = {
          ...createRequestHeader(),
        };
        return await api.request({
          url: "/api/v1/admin/users",
          method: "GET",
          headers:{...headers},
        }).then ( (response) => {
          return {
              status: response.status,
              data: response.data
          }
      }).catch((error) =>{
          return {
              status: error.status,
              data: error.response
          }
      })
      },
      delete: async function (data) {
        const headers = createRequestHeader();
          return await api.request({
            url: `/api/v1/admin/users/${data.user_guid}/roles/${data.role_name}`,
            method: "DELETE",
            headers:{...headers},
          }).then ( (response) => {
            return {
                status: response.status,
                data: response.data
            }
        }).catch((error) =>{
            // console.log(error)
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
          url: `/api/v1/users/${userId}`,
          method: "GET",
          headers:{...headers},
        }).then ( (response) => {
          return {
              status: response.status,
              data: response.data
          }
      }).catch((error) =>{
          // console.log(error)
          return {
              status: error.status,
              data: error.response
          }
      })
      },
    post: async function (data) {
      const headers = createRequestHeader();
        return await api.request({
          url: "/api/v1/users",
          method: "POST",
          headers:{...headers},
          data: {...data},
        }).then ( (response) => {
          return {
              status: response.status,
              data: response.data
          }
      }).catch((error) =>{
          // console.log(error)
          return {
              status: error.status,
              data: error.response
          }
      })
  
      },
      patch: async function (data) {
        const headers = createRequestHeader();
          return await api.request({
            url: `/api/v1/admin/users/${data.user_guid}/roles/officer`,
            method: "PATCH",
            headers:{...headers},
          }).then ( (response) => {
            return {
                status: response.status,
                data: response.data
            }
        }).catch((error) =>{
            // console.log(error)
            return {
                status: error.status,
                data: error.response
            }
        })
        },
        postAdmin: async function (data) {
          const headers = createRequestHeader();
            return await api.request({
              url: `/api/v1/admin/users/${data.user_guid}/roles`,
              method: "POST",
              data: {"role_name": "administrator"},
              headers:{...headers},
            }).then ( (response) => {
              return {
                  status: response.status,
                  data: response.data
              }
          }).catch((error) =>{
              // console.log(error)
              return {
                  status: error.status,
                  data: error.response
              }
          })
          },
};
