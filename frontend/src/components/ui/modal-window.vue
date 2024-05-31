<template>
  <div class="modal" v-if="props.isActive">
    <h4 v-if="props.title">{{ props.title }}</h4>
    <slot></slot>
  </div>
</template>

<script setup lang="ts">
interface Props {
  title: string;
  isActive: boolean;
}

const props = defineProps<Props>();
</script>

<style lang="scss">
.modal {
  position: absolute;
  top: 97%;
  left: 0;
  z-index: 3;
  background-color: $second-color-font;
  border-radius: 5px 5px 0 0;
  animation: fpFadeInDown 300ms cubic-bezier(0.23, 1, 0.32, 1);

  & h4 {
    font-size: 16px;
    color: $second-color-font;
    padding: 10px;
    white-space: nowrap;
    background-color: $header-color;
    border-radius: 5px 5px 0 0;
  }
}
</style>
