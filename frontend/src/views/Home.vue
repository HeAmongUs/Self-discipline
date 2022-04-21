<template>
  <div class="home">
    <daily-task-list />
  </div>
</template>

<script>
import DailyTaskList from "../components/dailyTask/DailyTaskList"
export default {
  name: "Home",
  components: { DailyTaskList },

  data() {
    return {}
  },

  methods: {},
  computed: {},
  watch: {},
}
</script>

<style scoped lang="scss"></style>
