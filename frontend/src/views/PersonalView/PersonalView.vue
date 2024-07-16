<template>
  <div class="p-4">
    <div class="header d-flex flex-column">
      <div class="header__top d-flex justify-content-between">
        <div class="header__top--left d-flex align-items-center gap-2">
          <i class="bi bi-person-circle h2"></i>
          <h5>Personal</h5>
        </div>
        <div v-if="activeKey == 1">
          <create-button buttonLabel="Create bot" @showModal="showModal"></create-button>
          <create-bot-modal v-model:open="open" @closeModal="closeModal"></create-bot-modal>
        </div>
        <div v-else>
          <create-button buttonLabel="Create knowledge base"></create-button>
        </div>
      </div>
      <div class="header__bottom d-flex align-items-center justify-content-between mt-3">
        <div class="tabs">
          <a-tabs @change="handleChangeActiveKey" :activeKey="activeKey">
            <a-tab-pane key="1" tab="Bots"></a-tab-pane>
            <a-tab-pane key="2" tab="Plugins" disabled></a-tab-pane>
            <a-tab-pane key="3" tab="Workflows" disabled></a-tab-pane>
            <a-tab-pane key="4" tab="Knowledge bases"></a-tab-pane>
            <a-tab-pane key="5" tab="Cards" disabled></a-tab-pane>
          </a-tabs>
        </div>
        <div class="filter d-flex gap-2">
          <a-input-search placeholder="Search" style="width: 200px" />
          <a-select style="width: 150px" :value="selectedValue" @change="handleChangeSelectedValue">
            <a-select-option value="All">All</a-select-option>
            <a-select-option value="Published">Published</a-select-option>
            <a-select-option value="My favorites">My favorites</a-select-option>
          </a-select>
        </div>
      </div>
    </div>
    <div class="main-content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter, onBeforeRouteUpdate } from 'vue-router'
import CreateButton from '@/components/Button/CreateButton.vue'
import CreateBotModal from '@/components/Modal/CreateBotModal.vue';

const tabsData = [
  {
    key: '1',
    tab: 'Bots',
    buttonLabel: 'Create bot',
    navigate: `/space/${spaceId}/bot`,
    path: 'bot'
  },
  {
    key: '2',
    tab: 'Plugins',
    buttonLabel: 'Create plugin',
    navigate: `/space/${spaceId}/plugin`,
    path: 'plugin'
  },
  {
    key: '3',
    tab: 'Workflows',
    buttonLabel: 'Create workflow',
    navigate: `/space/${spaceId}/workflow`,
    path: 'workflow'
  },
  {
    key: '4',
    tab: 'Knowledge bases',
    buttonLabel: 'Create knowledge base',
    navigate: `/space/${spaceId}/knowledge`,
    path: 'knowledge'
  },
  {
    key: '5',
    tab: 'Cards',
    buttonLabel: 'Created card',
    navigate: `/space/${spaceId}/card`,
    path: 'card'
  }
]
const route = useRoute()
const router = useRouter()
const path = route.fullPath.split('/')
const lastSegment = ref(path[path.length - 1])
const spaceId = '62'
const selectedValue = ref('All')
const activeKey = ref('1')
const open = ref(false)

tabsData.forEach((tabData) => {
  if (tabData.path == lastSegment.value) {
    activeKey.value = tabData.key
  }
})

const showModal = () => {
  open.value = true
}
const closeModal = () => {
  open.value = false
}
const handleChangeActiveKey = (newActiveKey) => {
  activeKey.value = newActiveKey
  router.push(tabsData[newActiveKey - 1].navigate)
}
const handleChangeSelectedValue = (newSelectedValue) => {
  selectedValue.value = newSelectedValue
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}
i {
  color: var(--color-background-base);
}
</style>
