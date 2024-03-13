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
  margin: 0 10px 0 10px;
  cursor: pointer;
  border-radius: 5px;
  padding: 10px 25px;
  color: black;
  border: none;
  background-color: #d7dfe2;
  box-shadow: -5px -5px 10px white, 5px 5px 10px #90a4ae;


}

button.has-success:hover {
  color: $default-success;

}

button.has-error:hover {
  color: $default-error;
}

button:disabled {
  box-shadow: -5px -5px 10px white, 5px 5px 10px #90a4ae,
    inset -5px -5px 10px white, inset 5px 5px 10px #90a4ae;
}

button.has-success:active {
  color: $default-success;
  box-shadow: inset 4px 4px 12px #c5c5c5, inset -4px -4px 12px #ffffff;
}

button.has-error:active {
  color: $default-error;
  box-shadow: inset 4px 4px 12px #c5c5c5, inset -4px -4px 12px #ffffff;

}
</style>