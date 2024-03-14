import { AdminUrlApi } from "@/api";
import { UsersState, User, Role } from "./types";

export default {
  state(): UsersState {
    return {
      users: [],
      roles: [],
    };
  },
  mutations: {
    setUsersArray(state: UsersState, newUsers: any) {
      state.users = [];
      newUsers.forEach((item) => {
        state.users.push(item);
      });
      // console.log(res.data);
      // state.users.push(item);
    },
    setRolesArray(state: UsersState, newRole: any) {
      state.roles = [];
      newRole.forEach((item) => {
        state.roles.push(item);
      });
    },
  },
  actions: {
    admin_get_all_users({ commit }) {
      AdminUrlApi.adminUserRoutes.getUsers().then((res) => {
        commit("setUsersArray", res.data);
      });
    },
    admin_get_all_roles({ commit }) {
      AdminUrlApi.adminUserRoutes.getRoles().then((res) => {
        commit("setRolesArray", res.data);
      });
    },
  },
  getters: {
    // isAuthenticatedUser: (state: User): boolean => state.email,
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
