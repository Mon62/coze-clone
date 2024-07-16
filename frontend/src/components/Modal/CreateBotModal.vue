<template>
  <div>
    <a-modal :open="open" title="Create bot" centered :closable="closable">
      <label for="bot-name" class="fw-medium mb-2 mt-3"
        >Bot name <span style="color: red">*</span></label
      >
      <br />
      <a-input
        v-model:value="botName"
        id="bot-name"
        show-count
        :maxlength="40"
        placeholder="Give the bot a unique name"
      />

      <div class="fw-medium mt-4 mb-2">User Message Billing <span style="color: red">*</span></div>
      <div>
        When enabled, the user covers the message credit costs; when disabled, the bot creator
        covers the message credit costs.
        <a-switch class="switch float-end" :checked="switchState" @click="handleClickSwitch" />
      </div>
      <div class="fw-medium mt-4 mb-2">Bot function description</div>
      <a-textarea
        class="mb-5"
        v-model:value="description"
        placeholder="It introduces the bot functions and is displayed to the bot users"
        :auto-size="{ minRows: 3 }"
        show-count
        :maxlength="800"
      />

      <template #footer>
        <a-button class="cancel-btn" @click="$emit('closeModal')">Cancel</a-button>
        <a-button class="submit-btn submit-btn--opacity" v-if="checkButtonDisabled" disabled
          >Confirm</a-button
        >
        <a-button class="submit-btn" v-else>Confirm</a-button>
      </template>
    </a-modal>
  </div>
</template>
<script setup>
import { ref, watch } from 'vue'

const props = defineProps(['open'])
const emits = defineEmits(['closeModal'])

const closable = false
const botName = {value: ref('')}
const switchState = ref(false)
const description = ref('')
const checkButtonDisabled = ref(true)

const handleClickSwitch = () => {
  switchState.value = !switchState.value
}

watch(
  () => botName.value,
  () => {
    checkButtonDisabled.value = botName.value.length == 0
  }
)
</script>

<style scoped>
.submit-btn {
  background-color: var(--color-background-base);
  color: white;
}
.submit-btn:hover {
  background-color: var(--color-background-base-hover);
  color: white;
}
.submit-btn--opacity {
  opacity: 0.5;
}
</style>
