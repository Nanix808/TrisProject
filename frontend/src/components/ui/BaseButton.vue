<template>


  <button :disabled="!props.isActive" :class="!props.isActive ? 'has-error' : 'has-success'"
    @click.stop="emit('click')">{{ props.name }}
  </button>



</template>


<script setup lang="ts">
import { ref } from 'vue';
interface Props {
  name: string
  isActive: boolean
}

const props = defineProps<Props>()



const emit = defineEmits<{
  (e: 'click'): void
}>()



</script>




<style lang="scss">
button {
  width: 100%;

  background-color: $second-color;
  /* Green */
  border: none;
  color: white;
  padding: 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;


}

button.has-success:hover {
  color: $second-color-font;
  background-color: $admin-left-side-background;

}

button.has-error:hover {
  color: $default-error;
}

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

button.has-success:active {
  color: $main-color-font;

}

button.has-error:active {
  color: $default-error;


}
</style>