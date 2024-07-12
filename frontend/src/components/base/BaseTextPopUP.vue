<template>
  <div v-if="props.isOpen">
    <BasePopUP :name="props.name" @close="close" :width="80" @click="close">
      {{ props.text }}
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

<style lang="scss"></style>
