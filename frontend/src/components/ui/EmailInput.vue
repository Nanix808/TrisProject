<template>
  <div class="email_input_container">
    <BaseInput
      :label="label"
      :isActive="isEmailValid && !props.error"
      @input_value="set_input_value"
    >
    </BaseInput>
  </div>
</template>

<script setup lang="ts">
import { ref} from "vue";
import { useStore } from 'vuex';
import BaseInput from "@/components/base/BaseInput.vue";

interface Props {
  error?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  error: false
})


const emit = defineEmits<{
  (e: 'valid_value', inEmail: boolean, value: string): void
}>()

const store = useStore()

const text = ref<string>("");
const label: string = "Электронная почта";
const isEmailValid = ref<boolean>(false);

function set_input_value(input_value) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (regex.test(input_value)) {
    isEmailValid.value = true;
  } else {
    isEmailValid.value = false;
  } 
 
  store.commit('request_unsuccess', false);
  emit('valid_value', isEmailValid.value, input_value)
  text.value = input_value;
}
</script>

<style lang="scss"></style>
