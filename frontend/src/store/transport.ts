import { UrlApi } from '@/api';
import { TransportState } from './types';

export default {
  state(): TransportState {
    return {
      transports: [],
      cars: [],
    };
  },
  mutations: {
    setTransportsArray(state: TransportState, newTransports: any) {
      state.transports = [];
      newTransports.forEach((item) => {
        state.transports.push(item);
      });
    },
    setCarsArray(state: TransportState, newCars: any) {
      state.cars = [];
      newCars.forEach((item) => {
        state.cars.push(item);
      });
    },
  },
  actions: {
    get_all_transport({ commit }) {
      UrlApi.transportRoutes
        .getTransport()
        .then((res) => {
          commit('setTransportsArray', res.data);
        })
        .catch((error) => {
          //   commit('cleanUsersArray');
        });
    },
    get_transport_by_date({ commit }, date) {
      UrlApi.transportRoutes
        .getTransport_by_date(date)
        .then((res) => {
          // commit('setTransportsArray', res.data);
        })
        .catch((error) => {
          //   commit('cleanUsersArray');
        });
    },
    async get_all_cars({ commit }) {
      await UrlApi.transportRoutes
        .getCars()
        .then((res) => {
          commit('setCarsArray', res.data);
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
