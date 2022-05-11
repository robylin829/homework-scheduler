<template>
  <div class="grid grid-cols-3 gap-4">
    <Slide/>
    <div class="col-span-1">{{classes_data}}</div>
    <div>{{ schedules_data }}</div>
  </div>
</template>

<script>
import Slide from "../components/Slide.vue"
import { inject, onMounted, ref } from 'vue'

export default {
  name: 'Home',
  setup() {
    // Inject axios
    const axios = inject('axios')

    let classes_data = ref([])
    let schedules_data = ref([])

    // get classes info
    const getClasses = () => {
      axios.get('http://127.0.0.1:5000/api/v1/class')
      .then((response) => {
        classes_data.value = response.data
      })
    }

    // get schedule
    const getSchedules = () => {
      axios.get('http://127.0.0.1:5000/api/v1/schedule')
      .then((response) => {
        schedules_data.value = response.data 
      })
    }

    onMounted(() =>{
      getClasses()
      getSchedules()
    })

    return {
      schedules_data,
      classes_data
    }
  },
  components: {
    Slide,
  }
}
</script>
