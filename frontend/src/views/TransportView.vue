<template>
  <div class="transport_container" @click="isCarModal = false">
    <div class="transport_button_box">
      <div class="left_button_container">
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
      <div class="right_button_container">
        <BaseButton
          :name="'Создать задачу'"
          :is-active="true"
          @click="addTransport"
        >
        </BaseButton>
      </div>
    </div>
    <BaseTable>
      <thead>
        <tr>
          <th class="tbox-1">Время</th>
          <th class="tbox-2">Имя</th>
          <th class="tbox-3">Пункт назначения</th>
          <th class="tbox-3">Контакт</th>
          <th class="tbox-4">Статус</th>
          <th class="tbox-2">Примечание</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in timeStamp(9, 18)"
          :key="item"
          :class="
            get_user(item).id ? 'collor_table_' + (get_user(item).id % 4) : ''
          "
          @click="editTransport(get_user(item))"
        >
          <td :class="['choised']" @click="">{{ item }}</td>
          <td :class="['choised']" @click="">
            {{ get_short_name(get_user(item).user.username) }}
          </td>
          <td :class="['choised']" @click="">
            {{ get_user(item).destination }}
          </td>
          <td :class="['choised']" @click="">{{ get_user(item).contact }}</td>
          <td :class="['choised']" @click="">{{ get_user(item).status }}</td>
          <td :class="['choised', 'notice_td']">
            <div
              v-if="get_user(item).notice"
              class="transport_notice_container transport_notice"
              @click.stop="set_notice_text(get_user(item).notice)"
            >
              <div class="transport_notice_icon"></div>
            </div>
          </td>
        </tr>
        <tr>
          <th class="box-1" colspan="7">Задачи вне времени</th>
        </tr>
        <tr
          v-for="item in store.state.transport.transports_without_time_to"
          :key="item"
          @click="editTransport(item)"
        >
          <td class="choised" @click="">9->18</td>
          <td class="choised" @click="">
            {{ get_short_name(item.user.username) }}
          </td>

          <td class="choised" @click="">{{ item.destination }}</td>
          <td class="choised" @click="">{{ item.contact }}</td>

          <td class="choised" @click="">{{ item.status }}</td>
          <td :class="['choised', 'notice_td']">
            <div
              v-if="item.notice"
              class="transport_notice_container transport_notice"
              @click.stop="set_notice_text(item.notice)"
            >
              <div class="transport_notice_icon"></div>
            </div>
          </td>
        </tr>
      </tbody>
    </BaseTable>

    <BaseTextPopUP
      :name="'Примечание'"
      :text="noticeText"
      :is-open="isNoticePopUpOpen"
      @close="isNoticePopUpOpen = false"
    >
    </BaseTextPopUP>
    <TransportAddPopup
      :is-open="isTransportPopUpOpen"
      :data="data"
      :update="edit"
      :name="'Добавить задачу'"
      :user_id="1"
      @close="isTransportPopUpOpen = false"
    />
  </div>
</template>
<script setup lang="ts">
import { ref, onMounted, watch } from 'vue';
import BaseTable from '@/components/base/BaseTable.vue';
import BaseButton from '@/components/base/BaseButton.vue';
import ModalWindow from '@/components/ui/modal-window.vue';
import flatPickr from 'vue-flatpickr-component';
import BaseTextPopUP from '@/components/base/BaseTextPopUP.vue';
import TransportAddPopup from '@/components/transport/TransportAddPopup.vue';
import { Russian } from 'flatpickr/dist/l10n/ru.js';
import 'flatpickr/dist/flatpickr.css';
import 'flatpickr/dist/themes/material_green.css';
import { useStore } from 'vuex';
import { useRouter, useRoute } from 'vue-router';

const store = useStore();
const router = useRouter();
const route = useRoute();
const date = ref(null);
const data = ref(null);
const car = ref(null);
const edit = ref(false);
const isCarModal = ref(false);
const isTransportPopUpOpen = ref(false);
const isNoticePopUpOpen = ref(false);
const noticeText = ref('');

onMounted(async () => {
  await store.dispatch('get_all_cars');
  const now = route.query.date || new Date().toLocaleDateString();
  const car_id = route.query.car || store.state.transport.cars[0].id;
  date.value = now;
  car.value = store.state.transport.cars.find((item) => item.id == car_id);
  router.push({
    name: 'transport',
    query: { date: now, car: car_id },
  });
  const payload = {
    date_in: date.value,
    car_id: car.value.id,
  };
  store.dispatch('get_transport_by_date', payload);
});
function timeStamp(startHour, endHour) {
  const timeSlots = [];
  for (let hour = startHour; hour <= endHour; hour++) {
    // Добавьте временной слот на половину часа
    timeSlots.push(`${hour}:00`);
    timeSlots.push(`${hour}:30`);
  }
  timeSlots.pop();
  timeSlots.pop();
  return timeSlots;
}

function addTransport() {
  isTransportPopUpOpen.value = true;
  edit.value = false;
  data.value = {
    user: '',
    id: '',
    date: date.value,
    destination: '',
    contact: '',
    type_task: '',
    status: 'Создана',
    notice: '',
    date_from: '',
    date_to: '',
  };
}

