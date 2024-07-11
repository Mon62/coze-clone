<template>
  <div class="sidebar container shadow px-2 py-4 my-2">
    <div class="sidebar__header d-inline-flex gap-2 align-items-center">
      <img src="../../assets/coze-logo.jpg" alt="" class="rounded" />
      <h2>coze</h2>
    </div>
    <div class="sidebar__main mt-4">
      <button
        class="btn d-inline-flex align-items-center justify-content-center gap-2 py-1 mb-3 w-100"
      >
        <i class="bi bi-plus-lg" style="color: white"></i>
        <h6 class="text-white">Create bot</h6>
      </button>

      <div v-for="navItem in navItems" :key="navItem.id">
        <SidebarNavItem v-bind="navItem" />
      </div>
    </div>
    <div
      class="sidebar__footer d-inline-flex align-items-center rounded-3 w-100 py-1 mt-2 gap-2"
      style="cursor: pointer"
    >
      <a-avatar>U</a-avatar>
      <div>
        <h6>userygR5wV</h6>
        <h6 class="fw-light">@Mon62</h6>
      </div>
    </div>
  </div>
</template>

<script setup>
import SidebarNavItem from './SidebarNavItem.vue'

const navItems = [
  {
    name: 'Home',
    iconClass: 'bi bi-house-door',
    check: 0,
    navigate: '/home'
  },
  {
    name: 'Personal',
    iconClass: 'bi bi-person',
    check: 0,
    navigate: '/space/10/bot'
  },
  { name: 'Bot Store', iconClass: 'bi bi-robot', check: 1, navigate: '/home' },
  { name: 'Plugin Store', iconClass: 'bi bi-box', check: 0, navigate: '/home'},
  {
    name: 'Workflow Store',
    iconClass: 'bi bi-bounding-box',
    check: 2,
    navigate: '/home'
  },
  { name: 'Coze Premium', iconClass: 'bi bi-gem', check: 0, navigate: '/home' },
  { name: 'Coze API', iconClass: 'bi bi-code-slash', check: 0, navigate: '/home' },
  {
    name: 'Coze Token',
    iconClass: 'bi bi-bank',
    navigate: '/home'
  }
]
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

.sidebar {
  width: 230px;
}
img {
  width: 32px;
  height: 32px;
}
.btn {
  background-color: var(--color-background-button-base);
}
.sidebar__footer:hover {
  background-color: var(--color-background-hover);
}
</style>
