<template>
  <div class="transport_container" @click="isCarModal = false" v-show="car">
    <div class="transport_button_box">
      <div class="input-group">
        <flat-pickr
          v-model="date"
          :config="config"
          class="form-control"
          placeholder="Выберете дату"
          name="date"
        />
      </div>
      <div class="car_button_container">
        <BaseButton
          :name="car ? car.name : 'Выберете транспорт'"
          :is-active="true"
          @click="isCarModal = !isCarModal"
        >
        </BaseButton>
        <ModalWindow :title="'Выберете транспорт'" :isActive="isCarModal">
          <ul class="car-list">
            <li
              v-for="item in store.state.transport.cars"
              :key="item"
              @click="car = item"
              :class="item.id === car.id ? 'active_car' : ''"
            >
              {{ item.name }}
            </li>
          </ul>
        </ModalWindow>
      </div>
    </div>
    <BaseTable>
      <thead>
        <tr>
          <th class="box-1">Время</th>
          <th class="box-2">Имя</th>
          <th class="box-3">Пункт назначения</th>
          <th class="box-4">Контакт</th>
          <th class="box-4">Тип задачи.</th>
          <th class="box-4">Примечание</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in timeStamp(9, 18)" :key="item">
          <td class="choised" @click="">{{ item }}</td>
          <td class="choised" @click=""></td>
          <td class="choised" @click=""></td>
          <td class="choised" @click=""></td>
          <td class="choised" @click=""></td>
          <td class="choised" @click=""></td>
        </tr>
        <tr>
          <th class="box-1" colspan="6">Задачи вне времени</th>
        </tr>
        <tr v-for="item in timeStamp(9, 11)" :key="item">
          <td class="choised" @click="">В течении дня</td>
          <td class="choised" @click=""></td>
          <td class="choised" @click=""></td>
          <td class="choised" @click=""></td>
          <td class="choised" @click=""></td>
          <td class="choised" @click=""></td>
        </tr>
      </tbody>
    </BaseTable>
  </div>
</template>
<script setup lang="ts">
import { ref, onMounted, watch } from 'vue';
import BaseTable from '@/components/base/BaseTable.vue';
import BaseButton from '@/components/base/BaseButton.vue';
import ModalWindow from '@/components/ui/modal-window.vue';
import flatPickr from 'vue-flatpickr-component';
import { Russian } from 'flatpickr/dist/l10n/ru.js';
import 'flatpickr/dist/flatpickr.css';
// import 'bootstrap/dist/css/bootstrap.css';
import 'flatpickr/dist/themes/material_green.css';
import { useStore } from 'vuex';
import { useRouter, useRoute } from 'vue-router';

const store = useStore();
const router = useRouter();
const route = useRoute();
const date = ref(null);
const car = ref(null);
const isCarModal = ref(false);

onMounted(async () => {
  await store.dispatch('get_all_cars');
  const now = new Date().toLocaleDateString();
  car.value = store.state.transport.cars[0];
  router.push({
    name: 'transport',
    query: { date: now, car: car.value.id },
  });
  date.value = now;
  store.dispatch('get_transport_by_date', now);
});

function timeStamp(startHour, endHour) {
  const timeSlots = [];
  for (let hour = startHour; hour <= endHour; hour++) {
    // Добавьте временной слот на половину часа
    timeSlots.push(`${hour}:00`);
    timeSlots.push(`${hour}:30`);
  }
  timeSlots.pop();

  return timeSlots;
}

const config = ref({
  wrap: true, // set wrap to true only when using 'input-group'
  altFormat: 'M j, Y',
  altInput: true,
  dateFormat: 'm/d/Y',
  locale: Russian, // locale for this instance only
});

watch([date, car], ([newA, newB], [prevA, prevB]) => {
  // console.log('bpvtytybt');
  router.push({
    name: 'transport',
    query: { date: newA, car: newB.id },
  });
});

// watch(
//   () => date.value,
//   (newId) => {
//     router.push({
//       name: 'transport',
//       query: { date: newId, car: car.value.id },
//     });
//   }
// );
</script>
<style lang="scss">
.transport_button_box {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  margin: 5px 10px 0px 10px;

  & .input-group {
    margin-right: 20px;

    & input {
      max-width: 150px;
      // height: 2vh;
      font-size: 16px;
      cursor: pointer;
      color: white;
      background-color: $second-color;
      border: none;
      text-align: center;
      margin: 4px 2px;
      padding: 6px;

      &:focus {
        outline: none;
      }

      &:hover {
        color: $second-color-font;
        background-color: $admin-left-side-background;
      }

      &::-webkit-input-placeholder {
        color: white !important;
        text-align: center;
      }

      &:-moz-placeholder {
        /* Firefox 18- */
        color: white !important;
        text-align: center;
      }

      &::-moz-placeholder {
        /* Firefox 19+ */
        color: white !important;
        text-align: center;
      }

      &:-ms-input-placeholder {
        color: white !important;
        text-align: center;
      }
    }
  }

  & .car_button_container {
    position: relative;

    & .car-list {
      background-color: white;
      border: 1px solid rgba(72, 72, 72, 0.2);

      & li {
        list-style: none;
        padding: 10px;

        font-size: 16px;
        cursor: pointer;

        &.active_car {
          background-color: $header-background;
        }

        &:hover {
          background-color: $second-color;
          color: $second-color-font;
        }
      }
    }
  }
}
</style>
