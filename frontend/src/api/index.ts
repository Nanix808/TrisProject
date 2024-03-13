import { DefaultApiInstance } from "@/api/apiinstanse.js";
import * as authRoutes from "./auth.js";
import * as userRoutes from "./users.js";
import * as adminUserRoutes from "./admin/users.js";

export const UrlApi = {
  // postResume(body) {
  //     const url = '/users';
  //     return DefaultApiInstance.get(url,body)
  // },

  //  login(body) {
  //     const url = '/users';
  //     console.log(body)
  //     return DefaultApiInstance.get(url,body)
  // },
  authRoutes,
  userRoutes,
  adminUserRoutes,
};
