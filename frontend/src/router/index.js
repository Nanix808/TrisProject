import { createRouter, createWebHistory } from "vue-router";
import { loadLayoutMiddleware } from "@/router/middleware/loadLayoutMiddleware";
import HomeView from "../views/HomeView.vue";
import auth from "./auth.js";
import admin from "./admin.js";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
      meta: {
        layout: "DefaultLayout",
      },
    },
    ...auth,
    ...admin,
  ],
});

router.beforeEach(loadLayoutMiddleware);
export default router;
