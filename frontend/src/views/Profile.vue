<template>
  <div>
    <h1>{{ username }}</h1>
    <canvas id="myCanvas"></canvas>
  </div>
</template>

<script>
export default {
  name: "Profile",
  data() {
    return {}
  },
  mounted() {

  },
  computed: {
    username() {
      return this.$store.getters.userInfo.username || null
    },
  },
  methods: {
    setup(completedDailyTaskList) {
      const ctx = document.getElementById("myCanvas")
      // eslint-disable-next-line no-undef
      new Chart(ctx, {
        type: "pie",
        data: {
          labels: categories.map((c) => c.title),
          datasets: [
            {
              label: "Расходы по категориям",
              data: categories.map((c) => {
                return this.records.reduce((total, record) => {
                  if (record.categoryId === c.id && record.type === "outcome") {
                    total += record.amount
                  }
                  return total
                }, 0)
              }),
              backgroundColor: [
                "rgba(255, 99, 132, 0.2)",
                "rgba(54, 162, 235, 0.2)",
                "rgba(255, 206, 86, 0.2)",
                "rgba(75, 192, 192, 0.2)",
                "rgba(153, 102, 255, 0.2)",
                "rgba(255, 159, 64, 0.2)",
              ],
              borderColor: [
                "rgba(255, 99, 132, 1)",
                "rgba(54, 162, 235, 1)",
                "rgba(255, 206, 86, 1)",
                "rgba(75, 192, 192, 1)",
                "rgba(153, 102, 255, 1)",
                "rgba(255, 159, 64, 1)",
              ],
              borderWidth: 1,
            },
          ],
        },
        options: {
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        },
      })
    },
  },
}
</script>

<style scoped></style>
