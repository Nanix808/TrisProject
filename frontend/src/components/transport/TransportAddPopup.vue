<template>
  <div class="transport-add-popup-container">
    <div v-if="props.isOpen" class="transport-add-popup">
      <BasePopUP
        :name="props.name"
        @close="close"
        :width="60"
        @click="close_calendars"
      >
        <div class="box car-box" :class="car_id ? 'car-active' : ''">
          <span class="car-box_name">Выберете машину</span>
          <BaseSelect
            :isActive="!(props.update && !get_router_name_admin_permission)"
            :options="store.state.transport.cars"
            @change="updateCarParameter($event)"
            :default="car_id"
          >
          </BaseSelect>
        </div>

        <div class="box calendar-box">
          <div class="calendar-box_date">
            <div
              class="calendar_date_from"
              @click.stop
              :class="date_from ? 'car-active' : ''"
            >
              <label for="date_from" @click="close_calendars">Время от</label>
              <flat-pickr
                id="date_from"
                v-model="date_from"
                :disabled="props.update && !get_router_name_admin_permission"
                :config="config"
                ref="datepicker_from"
                class="form-control"
                placeholder="Выберете дату начала"
                name="date"
                @on-close="onValueUpdateFrom($event)"
              />
            </div>
            <div
              class="calendar_date_to"
              @click.stop
              :class="date_to ? 'car-active' : ''"
            >
              <label for="date_from" @click="close_calendars">Время до</label>
              <flat-pickr
                v-model="date_to"
                id="date_to"
                :config="config"
                :disabled="props.update && !get_router_name_admin_permission"
                ref="datepicker_to"
                class="form-control"
                placeholder="Выберете дату окончания"
                name="date"
                @on-close="onValueUpdateTo($event)"
              />
            </div>
          </div>

          <div
            class="box destination-box"
            :class="status_value ? 'car-active' : ''"
            v-if="get_router_name_admin_permission && props.update"
          >
            <span class="car-box_name">Статус</span>
            <BaseSelect
              :options="status"
              @change="updateStatusParameter($event)"
              :default="
                status.find((item) => item.name === status_value)
                  ? status.find((item) => item.name === status_value).id
                  : ''
              "
            >
            </BaseSelect>
          </div>

          <div class="box destination-box">
            <BaseInput
              :label="'Пункт назначения'"
              @input_value="destination = $event"
              :startValue="destination"
              :disabled="props.update && !get_router_name_admin_permission"
            />
          </div>
          <div class="box destination-box">
            <BaseInput
              :label="'Контактные данные'"
              @input_value="contact = $event"
              :startValue="contact"
              :disabled="props.update && !get_router_name_admin_permission"
            />
          </div>
          <div class="box destination-box">
            <BaseInput
              :label="'Примечание'"
              @input_value="notice = $event"
              :startValue="notice"
              :disabled="props.update && !get_router_name_admin_permission"
            />
          </div>
        </div>
        <div class="car_button-box">
          <BaseButton
            v-if="!(props.update && !get_router_name_admin_permission)"
            :name="props.update ? 'Изменить' : 'Сохранить'"
            :is-active="isCorrectParams"
            @click="addTransport"
          >
          </BaseButton>
          <BaseButton
            v-if="props.update"
            :is-active="isCorrectParamsDellete || store.state.auth.isSuperUser"
            :name="'Удалить'"
            @click="deleteTransport"
          >
          </BaseButton>
        </div>
      </BasePopUP>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue';
import { useStore } from 'vuex';
import BasePopUP from '@/components/base/BasePopUP.vue';
import BaseSelect from '@/components/base/BaseSelect.vue';
import BaseButton from '@/components/base/BaseButton.vue';
import BaseInput from '@/components/base/BaseInput.vue';
import flatPickr from 'vue-flatpickr-component';
import { Russian } from 'flatpickr/dist/l10n/ru.js';
import { useRouter } from 'vue-router';
const store = useStore();

interface Props {
  isOpen: boolean;
  name: string;
  data: any;
  user_id: number;
  update: boolean;
}

const props = withDefaults(defineProps<Props>(), {
  isOpen: false,
  update: false,
});
const emit = defineEmits<{
  (e: 'close'): void;
}>();

