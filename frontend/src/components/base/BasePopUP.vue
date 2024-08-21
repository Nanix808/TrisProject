<template>
  <div class="backdrop" @mousedown="close">
    <div class="popup" @mousedown.stop>
      <div class="container_button_close" @mousedown="close">
        <ButtonClose />
      </div>

      <h3>{{ props.name }}</h3>

      <slot></slot>
    </div>
  </div>
</template>

<script setup lang="ts">
import ButtonClose from '@/components/ui/button-close.vue';
interface Props {
  name: string;
  width?: number;
}

const props = withDefaults(defineProps<Props>(), {
  name: 'Имя не заданно',
  width: 100,
});

const emit = defineEmits<{
  (e: 'close'): void;
}>();

function close() {
  emit('close');
}
</script>

<style lang="scss">
input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus,
input:-webkit-autofill:active {
  transition: background-color 5000s ease-in-out 0s;
}

.backdrop {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.3);
  z-index: 100;
}

.popup {
  position: absolute;
  top: 50%;
  left: 50%;

  padding: 40px;
  transform: translate(-50%, -50%);
  background: white;
  box-sizing: border-box;
  box-shadow: 0 15px 25px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  width: 90%;
  border-radius: 20px;
  cursor: default;
}

.container_button_close {
  position: absolute;
  top: -16px;
  right: -16px;
}

.popup h3 {
  margin: 0 0 30px;
  padding: 0;
  color: #000000;
  text-align: center;
}
</style>
