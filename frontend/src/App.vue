<template>
  <component :is="layout">
    <router-view />
  </component>
</template>

<script>
import EmptyLayout from "@/layouts/EmptyLayout"
import MainLayout from "@/layouts/MainLayout"

export default {
  components: {
    MainLayout,
    EmptyLayout,
  },
  computed: {
    layout() {
      return (this.$route.meta.layout || "empty") + "-layout"
    },
  },
}
</script>

<style lang="scss">
@import "~materialize-css/dist/css/materialize.min.css";
#app {
  text-align: center;
}
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

.flex-center {
  display: flex;
  justify-content: center;
  align-items: center;
}
textarea {
  resize: none;
}

* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
/* label color */
.input-field label.active{
  color: dodgerblue !important;
}

.input-field textarea:focus{
  border-bottom: 1px solid dodgerblue !important;
}

.input-field label {
  color: #a5a1ac;
}
/* label focus color */
.input-field input[type=text]:focus + label {
  color: #a5a1ac;
}
///* label underline focus color */
//.input-field input[type=text]:focus {
//  border-bottom: 1px solid #000;
//  box-shadow: 0 1px 0 0 #000;
//}
///* valid color */
//.input-field input[type=text].valid {
//  border-bottom: 1px solid #000;
//  box-shadow: 0 1px 0 0 #000;
//}
///* invalid color */
//.input-field input[type=text].invalid {
//  border-bottom: 1px solid #000;
//  box-shadow: 0 1px 0 0 #000;
//}
///* icon prefix focus color */
//.input-field .prefix.active {
//  color: #a5a1ac;
//}


</style>
