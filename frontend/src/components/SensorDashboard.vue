<template>
  <div class="sensor-dashboard">
    <h2>Sensor Dashboard</h2>
    <table>
      <thead>
        <tr>
          <th>Sensor ID</th>
          <th>Type</th>
          <th>Location</th>
          <th>Value</th>
          <th>Timestamp</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="data in sensorData" :key="data.id">
          <td>{{ data.sensor_id }}</td>
          <td>{{ data.type }}</td>
          <td>{{ data.location }}</td>
          <td>{{ data.value }}</td>
          <td>{{ new Date(data.timestamp).toLocaleString() }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const sensorData = ref([]);

const fetchSensorData = async () => {
  try {
    const response = await axios.get('/api/sensors/latest');
    sensorData.value = response.data;
  } catch (err) {
    console.error('Failed to fetch sensor data', err);
  }
};

onMounted(() => {
  fetchSensorData();
  // Poll every 5 seconds
  setInterval(fetchSensorData, 5000);
});
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
