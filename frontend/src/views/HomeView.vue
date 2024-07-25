<template>
  <main>
    <div class="home_container">
      <MainModule
        v-if="
          store.state.auth.isSuperUser ||
          'transport' in store.state.auth.permissions
        "
        :name="'Транспорт'"
        :name_path="'transport'"
        :image_path="'/src/assets/image/car.svg'"
        :image_path_hover="'/src/assets/image/car-hover.svg'"
      />
    </div>
  </main>
</template>

<script setup>
import MainModule from '@/components/MainModule.vue';
import { ref, onMounted, watch } from 'vue';
import { useStore } from 'vuex';

const store = useStore();
</script>

<style lang="scss">
.home_container {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  margin: 20px;
}

@media (max-width: 600px) {
  .home_container {
    flex-direction: column;
  }
}
</style>
