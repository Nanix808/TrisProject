<template>
  <div class="admin__user__container">
    <div class="admin__user__container_button_box">
      <BaseButton
        @click="saveChanges"
        :name="'Сохранить'"
        :is-active="isChangeParams"
      >
      </BaseButton>
      <BaseButton
        :name="'Добавить пользователя'"
        :is-active="true"
        @click="store.commit('openRegisterPopup')"
      >
      </BaseButton>
    </div>
    <div class="scrole_table_container">
      <BaseTable>
        <thead>
          <tr>
            <th class="box-1">№</th>
            <th class="box-2">Имя</th>
            <th class="box-3">Роль</th>
            <th class="box-4">Актив.</th>
            <th class="box-4">Суперюзер.</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(item, index) in store.state.admin_users.users"
            :key="item"
          >
            <td class="choised" @click="choiseuser(item.id)">{{ index }}</td>
            <td class="choised" @click="choiseuser(item.id)">
              {{ item.username.slice(0, 3) }}
            </td>
            <td class="hide_role">
              <BaseSelect
                :options="store.state.admin_users.roles"
                :default="item.role ? item.role.id : ''"
                @change="updateUserParameter($event, 'role_id', item.id)"
              >
              </BaseSelect>
            </td>
            <td>
              <BaseCheckbox
                :visible="item.is_active"
                @change="updateUserParameter($event, 'is_active', item.id)"
              >
              </BaseCheckbox>
            </td>
            <td>
              <BaseCheckbox
                :visible="item.is_superuser"
                @change="updateUserParameter($event, 'is_superuser', item.id)"
              >
              </BaseCheckbox>
            </td>
          </tr>
        </tbody>
      </BaseTable>
    </div>
    <AdminUserPopUp
      :name="'Изменить пользователя'"
      :isOpen="store.state.popup.isAdminUserPopupOpen"
      :data="user"
      @close="store.commit('closeAdminUserPopup')"
    >
    </AdminUserPopUp>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
import BaseTable from '@/components/base/BaseTable.vue';
import BaseButton from '@/components/base/BaseButton.vue';
import BaseSelect from '@/components/base/BaseSelect.vue';
import BaseCheckbox from '@/components/base/BaseCheckbox.vue';
import AdminUserPopUp from '@/components/admin/popup/AdminUserPopUp.vue';

const users = computed(() => store.state.admin_users.users);
const user = computed(() =>
  users.value.find((u: any) => u.id === change_user.value)
);

const store = useStore();

const isChangeParams = computed(() => {
  return Object.keys(change_params.value).length > 0;
});

const change_params = ref({});
let change_user = ref<number>(0);

function updateUserParameter(parameter: any, type: string, id: number) {
  const temp_arr = change_params.value[id] ?? [];
  const paramIndex = temp_arr.findIndex((p) => Object.keys(p)[0] === type);
  if (paramIndex === -1) {
    temp_arr.push({ [type]: parameter });
  } else {
    temp_arr[paramIndex] = { [type]: parameter };
  }
  change_params.value[id] = temp_arr;
}

function saveChanges() {
  store.dispatch('updatedUser', change_params.value);
  change_params.value = {};
  // Object.keys(change_params).forEach((key) => delete change_params[key]);
}

function choiseuser(id: number) {
  store.commit('openAdminUserPopup');
  change_user.value = id;
}
</script>
<style lang="scss">
.scrole_table_container {
  overflow-y: auto;
  height: 86vh;

  & .choised {
    cursor: pointer;

    &:hover {
      color: $admin-left-side-background;
    }
  }
}

.admin__user__container_button_box {
  display: flex;
  padding: 5px;
  height: 5vh;
  align-items: center;
  justify-content: flex-end;

  & button {
    max-width: 200px;
    border-radius: 15px;
  }
}

.box-1 {
  max-width: 50px;
  width: 50px;
}

.box-3 {
  width: 300px;
}

.box-4 {
  max-width: 120px;
  width: 120px;
}
@media (max-width: 900px) {
  .admin__user__container_button_box {
    flex-direction: column-reverse;
    justify-content: flex-start;
    align-items: flex-start;
    height: 12vh;

    & button {
      max-width: 100%;
      border-radius: 15px;
      height: 4vh;
    }
  }
  .scrole_table_container {
    & table {
      display: none;
      & tr {
        & th.box-3,
        .hide_role {
          display: none;
        }
      }
      & .box-4 {
        width: 90px;
      }
    }
  }
}
</style>
