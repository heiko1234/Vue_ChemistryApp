<template>
  <div class="modalrapper" v-if="isContactModalVisible">
    <div class="backdrop" @click.self="closeContactModal">
      <div class="contactmodal">
        <slot> </slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ContactModal',
  props: {
    isContactModalVisible: {
      type: Boolean,
      required: true
    }
  },
  methods: {
    closeContactModal() {
      this.$emit('closeContactModal')
      // console.log('toggleModal closeModal: ', this.isModalVisible)
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

.contactmodal {
  width: 90%;
  max-width: 40rem;
  background: white;
  border-radius: 6px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  z-index: 10;
  overflow: hidden;
}
</style>
