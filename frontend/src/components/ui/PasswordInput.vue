<template>
  <div class="email_input_container">
    <BaseInput :label="props.label" :isActive="isPasswordStrong && !props.error" :showPassword="true" @input_value="set_input_value">
    </BaseInput>
    <span class="passworderror"></span>
    <ul class="requirements">
      <li v-for="(requirement, key) in isPasswordError" :key="key"
        :class="requirement.predicate ? 'is-success' : 'is-error'">
        {{ requirement.name }}
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";
import { useStore } from 'vuex';
import BaseInput from "@/components/base/BaseInput.vue";

interface Props {
  label?: string
  error?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  label: 'Пароль',
  error: false
})
const emit = defineEmits<{
  (e: 'valid_value', inPassword: boolean, passwordValue: string): void
}>()

const store = useStore()

const text = ref<string>("");
const label: string = "Пароль";
const isPasswordValid = ref<boolean>(false);


const passwordRequirements = computed(() => ([
  {
    name: 'заглавные буквы',
    predicate: text.value.toLowerCase() !== text.value,
  },
  {
    name: 'строчные буквы',
    predicate: text.value.toUpperCase() !== text.value,
  },
  {
    name: 'цифры',
    predicate: /\d/.test(text.value),
  },
  // {
  //   name: 'Must contain symbols',
  //   predicate: /\W/.test(text.value),
  // },
  {
    name: 'минимум 8 символов',
    predicate: text.value.length >= 8,
  },
]))


const isPasswordStrong = computed(() => passwordRequirements.value.reduce((v, p) => v && p.predicate, true))
const isPasswordError = computed(() => passwordRequirements.value.filter(item => item.predicate == false))

function set_input_value(input_value) {
  store.commit('request_unsuccess', false);
  text.value = input_value;
  emit('valid_value', !isPasswordError.value.length, input_value)
}
</script>



<style lang="scss">
.requirements {
  position: absolute;
  font-size: 10px;
  display: flex;

  & li {
    margin-right: 10px;
  }
}


.is-success {
  color: $default-success;
}

.is-error {
  color: $default-error;
}
</style>