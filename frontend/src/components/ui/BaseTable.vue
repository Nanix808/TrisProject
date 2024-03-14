<template>
    <div class="base__table__container">
        <table class="table">
            <slot />
            <!-- <thead>
                <tr>
                    <th class="box-1">№</th>
                    <th class="box-2">Имя</th>
                    <th class="box-3">Роль</th>
                    <th class="box-4">Актив.</th>

                </tr>
            </thead>
            <tbody>

                <tr v-for="item in store.state.admin_users.users" :key="item">

                    <td>{{ item.id }}</td>
                    <td>{{ item.username }}</td>
                    <td>{{ item.role_id }}</td>
                    <td>{{ item.is_active }}</td>
                </tr>

            </tbody> -->
        </table>
    </div>
</template>


<style lang="scss">
.base__table__container {
    & .table {
        table-layout: fixed;
        width: 100%;
        margin-bottom: 20px;

    }

    & .table th {
        font-weight: bold;
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

    & .table td {
        color: $second-color-font;
        padding: 5px 10px;
        border: 1px solid #eee;
        text-align: center;
        word-wrap: break-word;

    }
}
</style>