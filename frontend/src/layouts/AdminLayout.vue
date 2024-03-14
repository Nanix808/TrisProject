<template>
    <div class="admin__container">
        <div class="admin__left_side">
            <LeftAdminMenu />
        </div>
        <div class="admin__right_side">
            <RouterView />
        </div>

    </div>
</template>

<script setup>
import LeftAdminMenu from '@/components/admin/LeftAdminMenu.vue'
import { RouterLink, RouterView } from 'vue-router'


</script>

<style lang="scss">
.admin__container {
    display: flex;
    flex-direction: row;
    align-content: flex-start;




    & .admin__left_side {
        flex: 0 0 270px;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    }

    & .admin__right_side {
        flex: 1 1 auto;
        min-height: 95vh;
    }

}
</style>