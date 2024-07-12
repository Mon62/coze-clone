<template>
    <div>
        <div class="space_content">
            <Prompt />
            <KnowLedge />
        </div>
    </div>
</template>

<script setup>
import Prompt from '../components/Prompt.vue'
import KnowLedge from '../components/KnowLedge.vue'
</script>

<style lang="scss" scoped>
.space_content {
    display: grid;
    grid-template-columns: 13fr 13fr 13fr;
    height: 100%;
    overflow: hidden;
}
</style>