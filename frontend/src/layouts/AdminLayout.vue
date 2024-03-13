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
    align-items: flex-end;
    justify-content: flex-end;



    & .admin__left_side {
        width: 15%;
        background-color: $admin-left-side-background;
        min-height: 100vh;
        position: absolute;
        top: 0;
        left: 0;
        display: flex;
        flex-direction: column;

        justify-content: flex-start;






    }


    & .admin__right_side {
        width: 85%;
        min-height: 95vh;


    }

}
</style>