<template>
  <div class="d-inline-flex">
    <component :is="this.$route.meta.layout || 'div'">
    </component>
    <router-view></router-view>
  </div>
</template>

<script setup>
</script>

<style scoped></style>
