import { UrlApi } from '@/api';
import { UserPayload, ILoginResponse } from './types';
import {
  isTokenExpired,
  isSuperUser,
  getIdUser,
  isPermissions,
} from '@/utils/jwt';
import { AxiosPromise } from 'axios';

interface State {
  userId: number | null;
  userName: string;
  userEmail: string;
  accessToken: string | null;
  refreshToken: string | null;
  name: string | null;
  isAuthenticated: boolean;
  isSuperUser: boolean;
  refreshTokenRequest: AxiosPromise<ILoginResponse> | null;
  permissions: any;
}

let refreshTokenRequest: any = null;

export default {
  state: (): State => {
    const accessToken = localStorage.getItem('accessToken') || null;
    const refreshToken = localStorage.getItem('refreshToken') || null;
    const isAuthenticated = localStorage.getItem('isAuthenticated') === 'true';
    const isSuperUser = localStorage.getItem('isSuperUser') === 'true';
    const name = localStorage.getItem('name');
    const refreshTokenRequest = null;
    const permissions = JSON.parse(localStorage.getItem('permissions')) || null;

    return {
      userName: '',
      userId: null,
      userEmail: '',
      accessToken,
      refreshToken,
      isAuthenticated,
      name: name || '',
      isSuperUser,
      permissions,
      // переменная для хранения запроса токена (для избежания race condition)
      refreshTokenRequest,
    };
  },
  mutations: {
    setUserName(state: any, payload: any) {
      localStorage.setItem('name', payload.email);
      state.name = payload.email;
    },
    setrefreshTokenRequest(state: any, data: any) {
      state.refreshTokenRequest = data;
    },
    setToken(state, data) {
      state.accessToken = data.access_token;
      state.refreshToken = data.refresh_token;
      state.isAuthenticated = true;
      const is_admin = isSuperUser(data.access_token);
      state.isSuperUser = is_admin;
      const permissions = isPermissions(data.access_token);
      state.permissions = permissions;
      state.userId = getIdUser(data.access_token);
      localStorage.setItem('accessToken', data.access_token);
      localStorage.setItem('isSuperUser', is_admin.toString());
      localStorage.setItem('refreshToken', data.refresh_token);
      localStorage.setItem('isAuthenticated', 'true');
      localStorage.setItem('permissions', JSON.stringify(permissions));
    },
  },

  actions: {
    setUser({ commit }, payload: UserPayload) {
      commit('setUSER', payload);
    },

    login({ commit }, payload: UserPayload) {
      UrlApi.authRoutes
        .login({ username: payload.email, password: payload.password })
        .then((res) => {
          commit('setUserName', payload);
          commit('setToken', res.data);
          commit('closeLoginPopup', res.data);
        })
        .catch(() => {
          commit('request_unsuccess', true);
        });
    },

    async getAccessToken({ commit, state }) {
      try {
        const accessToken = localStorage.getItem('accessToken');
        if (!accessToken || isTokenExpired(accessToken)) {
          if (state.refreshTokenRequest === null) {
            // state.refreshTokenRequest = UrlApi.authRoutes.refresh();
            commit('setrefreshTokenRequest', UrlApi.authRoutes.refresh());
          }
          const res = await state.refreshTokenRequest;

          commit('setToken', res.data);
          commit('setrefreshTokenRequest', null);
          // refreshTokenRequest = null;
          return res.data.access_token;
        }
        return accessToken;
      } catch (error) {
        commit('setrefreshTokenRequest', null);
        return null;
      }
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
