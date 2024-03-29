<template>
  <div class="admin__roles__container">
    <BaseTable>
      <thead>
        <tr>
          <th class="box-1">№</th>
          <th class="box-2">Название роли</th>
          <th class="box-3">Описание роли</th>
          <th class="box-4">Разрешения</th>
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
      :name="'Изменить пользователя'"
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
import BaseTextarea from '@/components/base/BaseTextarea.vue';
import AdminRolePopUp from '@/components/admin/popup/AdminRolePopUp.vue';

const roles = computed(() => store.state.admin_users.roles);
const role = computed(() =>
  roles.value.find((u: any) => u.id === change_role.value)
);

const change_role = ref<number>(0);

const store = useStore();

function choiserole(id: number) {
  console.log(id);
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
  width: 150px;
}

tr {
  cursor: pointer;
  &:hover {
    color: $admin-left-side-background;
  }
}
</style>
