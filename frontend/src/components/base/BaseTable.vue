<template>
  <div class="base__table__container">
    <table class="table">
      <slot />
    </table>
  </div>
</template>

<script setup lang="ts"></script>

<style lang="scss">
.base__table__container {
  & .table {
    width: 100%;
    table-layout: fixed;
    border: none;

 

    & th {
      font-size: 16px;
      padding: 5px;
      background: $second-color;
      border: 1px solid #dddddd;
      position: sticky;
      top: 0;
      z-index: 2;
      -moz-user-select: none;
      -khtml-user-select: none;
      user-select: none;
    }

    & td {
      color: $second-color-font;
      padding: 5px 10px;
      border: 1px solid #eee;
      text-align: center;
      word-wrap: break-word;
      position: relative;
    }

    & tbody tr:nth-child(even) {
      background: #f3f3f3;
    }
  }
}
</style>
