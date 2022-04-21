<template>
  <teleport to="body">
    <div class="modal-window" @click="showModal">
      <div class="modal-window-wrapper" @click.stop="">
        <div class="modal-window-header">
          <div class="modal-window__title">
            <slot name="title">slotNameTitle</slot>
          </div>
        </div>
        <div class="modal-window-content">
          <slot name="content">slotNameContent</slot>
        </div>
      </div>
    </div>
  </teleport>
</template>

<script>
export default {
  name: "ModalWindow",
  emits: ["showModal", "updateTarget", "deleteTarget", "createTarget"],
  methods: {
    showModal() {
      this.$emit("showModal")
    },
  },
}
</script>

<style scoped lang="scss">
.modal-window {
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(30, 144, 255, 0.4);
  display: flex;
  position: fixed;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  &__title {
    width: 100%;
    font-size: 28px;
    color: #333;
    text-align: center;
  }

  &-wrapper {
    padding: 20px;
    background: #fff;
    min-height: 50px;
    min-width: 300px;
  }
}
</style>
