<template>
    <div class="admin__user__container">
        <div class="admin__user__header">
            <div class="admin__user__header_users admin__user__header_items">
                <router-link :to="{ name: 'admin_users' }">
                    Пользователи
                </router-link>
            </div>
            <div class="admin__user__header_roles admin__user__header_items">
                <router-link :to="{ name: 'admin_roles' }">
                    Роли
                </router-link>
            </div>
            <div class="admin__user__header_permissions admin__user__header_items">
                <router-link :to="{ name: 'admin_permissions' }">
                    Разрешения
                </router-link>
            </div>
        </div>

        <div class="admin__user__main__container">
            <RouterView />
        </div>
    </div>
</template>


<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref, onMounted } from 'vue'
import { UrlApi } from "@/api";
import { useStore } from 'vuex';

const store = useStore()
const users = ref<any>([])
const roles = ref<any>([])

onMounted(() => {
    store.dispatch('admin_get_all_users');
    store.dispatch('admin_get_all_roles');

    // UrlApi.adminUserRoutes.getUsers().then((res) => {

    //     users.value = res.data
    // });

    // UrlApi.adminUserRoutes.getRoles().then((res) => {

    //     roles.value = res.data
    // });

})




</script>


<style lang="scss">
.admin__user__container {


    & .admin__user__header {
        height: 40px;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        justify-content: stretch;


        color: $main-color-font;

        & .admin__user__header_items {
            background-color: $second-color;

            border-left: 1px solid $admin-left-side-background;

            &:hover {
                background-color: $admin-left-side-background;
                color: $second-color-font;
            }

            & a {
                width: 100%;
                height: 100%;
                display: flex;
                align-items: center;
                justify-content: center;

                &.router-link-active {
                    color: $main-color-font;
                }

                &.router-link-exact-active {
                    color: $second-color-font;
                }
            }
        }
    }

    & .admin__user__main__container {}
}
</style>