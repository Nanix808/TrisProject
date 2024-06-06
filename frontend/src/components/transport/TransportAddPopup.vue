<template>
  <div v-if="props.isOpen">
    <BasePopUP
      :name="props.name"
      @close="close"
      :width="60"
      @click="close_calendars"
    >
      <div class="box car-box" :class="car_id ? 'car-active' : ''">
        <span class="car-box_name">Выберете машину</span>
        <BaseSelect
          :options="store.state.transport.cars"
          @change="updateCarParameter($event)"
          :default="car_id ? car_id : ''"
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
              :config="config"
              ref="datepicker_from"
              class="form-control"
              placeholder="Выберете дату начала"
              name="date"
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
              ref="datepicker_to"
              class="form-control"
              placeholder="Выберете дату окончания"
              name="date"
            />
          </div>
        </div>

        <div class="box destination-box">
          <BaseInput
            :label="'Пункт назначения'"
            @input_value="destination = $event"
            :startValue="destination"
            :isActive="true"
          />
        </div>
        <div class="box destination-box">
          <BaseInput
            :label="'Контактные данные (Имя и телефон)'"
            @input_value="contact = $event"
            :startValue="contact"
            :isActive="true"
          />
        </div>
        <div class="box destination-box">
          <BaseInput
            :label="'Примечание'"
            @input_value="notice = $event"
            :startValue="notice"
            :isActive="true"
          />
        </div>
      </div>

      <div class="car_button-box">
        <BaseButton
          :name="'Сохранить'"
          :is-active="isCorrectParams"
          @click="addTransport"
        >
        </BaseButton>
        <BaseButton
          v-if="props.user_id == store.state.auth.userId"
          :name="'Удалить'"
          :is-active="true"
          @click="deleteUser"
        >
        </BaseButton>
      </div>
    </BasePopUP>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
import BasePopUP from '@/components/base/BasePopUP.vue';
import BaseSelect from '@/components/base/BaseSelect.vue';
import BaseButton from '@/components/base/BaseButton.vue';
import BaseInput from '@/components/base/BaseInput.vue';
import flatPickr from 'vue-flatpickr-component';
import { Russian } from 'flatpickr/dist/l10n/ru.js';

const store = useStore();

interface Props {
  isOpen: boolean;
  name: string;
  data: any;
  user_id: number;
}
const emit = defineEmits<{
  (e: 'close'): void;
}>();
const car_id = ref(null);
const props = defineProps<Props>();
const date_from = ref(null);
const date_to = ref(null);

const datepicker_from = ref(null);
const datepicker_to = ref(null);
const destination = ref(null);
const contact = ref(null);
const notice = ref(null);

const config = ref({
  // wrap: true, // set wrap to true only when using 'input-group'
  altFormat: 'd-M-Y H:i',
  altInput: true,
  dateFormat: 'Y-m-d H:i',
  enableTime: true,
  minDate: 'today',
  static: true,
  minTime: '9:00',
  maxTime: '18:00',
  minuteIncrement: 30,
  time_24hr: true,
  weekNumbers: false,
  locale: Russian, // locale for this instance only
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
  if (date_to.value) {
    return allField && new Date(date_from.value) < new Date(date_to.value);
  }
  return allField;
});

function close() {
  emit('close');
}

function close_calendars() {
  datepicker_from.value.fp.close();
  datepicker_to.value.fp.close();
}

function deleteUser() {
  if (confirm('Вы действительно хотите удалить пользователя?')) {
    store.dispatch('deleteUser', props.data.id);
  }
}

function updateCarParameter(event) {
  car_id.value = event;
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
    date_to_without_time.setMinutes(date_to_without_time.getMinutes() - 1);
    var mm = ('0' + (date_to_without_time.getMonth() + 1)).slice(-2);
    var dd = ('0' + date_to_without_time.getDate()).slice(-2);
    var yy = date_to_without_time.getFullYear();
    var hh = date_to_without_time.getHours();
    var min = date_to_without_time.getMinutes();
    date_to_new = yy + '-' + mm + '-' + dd + ' ' + hh + ':' + min + ':00';
  }
  const payload = {
    user_id: props.user_id,
    date_from: date_from.value,
    date_to: date_to_new,
    car_id: car_id.value,
    destination: destination.value,
    type_task: 'Подписать',
    status: 'Создана',
    contact: contact.value,
    notice: notice.value,
  };
  store.dispatch('addTransport', payload);
  emit('close');
}
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
</style>
