import * as authRoutes from "./auth.js";
import * as userRoutes from "./users.js";
import AdminApi from "./admin";

export const UrlApi = {
  authRoutes,
  userRoutes,
};

export const AdminUrlApi = {
  ...AdminApi,
};
