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
  mutations: {
    setUsersArray(state: UsersState, newUsers: any) {
      state.users = [];
      newUsers.forEach((item) => {
        state.users.push(item);
      });
    },
    cleanUsersArray(state: UsersState, newUsers: any) {
      state.users = [];
    },
    setRolesArray(state: UsersState, newRole: any) {
      state.roles = [];
      newRole.forEach((item) => {
        state.roles.push(item);
      });
    },
    cleanRolesArray(state: UsersState, newRole: any) {
      state.roles = [];
    },
    setEndpointsArray(state: UsersState, newEndpoint: any) {
      state.list_endpoints = newEndpoint;

      // for (let key in newEndpoint) {
      //   if (newEndpoint.hasOwnProperty(key)) {
      //     console.log(`${key} : ${newEndpoint[key]}`);
      //   }

      // newEndpoint.forEach((item) => {
      //   state.list_endpoints.push(item);
      // });
      // }
    },
    cleanEndpointsArray(state: UsersState, newEndpoint: any) {
      state.list_endpoints = [];
    },
  },
  actions: {
    admin_get_all_users({ commit }) {
      AdminUrlApi.adminUserRoutes
        .getUsers()
        .then((res) => {
          commit('setUsersArray', res.data);
        })
        .catch((error) => {
          commit('cleanUsersArray');
        });
    },
    admin_get_all_roles({ commit }) {
      AdminUrlApi.adminUserRoutes
        .getRoles()
        .then((res) => {
          commit('setRolesArray', res.data);
        })
        .catch((error) => {
          commit('cleanRolesArray');
        });
    },
    admin_get_all_endpoints({ commit }) {
      AdminUrlApi.adminUserRoutes
        .getEndpoints()
        .then((res) => {
          commit('setEndpointsArray', res.data);
        })
        .catch((error) => {
          commit('cleanEndpointsArray');
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
    addRole({ commit, dispatch }, payload) {
      AdminUrlApi.adminUserRoutes
        .adminaddRole(payload)
        .then((res) => {
          dispatch('admin_get_all_roles');

          // commit('setEndpointsArray', res.data);
        })
        .catch((error) => {
          // commit('cleanEndpointsArray');
        });
    },
    updateRole({ commit, dispatch }, payload) {
      AdminUrlApi.adminUserRoutes
        .adminupdateRole(payload.id, payload)
        .then((res) => {
          dispatch('admin_get_all_roles');

          // commit('setEndpointsArray', res.data);
        })
        .catch((error) => {
          // commit('cleanEndpointsArray');
        });
    },

    deleteRole({ commit, dispatch }, id: number) {
      AdminUrlApi.adminUserRoutes
        .deleteRole(id)
        .then((res) => {})
        .catch((error) => {})
        .finally(() => {
          dispatch('admin_get_all_roles');
        });
    },
  },
  getters: {},
};
