<template>
    <div>
        <div class="d-flex align-items-center justify-content-between mb-3 py-4 px-5"
            style="box-shadow: 0 2px 2px 0 rgba(29, 28, 35, .04);">
            <div class="d-flex align-items-center">
                <RouterLink to="/space" style=" padding: 4.5px 12px; font-size: 16px;">
                    <CloseOutlined />
                </RouterLink>
                <span>
                    <FileTextOutlined style="font-size: 30px; color: royalblue;" />
                </span>

                <span style="margin-left: 8px; font-weight: 700; font-size: 18px;">Create new knowledge base</span>

            </div>
        </div>

        <div style="padding: 32px 24px 0;">
            <div style="height: 100%; min-width: 1008px; width: calc(100% - 200px); margin: 0 auto;">
                <div style="margin: 0 20px 36px;">
                    <a-steps :current="step" size="small" :items="[
                        {
                            title: 'Upload',
                        },
                        {
                            title: 'Set segmentation',
                        },
                        {
                            title: 'Process Data',
                        },
                    ]"></a-steps>
                </div>

                <div v-if="step === 0">
                    <a-upload-dragger v-model:fileList="fileList" name="file" :multiple="true"
                        action="" 
                        @change="handleChange"
                        @drop="handleDrop">
                        <p class="ant-upload-drag-icon">
                            <inbox-outlined></inbox-outlined>
                        </p>
                        <p class="ant-upload-text">Click or drag file to this area to upload</p>
                        <p class="ant-upload-hint">
                            Support for a single or bulk upload. Strictly prohibit from uploading company data or other
                            band files
                        </p>
                    </a-upload-dragger>
                </div>

                <div v-if="step === 1" class="d-flex flex-column gap-4">
                    <div
                        style="display: flex; padding: 16px; border: 1px solid  rgba(28, 31, 35, .08); border-radius: 8px; gap: 8px; background-color: #f1f2fe;">
                        <input type="radio" name="segmentation" id="">
                        <span>Automatic segmentation & cleaning</span>
                    </div>
                    <div
                        style="display: flex; flex-direction: column; padding: 16px; border: 1px solid rgba(28, 31, 35, .08); border-radius: 8px; gap: 8px; background-color: #f1f2fe">
                        <div class="d-flex gap-2">
                            <input type="radio" name="segmentation" id="">
                            <span>Custom</span>
                        </div>
                        <div style="width: 100%; margin-top: 10px; padding-left: 16px;">

                                <div style="margin-bottom: 30px;">
                                    <label for="">Segment ID</label>
                                    <div>
                                        <select style="width: 100%; border: 1px solid rgb(56 55 67 / 8%); outline: none; padding: 5px 3px; border-radius: 5px;" name="" id="">
                                            <option value="">Line break</option>
                                            <option value="">1</option>
                                            <option value="">2</option>
                                            <option value="">3</option>
                                        </select>
                                    </div>
                                </div>

                                <div>
                                    <label for="">Maximum segment length</label>
                                    <div>
                                        <input type="text" name="" id="" style="width: 100%; border: 1px solid rgb(56 55 67 / 8%); outline: none; padding: 5px 3px; border-radius: 5px;">
                                    </div>
                                </div>

                        </div>
                    </div>
                </div>

                <div class="d-flex justify-content-end mt-5 gap-3">
                    <button v-if="step >= 1" @click="step--"
                        style="background-color: whitesmoke; border-radius: 8px; border: 0 solid transparent; outline: none; height: 40px; padding: 8px 16px;">
                        <span>Previous</span>
                    </button>
                    <button @click="step++"
                        style="background-color: rgb(77 83 232); border-radius: 8px; border: 0 solid transparent; outline: none; height: 40px; color: white; padding: 8px 16px;">
                        <span>Next</span>
                    </button>
                </div>
            </div>
        </div>

    </div>
</template>

<script setup>
import { CloseOutlined, FileTextOutlined, InboxOutlined } from '@ant-design/icons-vue';
import { ref } from 'vue';
import { message } from 'ant-design-vue';

const step = ref(0)

const fileList = ref([]);
const handleChange = info => {
    const status = info.file.status;
    if (status !== 'uploading') {
        console.log(info.file, info.fileList);
    }
    if (status === 'done') {
        message.success(`${info.file.name} file uploaded successfully.`);
    } else if (status === 'error') {
        message.error(`${info.file.name} file upload failed.`);
    }
};
function handleDrop(e) {
    console.log(e);
}
</script>

<style lang="scss" scoped></style>