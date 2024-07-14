<template>
    <div style="min-width: 1280px; min-height: 600px;">
        <div class="wrapper">
            <div class="content">
                <div class="logo">
                    <img src="../assets/coze-logo.jpg" alt="logo"
                        style="width: 25px; height: 25px; border-radius: 2px;">
                    <span>coze</span>
                </div>
                <div class="wrapper-form-login">
                    <div class="form-login">
                        <div class="mb-5 fw-bold fs-2">Welcome to Coze</div>

                        <div v-if="stateForm === 'login'" style="width: 100%;">
                            <button class="google-btn">
                                <span class="d-flex align-items-center text-center justify-content-center gap-2">
                                    <img src="../assets/gg.png" alt="" style="width: 15px; height: 15px;">
                                    <span>Continue with google</span>
                                </span>
                            </button>
                            <div class="d-flex justify-content-center align-items-center fs-6 fw-light lh-1 my-4"
                                style="width: 100%">
                                <span class="px-1 fw-lighter">or</span>
                            </div>
                        </div>

                        <div>
                            <div class="email-input mt-3">
                                <span style="color: #010101; font-size: 14px;">Email</span>
                                <input type="email" required>
                            </div>
                            <div class="password-input mt-4">
                                <span style="color: #010101; font-size: 14px;">Password</span>
                                <input type="password" required>
                            </div>
                        </div>

                        <div class="btn-next">
                            <span>Next</span>
                        </div>
                        <div v-if="stateForm === 'login'" class="mt-2 fw-medium">
                            Don't have an account yet, register<span @click="changeStateForm1"
                                style="color: #4d53e8; cursor: pointer;">
                                here</span>
                        </div>
                        <div v-if="stateForm === 'signup'" class="mt-2 fw-medium">
                            Already have an account, login<span @click="changeStateForm2"
                                style="color: #4d53e8; cursor: pointer;">
                                here</span>
                        </div>

                        <span class="policy">
                            By continuing, you are agreeing to Coze's<span style="color: #4d53e8;;"> Terms of
                                Service</span> and <span style="color: #4d53e8;;">Privacy Policy</span>
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const stateForm = ref('login')
const changeStateForm1 = () => {
    stateForm.value = 'signup';
};
const changeStateForm2 = () => {
    stateForm.value = 'login';
};
</script>

<style lang="scss" scoped>
.wrapper {
    width: 100%;
    height: 100vh;
    position: relative;

    .content {
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(173deg, #ecf4ff -.79%, #d3e1ff 94.5%);
        height: 100%;
        width: 100%;

        .logo {
            display: flex;
            justify-content: center;
            align-items: center;
            color: #000;
            font-size: 22px;
            font-weight: 600;
            position: absolute;
            top: 16px;
            left: 24px;
        }

        .wrapper-form-login {
            background: #fff;
            border: 1px solid rgba(28, 31, 35, .08);
            border-radius: 12px;
            box-shadow: 0 4px 14px 0 rgba(0, 0, 0, .1), 0 0 1px 0 rgba(0, 0, 0, .3);
            height: 642px;
            padding: 40px 64px;
            width: 482px;

            .form-login {
                align-items: center;
                display: flex;
                flex-direction: column;
                height: 100%;
                width: 100%;

                .google-btn {
                    background-color: rgb(255 255 255);
                    width: 100%;
                    color: #1d1c23;
                    font-weight: 600;
                    height: 40px;
                    line-height: 20px;
                    cursor: pointer;
                    border-radius: 8px;
                    border: 1px rgb(240 240 245) solid;
                }

                input {
                    width: 100%;
                    outline: none;
                    border: none;
                    border-bottom: 1px solid #d7d7d7;
                    border-radius: 0;
                    font-size: 14px;
                    font-weight: 400;
                    height: 34px;
                    line-height: 34px;
                }

                .btn-next {
                    background-color: rgb(77 83 232);
                    height: 40px;
                    margin-top: 24px;
                    width: 100%;
                    border-radius: 8px;
                    border: 0 solid transparent;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    font-size: 14px;
                    font-weight: 600;
                    color: white;
                    cursor: pointer;
                }

                .policy {
                    font-size: 13px;
                    font-weight: 400;
                    line-height: 20px;
                    color: rgba(29, 28, 35, .6);
                    height: 44px;
                    margin-top: auto;
                    text-align: center;
                    white-space: break-spaces;
                }
            }

        }
    }
}
</style>