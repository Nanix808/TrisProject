<template>
    <div class="base__select">
        <select>
            <option v-for="item in props.options" :key="item" :value=item.id>{{ item.name }}</option>
        </select>
    </div>
</template>


<script setup lang="ts">

interface Props {
    options?: any[string]
}

const props = withDefaults(defineProps<Props>(), {
    options: ['----'],
})

</script>
<style lang="scss">
.base__select {
    position: relative;

    & select {
        appearance: none;
        /* safari */
        -webkit-appearance: none;
        width: 100%;
        font-size: 1rem;
        padding: 5px;
        background-color: #fff;
        border: 1px solid $second-color;
        border-radius: 0.25rem;
        color: #000;
        cursor: pointer;

        &::-webkit-scrollbar {
            width: 14px;
            height: 14px;
        }

        &::-webkit-scrollbar-track {
            border: rgb(180, 180, 180);
            background-color: $main-color-font;
        }

        &::-webkit-scrollbar-thumb {
            background-color: $second-color;
            border-radius: 0.25rem;
            border: 1px solid rgb(193, 193, 193);

        }

    }

    &::before,
    &::after {
        --size: 0.2rem;
        position: absolute;
        content: "";
        right: 1rem;
        pointer-events: none;
    }

    &::before {
        border-left: var(--size) solid transparent;
        border-right: var(--size) solid transparent;
        border-bottom: var(--size) solid $second-color-font;
        top: 40%;
    }

    &::after {
        border-left: var(--size) solid transparent;
        border-right: var(--size) solid transparent;
        border-top: var(--size) solid $second-color-font;
        top: 55%;
    }





}
</style>