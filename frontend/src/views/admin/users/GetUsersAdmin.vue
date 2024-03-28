<template>
  <div class="admin__user__container">
    <div class="admin__user__container_button_box">
      <BaseButton @click="saveChanges" :name="'Сохранить'" :is-active="true">
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
          <tr v-for="item in store.state.admin_users.users" :key="item">
            <td @click="choiseuser(item.id)">{{ item.id }}</td>
            <td @click="choiseuser(item.id)">{{ item.username }}</td>
            <td>
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
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useStore } from 'vuex';
import BaseTable from '@/components/base/BaseTable.vue';
import BaseButton from '@/components/base/BaseButton.vue';
import BaseSelect from '@/components/base/BaseSelect.vue';
import BaseCheckbox from '@/components/base/BaseCheckbox.vue';

const store = useStore();

const change_params = {};

function updateUserParameter(parameter: any, type: string, id: number) {
  const temp_arr = change_params[id] ?? [];
  const paramIndex = temp_arr.findIndex((p) => Object.keys(p)[0] === type);
  if (paramIndex === -1) {
    temp_arr.push({ [type]: parameter });
  } else {
    temp_arr[paramIndex] = { [type]: parameter };
  }
  change_params[id] = temp_arr;
}

function saveChanges() {
  store.dispatch('updatedUser', change_params);
  Object.keys(change_params).forEach((key) => delete change_params[key]);
}
</script>
<style lang="scss">
.scrole_table_container {
  overflow-y: auto;
  height: 86vh;
}

.admin__user__container_button_box {
  display: flex;
  height: 5vh;
  align-items: flex-end;
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
</style>
