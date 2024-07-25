import { createRouter, createWebHistory } from 'vue-router';
import { loadLayoutMiddleware } from '@/router/middleware/loadLayoutMiddleware';
import HomeView from '../views/HomeView.vue';
// import auth from './auth.js';
import admin from './admin.js';
import { useStore } from 'vuex';
import store from '@/store/index.js';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: {
        layout: 'DefaultLayout',
      },
    },
    {
      path: '/transport',
      name: 'transport',
      component: () => import('@/views/TransportView.vue'),
      meta: {
        layout: 'DefaultLayout',
      },
    },
    // ...auth,
    ...admin,
  ],
});

router.beforeEach(loadLayoutMiddleware);

router.beforeEach((to, from, next) => {
  if (to.fullPath.split('/')[1] === 'admin') {
    store.dispatch('checkUserActivityAdmin');
  } else {
    store.dispatch('checkUserActivity');
  }
  next();
});
export default router;
