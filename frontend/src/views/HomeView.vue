<template>
  <main>
    <div class="home_container">
      <MainModule
        :name="'Транспорт'"
        :name_path="'transport'"
        :image_path="'/src/assets/image/car.svg'"
        :image_path_hover="'/src/assets/image/car-hover.svg'"
      />
      <!-- <div class="transport_module_container">
          <router-link :to="{ name: 'transport' }">Транспорт</router-link>
        </div> -->
    </div>
  </main>
</template>

<script setup>
import MainModule from '@/components/MainModule.vue';
</script>

<style lang="scss">
.module_content {
  display: flex;
  & .transport_module_container {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 200px;
    height: 200px;
    border: 1px solid black;
  }
}
</style>
