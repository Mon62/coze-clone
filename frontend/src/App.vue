<template>
  <component :is="this.$route.meta.layout || 'div'">
    <router-view></router-view>
  </component>
</template>

<script setup>
import { RouterView } from 'vue-router'
</script>

<style scoped></style>
