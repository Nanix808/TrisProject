<template>
  <div class="transport_container">
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
        <BaseButton :name="'Выбрать транспорт'" :is-active="true" @click="">
        </BaseButton>
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
import { ref } from 'vue';
import BaseTable from '@/components/base/BaseTable.vue';
import BaseButton from '@/components/base/BaseButton.vue';
import flatPickr from 'vue-flatpickr-component';
import { Russian } from 'flatpickr/dist/l10n/ru.js';
import 'flatpickr/dist/flatpickr.css';
// import 'bootstrap/dist/css/bootstrap.css';
import 'flatpickr/dist/themes/material_green.css';

const date = ref(null);
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
  dateFormat: 'Y-m-d',
  locale: Russian, // locale for this instance only
});
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
}
</style>
