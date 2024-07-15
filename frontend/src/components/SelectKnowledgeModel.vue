<template>
  <a-modal v-model:open="isVisible" title="Select Knowledge" centered width="1000px" :bodyStyle="{ height: '500px' }"
    :footer="null" @ok="closeModal">
    <div class="select-knowledge pt-3">
      <div class="select-knowledge-header d-flex flex-row justify-content-between align-items-center">
        <div class="d-flex">
          <div class="type-knowledge">All</div>
          <div class="mx-2 semi-divider-vertical"></div>
          <div class="type-knowledge">Document</div>
          <div class="mx-2 semi-divider-vertical"></div>
          <div class="type-knowledge">Table</div>
          <div class="mx-2 semi-divider-vertical"></div>
          <div class="type-knowledge">Photo</div>
        </div>

        <div class="create-knowledge">
          <button>
            <RouterLink to="/space/upload"><span style="color: white;">Create knowledge</span></RouterLink>
          </button>
        </div>
      </div>
      <div class="select-knowledge-content d-flex flex-column justify-content-center">
        <div class=" d-flex justify-content-center align-items-center">
          <div class="d-flex flex-column align-items-center">
            <div>
              <!-- image -->
            </div>
            <div>
              <h4 style="font-size: 16px; font-weight: 600;">No knowledge base found</h4>
              <div style="font-size: 13px; margin-top: 8px;">Please create first and then add</div>
              <div class="d-flex justify-content-center mt-4">
                <button>
                  <RouterLink to="/space/upload"><span style="color: white;">Create knowledge</span></RouterLink>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </a-modal>
</template>

<script setup>
import { ref, defineEmits } from 'vue';
import { RouterLink } from 'vue-router';

const isVisible = ref(false);
const emit = defineEmits(['update:visible']);

const closeModal = () => {
  isVisible.value = false;
  emit('update:visible', false);
};

const showModal = () => {
  isVisible.value = true;
  emit('update:visible', true);
};

defineExpose({
  showModal
});
</script>

<style lang="scss" scoped>
button {
      background-color: rgb(59, 106, 187);
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 0 solid transparent;
      border-radius: 8px;
      outline: none;
      padding-bottom: 6px;
      padding-left: 16px;
      padding-right: 16px;
      padding-top: 6px;

      &:hover {
        background-color: rgb(8, 50, 124);
      }
    }

.select-knowledge {
  height: 100%;
  .select-knowledge-header {
    .type-knowledge {
      color: #1d1c2399;
      cursor: pointer;
      font-weight: 600;
      height: 14px;
      line-height: 20px;
    }

    .semi-divider-vertical {
      border-bottom: 0;
      border-left: 1px solid #ccc;
      display: inline-block;
      height: 20px;
      margin: 0 1px 0 1px;
      vertical-align: middle;
    }

    
  }
  .select-knowledge-content{
    height: calc(100% - 34px);
  }
}
</style>