<template>
  <div class="sidebar container shadow px-2 py-4 my-2" style="width: 230px">
    <div class="sidebar__header d-flex gap-2 align-items-center">
      <img src="../../assets/coze-logo.jpg" alt="" class="rounded" height="32px" width="32px" />
      <h2>coze</h2>
    </div>
    <div class="sidebar__navigate mt-4">
      <button class="btn d-flex align-items-center justify-content-center gap-2 py-1 mb-3 w-100">
        <i class="bi bi-plus-lg" style="color: white"></i>
        <h6 class="text-white">Create bot</h6>
      </button>

      <div v-for="navItem in navItems" :key="navItem.id">
        <SidebarNavItem v-bind="navItem" :class="navItem.name" />
      </div>
    </div>
    <RouterLink to="/account" style="text-decoration: none; color: black;">
      <div
      class="sidebar__profile d-flex align-items-center rounded-3 w-100 py-1 mt-2 gap-2"
      style="cursor: pointer"
    >
      <a-avatar>U</a-avatar>
      <div>
        <h6 class="fw-normal">userygR5wV</h6>
        <h6 class="fw-light">@Mon62</h6>
      </div>
    </div>
    </RouterLink>
  </div>
</template>

<script setup>
import SidebarNavItem from './SidebarNavItem.vue'
import { RouterLink } from 'vue-router';

const navItems = [
  {
    name: 'Home',
    iconClass: 'bi bi-house-door',
    checkInsert: 'none',
    navigate: '/home'
  },
  {
    name: 'Personal',
    iconClass: 'bi bi-person',
    checkInsert: 'none',
    navigate: '/space/10/bot'
  },
  { name: 'Bot Store', iconClass: 'bi bi-robot', checkInsert: 'before', navigate: '/home' },
  { name: 'Plugin Store', iconClass: 'bi bi-box', checkInsert: 'none', navigate: '/home' },
  {
    name: 'Workflow Store',
    iconClass: 'bi bi-bounding-box',
    checkInsert: 'after',
    navigate: '/home'
  },
  { name: 'Coze Premium', iconClass: 'bi bi-gem', checkInsert: 'none', navigate: '/home' },
  { name: 'Coze API', iconClass: 'bi bi-code-slash', checkInsert: 'none', navigate: '/home' },
  {
    name: 'Coze Token',
    iconClass: 'bi bi-bank',
    checkInsert: 'none',
    navigate: '/home'
  }
]
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}
.btn {
  background-color: var(--color-background-base);
}
.sidebar__footer:hover {
  background-color: var(--color-background-hover);
}
</style>
