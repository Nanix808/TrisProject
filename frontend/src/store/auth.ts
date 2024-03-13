import { UrlApi } from "@/api";
import { UserPayload } from "./types";

interface State {
  userName: string;
  userEmail: string;
  accessToken: string | null;
  refreshToken: string | null;
  isAuthenticated: boolean;
}


export default {
  state: (): State => {
    const accessToken = localStorage.getItem("accessToken") || null;
    const refreshToken = localStorage.getItem("refreshToken") || null;
    const isAuthenticated = localStorage.getItem("isAuthenticated") === "true";
    return {
      userName: "",
      userEmail: "",
      accessToken,
      refreshToken,
      isAuthenticated,
    };
  },
  mutations: {
    setUserName(state: any, payload: any) {
      state.name = payload.email;
    },
    setToken(state, data) {
      state.accessToken = data.access_token;
      state.refreshToken = data.refresh_token;
      state.isAuthenticated = true;
      localStorage.setItem("accessToken", data.access_token);
      localStorage.setItem("refreshToken", data.refresh_token);
      localStorage.setItem("isAuthenticated", "true");
    },
  },
  actions: {
    setUser({ commit }, payload: UserPayload) {
      commit("setUSER", payload);
    },

    login({ commit }, payload: UserPayload) {
      UrlApi.authRoutes
        .login({ username: payload.email, password: payload.password })
        .then((res) => {
          commit("setUserName", payload);
          commit("setToken", res.data);
        });
      // .catch(() => {
      //         commit('showModal', "Вы ввели неправильное имя и пароль", {root: true})
      //     }
      // )
    },
  },
  getters: {
    isAuthenticated: (state: State): boolean => state.isAuthenticated,
  },
};

//   import {AuthApi} from '@/_api';
// import {DefaultApiInstance} from "@/_api/apiinstanse";
// // import config from "vue/src/core/config";
// // import {AxiosRequestConfig} from "axios";

// export const authModule = {
//     namespaced: true,
//     state() {
//         return {
//             token: {
//                 access: localStorage.getItem('token_access') || null,
//                 // refresh: localStorage.getItem('token_refresh') || null,

//             },
//             authUser: localStorage.getItem('authUser') || '',
//         }
//     },

//     mutations: {
//         setToken(state, data) {
//             state.token.access = data.auth_token
//             state.authUser = true
//             localStorage.setItem('token_access', data.auth_token)
//             localStorage.setItem('authUser', true)

//         },

//         delToken(state) {

//             state.token.access = null
//             state.authUser = false
//             localStorage.setItem('token_access', null)
//             localStorage.setItem('authUser', '')
//         }
//     },

//     actions: {
//         login({commit}, {login, password}) {
//             AuthApi.login(login, password).then((res) => {
//                 commit('setToken', res.data);
//                 DefaultApiInstance.interceptors.request.use(function (AxiosRequestConfig) {
//                     AxiosRequestConfig.headers['Authorization'] = `Token ${res.data.auth_token}`
//                     return AxiosRequestConfig
//                 })

//             }).catch(() => {
//                     commit('showModal', "Вы ввели неправильное имя и пароль", {root: true})
//                 }
//             )

//         },

//         logout({commit}) {

//             AuthApi.logout().then(() => {
//                 commit('delToken');

//             }).catch(() => {
//                     commit('showModal', "Вы вышли из системы", {root: true})
//                 }
//             )

//         },

//     },

// }
