<template>
  <div class="modalrapper" v-if="isIdeaModalVisible">
    <div class="backdrop" @click.self="closeIdeaModal">
      <div class="ideamodal">
        <div>
            <h1> Submit Ideas</h1>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'IdeaModal',
  props: {
    isIdeaModalVisible: {
      type: Boolean,
      required: true
    }
  },
  methods: {
    closeIdeaModal() {
      this.$emit('closeIdeaModal')
      console.log('toggleModal closeModal: ', this.isIdeaModalVisible)
    }
  }
}
</script>

<style scoped>
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

.ideamodal {
  width: 90%;
  max-width: 40rem;
  background: white;
  border-radius: 6px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  z-index: 10;
  overflow: hidden;
}
</style>
