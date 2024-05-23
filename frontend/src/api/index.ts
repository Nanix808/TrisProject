import * as authRoutes from './auth.js';
import * as userRoutes from './users.js';
import * as transportRoutes from './transport.js';
import AdminApi from './admin';

export const UrlApi = {
  authRoutes,
  userRoutes,
  transportRoutes,
};

export const AdminUrlApi = {
  ...AdminApi,
};
