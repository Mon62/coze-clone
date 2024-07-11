<template>
  <div>
    <div v-if="check == 1">
      <hr class="my-2" />
      <h6 class="px-2 fw-light">Explore</h6>
    </div>
    <div class="link-item d-inline-flex align-items-center p-2 gap-2">
      <i :class="iconClass"></i>
      <h6>{{ name }}</h6>
    </div>
    <div v-if="check == 2">
      <hr class="my-2" />
      <h6 class="px-2 fw-light d-inline">Team</h6>
      <i class="bi bi-plus-lg float-end"></i>
      <br />
      <br />
      <br />
      <div class="d-flex justify-content-between px-2">
        <div v-for="iconClass in iconClassList" :key="iconClass.id">
          <i :class="iconClass" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Tooltip on top"></i>
        </div>
      </div>
      <hr class="my-2" />
        
    </div>
  </div>
</template>

<script setup>
const props = defineProps(['name', 'iconClass', 'check'])
const iconClassList = ['bi bi-journal-text', 'bi bi-alexa', 'bi bi-chat-text', 'bi bi-envelope']
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}
.link-item {
  cursor: pointer;
}
i {
  cursor: pointer;
}
</style>
