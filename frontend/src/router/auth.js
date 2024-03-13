export default [
  {
    path: "/about",
    name: "about",
    component: () => import("../views/AboutView.vue"),
    meta: {
      layout: "DefaultLayout",
    },
  },
];
