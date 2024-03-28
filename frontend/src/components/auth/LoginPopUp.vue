<template>
  <div v-if="props.isOpen">
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
        <span>Востановить пароль</span>
      </div>
    </BasePopUP>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useStore } from 'vuex';
import BasePopUP from '@/components/base/BasePopUP.vue';
import EmailInput from '@/components/ui/EmailInput.vue';
import PasswordInput from '@/components/ui/PasswordInput.vue';
import BaseButton from '@/components/base/BaseButton.vue';

const store = useStore();

interface Props {
  isOpen: boolean;
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
</style>
