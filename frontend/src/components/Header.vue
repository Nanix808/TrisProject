<template>
    <div class="header__container">
        <span @click="Upload">Upload</span>
        <router-link to="/admin">Go to Admin</router-link>
        <!-- <span @click="/admin">Admin</span> -->
        <LoginPopUP :isOpen=isLoginPopupOpen @close="closeLoginPopup" />
        <div class="login" @click="openLoginPopup">Войти</div>

        <RegisterPopUP :isOpen=false @close="closeLoginPopup" />
    </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import LoginPopUP from '@/components/auth/LoginPopUp.vue'
import RegisterPopUP from '@/components/auth/RegisterPopUp.vue'
import { useStore } from 'vuex'

const store = useStore()
const isLoginPopupOpen = computed(() => store.state.popup.isLoginPopupOpen);
function Upload() {
    store.dispatch('getUsers');
}

function closeLoginPopup() {
    store.commit('closeLoginPopup');
}
function openLoginPopup() {
    store.commit('openLoginPopup');
}

</script>

<style lang="scss">
.header__container {
    height: 5vh;
    background-color: $header-background;
    width: 100%;
    box-shadow: 5px 5px 10px #90a4ae;
    transition: box-shadow 0.3s ease-in-out;
}

.login {
    cursor: pointer;
}
</style>