<template>
  <div class="admin__roles__container">
    <div class="admin__role__container_button_box">
      <!-- <BaseButton :is-active="false" :name="'Сохранить'"> </BaseButton> -->
      <BaseButton
        :name="'Добавить транспорт'"
        :is-active="true"
        @click="choiserole(0)"
      >
      </BaseButton>
    </div>
    <BaseTable>
      <thead>
        <tr>
          <th class="box-1">№</th>
          <th class="box-2">Название</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(item, index) in store.state.transport.cars"
          :key="item.id"
          @click="choiserole(item.id)"
        >
          <td class="choised">{{ index + 1 }}</td>
          <td class="choised">{{ item.name }}</td>
        </tr>
      </tbody>
    </BaseTable>

    <AdminCarPopUp
      :name="'Изменить машину'"
      :isOpen="store.state.popup.isAdminCarPopupOpen"
      :data="car"
      @close="store.commit('closeAdminCarPopup')"
    >
    </AdminCarPopUp>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
import BaseTable from '@/components/base/BaseTable.vue';
import BaseButton from '@/components/base/BaseButton.vue';
import BaseTextarea from '@/components/base/BaseTextarea.vue';
import AdminCarPopUp from '@/components/admin/popup/AdminCarPopUp.vue';

const cars = computed(() => store.state.transport.cars);
const found_car = computed(() =>
  cars.value.find((u: any) => u.id === change_car.value)
);
const car = computed(() =>
  found_car.value
    ? found_car.value
    : {
        id: 0,
        name: '',
      }
);

const change_car = ref<number>(0);

const store = useStore();

function choiserole(id: number) {
  store.commit('openAdminCarPopup');
  change_car.value = id;
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
