<template>
    <div style="border-left: 1px solid rgba(28, 29, 35, .12);">
        <div class="knowledge_wrapper">
            <div class="knowledge">
                <div class="knowledge_item">
                    <span class="type">Knowledge</span>
                    <div class="knowledge_item_type">
                        <div class="item_type_left">
                            <span>></span>
                            <span>Text</span>
                        </div>
                        <div class="item_type_right">
                            <a-tooltip placement="top" color="white">
                                <template #title>
                                    <span style="color: #111; font-size: 13px;">Add knowledge</span>
                                </template>
                                <div @click="openModal">+</div>
                                
                            </a-tooltip>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>
    <SelectKnowledgeModel ref="knowledgeModal"/>
</template>

<script setup>
import { ref } from 'vue';
import SelectKnowledgeModel from './SelectKnowledgeModel.vue'

const knowledgeModal = ref(null);

const openModal = () => {
  knowledgeModal.value.showModal();
};
</script>

<style lang="scss" scoped>
.knowledge_wrapper {
    // border-left: 1px solid rgba(28, 29, 35, .12);
    display: flex;
    flex-direction: column;
    overflow: hidden;

    .knowledge {
        padding: 8px 12px;

        span.type {
            font-size: 14px;
            font-weight: 600;
            color: #787171;
        }

        .knowledge_item_type {
            display: flex;
            align-items: center;
            justify-content: space-between;
            text-align: center;
            width: 100%;
            height: 40px;
            border-radius: 5px;
            border-bottom: 1px solid rgba(6, 7, 9, 0.10);

            &:hover {
                background-color: #ebe1e1;
            }
        }

        .item_type_left {
            padding: 0 7px;
            display: flex;
            align-items: center;
            align-items: center;
            font-size: 14px;
            font-weight: 600;
            height: 100%;
            line-height: 20px;


            span:nth-child(1) {
                color: #787171;
                margin-right: 8px;
            }
        }

        .item_type_right {
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            height: 100%;
            width: 40px;

            div {
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                padding: 3px;
                width: 20px;
                height: 20px;
                color: #787171;
                cursor: pointer;
                border-radius: 5px;

                &:hover {
                    background-color: #aba2a2;
                }
            }
        }
    }
}


</style>