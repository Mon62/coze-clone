<template>
  <div class="d-flex flex-column align-items-center gap-2 mt-5">
    <h4 class="fw-normal">Knowledge not found</h4>
    <h6 class="fw-light">Please create first and then add</h6>
    <create-button buttonLabel="Create knowledge base"></create-button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import CreateButton from '@/components/Button/CreateButton.vue'
</script>

<style scoped></style>
