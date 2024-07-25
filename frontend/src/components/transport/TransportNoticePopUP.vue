<template>
  <div v-if="props.isOpen" class="transport-notice-popup-container">
    <BasePopUP :name="props.name" @close="close" :width="80" @click="close">
      <h4>Примечание:</h4>
      <p>{{ props.text }}</p>
      <h4>Пункт назначения:</h4>
      <p>{{ props.destination }}</p>
      <h4>Контакт:</h4>
      <p>{{ props.contact }}</p>
    </BasePopUP>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import BasePopUP from '@/components/base/BasePopUP.vue';

interface Props {
  isOpen: boolean;
  name: string;
  text: string;
  destination: string;
  contact: string;
}
const emit = defineEmits<{
  (e: 'close'): void;
}>();
const car_id = ref(null);
const props = defineProps<Props>();

function close() {
  emit('close');
}
</script>

<style lang="scss">
h4 {
  margin: 10px 0;
  font-size: 18px;
  font-weight: bold;
}

.transport-notice-popup-container {
  & p {
    word-break: break-all;
  }
  & .popup {
    max-width: 660px;
  }
}

@media (max-width: 720px) {
  .transport-add-popup-container {
    & .popup {
      max-width: auto;
    }
  }
}
</style>
