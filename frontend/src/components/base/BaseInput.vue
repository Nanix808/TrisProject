<template>
  <div class="input_base_container">
    <input
      v-model="input_value"
      :id="generateRandomId"
      @input="handleChange"
      required=""
      spellcheck="false"
      autocomplete="username"
      :type="iconPasswordShow ? props.showPassword ?'password' : 'text' : 'text'" 
    />
    <span 
    v-if="props.showPassword"
    class="password-control" @click="iconPasswordShow =!iconPasswordShow"
                :class="{ password_show: !iconPasswordShow }"
          ></span>

    <label :for="generateRandomId" :class="{ active: input_value, inactive: props.isActive }">{{
      props.label
    }}</label>
  </div>
</template>
<script setup lang="ts">
import { ref} from "vue";
interface Props {
  label: string;
  isActive: boolean;
  showPassword?: boolean;
}


const props = withDefaults(defineProps<Props>(), {
  showPassword: false
})


// const props = defineProps<Props>();

const emit = defineEmits<{
  (e: "input_value", value: string): void;
}>();

const generateRandomId = ref<string>(
  Math.floor(Math.random() * Date.now()).toString(36)
);
const input_value = ref<string>("");
const iconPasswordShow = ref<boolean>(true);
function handleChange(event) {
  emit("input_value", event.target.value);
}
</script>

<style lang="scss">
.input_base_container {
  position: relative;

  & input {
    width: 100%;
    padding: 10px 0 0 0;
    height: 30px;
    line-height: 30px;
    font-size: 16px;
    color: black;
    border: none;
    border-bottom: 1px solid #000000;
    outline: none;
    background: transparent;
    padding-right: 30px;

    &:focus ~ label {
      top: -20px;
      left: 0;
      font-size: 16px;
    }
  }

  & label {
    position: absolute;
    top: 0;
    left: 0;
    padding: 10px 0;
    font-size: 16px;
    color: #000000;
    pointer-events: none;
    transition: 0.5s;

    &.active {
      top: -20px;
    left: 0;
    font-size: 16px;
    color: $default-error;
    }

    &.active.inactive {
      color: $default-success;
    }
  }

  & span.password-control {
    &.password-control {
      position: absolute;
      z-index: 2;
      top: 7px;
      right: 0;
      display: inline-block;
      width: 24px;
      height: 24px;
      background: url(@/assets/image/showpassword.svg);
      background-size: cover;
      cursor: pointer;
      
    }
    &.password_show {
      background: url(@/assets/image/hidepassword.svg);
      background-size: cover;
    }
}
  

}
</style>
