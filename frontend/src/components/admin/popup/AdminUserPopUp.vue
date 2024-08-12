<template>
  <div class="admin-user-popup-container">
    <div v-if="props.isOpen">
      <BasePopUP :name="props.name" @close="close" :width="60">
        <h3>{{ props.data.username }} id: {{ props.data.id }}</h3>
        <div class="user-box">
          <BaseInput
            :isActive="true"
            :label="'Имя пользователя'"
            :start-value="props.data.username"
            @input_value="updateUserParameter($event, 'username')"
          >
          </BaseInput>
        </div>
        <div class="user-box">
          <EmailInput
            :error="false"
            :start-value="props.data.email"
            @valid_value="set_email_valid_value"
          >
          </EmailInput>
        </div>
        <div class="user-box">
          <span class="user-box_name">Активый</span>
          <BaseCheckbox
            :visible="props.data.is_active"
            @change="updateUserParameter($event, 'is_active')"
          >
          </BaseCheckbox>
        </div>
        <div class="user-box">
          <span class="user-box_name">Суперпользователь</span>
          <BaseCheckbox
            :visible="props.data.is_superuser"
            @change="updateUserParameter($event, 'is_superuser')"
          >
          </BaseCheckbox>
        </div>
        <div class="user-box role_box">
          <span class="user-box_name">Роль</span>
          <BaseSelect
            :options="store.state.admin_users.roles"
            :default="props.data.role ? props.data.role.id : ''"
            @change="updateUserParameter($event, 'role_id')"
          >
          </BaseSelect>
        </div>
        <div class="button-box">
          <BaseButton
            :name="'Сохранить'"
            :is-active="isChangeParams"
            @click="saveChanges"
          >
          </BaseButton>
          <BaseButton :name="'Удалить'" :is-active="true" @click="deleteUser">
          </BaseButton>
        </div>
      </BasePopUP>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
import BasePopUP from '@/components/base/BasePopUP.vue';
import EmailInput from '@/components/ui/EmailInput.vue';
import BaseButton from '@/components/base/BaseButton.vue';
import BaseSelect from '@/components/base/BaseSelect.vue';
import BaseCheckbox from '@/components/base/BaseCheckbox.vue';
import BaseTextarea from '@/components/base/BaseTextarea.vue';
import BaseInput from '@/components/base/BaseInput.vue';

const store = useStore();

interface Props {
  isOpen: boolean;
  name: string;
  data: any;
}
const props = defineProps<Props>();

const isEmailValid = ref<boolean>(false);
const emailValue = ref<string>('');

const change_params = ref({});

const isChangeParams = computed(() => {
  return Object.keys(change_params.value).length > 0;
});

const emit = defineEmits<{
  (e: 'close'): void;
}>();

function close() {
  emit('close');
}

function set_email_valid_value(isEmail: boolean, value: string) {
  isEmailValid.value = isEmail;
  emailValue.value = value;
  if (isEmailValid.value) {
    updateUserParameter(emailValue.value, 'email');
  }
}

function updateUserParameter(parameter: any, type: string) {
  const temp_arr = change_params.value[props.data.id] ?? [];
  const paramIndex = temp_arr.findIndex((p) => Object.keys(p)[0] === type);
  if (paramIndex === -1) {
    temp_arr.push({ [type]: parameter });
  } else {
    temp_arr[paramIndex] = { [type]: parameter };
  }
  change_params.value[props.data.id] = temp_arr;
}

function saveChanges() {
  store.dispatch('updatedUser', change_params.value);
  change_params.value = {};
}

function deleteUser() {
  if (confirm('Вы действительно хотите удалить пользователя?')) {
    store.dispatch('deleteUser', props.data.id);
  }
}
</script>

<style lang="scss">
.user-box {
  display: flex;
  align-items: center;
  width: 100%;

  & .user-box_name {
    margin-right: 10px;
  }
}
.button-box {
  display: flex;
  flex-direction: row;
}

.admin-user-popup-container {
  & .popup {
    max-width: 660px;
  }
}

@media (max-width: 720px) {
  .admin-user-popup-container {
    & .button-box {
      flex-direction: column;
    }
  }
  .role_box {
    display: flex;
    flex-direction: column;
    align-items: flex-start;

    & span {
      margin-bottom: 5px;
    }
  }
}
</style>
