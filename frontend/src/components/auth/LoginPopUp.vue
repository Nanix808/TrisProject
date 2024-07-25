<template>
  <div v-if="props.isOpen">
    <div class="login-popup-container">
      <BasePopUP :name="name" @close="close">
        <div class="user-box">
          <EmailInput
            :error="store.state.user.request_unsuccess"
            @valid_value="set_email_valid_value"
          >
          </EmailInput>
        </div>
        <div class="user-box">
          <PasswordInput
            :error="store.state.user.request_unsuccess"
            @valid_value="set_password_valid_value"
          >
          </PasswordInput>
        </div>
        <div class="button-box">
          <BaseButton
            :name="'Войти'"
            :is-active="isEmailValid && isPasswordValid"
            @click="userLogin"
          >
          </BaseButton>
          <span @click="openRegisterPopup">Зарегистрироваться</span>
          <span @click="logout">Выйти</span>
        </div>
      </BasePopUP>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import BasePopUP from '@/components/base/BasePopUP.vue';
import EmailInput from '@/components/ui/EmailInput.vue';
import PasswordInput from '@/components/ui/PasswordInput.vue';
import BaseButton from '@/components/base/BaseButton.vue';

const store = useStore();
const rooter = useRouter();
interface Props {
  isOpen: boolean;
  width?: string;
}
const props = defineProps<Props>();
const isEmailValid = ref<boolean>(false);
const emailValue = ref<string>('');
const isPasswordValid = ref<boolean>(false);
const passwordValue = ref<string>('');
const name = <string>'Введите логин и пароль';

const emit = defineEmits<{
  (e: 'close'): void;
}>();

function close() {
  emit('close');
}

function userLogin() {
  store.dispatch('login', {
    email: emailValue.value,
    password: passwordValue.value,
  });
}

function logout() {
  store.dispatch('resetUser');
  rooter.push({ path: '/' });
}

function set_email_valid_value(isEmail: boolean, value: string) {
  isEmailValid.value = isEmail;
  emailValue.value = value;
}
function set_password_valid_value(isPassword: boolean, value: string) {
  isPasswordValid.value = isPassword;
  passwordValue.value = value;
}

function openRegisterPopup() {
  store.commit('closeLoginPopup');
  store.commit('openRegisterPopup');
}
</script>

<style lang="scss">
.login-popup-container {
  & .popup {
    max-width: 480px;
  }
}

.user-box {
  position: relative;
  padding-bottom: 30px;
}

.button-box {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  & button {
    width: 200px;
    margin-bottom: 10px;
  }

  & span {
    margin-top: 10px;
    cursor: pointer;
    font-size: 12px;

    &:hover {
      color: $default-success;
    }
  }
}
@media (max-width: 720px) {
  .button-box {
    flex-direction: column;
  }
}
</style>
