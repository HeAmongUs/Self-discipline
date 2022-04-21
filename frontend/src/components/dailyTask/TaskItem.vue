<template>
  <li
    :class="{
      'task-completed': task.completed,
    }"
  >
    <div
      class="task-control"
      :class="[
        task.completed ? 'task-control-disabled' : 'task-control-active',
      ]"
    >
      <div class="task-control-container">
        <label
          @click="completeTask"
          :class="[
            task.completed
              ? 'task-control-checkbox-disabled'
              : 'task-control-checkbox-active',
          ]"
          class="task-control-checkbox"
          :for="task.title"
        >
          <span
            :class="[
              task.completed
                ? 'task-control-icon-disabled'
                : 'task-control-icon-active',
            ]"
            class="task-control-icon flex-center"
          >
            <svg
              class="task-control__icon"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 13 10"
            >
              <path
                fill-rule="evenodd"
                d="M4.662 9.832c-.312 0-.61-.123-.831-.344L0 5.657l1.662-1.662 2.934 2.934L10.534 0l1.785 1.529-6.764 7.893a1.182 1.182 0 0 1-.848.409l-.045.001"
              ></path>
            </svg>
          </span>
        </label>
        <input
          class="task-control__checkbox"
          type="checkbox"
          :id="task.title"
        />
      </div>
    </div>
    <div class="task-content">
      <div class="task-clickable-area">
        <div class="task-content-header">
          <h3
            class="task-content__title"
            :class="{ 'task-completed': task.completed }"
          >
            {{ task.title }}
          </h3>
          <my-dropdown>
            <template v-slot:content>
              <ul>
                <li @click="updateTask">
                  <span class="button">
                    <i class="tiny left material-icons">mode_edit</i>
                    Update
                  </span>
                </li>
                <li @click="deleteTask">
                  <span class="button">
                    <i class="tiny left material-icons">delete</i>
                    Delete
                  </span>
                </li>
              </ul>
            </template>
          </my-dropdown>
        </div>
        <p class="task-content__description">{{ task.description }}</p>
      </div>
      <div class="task-advanced-info">
        <div class="task-advanced-info-icons">
          <div class="task-advanced-info-icons-streak">
            <div class="icon-container-streak">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 12 8">
                <path
                  fill-rule="evenodd"
                  d="M11.376 3.15L6.777.086A.5.5 0 0 0 6 .5v6.132a.5.5 0 0 0 .777.416l4.599-3.066a.5.5 0 0 0 0-.832M.777.085L6 3.567.777 7.049A.5.5 0 0 1 0 6.633V.5A.5.5 0 0 1 .777.085"
                ></path>
              </svg>
            </div>
            <span class="streak-data">
              {{ task.streak }}
            </span>
          </div>
          <div class="task-advanced-info-icons-tags">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 14 14">
              <path
                fill-rule="evenodd"
                d="M10 3a1 1 0 1 1 0 2 1 1 0 0 1 0-2zM2.004 6.994L7 2h5l-.004 5.006L7 12l.004-.004-5-5.002zM0 7c0 .55.22 1.05.59 1.41l5 5a1.996 1.996 0 0 0 2.83 0l4.99-4.99c.37-.37.59-.87.59-1.42V2c0-1.11-.89-2-2-2H7c-.55 0-1.05.22-1.41.58l-5 5C.23 5.94 0 6.44 0 7z"
              ></path>
            </svg>
          </div>
        </div>
      </div>
    </div>
  </li>
</template>

<script>
import MyDropdown from "../UI/MyDropdown"
export default {
  name: "TaskItem",
  components: { MyDropdown },

  props: {
    task: {
      type: Object,
      required: true,
    },
  },
  emits: ["completeTask", "updateTask", "deleteTask"],
  methods: {
    completeTask() {
      this.$emit("completeTask", this.task)
    },
    updateTask() {
      this.$emit("updateTask", this.task.id)
    },
    deleteTask() {
      this.$emit("deleteTask", this.task.id)
    },
  },
}
</script>

<style scoped lang="scss">
.dropdown {
  span {
    color: dodgerblue !important;
  }
}
span.button {
  display: flex;
  justify-content: flex-start;
  align-items: center;
}
.task {
  $task: &;
  &-list-item {
    display: flex;
    background: #fff;
    transition: 0.15s ease-in;
    border: 1px solid transparent;

    &:hover {
      .dropdown {
        opacity: 1;
      }
      border: 1px solid dodgerblue;
    }

    &:not(:first-child) {
      margin-top: 2px;
    }
    #{$task}-control {
      min-width: 40px;
      display: flex;
      justify-content: center;
      min-height: 100%;

      &-container {
        min-height: 75px;
      }
      &-active {
        background: #ff944c;
      }
      &-disabled {
        background: #878190;
      }
      &-checkbox {
        margin-top: 16px;
        display: block;
        border-radius: 4px;
        width: 28px;
        height: 28px;
        background: rgba(255, 255, 255, 0.5);
        cursor: pointer;

        &:hover {
          background: rgba(255, 255, 255, 0.8);
        }
      }
      &-icon {
        width: 100%;
        height: 100%;
        transition: 0.2s;
        opacity: 0;

        &:hover,
        &-disabled {
          opacity: 1;
        }
        &-active {
          fill: #7f3300;
        }
        &-disabled {
          fill: #34313a;
        }
      }
      &__icon {
        width: 14px;
      }
      &__checkbox {
        display: none;
      }
    }
    #{$task}-content {
      user-select: none;
      width: 100%;
      padding-bottom: 7px;
      &-header {
        display: flex;
        justify-content: space-between;
      }
      &__title {
        font-family: Roboto Condensed, sans-serif;
        font-size: 16px;
        line-height: 1.25;
        font-weight: 400;
        margin: 6px 15px 4px 0;
      }
      &__description {
        font-size: 13px;
        line-height: 1.4;
        max-width: 350px;
        text-align: justify;
        margin-bottom: 8px;
        margin-right: 20px;
      }
      #{$task}-advanced-info {
        margin-top: 4px;
        display: flex;
        justify-content: flex-end;
        padding: 0 8px;
        &-icons {
          display: flex;
          &-streak {
            display: flex;
            align-items: center;

            .icon-container-streak {
              svg {
                width: 12px;
                height: 8px;
              }
              fill: #a5a1ac;
            }
            .streak-data {
              margin-left: 4px;
              font-size: 12px;
              line-height: 1.4;
            }
          }
          &-tags {
            margin-left: 8px;
            fill: #a5a1ac;
            display: flex;
            align-items: center;
            svg {
              width: 14px;
            }
          }
        }
      }
    }
  }
  &-clickable-area {
    cursor: pointer;
    padding: 7px 8px 0 8px;
  }
}
.task-completed {
  color: #a5a1ac;
}
</style>
