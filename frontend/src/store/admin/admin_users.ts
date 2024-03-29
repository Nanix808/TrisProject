import { AdminUrlApi } from '@/api';
import { UsersState, User, Role } from './types';

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
        commit('setUsersArray', res.data);
      });
    },
    admin_get_all_roles({ commit }) {
      AdminUrlApi.adminUserRoutes.getRoles().then((res) => {
        commit('setRolesArray', res.data);
      });
    },
    updatedUser({ commit }, payload: any) {
      for (var user in payload) {
        let id = user;
        let userUpgradeParametrs = {};
        payload[user].forEach((element) => {
          Object.assign(userUpgradeParametrs, element);
        });

        AdminUrlApi.adminUserRoutes
          .updateUser(id, userUpgradeParametrs)
          .then((res) => {})
          .catch(() => {})
          .finally(() => {
            this.dispatch('admin_get_all_users');
          });
      }
    },

    deleteUser({ commit }, id: number) {
      AdminUrlApi.adminUserRoutes
        .deleteUser(id)
        .then((res) => {})
        .catch((error) => {})
        .finally(() => {
          this.dispatch('admin_get_all_users');
        });
    },
  },
  getters: {
    // isAuthenticatedUser: (state: User): boolean => state.email,
  },
};
