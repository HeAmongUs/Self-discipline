<template>
  <div>
    <h1 class="deep-orange-text">{{ username }}</h1>
    <div class="canvas">
      <canvas ref="profileCanvas" id="myCanvas"></canvas>
    </div>
  </div>
</template>

<script>
export default {
  name: "Profile",
  data() {
    return {
      completedDailyTaskList: [],
    }
  },
  async mounted() {
    this.completedDailyTaskList = (await this.$api.dailyTask.completed()).data
    this.setup()
  },
  computed: {
    username() {
      return this.$store.getters.userInfo.username || null
    },
  },
  methods: {
    setup() {
      const date = new Date(this.completedDailyTaskList[0].date)
      const months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
      ]
      const daysInMonth = new Date(
        date.getFullYear(),
        date.getMonth() + 1,
        0
      ).getDate()
      const month = months[date.getMonth()]

      const labels = Array.from({ length: daysInMonth }, (v, k) => k + 1)

      const completedDailyTaskDayCount = labels.reduce((target, key) => {
        target[key] = 0
        return target
      }, {})

      for (let i = 0; i < this.completedDailyTaskList.length; i++) {
        completedDailyTaskDayCount[
          this.completedDailyTaskList[i].date.slice(8, 10)
        ]++
      }

      const ctx = this.$refs.profileCanvas
      // eslint-disable-next-line no-undef
      const chart = new Chart(ctx, {
        type: "line",
        data: {
          labels: labels.map((label) => {
            return `${label}`
          }),
          datasets: [
            {
              label: "Completed",
              data: Object.values(completedDailyTaskDayCount),
              fill: false,
              borderColor: "rgba(54, 162, 235, 1)",
              backgroundColor: "rgba(54, 162, 235, 1)",
            },
          ],
        },
        options: {
          responsive: false,
          maintainAspectRatio: false,
          interaction: {
            mode: "index",
            intersect: false,
          },
          plugins: {
            title: {
              display: true,
              text: `${month} Statistic`,
              font: { size: "24px" },
            },
            tooltip: {
              enabled: false,
              position: "nearest",
              external: this.externalTooltipHandler,
            },
          },
        },
      })
      chart.resize(window.screen.width / 2, 500)
    },
    getOrCreateTooltip(chart) {
      let tooltipEl = chart.canvas.parentNode.querySelector("div")

      if (!tooltipEl) {
        tooltipEl = document.createElement("div")
        tooltipEl.style.background = "rgba(0, 0, 0, 0.7)"
        tooltipEl.style.borderRadius = "3px"
        tooltipEl.style.color = "white"
        tooltipEl.style.opacity = 1
        tooltipEl.style.pointerEvents = "none"
        tooltipEl.style.position = "absolute"
        tooltipEl.style.transform = "translate(-50%, 0)"
        tooltipEl.style.transition = "all .1s ease"

        const table = document.createElement("table")
        table.style.margin = "0px"

        tooltipEl.appendChild(table)
        chart.canvas.parentNode.appendChild(tooltipEl)
      }

      return tooltipEl
    },
    externalTooltipHandler(context) {
      // Tooltip Element
      const { chart, tooltip } = context
      const tooltipEl = this.getOrCreateTooltip(chart)

      // Hide if no tooltip
      if (tooltip.opacity === 0) {
        tooltipEl.style.opacity = 0
        return
      }

      // Set Text
      if (tooltip.body) {
        const titleLines = tooltip.title || []
        const bodyLines = tooltip.body.map((b) => b.lines)

        const tableHead = document.createElement("thead")

        titleLines.forEach((title) => {
          const tr = document.createElement("tr")
          tr.style.borderWidth = 0

          const th = document.createElement("th")
          th.style.borderWidth = 0
          const text = document.createTextNode(title)

          th.appendChild(text)
          tr.appendChild(th)
          tableHead.appendChild(tr)
        })

        const tableBody = document.createElement("tbody")
        bodyLines.forEach((body, i) => {
          const colors = tooltip.labelColors[i]

          const span = document.createElement("span")
          span.style.background = colors.backgroundColor
          span.style.borderColor = colors.borderColor
          span.style.borderWidth = "2px"
          span.style.marginRight = "10px"
          span.style.height = "10px"
          span.style.width = "10px"
          span.style.display = "inline-block"

          const tr = document.createElement("tr")
          tr.style.backgroundColor = "inherit"
          tr.style.borderWidth = 0

          const td = document.createElement("td")
          td.style.borderWidth = 0

          const text = document.createTextNode(body)

          td.appendChild(span)
          td.appendChild(text)
          tr.appendChild(td)
          tableBody.appendChild(tr)
        })

        const tableRoot = tooltipEl.querySelector("table")

        // Remove old children
        while (tableRoot.firstChild) {
          tableRoot.firstChild.remove()
        }

        // Add new children
        tableRoot.appendChild(tableHead)
        tableRoot.appendChild(tableBody)
      }

      const { offsetLeft: positionX, offsetTop: positionY } = chart.canvas

      // Display, position, and set styles for font
      tooltipEl.style.opacity = 1
      tooltipEl.style.left = positionX + tooltip.caretX + "px"
      tooltipEl.style.top = positionY + tooltip.caretY + "px"
      tooltipEl.style.font = tooltip.options.bodyFont.string
      tooltipEl.style.padding =
        tooltip.options.padding + "px " + tooltip.options.padding + "px"
    },
  },
}
</script>

<style scoped>
.canvas {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
