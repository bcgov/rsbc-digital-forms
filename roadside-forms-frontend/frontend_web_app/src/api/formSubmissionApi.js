import { api } from "./config/axiosConfig";
import { createRequestHeader } from "../utils/requestHeaders";

export const FormSubmissionApi = {

    post: async function (data) {
      const headers = {
        ...createRequestHeader(),
      };
      console.log(data)
        const response = await api.request({
          url: "/api/v1/event",
          method: "POST",
          headers: {...headers},
          data: {...data},
        })
        console.log(response)
        return response.json()
      },
};