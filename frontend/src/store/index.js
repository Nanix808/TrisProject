import { createStore } from 'vuex';
import auth from './auth';
import user from './user';
import popup from './popup';
import transport from './transport';
import admin_modules from './admin';

const store = createStore({
  modules: {
    auth: auth,
    user: user,
    popup: popup,
    transport: transport,
    ...admin_modules,
  },
});

export default store;
