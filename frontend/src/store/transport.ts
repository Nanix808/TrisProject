import { UrlApi } from '@/api';
import { TransportState } from './types';

export default {
  state(): TransportState {
    return {
      transports: [],
      transports_without_time_to: [],
      cars: [],
    };
  },
  mutations: {
    setTransportsArray(state: TransportState, newTransports: any) {
      state.transports = [];
      (state.transports_without_time_to = []),
        newTransports.forEach((item) => {
          if (item.date_to == null) {
            state.transports_without_time_to.push(item);
          } else {
            state.transports.push(item);
          }
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
    get_transport_by_date({ commit }, payload: any) {
      UrlApi.transportRoutes
        .getTransport_by_date(payload)
        .then((res) => {
          // console.log(res.data);
          commit('setTransportsArray', res.data);
        })
        .catch((error) => {
          //   commit('cleanUsersArray');
        });
    },
    addTransport({ commit, dispatch }, payload: any) {
      UrlApi.transportRoutes
        .addTransport(payload)
        .then((res) => {
          dispatch(
            'get_transport_by_date',
            (payload = { date_in: payload.date, car_id: payload.car_id })
          );
        })
        .catch((error) => {
          commit('cleanUsersArray');
        });
    },
    editTransport({ commit, dispatch }, payload: any) {
      UrlApi.transportRoutes
        .editTransport(payload.id, payload)
        .then((res) => {
          // location.reload();
          dispatch(
            'get_transport_by_date',
            (payload = { date_in: payload.date, car_id: payload.car_id_page })
          );
          // self.get_transport_by_date({ commit }, payload);

          // commit('setTransportsArray', res.data);
        })
        .catch((error) => {
          commit('cleanUsersArray');
        });
    },
    deleteTransport({ commit, dispatch }, payload: any) {
      UrlApi.transportRoutes
        .deleteTransport(payload.id)
        .then((res) => {
          dispatch(
            'get_transport_by_date',
            (payload = { date_in: payload.date, car_id: payload.car_id_page })
          );
        })
        .catch((error) => {
          commit('cleanUsersArray');
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
