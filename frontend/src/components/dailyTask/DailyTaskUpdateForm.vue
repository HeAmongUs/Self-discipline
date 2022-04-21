<template>
  <form @submit.prevent="">
    <div class="input-field">
      <textarea
        class="materialize-textarea"
        v-model="form.title"
        id="textareaTitle"
      ></textarea>
      <label for="textareaTitle">Title</label>
    </div>

    <div class="input-field">
      <textarea
        class="materialize-textarea"
        v-model="form.description"
        id="textareaDescription"
      ></textarea>
      <label for="textareaDescription">Description</label>
    </div>

    <div class="actions">
      <my-button @click="updateTask">
        <template v-slot:left-icon>
          <i class="tiny left material-icons">mode_edit</i>
        </template>
        Save</my-button
      >
      <my-button @click="deleteTask">
        <template v-slot:left-icon>
          <i class="tiny left material-icons">delete</i>
        </template>
        Delete</my-button
      >
    </div>
  </form>
</template>

<script>
import MyButton from "../UI/MyButton"
export default {
  name: "DailyTaskUpdateForm",
  components: { MyButton },

  props: {
    task: {
      required: true,
      type: Object,
    },
  },
  data() {
    return {
      form: {
        title: "",
        description: "",
      },
    }
  },
  created() {
    this.form = {
      title: this.task.title,
      description: this.task.description,
    }
  },
  mounted() {
    window.M.updateTextFields()
  },
  methods: {
    updateTask() {
      this.$parent.$emit("updateTarget", this.task.id, this.form)
    },
    deleteTask() {
      this.$parent.$emit("deleteTarget", this.task.id)
    },
  },
}
</script>

<style scoped lang="scss">
.actions {
  margin-top: 10px;
  display: flex;
  justify-content: space-between;
}
</style>
