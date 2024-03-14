<template>
    <div class="base__checkbox">
        <input type="checkbox" class="custom-checkbox" :id="'happy' + props.id" v-model="checked">
        <label :for="'happy' + props.id"></label>
    </div>
</template>



<script setup lang="ts">
import { ref } from 'vue'

const props = withDefaults(defineProps<Props>(), {
    id: 1,
    visible: false
})

const checked = ref(props.visible)

interface Props {
    id?: number
    visible?: boolean
}



</script>




<style lang="scss" scoped>
.base__checkbox {
    & .custom-checkbox {
        position: absolute;
        z-index: -1;
        opacity: 0;
    }

    & .custom-checkbox+label {
        display: inline-flex;
        align-items: center;
        user-select: none;
    }

    & .custom-checkbox+label::before {
        content: '';
        display: inline-block;
        width: 1.3em;
        height: 1.3em;
        flex-shrink: 0;
        flex-grow: 0;
        border: 1px solid #adb5bd;
        border-radius: 0.25em;
        margin-right: 0.5em;
        background-repeat: no-repeat;
        background-position: center center;
        background-size: 50% 50%;
    }

    & .custom-checkbox:checked+label::before {
        border-color: $second-color;
        background-color: $second-color;
        background-image: url('@/assets/image/ok.svg');
    }
}
</style>