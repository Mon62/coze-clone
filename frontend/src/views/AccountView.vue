<template>
    <div style="padding: 50px 150px;">
        <div class="d-flex justify-content-between align-items-center">
            <div class="d-flex justify-content-center align-items-center gap-4">
                <div class="avatar">
                    <img src="../assets/coze-logo.jpg" alt="">
                </div>
                <p class="username">userz3sDff</p>
            </div>
            <div>
                <SettingOutlined class="icon-setting" />
            </div>
        </div>

        <div class="d-flex flex-column p-3">
            <div class="item-field-info">
                <label for="">Username</label>
                <div v-if="!openEdit" class="d-flex align-items-center gap-3">
                    <span>user3Efd</span>
                    <FormOutlined class="icon-edit" @click="openEdit = !openEdit" />
                </div>
                
            <!-- form edit username -->
                <div v-if="openEdit" class="d-flex gap-3">
                    <a-input v-model:value="value" size="small" style="width: 300px;"/>
                    <a-button @click="openEdit = !openEdit"  >Cancel</a-button>
                    <a-button type="primary">Save</a-button>
                </div>
             <!-- form edit username -->

            </div>
            <div class="item-field-info">
                <label for="">Email</label>
                <div class="d-flex align-items-center gap-3">
                    <span>abc@gmail.com</span>
                </div>
            </div>
            <div class="item-field-info">
                <label for="">Account</label>
                <div class="d-flex align-items-center gap-3">
                    <a-popconfirm title="Are you sure delete account？" ok-text="Yes" cancel-text="No">
                        <DeleteOutlined class="icon-remove" />
                    </a-popconfirm>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { SettingOutlined, FormOutlined, DeleteOutlined } from '@ant-design/icons-vue';
import { ref } from 'vue';

const openEdit = ref(false)
</script>

<style lang="scss" scoped>
.avatar img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
}

.username {
    font-size: 20px;
    font-weight: 600;
}

.icon-setting{
    padding: 10px;
    background-color: #e9dfdf;
    border-radius: 8px;
    &:hover{
        cursor: pointer;
        background-color: #958c8c
    }
}

.item-field-info {
    margin-top: 20px;

    label {
        font-size: 15px;
        font-weight: 600;
        color: #1c1f23;
        margin-bottom: 5px;
    }

    div {
        span {
            font-size: 14px;
            color: rgba(28, 29, 35, .8);
        }

        .icon-edit {
            color: rgb(77 83 232);
            padding: 5px;
            font-size: 18px;

            &:hover {
                background-color: #ccc;
                cursor: pointer;
            }
        }

        .icon-remove {
            color: rgb(198, 31, 56);
            font-size: 20px;
            padding: 5px 0;

            &:hover {
                cursor: pointer;
                background-color: #ccc
            }
        }
    }
}
</style>