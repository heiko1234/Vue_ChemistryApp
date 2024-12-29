<template>
  <div class="modalrapper" v-if="isFeatureModalVisible">
    <div class="backdrop" @click.self="closeFeatureModal">
        <div class="featuremodal">
            <h1> Feature</h1>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    name: "FeatureModal",
    props: {
        isFeatureModalVisible: {
            type: Boolean,
            required: true
        }
    },
    methods: {
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
    max-width: 50rem;
    background: white;
    border-radius: 6px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
    z-index: 10;
    overflow: hidden;
}

</style>