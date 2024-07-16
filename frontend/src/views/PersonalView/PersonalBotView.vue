<template>
  <div class="d-flex flex-column align-items-center gap-2 mt-5">
    <h4 class="fw-normal">No results found</h4>
    <h6 class="fw-light">Build an AI Bot with the power of LLM and plugins in minutes</h6>
    <button-create :button-label="'Create bot'"></button-create>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ButtonCreate from '@/components/Button/ButtonCreate.vue'
</script>

<style scoped></style>
