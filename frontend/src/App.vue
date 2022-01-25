<template>
  <div class="w-full bg-slate">
    <div class="h-screen max-w-md mx-auto shadow-md overflow-hidden md:max-w-2xl">
      <Logo/>
      <Slide/>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Logo from "./components/Logo.vue"
import Slide from "./components/Slide.vue"

export default {
  setup(){
    return {
    }
  },
  components: {
    Slide,
    Logo
  }
}
</script>

<style>

</style>