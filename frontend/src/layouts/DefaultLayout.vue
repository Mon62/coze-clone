<template>
  <div>
    <Sidebar class="position-fixed" />
    <router-view class="content"></router-view>
  </div>
</template>

<script setup>
import Sidebar from '@/components/Sidebar/Sidebar.vue'
</script>

<style scoped>
.content {
  margin-left: 230px;
}
</style>
