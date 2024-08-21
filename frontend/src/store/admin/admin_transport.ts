import { AdminUrlApi } from '@/api';
import { UsersState, User, Role } from './types';

export default {
  state(): UsersState {
    return {
      users: [],
      roles: [],
      list_endpoints: {},
    };
  },
  mutations: {},
  actions: {
    async addCar({ commit, dispatch }, payload: any) {
      await AdminUrlApi.adminTransportRoutes
        .addCar(payload)
        .then((res) => {
          dispatch('get_all_cars');
        })
        .catch((error) => {
        });
    },
    async updateCar({ commit, dispatch }, payload: any) {
      await AdminUrlApi.adminTransportRoutes
        .updateCar(payload.id, payload)
        .then((res) => {
          dispatch('get_all_cars');
        })
        .catch((error) => {
        });
    },
    deleteCar({ commit, dispatch }, id: number) {
      AdminUrlApi.adminTransportRoutes
        .deleteCar(id)
        .then((res) => {})
        .catch((error) => {})
        .finally(() => {
          dispatch('get_all_cars');
        });
    },
  },
  getters: {},
};
