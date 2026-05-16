<template>
  <div class="sensor-dashboard">
    <h2>센서 데이터</h2>
    <table>
      <thead>
        <tr>
          <th>센서 ID</th>
          <th>타입</th>
          <th>값</th>
          <th>측정 시간</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="data in sensorData" :key="data.id">
          <td>{{ data.sensor_id }}</td>
          <td>{{ data.type }}</td>
          <td>{{ data.value }}</td>
          <td>{{ data.timestamp }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const sensorData = ref([])

const fetchSensorData = async () => {
  try {
    const res = await axios.get('/api/sensors/latest')
    sensorData.value = res.data
  } catch (e) {
    console.error('Failed to fetch sensor data', e)
  }
}

onMounted(() => {
  fetchSensorData()
  setInterval(fetchSensorData, 5000)
})
</script>

<style scoped>
.sensor-dashboard {
  padding: 20px;
}
.sensor-dashboard table {
  width: 100%;
  border-collapse: collapse;
}
.sensor-dashboard th,
.sensor-dashboard td {
  border: 1px solid #ddd;
  padding: 8px;
}
.sensor-dashboard th {
  background-color: #f2f2f2;
}
</style>
