<script setup>

import Header from './components/Header.vue'
</script>

<template>
  <div class="wrapper">
    <Header />
    <component :is="$route.meta.layoutComponent || 'div'">

    </component>


  </div>
</template>

<style scoped></style>