const router = useRouter();
const car_id = ref(null);
const date_from = ref(null);
const date_to = ref(null);
const datepicker_from = ref(null);
const datepicker_to = ref(null);
const destination = ref(null);
const contact = ref(null);
const notice = ref(null);
const status_value = ref(null);

const status = ref([
  { name: 'Создана', id: 1 },
  { name: 'Принята', id: 2 },
  { name: 'Выполнена', id: 3 },
  { name: 'Отменена', id: 4 },
]);

const get_router_name_admin_permission = computed(() => {
  if (
    store.state.auth.isSuperUser ||
    store.state.auth.permissions[router.currentRoute.value.name].includes(
      'ADMIN'
    )
  ) {
    return true;
  }
  return false;
});

const config = computed(() => {
  return {
    altFormat: 'd-M-Y H:i',
    altInput: true,
    allowInput: false,
    dateFormat: 'Y-m-d H:i',
    enableTime: true,
    defaultHour: 9,
    defaultMinute: 0,
    minDate: get_router_name_admin_permission.value
      ? new Date(Date.now() - 3600 * 1000 * 24).setHours(0, 0, 0, 0)
      : roundToNearestHalfHour(),
    static: true,
    minTime: get_router_name_admin_permission.value
      ? '09:00'
      : new Date().setHours(0, 0, 0, 0) ===
        new Date(date_from.value).setHours(0, 0, 0, 0)
      ? get_time_roundToNearestHalfHour()
      : '09:00',
    maxTime: '18:00',
    minuteIncrement: 30,
    time_24hr: true,
    weekNumbers: false,
    locale: Russian,
  };
});
const isCorrectParams = computed(() => {
  const allField =
    car_id.value &&
    date_from.value &&
    destination.value &&
    contact.value &&
    notice.value
      ? true
      : false;
  if (date_to.value && get_router_name_admin_permission.value) {
    return (
      allField &&
      new Date(date_from.value) < new Date(date_to.value) &&
      get_router_name_admin_permission.value
    );
  } else if (date_to.value && !get_router_name_admin_permission.value) {
    return (
      allField &&
      new Date(date_from.value) < new Date(date_to.value) &&
      new Date(date_from.value) >= new Date()
    );
  }
  return allField;
});

const isCorrectParamsDellete = computed(() => {
  if (
    !get_router_name_admin_permission.value &&
    date_to.value &&
    new Date(date_to.value) <= new Date()
  ) {
    return false;
  }

  return true;
});

function get_time_roundToNearestHalfHour() {
  const time = roundToNearestHalfHour();
  var hh = ('0' + time.getHours()).slice(-2);
  var min = time.getMinutes();
  return hh + ':' + min + ':00';
}
function roundToNearestHalfHour() {
  const halfHour = 30 * 60 * 1000; // 30 минут в миллисекундах
  const currentTime = new Date().getTime();
  const nextHalfHour = Math.ceil(currentTime / halfHour) * halfHour;
  return new Date(nextHalfHour);
}

function onValueUpdateFrom(time) {
  const halfHour = 30 * 60 * 1000;
  const currentTime = new Date(time).getTime();
  const nextHalfHour = Math.ceil(currentTime / halfHour) * halfHour;
  datepicker_from.value.fp.setDate(new Date(nextHalfHour));
}
function onValueUpdateTo(time) {
  const halfHour = 30 * 60 * 1000;
  const currentTime = new Date(time).getTime();
  const nextHalfHour = Math.ceil(currentTime / halfHour) * halfHour;
  datepicker_to.value.fp.setDate(new Date(nextHalfHour));
}

function close() {
  car_id.value = props.data.car_id;
  destination.value = props.data.destination;
  contact.value = props.data.contact;
  notice.value = props.data.notice;
  date_from.value = props.data.date_from;
  date_to.value = props.data.date_to;
  status_value.value = props.data.status;
  emit('close');
}

function close_calendars() {
  datepicker_from.value.fp.close();
  datepicker_to.value.fp.close();
}

