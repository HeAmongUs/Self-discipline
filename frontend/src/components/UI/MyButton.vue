<template>
  <div class="wrapper">
    <button class="button">
      <slot name="left-icon"></slot><slot></slot>
    </button>
  </div>
</template>

<script>
export default {
  name: "MyButton",
}
</script>

<style scoped lang="scss">
.wrapper {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 2;
  transition: 0.01s 0.23s ease-out all;
  overflow: hidden;
  outline: none;

  & + & {
    margin-left: 10px;
  }
}
.button {
  position: relative;
  background: #fff;
  color: dodgerblue;
  padding: 10px;
  width: 100%;
  border: 2px solid dodgerblue;
  border-radius: 4px;
  z-index: 2;
  transition: 0.01s 0.23s ease-out all;
  overflow: hidden;
  outline: none;
  display: flex;
  justify-content: center;
  align-items: center;

  &:before {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    height: 100%;
    width: 0;
    background: dodgerblue;
    z-index: -1;
    transition: 0.3s ease-in all;
  }
  &:hover {
    cursor: pointer;
    color: white;
    &:before {
      width: 100%;
    }
  }
}
</style>
