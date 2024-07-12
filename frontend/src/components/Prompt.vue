<template>
    <div class="prompt">
        <header class="prompt_header">
            <div class="prompt_header_title">
                <span>Persona & Prompt</span>
            </div>
            <div class="prompt_header_optimize">
                <span>Optimize</span>
            </div>
        </header>

        <div class="prompt_area_wrapper">
            <div class="prompt_area">
                <textarea name="" id="" placeholder="Design the bot's persona, features and workflows using natural language."></textarea>
            </div>
        </div>
    </div>
</template>

<script setup>

</script>

<style lang="scss" scoped>
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
.prompt {
    display: flex;
    flex-direction: column;
    width: 100%;

    .prompt_header {
        display: flex;
        align-items: center;
        height: 40px;
        justify-content: space-between;
        width: 100%;
        padding: 0 28px;

        .prompt_header_title {
            span {
                font-size: 14px;
                font-weight: 600;
                line-height: 20;
            }
        }

        .prompt_header_optimize {
            cursor: pointer;
            cursor: not-allowed;

            span {
                font-size: 14px;
                font-weight: 600;
                color: #787171;
            }
        }
    }

    .prompt_area_wrapper {
        height: calc(100vh - 48px);
        overflow: auto;

        .prompt_area {
            height: 100%;
            width: 100%;
            padding: 28px;

            textarea {
                
                width: 100%;
                height: 100%;
                color: rgba(28, 29, 35, .8);
                font-size: 13px;
                line-height: 22px;
                border: 0 solid transparent;
                outline: none;
                resize: none;
                padding: 0;
            }
        }
    }
}
</style>