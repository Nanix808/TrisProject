<template>
  <div class="base__checkbox">
    <input
      type="checkbox"
      class="custom-checkbox"
      :id="'happy' + generateRandomId"
      v-model="checked"
      @change="emit('change', checked)"
    />
    <label :for="'happy' + generateRandomId"></label>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

interface Props {
  visible?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
  visible: false,
});

const emit = defineEmits<{
  (e: 'change', checked: boolean): void;
}>();

const checked = ref(props.visible);

const generateRandomId = ref<string>(
  Math.floor(Math.random() * Date.now()).toString(36)
);
</script>

<style lang="scss" scoped>
.base__checkbox {
  & .custom-checkbox {
    position: absolute;
    z-index: -1;
    opacity: 0;
  }

  & .custom-checkbox + label {
    display: inline-flex;
    align-items: center;
    user-select: none;
  }

  & .custom-checkbox + label::before {
    content: '';
    display: inline-block;
    width: 1.3em;
    height: 1.3em;
    flex-shrink: 0;
    flex-grow: 0;
    border: 1px solid #adb5bd;
    border-radius: 0.25em;

    background-repeat: no-repeat;
    background-position: center center;
    background-size: 50% 50%;
  }

  & .custom-checkbox:checked + label::before {
    border-color: $second-color;
    background-color: $second-color;
    background-image: url('@/assets/image/ok.svg');
  }
}
</style>
