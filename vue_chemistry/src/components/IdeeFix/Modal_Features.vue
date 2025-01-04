<template>
  <div class="modalrapper" v-if="isFeatureModalVisible">
    <div class="backdrop" @click.self="closeFeatureModal">
        <div class="featuremodal">
            <h1> Feature Overview</h1>
            <div class="featuremodal_buttons">
                <button @click="openFeatureEditor" class="text_button">
                    <img class="text_button_img" src="@/assets/buttons_icons/plus.png" alt="Add Instruction" />
                    <h3> Add Feature</h3>
                </button>
            </div>
            <hr>
            <div class="feature_table">
                
            </div>

        </div>
    </div>
    <FeatureEditorModal :isFeatureEditorModalVisible="isFeatureEditorModalVisible" @closeFeatureEditorModal="closeFeatureEditorModal"></FeatureEditorModal>
  </div>
</template>

<script>
import FeatureEditorModal from '@/components/IdeeFix/Modal_FeatureEditor.vue'

export default {
    name: "FeatureModal",
    components: {
        FeatureEditorModal
    },
    props: {
        isFeatureModalVisible: {
            type: Boolean,
            required: true
        }
    },
    data() {
        return {
            isFeatureEditorModalVisible: false,
        }
    },
    methods: {
        openFeatureEditor() {
            console.log('openFeatureEditor');
            this.isFeatureEditorModalVisible = true;
        },
        closeFeatureEditorModal() {
            this.isFeatureEditorModalVisible = !this.isFeatureEditorModalVisible;
        },
        closeFeatureModal() {
            this.$emit('closeFeatureModal');
        }
    }

}
</script>

<style>
.backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 10;
}
.modalrapper {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 10;
}

.featuremodal {
    width: 90%;
    min-width: 50rem;
    height: 80%;
    background: white;
    border-radius: 6px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
    z-index: 10;
    overflow: hidden;
}

.featuremodal_buttons {
    display: flex;
    justify-content: center;
    align-items: center;
}

.text_button {
    display: block;
    align-items: center;
    justify-content: center;
    padding: 0.5rem 1rem;
    margin: 1rem;
    border: 1px solid #000000;
    border-radius: 24px;
    background-color: white;
    cursor: pointer;
}

.text_button:hover {
    background-color: var(--primary-color);
}

.text_button_img {
    width: 28px;
    height: 28px;
    margin: 0.2rem 0.5rem;
}

</style>