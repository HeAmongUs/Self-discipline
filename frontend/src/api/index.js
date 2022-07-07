import instance from "./instance"
import authModule from "./auth"
import userModule from "./user"
import dailyTaskModule from "./dailyTask"
import taskModule from "./task"

export default {
  auth: authModule(instance),
  user: userModule(instance),
  dailyTask: dailyTaskModule(instance),
  task: taskModule(instance),
}
