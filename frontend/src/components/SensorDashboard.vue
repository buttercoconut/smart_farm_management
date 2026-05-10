<template>
  <div class="sensor-dashboard">
    <h2>Sensor Dashboard</h2>
    <div v-for="data in sensorData" :key="data.id" class="sensor-card">
      <p><strong>ID:</strong> {{ data.sensor_id }}</p>
      <p><strong>Timestamp:</strong> {{ data.timestamp }}</p>
      <p><strong>Value:</strong> {{ data.value }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const sensorData = ref([]);

onMounted(async () => {
  const res = await axios.get('/api/sensors/data');
  sensorData.value = res.data;
});
</script>

<style scoped>
.sensor-dashboard { padding: 1rem; }
.sensor-card { border: 1px solid #ccc; padding: 0.5rem; margin-bottom: 0.5rem; }
</style>
