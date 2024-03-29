interface PopapState {
  isLoginPopupOpen: boolean;
  isRegisterPopupOpen: boolean;
  isAdminUserPopupOpen: boolean;
  isAdminRolePopupOpen: boolean;
}

export default {
  state: (): PopapState => {
    const isLoginPopupOpen = false;
    const isRegisterPopupOpen = false;
    const isAdminUserPopupOpen = false;
    const isAdminRolePopupOpen = false;
    return {
      isLoginPopupOpen: false,
      isRegisterPopupOpen: false,
      isAdminUserPopupOpen: false,
      isAdminRolePopupOpen: false,
    };
  },
  mutations: {
    openLoginPopup(state: PopapState) {
      state.isLoginPopupOpen = true;
    },
    closeLoginPopup(state: PopapState) {
      state.isLoginPopupOpen = false;
    },
    openRegisterPopup(state: PopapState) {
      state.isRegisterPopupOpen = true;
    },
    closeRegisterPopup(state: PopapState) {
      state.isRegisterPopupOpen = false;
    },
    openAdminUserPopup(state: PopapState) {
      state.isAdminUserPopupOpen = true;
    },
    closeAdminUserPopup(state: PopapState) {
      state.isAdminUserPopupOpen = false;
    },
    openAdminRolePopup(state: PopapState) {
      state.isAdminRolePopupOpen = true;
    },
    closeAdminRolePopup(state: PopapState) {
      state.isAdminRolePopupOpen = false;
    },
  },
};
