export default function (instance) {
  return {
    list() {
      return instance.get("api/v1/daily_task/")
    },
    create(payload) {
      return instance.post("api/v1/daily_task/", payload)
    },

    complete(pk, payload) {
      return instance.post(`api/v1/daily_task/complete/${pk}/`, payload)
    },

    completed() {
      return instance.get(`api/v1/daily_task/completed/`)
    },

    update(pk, payload) {
      return instance.patch(`api/v1/daily_task/${pk}/`, payload)
    },
    delete(pk) {
      return instance.delete(`api/v1/daily_task/${pk}/`)
    },
  }
}
