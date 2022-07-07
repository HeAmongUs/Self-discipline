export default function (instance) {
  return {
    list() {
      return instance.get("api/v1/task/")
    },
    create(payload) {
      return instance.post("api/v1/task/", payload)
    },

    complete(pk, payload) {
      return instance.patch(`api/v1/task/${pk}/`, payload)
    },
    completed() {
      return instance.get(`api/v1/task/completed/`)
    },
    update(pk, payload) {
      return instance.patch(`api/v1/task/${pk}/`, payload)
    },
    delete(pk) {
      return instance.delete(`api/v1/task/${pk}/`)
    },
  }
}
