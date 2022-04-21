<template>
  <div class="dropdown" @click="isOpen = !isOpen">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 4 16">
      <path
        fill-rule="evenodd"
        d="M2 4a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm0 6a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm0 6a2 2 0 1 1 0-4 2 2 0 0 1 0 4z"
      ></path>
    </svg>
    <div class="dropdown-content" :class="{ 'dropdown-open': isOpen }">
      <slot name="content"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "MyDropdown",
  data() {
    return {
      isOpen: false,
    }
  },
}
</script>

<style scoped lang="scss">
.dropdown {
  position: relative;
  transition: 0.3s;
  opacity: 0;
  border: 1px solid transparent;
  padding: 0 8px;

  svg {
    width: 4px;
  }

  &-content {
    opacity: 1;
    display: block;
    top: 0;
    left: -160px;
    position: absolute;
    width: 160px;
    height: 0;
  }
  &-open {
    height: auto;
  }
}
</style>
