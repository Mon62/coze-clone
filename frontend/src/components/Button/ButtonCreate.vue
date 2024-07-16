<template>
  <div>
    <button class="btn px-3 py-2 fw-medium">
      {{ buttonLabel }}
    </button>
  </div>
</template>

<script setup>
const props = defineProps(['buttonLabel']);
</script>

<style scoped>
.btn {
  color: var(--color-background-base);
  background-color: #bac0ff33;
}
.btn:hover {
  background-color: #bac0ff88;
}
</style>
