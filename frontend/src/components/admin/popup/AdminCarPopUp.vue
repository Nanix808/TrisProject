<template>
  <div v-if="props.isOpen" class="admin-car-popup-container">
    <BasePopUP :name="props.name" @close="close" :width="60">
      <div class="user-box">
        <BaseInput
          :isActive="true"
          :label="'Название машины'"
          @input_value="name = $event"
          :start-value="name"
        >
        </BaseInput>
      </div>

      <div class="button-box">
        <BaseButton
          :name="'Сохранить'"
          :is-active="isChangeParams"
          @click="saveChanges"
        >
        </BaseButton>
        <BaseButton
          v-if="data.id != 0"
          :name="'Удалить'"
          :is-active="true"
          @click="deleteRole"
        >
        </BaseButton>
      </div>
    </BasePopUP>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue';
import { useStore } from 'vuex';

import BasePopUP from '@/components/base/BasePopUP.vue';
import BaseButton from '@/components/base/BaseButton.vue';
import BaseTable from '@/components/base/BaseTable.vue';
import BaseInput from '@/components/base/BaseInput.vue';

const store = useStore();

interface Props {
  isOpen: boolean;
  name: string;
  data: any;
}
const props = withDefaults(defineProps<Props>(), {
  // update: false,
});
const name = ref('');
const description = ref();

const checked_value = ref<any>({});

const change_params = ref<any>({});

// onMounted(() => {
//   console.log('mounted');
//   checked_value.value = store.state.admin_users.list_endpoints;
// });

const isChangeCheckedValue = computed(() => {
  return (
    JSON.stringify(checked_value.value) !==
    JSON.stringify(store.state.admin_users.list_endpoints)
  );
});

const isCorrectDescriptionName = computed(() => {
  return name.value !== '' && description.value !== '';
});

const isChangeDescriptionName = computed(() => {
  return (
    props.data.name !== name.value ||
    props.data.description !== description.value
  );
});
const isChangeParams = computed(() => {
  return (
    (isChangeDescriptionName.value && isCorrectDescriptionName.value) ||
    (isChangeCheckedValue.value && isCorrectDescriptionName.value)
  );
});

const store_endpoints = computed(() => {
  return store.state.admin_users.list_endpoints;
});

const emit = defineEmits<{
  (e: 'close'): void;
}>();

function close() {
  emit('close');
}

function updateUserParameter(event, key, value) {
  if (event.target.checked) {
    if (!checked_value.value[key]) {
      checked_value.value[key] = [];
    }
    checked_value.value[key].push(value);
  } else {
    var index = checked_value.value[key].indexOf(value);
    if (index > -1) {
      checked_value.value[key].splice(index, 1);
    }
  }
}

function saveChanges() {
  let payload = {
    id: props.data.id,
    name: name.value,
  };
  if (props.data.id == 0) {
    store.dispatch('addCar', payload);
  } else {
    store.dispatch('updateCar', payload);
  }
  emit('close');
}

function deleteRole() {
  if (confirm('Вы действительно хотите удалить роль?')) {
    store.dispatch('deleteCar', props.data.id);
    emit('close');
  }
}

watch(
  () => props.isOpen,
  () => {
    checked_value.value = props.data.permissions;
    // checked_value.value = JSON.parse(
    //   JSON.stringify(store.state.admin_users.list_endpoints)
    // );
    name.value = props.data.name;
    description.value = props.data.description;
  }
);
</script>

<style lang="scss">
.user-box {
  display: flex;
  align-items: center;
  width: 100%;

  & .user-box_name {
    margin-right: 10px;
  }
}
.button-box {
  display: flex;
  flex-direction: row;
}
.check {
  -webkit-appearance: none;
  height: 20px;
  width: 20px;

  transition: 0.1s;
  background-color: #fe0006;
  text-align: center;
  font-weight: 600;
  color: white;
  border-radius: 3px;
  outline: none;
}

.check:checked {
  background-color: #0e9700;
}

.check:before {
  content: '✖';
}
.check:checked:before {
  content: '✔';
}

.check:hover {
  cursor: pointer;
  opacity: 0.8;
}
.admin-car-popup-container {
  & .popup {
    max-width: 660px;
  }
}
@media (max-width: 720px) {
  .admin-car-popup-container {
    & .popup {
      max-width: auto;
    }
    & .button-box {
      flex-direction: column;
    }
  }
}
</style>
