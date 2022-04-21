<template>
  <div class="daily-task-list">
    <task-input @createTask="(taskTitle) => createTask(taskTitle)" />
    <task-list
      :taskList="sortedTasks"
      @updateTask="(taskId) => showUpdateModal(taskId)"
      @deleteTask="(taskId) => deleteTask(taskId)"
      @completeTask="(task) => completeTask(task)"
    />
    <modal-window
      v-if="showModal"
      @showModal="showModal = !showModal"
      @deleteTarget="(taskId) => deleteTask(taskId)"
      @updateTarget="(taskId, taskPayload) => updateTask(taskId, taskPayload)"
    >
      <template v-slot:title>Изменить задачу</template>
      <template v-slot:content
        ><daily-task-update-form :task="taskToUpdate"
      /></template>
    </modal-window>
  </div>
</template>

<script>
import TaskList from "./TaskList"
import TaskInput from "./TaskInput"
import ModalWindow from "../UI/ModalWindow"
import DailyTaskUpdateForm from "./DailyTaskUpdateForm"
export default {
  name: "DailyTaskList",
  components: { DailyTaskUpdateForm, ModalWindow, TaskInput, TaskList },
  data() {
    return {
      dailyTaskList: [],
      taskToUpdate: {},
      showModal: false,
    }
  },
  async created() {
    this.dailyTaskList = (await this.$api.dailyTask.list()).data
  },
  methods: {
    showUpdateModal(id) {
      this.taskToUpdate = this.dailyTaskList.find((task) => task.id === id)
      this.showModal = true
    },
    async createTask(taskTitle) {
      const newTask = {
        title: taskTitle,
        description: "",
        streak: 0,
        order: this.dailyTaskList.length + 1,
      }

      const r = await this.$api.dailyTask.create(newTask)
      if (r.status === 200) {
        this.dailyTaskList.push(newTask)
      }
    },
    async updateTask(id, payload) {
      const r = await this.$api.dailyTask.update(id, payload)
      if (r.status === 200) {
        for (const k in payload) this.taskToUpdate[k] = payload[k]
      }
      this.showModal = !this.showModal
    },
    async completeTask(task) {
      task.completed = !task.completed

      await this.$api.dailyTask.complete(task.id, {
        daily_task: task.id,
        value: task.completed,
      })
    },
    async deleteTask(id) {
      await this.$api.dailyTask.delete(id)
      this.dailyTaskList = this.dailyTaskList.filter((task) => task.id !== id)
    },
  },
  computed: {
    sortedTasks() {
      // сортировка по завершенности и порядку
      return [...this.dailyTaskList].sort((a, b) => {
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
}
</script>

<style scoped>
.daily-task-list {
  max-width: 450px;
}
</style>
