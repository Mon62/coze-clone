<template>
  <div class="sidebar container shadow bg-secondary-subtle mx-auto p-2">
    <div class="sidebar__header d-inline-flex gap-2 align-items-center">
      <img src="../assets/coze-logo.jpg" alt="" class="rounded" />
      <h2>coze</h2>
    </div>
    <div class="sidebar__main mt-3">
      <button
        class="btn d-inline-flex align-items-center justify-content-center gap-2 py-1 mb-3 w-100"
      >
        <i class="bi bi-plus-lg" style="color: white"></i>
        <h6 class="text-white">Create bot</h6>
      </button>

      <div v-for="linkItem in linkItems" :key="linkItem.id">
        <SidebarLinkItem
          :name="linkItem.name"
          :iconClass="linkItem.iconClass"
          :check="linkItem.check"
        />
      </div>
    </div>
    <div class="sidebar__footer"></div>
  </div>
</template>

<script setup>
import SidebarLinkItem from './SidebarLinkItem.vue'

const linkItems = [
  {
    name: 'Home',
    iconClass: 'bi bi-house-door',
    check: 0
  },
  {
    name: 'Personal',
    iconClass: 'bi bi-person',
    check: 0
  },
  { name: 'Bot Store', iconClass: 'bi bi-robot', check: 1 },
  { name: 'Plugin Store', iconClass: 'bi bi-box', check: 0 },
  {
    name: 'Workflow Store',
    iconClass: 'bi bi-bounding-box',
    check: 2
  },
  { name: 'Coze Premium', iconClass: 'bi bi-gem', check: 0 },
  { name: 'Coze API', iconClass: 'bi bi-code-slash', check: 0 },
  {
    name: 'Coze Token',
    iconClass: 'bi bi-bank'
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
  background-color: #4e40e5;
}
</style>
