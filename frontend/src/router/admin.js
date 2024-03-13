export default [
  {
    path: "/admin",
    name: "admin",
    component: () => import("../views/admin/HomeAdmin.vue"),
    meta: {
      layout: "AdminLayout",
    },
  },
  {
    path: "/admin/users",
    name: "users",
    component: () => import("../views/admin/UsersAdmin.vue"),
    meta: {
      layout: "AdminLayout",
    },
    children: [
      {
        path: "allusers",
        component: () => import("../views/admin/users/GetUsersAdmin.vue"),
      },
      {
        path: "roles",
        component: () => import("../views/admin/users/GetRolesAdmin.vue"),
      },
      {
        path: "permissions",
        component: () => import("../views/admin/users/GetPermissionsAdmin.vue"),
      },
    ],
  },
  {
    path: "/admin/statistics",
    name: "statistics",
    component: () => import("../views/admin/StatisticsAdmin.vue"),
    meta: {
      layout: "AdminLayout",
    },
  },
];
