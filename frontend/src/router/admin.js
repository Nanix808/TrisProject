export default [
  {
    path: '/admin',
    name: 'admin',
    component: () => import('../views/admin/HomeAdmin.vue'),
    meta: {
      layout: 'AdminLayout',
    },
  },
  {
    path: '/admin/users',
    name: 'users',
    component: () => import('../views/admin/UsersAdmin.vue'),
    meta: {
      layout: 'AdminLayout',
    },
    props: true,
    children: [
      {
        path: '',
        name: 'admin_users',
        component: () => import('../views/admin/users/GetUsersAdmin.vue'),
      },
      {
        path: 'roles',
        name: 'admin_roles',
        component: () => import('../views/admin/users/GetRoleAdmin.vue'),
      },
      {
        path: 'permissions',
        name: 'admin_permissions',
        component: () => import('../views/admin/users/GetPermissionsAdmin.vue'),
      },
    ],
  },
  {
    path: '/admin/transport',
    name: 'admin_transport',
    component: () => import('../views/admin/TransportAdmin.vue'),
    meta: {
      layout: 'AdminLayout',
    },
    props: true,
    children: [
      {
        path: '',
        name: 'admin_cars',
        component: () =>
          import('../views/admin/transport/GetTransportAdmin.vue'),
      },
      {
        path: '',
        name: 'admin_users1',
        // component: () => import('../views/admin/users/GetUsersAdmin.vue'),
      },
    ],
  },
  {
    path: '/admin/statistics',
    name: 'statistics',
    component: () => import('../views/admin/StatisticsAdmin.vue'),
    meta: {
      layout: 'AdminLayout',
    },
  },
];
