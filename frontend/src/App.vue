<template>
  <div class="w-full bg-slate">
    <div class="h-screen max-w-md mx-auto shadow-md overflow-hidden md:max-w-2xl">
      <Logo/>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Logo from "./components/Logo.vue"

export default {
  setup(){
    return {
    }
  },
  components: {
    Logo
  }
}
</script>

<style>

</style>