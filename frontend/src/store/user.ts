import { UrlApi } from '@/api';
import { UserPayload } from './types';

interface User {
  email: string;
  request_unsuccess: boolean;
}

export default {
  state: (): User => {
    const email = localStorage.getItem('accessToken') || null;
    return {
      email: '',
      request_unsuccess: false,
    };
  },
  mutations: {
    setUserName(state: User, email: string) {
      state.email = email;
    },
    request_unsuccess(state: User, success: boolean) {
      state.request_unsuccess = success;
    },
  },
  actions: {
    register({ commit }, payload: UserPayload) {
      UrlApi.userRoutes
        .createUser({
          username: payload.email,
          password_hash: payload.password,
        })
        .then((res) => {
          commit('closeRegisterPopup');
          alert(
            'Вы успешно зарегистрировались! Ожидайте пока администратор активирует вашу учетную запись'
          );
        })
        .catch(() => {
          commit('request_unsuccess', true);
        });
    },
  },
  getters: {},
};
