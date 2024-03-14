<template>
    <div class="admin__user__container">

        <div class="admin__user__container_button_box">


            <BaseButton :name="'Сохранить'" :is-active=true>

            </BaseButton>

            <BaseButton :name="'Добавить пользователя'" :is-active=true>

            </BaseButton>



        </div>

        <BaseTable>
            <thead>
                <tr>
                    <th class=" box-1">№</th>
                    <th class="box-2">Имя</th>
                    <th class="box-3">Роль</th>
                    <th class="box-4">Актив.</th>

                </tr>
            </thead>
            <tbody>

                <tr v-for="item in store.state.admin_users.users" :key="item">


                    <td>{{ item.id }}</td>
                    <td>{{ item.username }}</td>
                    <td>
                        <BaseSelect :options=store.state.admin_users.roles></BaseSelect>
                    </td>
                    <td>
                        <BaseCheckbox :id="item.id" :visible="item.is_active">

                        </BaseCheckbox>

                    </td>

                </tr>

            </tbody>
        </BaseTable>
    </div>

</template>


<script setup lang="ts">
import { useStore } from 'vuex';
import BaseTable from '@/components/ui/BaseTable.vue'
import BaseButton from '@/components/ui/BaseButton.vue';
import BaseSelect from '@/components/ui/BaseSelect.vue';
import BaseCheckbox from '@/components/ui/BaseCheckbox.vue';

const store = useStore()

// interface Props {
//     item: string
// }

// const props = defineProps<Props>()


</script>





<style lang="scss">
.admin__user__container_button_box {
    display: flex;
    padding: 10px;
    align-items: flex-end;
    justify-content: flex-end;

    & button {

        max-width: 200px;
        border-radius: 15px;
    }
}

.box-1 {
    max-width: 10px;
    width: 10px;
}

.box-2,
.box-3,
.box-4 {
    max-width: 65px;
    width: 65px;
}
</style>