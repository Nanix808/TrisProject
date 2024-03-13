interface UserPayload {
  isLoginPopupOpen: boolean;
}

export default {
  state: (): UserPayload => {
    const isLoginPopupOpen = false;
    return {
      isLoginPopupOpen: false,
    };
  },
  mutations: {
    openLoginPopup(state: any) {
      state.isLoginPopupOpen = true;
    },
    closeLoginPopup(state: any) {
      state.isLoginPopupOpen = false;
    },
  },
  // actions: {
  //   getUsers({commit}) {
  //         UrlApi.userRoutes.getUsers().then((res) => {
  //             console.log(res.data)

  //         }).catch(() => {

  //             }
  //         )

  //     },

  // },
  // getters: {
  //    isAuthenticated: (state: State): boolean => state.isAuthenticated,
  // }
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
