<template>
  <div class="d-flex flex-column align-items-center gap-2 mt-5">
    <h4 class="fw-normal">Knowledge not found</h4>
    <h6 class="fw-light">Please create first and then add</h6>
    <button-create :button-label="'Create knowledge base'"></button-create>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ButtonCreate from '@/components/Button/ButtonCreate.vue'
</script>

<style scoped></style>
