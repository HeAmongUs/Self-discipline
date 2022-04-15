<template>
  <ul class="task-list">
    <task-input @enter="(taskTitle) => addNewTask(taskTitle)" />
    <span v-if="taskList.length === 0">Задач нет</span>
    <task-item
      v-else
      v-for="task in sortedTasks"
      :task="task"
      :key="task.order"
      class="task-list-item"
      draggable="true"
      @dragstart="dragStartHandler(task)"
      @dragenter="dragEnterHandler(task)"
    />
  </ul>
</template>

<script>
import TaskItem from "@/components/TaskItem"
import TaskInput from "@/components/UI/TaskInput"

export default {
  name: "TaskList",
  components: { TaskItem, TaskInput },
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
  methods: {
    async addNewTask(taskTitle) {
      const newTask = {
        title: taskTitle,
        description: "",
        streak: 0,
        order: this.taskList.length + 1,
      }
      await this.$api.dailyTask.create(newTask)
      // eslint-disable-next-line vue/no-mutating-props
      this.taskList.push(newTask)
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
  computed: {
    sortedTasks() {
      // сортировка по завершенности и порядку
      // eslint-disable-next-line vue/no-mutating-props,vue/no-side-effects-in-computed-properties
      return this.taskList.sort((a, b) => {
        if (b.completed > a.completed) {
          return -1
        } else if (b.completed < a.completed) {
          return 1
        } else if (a.order < b.order) {
          return -1
        } else if (a.order > b.order) {
          return 1
        } else {
          return 0
        }
      })
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
    max-width: 450px;
    transition: 0.3s;
  }
}
</style>
