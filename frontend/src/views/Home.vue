<template>
  <div class="home">
    <daily-task-list />
    <div>
      <task-input @createTask="(taskTitle) => createTask(taskTitle)" />
      <task-list :taskList="taskList"></task-list>
    </div>

  </div>
</template>

<script>
import DailyTaskList from "../components/dailyTask/DailyTaskList"
import TaskList from "../components/dailyTask/TaskList"
import TaskInput from "../components/dailyTask/TaskInput";
export default {
  name: "Home",
  components: {TaskInput, TaskList, DailyTaskList },

  data() {
    return {
      taskList: [],
    }
  },
  async mounted() {

    this.taskList = (await this.$api.task.list()).data
  },

  methods: {
    async createTask(taskTitle) {
      const newTask = {
        title: taskTitle,
        description: "",
        order: this.taskList.length + 1,
      }

      const r = await this.$api.task.create(newTask)
      if (300 < r.status >= 200) {
        this.taskList.push(newTask)
      }
    },
  },
  computed: {},
  watch: {},
}
</script>

<style scoped lang="scss">
.home {
  display: flex;
}
</style>
