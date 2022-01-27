class SchedulesAPI{
    constructor(axios, schedules_data) {
        this.api = "http://localhost:5000/api/v1/schedule"
        this.axios = axios
        this.schedules_data = schedules_data
    }
    getSchedules() {
        axios.get('http://127.0.0.1:5000/api/v1/schedule')
            .then((response) => {
                this.schedules_data.value = response.data 
        })
    }
}

export default SchedulesAPI