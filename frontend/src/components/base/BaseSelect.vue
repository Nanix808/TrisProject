<template>
  <div class="base__select">
    <select v-model="selected_value" @change="emit('change', selected_value)">
      <option value="" selected disabled hidden>-----Выбрать-----</option>
      <option v-for="item in props.options" :key="item.id" :value="item.id">
        {{ item.name }}
      </option>
    </select>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

interface Props {
  options?: Array<{ id: number; name: string; description: string }>;
  default?: number | string;
}

const selected_value = ref<string>('');

const emit = defineEmits<{
  (e: 'change', value: number): void;
}>();

const props = withDefaults(defineProps<Props>(), {
  options: ['----'],
  default: '',
});

onMounted(() => {
  selected_value.value = props.default;
});
</script>
<style lang="scss">
.base__select {
  position: relative;

  & select {
    appearance: none;
    /* safari */
    -webkit-appearance: none;
    width: 100%;
    font-size: 1rem;
    padding: 5px;
    background-color: #fff;
    border: 1px solid $second-color;
    border-radius: 0.25rem;
    color: #000;
    cursor: pointer;

    &::-webkit-scrollbar {
      width: 14px;
      height: 14px;
    }

    &::-webkit-scrollbar-track {
      border: rgb(180, 180, 180);
      background-color: $main-color-font;
    }

    &::-webkit-scrollbar-thumb {
      background-color: $second-color;
      border-radius: 0.25rem;
      border: 1px solid rgb(193, 193, 193);
    }
  }

  &::before,
  &::after {
    --size: 0.2rem;
    position: absolute;
    content: '';
    right: 1rem;
    pointer-events: none;
  }

  &::before {
    border-left: var(--size) solid transparent;
    border-right: var(--size) solid transparent;
    border-bottom: var(--size) solid $second-color-font;
    top: 40%;
  }

  &::after {
    border-left: var(--size) solid transparent;
    border-right: var(--size) solid transparent;
    border-top: var(--size) solid $second-color-font;
    top: 55%;
  }
}
</style>
