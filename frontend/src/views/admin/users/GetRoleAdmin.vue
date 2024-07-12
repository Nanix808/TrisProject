<template>
  <div class="admin__roles__container">
    <div class="admin__role__container_button_box">
      <!-- <BaseButton :is-active="false" :name="'Сохранить'"> </BaseButton> -->
      <BaseButton
        :name="'Добавить роль'"
        :is-active="true"
        @click="choiserole(0)"
      >
      </BaseButton>
    </div>
    <BaseTable>
      <thead>
        <tr>
          <th class="box-1">№</th>
          <th class="box-2">Название роли</th>
          <th class="box-4">Описание роли</th>
          <th class="box-3">Разрешения</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in store.state.admin_users.roles"
          :key="item.id"
          @click="choiserole(item.id)"
        >
          <td class="choised">{{ item.id }}</td>
          <td class="choised">
            {{ item.name }}
          </td>
          <td>
            {{ item.description }}
            <!-- <BaseTextarea :text="item.description"> </BaseTextarea> -->
          </td>
          <td>
            {{ item.permissions }}
            <!-- <BaseTextarea :text="item.permissions"> </BaseTextarea> -->
          </td>
        </tr>
      </tbody>
    </BaseTable>

    <AdminRolePopUp
      :name="'Изменить роль'"
      :isOpen="store.state.popup.isAdminRolePopupOpen"
      :data="role"
      @close="store.commit('closeAdminRolePopup')"
    >
    </AdminRolePopUp>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
import BaseTable from '@/components/base/BaseTable.vue';
import BaseButton from '@/components/base/BaseButton.vue';
import BaseTextarea from '@/components/base/BaseTextarea.vue';
import AdminRolePopUp from '@/components/admin/popup/AdminRolePopUp.vue';

const roles = computed(() => store.state.admin_users.roles);
const found_role = computed(() =>
  roles.value.find((u: any) => u.id === change_role.value)
);
const role = computed(() =>
  found_role.value
    ? found_role.value
    : {
        id: 0,
        name: '',
        description: '',
        permissions: '',
      }
);

const change_role = ref<number>(0);

const store = useStore();

function choiserole(id: number) {
  store.commit('openAdminRolePopup');
  change_role.value = id;
}
</script>

<style lang="scss">
.box-1 {
  max-width: 50px;
  width: 50px;
}

.box-2 {
  width: 100px;
}

tr {
  cursor: pointer;
  &:hover {
    color: $admin-left-side-background;
  }
}

.admin__role__container_button_box {
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
</style>
