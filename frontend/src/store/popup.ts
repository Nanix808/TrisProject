interface PopapState {
  isLoginPopupOpen: boolean;
  isRegisterPopupOpen: boolean;
  isAdminUserPopupOpen: boolean;
}

export default {
  state: (): PopapState => {
    const isLoginPopupOpen = false;
    const isRegisterPopupOpen = false;
    const isAdminUserPopupOpen = false;
    return {
      isLoginPopupOpen: false,
      isRegisterPopupOpen: false,
      isAdminUserPopupOpen: false,
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
  },
};
