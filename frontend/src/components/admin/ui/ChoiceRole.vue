<template>
  <div class="email_input_container">
    {{ store.state.admin_users.list_endpoints }}
    <!-- <span class="passworderror"></span>
    <ul class="requirements">
      <li v-for="(requirement, key) in isPasswordError" :key="key"
        :class="requirement.predicate ? 'is-success' : 'is-error'">
        {{ requirement.name }}
      </li>
    </ul> -->
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { useStore } from 'vuex';

interface Props {
  label?: string;
  error?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
  label: 'Пароль',
  error: false,
});
const emit = defineEmits<{
  (e: 'valid_value', inPassword: boolean, passwordValue: string): void;
}>();

const store = useStore();

const text = ref<string>('');
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
