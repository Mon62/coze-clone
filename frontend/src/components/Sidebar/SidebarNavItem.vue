<template>
  <div>
    <div v-if="check == 1">
      <hr class="my-3" />
      <h6 class="px-2 fw-light mb-2">Explore</h6>
    </div>
    <router-link :to="navigate" style="text-decoration: none">
      <div class="nav-item d-inline-flex align-items-center rounded-3 p-2 gap-2 w-100">
        <i :class="iconClass"></i>
        <h6>{{ name }}</h6>
      </div>
    </router-link>
    <div v-if="check == 2">
      <hr class="my-3" />
      <h6 class="px-2 py-2 fw-light d-inline">Teams</h6>
      <i class="bi bi-plus-lg float-end rounded-3"></i>
      <div style="height: 80px"></div>
      <div class="d-flex justify-content-between px-2">
        <div v-for="icon in iconList" :key="icon.id">
          <a-tooltip :arrow="icon.onlyContainText" color="white">
            <template #title>
              <div v-if="icon.onlyContainText">
                {{ icon.title }}
              </div>
              <div v-else-if="icon.class === 'bi bi-alexa'">
                <div class="d-inline-flex gap-2">
                  <i class="bi bi-discord"></i>
                  <h6 class="fw-normal">Discord</h6>
                </div>
                <br />
                <div class="d-inline-flex gap-2">
                  <i class="bi bi-telegram"></i>
                  <h6 class="fw-normal">Telegram</h6>
                </div>
              </div>
              <div v-else>
                <div class="d-inline-flex gap-2">
                  <i class="bi bi-youtube"></i>
                  <h6 class="fw-normal">Youtube</h6>
                </div>
                <br />
                <div class="d-inline-flex gap-2">
                  <i class="bi bi-twitter-x"></i>
                  <h6 class="fw-normal">X</h6>
                </div>
              </div>
            </template>
            <i :class="icon.class"></i>
          </a-tooltip>
        </div>
      </div>
      <hr class="my-3" />
    </div>
  </div>
</template>

<script setup>
const props = defineProps(['name', 'iconClass', 'check', 'navigate'])
const iconList = [
  { class: 'bi bi-journal-text p-2 rounded-3', title: 'Documents', onlyContainText: true },
  { class: 'bi bi-alexa p-2 rounded-3', title: '', onlyContainText: false },
  { class: 'bi bi-chat-text p-2 rounded-3', title: '', onlyContainText: false },
  { class: 'bi bi-envelope p-2 rounded-3', title: 'Feedback', onlyContainText: true }
]
</script>

<style scoped>
* {
  margin: 0;
  color: black;
  padding: 0;
}
.nav-item,
i {
  cursor: pointer;
}
.nav-item:hover,
i:hover {
  background-color: var(--color-background-hover);
}
</style>
