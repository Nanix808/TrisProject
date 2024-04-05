<template>
  <div class="header__container">
    <!-- <span @click="/admin">Admin</span> -->
    <div>
      <div class="main_home">
        <router-link to="/"
          ><img src="@/assets/image/logo.jpg" alt=""
        /></router-link>
      </div>
    </div>
    <div class="login_block">
      <div
        class="login"
        :class="{ is_login: store.state.auth.isAuthenticated }"
        @click="store.commit('openLoginPopup')"
      ></div>
      <div class="admin" v-if="store.state.auth.isSuperUser">
        <router-link to="/admin"></router-link>
      </div>

      <LoginPopUP
        :isOpen="store.state.popup.isLoginPopupOpen"
        @close="store.commit('closeLoginPopup')"
      />
      <RegisterPopUP
        :isOpen="isRegisterPopupOpen"
        @close="store.commit('closeRegisterPopup')"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import LoginPopUP from '@/components/auth/LoginPopUp.vue';
import RegisterPopUP from '@/components/auth/RegisterPopUp.vue';
import { useStore } from 'vuex';

const store = useStore();
const isLoginPopupOpen = computed(() => store.state.popup.isLoginPopupOpen);
const isRegisterPopupOpen = computed(
  () => store.state.popup.isRegisterPopupOpen
);
// && !store.state.user.registerSuccess

// function closeLoginPopup() {
//     store.commit('closeLoginPopup');
// }
// function openLoginPopup() {
//     store.commit('openLoginPopup');
// }

// function closeRegisterPopup() {
//     store.commit('closeRegisterPopup');
// }
// function openRegisterPopup() {

//     return store.state.popup.isRegisterPopupOpen && !store.state.user.registerSuccess
//     store.commit('openRegisterPopup');
// }
</script>

<style lang="scss">
.header__container {
  height: 5vh;
  background-color: $header-background;
  width: 100%;
  box-shadow: 5px 5px 10px #90a4ae;
  transition: box-shadow 0.3s ease-in-out;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.main_home {
  margin-left: 25px;
  & img {
    width: 5vh;
  }
}

.login_block {
  display: flex;
  align-items: center;
  & .login {
    width: 4vh;
    height: 4vh;
    cursor: pointer;
    background-image: url(@/assets/image/user.svg);
    background-repeat: no-repeat;
    margin-right: 20px;
  }
  & .is_login {
    background-image: url(@/assets/image/user-hover.svg);
  }
  & .admin {
    width: 3vh;
    height: 3vh;
    background-image: url(@/assets/image/settings.svg);
    background-repeat: no-repeat;
    margin-right: 20px;

    &:hover {
      background-image: url(@/assets/image/settings-hover.svg);
    }
  }

  & a {
    width: 3vh;
    height: 3vh;
    display: block;
    cursor: pointer;
  }
}
</style>
