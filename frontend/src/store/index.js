import { createStore } from "vuex";
import auth from "./auth";
import user from "./user";
import popup from "./popup";

const store = createStore({
  modules: {
    auth: auth,
    user: user,
    popup: popup,
  },
});

export default store;
