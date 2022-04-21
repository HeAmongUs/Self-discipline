<template>
  <ul class="task-list">
    <span v-if="taskList.length === 0">Задач нет</span>
    <task-item
      v-else
      v-for="task in taskList"
      :task="task"
      :key="task.order"
      class="task-list-item"
      draggable="true"
      @dragstart="dragStartHandler(task)"
      @dragenter="dragEnterHandler(task)"
      @completeTask="(completedTask) => completeTask(completedTask)"
      @updateTask="(taskId) => updateTask(taskId)"
      @deleteTask="(taskId) => deleteTask(taskId)"
    />
  </ul>
</template>

<script>
import TaskItem from "./TaskItem"
export default {
  name: "TaskList",
  components: { TaskItem },
  props: {
    taskList: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      draggingTask: null,
    }
  },
  emits: ["completeTask", "updateTask", "deleteTask"],
  methods: {
    completeTask(task) {
      this.$emit("completeTask", task)
    },
    updateTask(id) {
      this.$emit("updateTask", id)
    },
    deleteTask(id) {
      this.$emit("deleteTask", id)
    },
    dragStartHandler(dragging) {
      this.draggingTask = dragging
    },
    dragEnterHandler(targetTask) {
      if (
        targetTask !== this.draggingTask &&
        targetTask.completed === this.draggingTask.completed
      ) {
        ;[this.draggingTask.order, targetTask.order] = [
          targetTask.order,
          this.draggingTask.order,
        ]
      }
    },
  },

  watch: {},
}
</script>

<style scoped lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@300;400;700&family=Roboto:ital,wght@0,300;0,400;0,700;1,900&display=swap");
.task {
  &-list {
    margin-left: 10px;
    padding: 8px;
    background: rgba(0, 0, 0, 0.1);
    transition: 0.3s;
  }
}
</style>
