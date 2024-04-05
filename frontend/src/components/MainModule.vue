<template>
  <div class="module__container">
    <router-link :to="{ name: props.name_path }">
      <div class="container_position">
        {{ props.name }}

        <div class="main_module_image"></div>
      </div>
    </router-link>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
interface Props {
  name: string;
  name_path: string;
  image_path?: string;
  image_path_hover?: string;
}

const props = withDefaults(defineProps<Props>(), {
  name: 'Нет Названия',
  name_path: 'home',
  image_path: '@/assets/image/no-image.svg',
  image_path_hover: '@/assets/image/no-image.svg',
});

const cssProps = computed(() => {
  return `url('${props.image_path}')`;
});
const cssPropsHover = computed(() => {
  return `url('${props.image_path_hover}')`;
});
</script>

<style lang="scss">
.module__container {
  height: 200px;
  margin: 20px;
  max-width: 250px;
  & a:visited {
    color: $main-color-font;
  }
}

.container_position {
  margin: 0 auto;
  height: 100%;
  border-radius: 8px;
  box-shadow: 0 0 2px rgba(0, 0, 0, 0.3);

  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-around;
  font-size: x-large;

  &:hover {
    color: $second-color;
    transition: all 0.1s linear;
    box-shadow: 0 0 5px $second-color;

    & .main_module_image {
      transition: all 0.1s linear;
      background-image: v-bind(cssPropsHover);
    }
  }

  .main_module_image {
    width: 100px;
    height: 100px;
    background-size: 100%;
    background-image: v-bind(cssProps);
    background-repeat: no-repeat;
    background-position: center;
  }
}
</style>
