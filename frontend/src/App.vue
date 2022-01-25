<template>
  <div>
    <Home/> 
    <router-view></router-view>
  </div>
</template>

<script>
import Home from "./views/Home.vue"

export default {
  setup(){
    return {
      Home,
    }
  }
}
</script>

<style>

</style>