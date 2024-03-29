<template>
  <div class="base_text_area_container">
    <span>{{ props.name }}</span>
    <textarea>{{ props.text }}</textarea>
  </div>
</template>

<script setup lang="ts">
interface Props {
  text?: string;
  name?: string;
}

const props = withDefaults(defineProps<Props>(), {
  text: '',
  name: '',
});
</script>
<style lang="scss">
.base_text_area_container {
  width: 100%;

  & textarea {
    width: 100%;
    height: 11vh;
    resize: none;
  }

  & span {
    display: block;
    margin-bottom: 5px;
  }
}
</style>
