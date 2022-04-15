<template>
  <div>
    <textarea
      ref="textarea"
      rows="1"
      class="textarea"
      placeholder="Добавить ежедневное дело"
      v-model="input"
      @keydown.enter.prevent="addNewTask"
    />
  </div>
</template>

<script>
export default {
  name: "TaskInput",
  data() {
    return {
      input: "",
    }
  },
  emits: ["enter"],
  methods: {
    addNewTask() {
      this.$emit("enter", this.input)
      this.input = ""
      this.$refs.textarea.blur()
    },
  },
}
</script>

<style scoped lang="scss">
.textarea {
  width: 100%;
  color: #4e4a57;
  border: 1px solid transparent;
  border-radius: 2px;
  background-color: rgba(26, 24, 29, 0.06);
  margin-bottom: 3px;
  padding: 12px 16px;
  transition: background 0.15s ease-in;
  overflow: hidden;
  font-size: 14px;
  line-height: 1.4;
  font-family: Roboto, sans-serif;

  &::placeholder {
    font-weight: 600;
    color: #333;
  }

  &:hover {
    background: rgba(0, 0, 0, 0.1);
  }
  &:focus {
    outline: none;
    background: #fff;
    border: 1px solid #bda8ff;
  }
}
</style>
