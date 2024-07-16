<template>
  <div class="d-flex flex-column align-items-center gap-2 mt-5">
    <h4 class="fw-normal">No results found</h4>
    <h6 class="fw-light">Build an AI Bot with the power of LLM and plugins in minutes</h6>
    <create-button @showModal="showModal" buttonLabel="Create bot"></create-button>
    <create-bot-modal v-model:open="open" @closeModal="closeModal"></create-bot-modal>
    <!-- <a-button type="primary" @click="showModal">Open Modal</a-button>
    <a-modal v-model:open="open" title="Basic Modal" @ok="handleOk">
      <p>Some contents...</p>
      <p>Some contents...</p>
      <p>Some contents...</p>
    </a-modal> -->
  </div>
</template>

<script setup>
import { ref } from 'vue'
import CreateButton from '@/components/Button/CreateButton.vue';
import CreateBotModal from '@/components/Modal/CreateBotModal.vue';

const open = ref(false);
const showModal = () => {
  open.value = true;
}
const closeModal = () => {
  open.value = false;
}
</script>

<style scoped></style>
