<template>
  <div class="home">
    <task-list :taskList="taskList" />
  </div>
</template>

<script>
import TaskList from "@/components/TaskList"

export default {
  name: "Home",
  components: { TaskList },
  data() {
    return {
      taskList: [],
    }
  },
  async created() {
    this.taskList = (await this.$api.dailyTask.list()).data
  },
  methods: {},
  computed: {},
  watch: {},
}
</script>

<style scoped lang="scss"></style>
