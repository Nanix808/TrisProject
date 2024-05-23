import { UrlApi } from '@/api';
import { TransportState } from './types';

export default {
  state(): TransportState {
    return {
      transports: [],
    };
  },
  mutations: {
    setTransportsArray(state: TransportState, newUsers: any) {
      state.transports = [];
      newUsers.forEach((item) => {
        state.transports.push(item);
      });
    },
  },
  actions: {
    get_all_transport({ commit }) {
      UrlApi.transportRoutes
        .getTransport()
        .then((res) => {
          console.log(res.data);
          commit('setTransportsArray', res.data);
        })
        .catch((error) => {
          //   commit('cleanUsersArray');
        });
    },
  },
  getters: {
    // isAuthenticatedUser: (state: User): boolean => state.email,
  },
};