function set_notice_text(notice) {
  noticeText.value = notice;
  isNoticePopUpOpen.value = true;
}

function get_short_name(item) {
  if (item) {
    return item.split('@')[0];
  }
}

function get_router_name_admin_permission() {
  return store.state.auth.permissions[router.currentRoute.value.name].includes(
    'ADMIN'
  );
}

function editTransport(item) {
  if (
    item.user.username &&
    ((item.user.username == store.state.auth.name &&
      item.status == 'Создана' &&
      new Date(date.value) >= new Date(new Date().setHours(0, 0, 0, 0))) ||
      store.state.auth.isSuperUser ||
      (get_router_name_admin_permission() &&
        new Date(date.value) >=
          new Date(
            new Date(Date.now() - 3600 * 1000 * 24).setHours(0, 0, 0, 0)
          )) ||
      store.state.auth.isSuperUser)
  ) {
    isTransportPopUpOpen.value = true;
    edit.value = true;
    // data.value = item;
    const date_without_time = new Date(item.date_from);
    var mm = ('0' + (date_without_time.getMonth() + 1)).slice(-2);
    var dd = ('0' + date_without_time.getDate()).slice(-2);
    var yy = date_without_time.getFullYear();
    var hh = date_without_time.getHours();
    var min = date_without_time.getMinutes();
    const date_from = yy + '-' + mm + '-' + dd + ' ' + hh + ':' + min + ':00';

    if (item.date_to) {
      const date_without_time_to = new Date(item.date_to);
      var mm = ('0' + (date_without_time_to.getMonth() + 1)).slice(-2);
      var dd = ('0' + date_without_time_to.getDate()).slice(-2);
      var yy = date_without_time_to.getFullYear();
      var hh = date_without_time_to.getHours();
      var min = date_without_time_to.getMinutes();
      const date_to = yy + '-' + mm + '-' + dd + ' ' + hh + ':' + min + ':00';
      item.date_to = date_to;
    }

    item.date = date.value;
    data.value = item;
  }
}

function get_user(item) {
  const item_date = new Date(date.value);
  const hour = item.split(':')[0];
  const min = item.split(':')[1];
  item_date.setHours(hour);
  item_date.setMinutes(min);
  const item_time = item_date;

  const transports = store.state.transport.transports.find((element) => {
    return (
      item_time >= new Date(element.date_from) &&
      item_time <= new Date(element.date_to)
    );
  });

  if (transports == undefined) {
    return {
      user: '',
      id: '',
      destination: '',
      contact: '',
      type_task: '',
      status: '',
      notice: '',
    };
  }
  return transports;
}

const config = ref({
  wrap: true, // set wrap to true only when using 'input-group'
  altFormat: 'M j, Y',
  altInput: true,
  dateFormat: 'm/d/Y',
  locale: Russian, // locale for this instance only
});

watch(route, (newValue, oldValue) => {
  router.push({
    name: 'transport',
    query: { date: date.value, car: car.value.id },
  });
  const payload = {
    date_in: date.value,
    car_id: car.value.id,
  };
  store.dispatch('get_transport_by_date', payload);
});

watch([date, car], ([newA, newB], [prevA, prevB]) => {
  router.push({
    name: 'transport',
    query: { date: newA, car: newB.id },
  });
});
</script>
<style lang="scss">
.transport_container {
  & table.table {
    width: auto;
  }
}
.tbox-1 {
  min-width: 75px;
}
.tbox-2 {
  width: 60px;
}
.tbox-3 {
  width: 100%;
}
.tbox-4 {
  width: 105px;
}
.base__table__container .table td.notice_td {
  padding: 0;
  position: relative;
}
.base__table__container .table tbody tr:nth-child(even) {
  background-color: white;
}

.base__table__container .table tbody tr.collor_table_0 {
  background-color: #d49dc5;
}

.base__table__container .table tbody tr.collor_table_1 {
  background-color: #b2ba80;
}
.base__table__container .table tbody tr.collor_table_2 {
  background-color: #84a0bf;
}
.base__table__container .table tbody tr.collor_table_3 {
  background-color: #82b7aa;
}

.base__table__container tr.collor_table_0 > td,
.base__table__container tr.collor_table_1 > td,
.base__table__container tr.collor_table_2 > td,
.base__table__container tr.collor_table_3 > td {
  border: none;
}

.transport_button_box {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 5px 10px 0px 10px;

  & .left_button_container {
    display: flex;
    justify-content: flex-start;
    align-items: center;
  }

  & .input-group {
    margin-right: 20px;

    .form-control {
      border-radius: 5px;
    }

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

.transport_notice {
  cursor: pointer;
}
.transport_notice_container {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  display: flex;
  justify-content: center;
  align-items: center;

  & .transport_notice_icon {
    width: 30px;
    height: 30px;
    background-image: url('../assets/image/timetable.svg');
    background-size: contain;
    background-repeat: no-repeat;
  }
}
</style>