function deleteTransport() {
  if (confirm('Вы действительно хотите удалить запись?')) {
    const payload = {
      car_id_page: router.currentRoute.value.query.car,
      id: props.data.id,
      date: props.data.date,
    };
    store.dispatch('deleteTransport', payload);
    emit('close');
  }
}

function updateCarParameter(event) {
  car_id.value = event;
}

function updateStatusParameter(event) {
  if (status.value.find((item) => item.id === event)) {
    status_value.value = status.value.find((item) => item.id === event).name;
  }
}

function addTransport() {
  let date_to_new = null;
  if (!date_to.value) {
    const date_without_time = new Date(date_from.value);
    var mm = ('0' + (date_without_time.getMonth() + 1)).slice(-2);
    var dd = ('0' + date_without_time.getDate()).slice(-2);
    var yy = date_without_time.getFullYear();
    date_from.value = yy + '-' + mm + '-' + dd + ' 00:00:00';
  }
  if (date_to.value) {
    var date_to_without_time = new Date(date_to.value);

    if (
      date_to_without_time.getMinutes() === 30 ||
      date_to_without_time.getMinutes() === 0
    ) {
      date_to_without_time.setMinutes(date_to_without_time.getMinutes() - 1);
    }

    var mm = ('0' + (date_to_without_time.getMonth() + 1)).slice(-2);
    var dd = ('0' + date_to_without_time.getDate()).slice(-2);
    var yy = date_to_without_time.getFullYear();
    var hh = ('0' + date_to_without_time.getHours()).slice(-2);
    var min = date_to_without_time.getMinutes();
    date_to_new = yy + '-' + mm + '-' + dd + ' ' + hh + ':' + min + ':00';
  }
  const payload = {
    car_id_page: router.currentRoute.value.query.car,
    id: props.data.id,
    date: props.data.date,
    date_from: date_from.value,
    date_to: date_to_new,
    car_id: car_id.value,
    destination: destination.value,
    type_task: 'Подписать',
    status: status_value.value,
    contact: contact.value,
    notice: notice.value,
  };
  console.log(payload);
  if (props.update) {
    store.dispatch('editTransport', payload);
  } else {
    payload['user_id'] = props.user_id;
    store.dispatch('addTransport', payload);
  }

  emit('close');
}

watch(
  () => props.data,
  (newValue) => {
    car_id.value = newValue.car_id;
    destination.value = newValue.destination;
    contact.value = newValue.contact;
    notice.value = newValue.notice;
    date_from.value = newValue.date_from;
    date_to.value = newValue.date_to;
    status_value.value = newValue.status;
  }
);
</script>

<style lang="scss">
.box {
  margin-bottom: 30px;
}
label,
.car-box_name {
  margin-bottom: 15px;
  display: block;
  font-size: 16px;
}

.car-active {
  & select,
  & input.form-control {
    background-color: $second-color;
    color: white;

    & option {
      background-color: white;
      color: black;
    }

    &:hover {
      color: $second-color-font;
      background-color: $admin-left-side-background;
    }
  }
  & input.form-control {
    border: 2px solid $second-color;
  }
}

.calendar-box_date {
  display: flex;
  align-items: center;
  justify-content: space-around;

  & .calendar_date_from {
    margin-right: 20px;
  }

  & .calendar_date_from,
  .calendar_date_to {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;

    & .flatpickr-wrapper {
      width: 100%;
    }

    & input.form-control {
      padding: 5px 10px;
      width: 100%;
      border-radius: 5px;
      text-align: center;

      &::-webkit-input-placeholder {
        text-align: center;
      }

      &:-moz-placeholder {
        text-align: center;
      }

      &::-moz-placeholder {
        text-align: center;
      }
    }
  }
}
.destination-box {
  margin-top: 25px;
}
.car_button-box {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.transport-add-popup-container {
  & .popup {
    max-width: 660px;
  }
}

@media (max-width: 720px) {
  .calendar-box_date {
    flex-direction: column;

    & .calendar_date_from {
      margin: 0 0 10px 0;
    }
  }
  .transport-add-popup-container {
    & .popup {
      max-width: auto;
    }
    & .car_button-box {
      flex-direction: column;
    }
  }
}
</style>
