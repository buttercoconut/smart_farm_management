<template>
  <div class="actuator-control">
    <h2>액추에이터 제어</h2>
    <div v-for="actuator in actuators" :key="actuator.id" class="actuator-item">
      <p><strong>{{ actuator.name }}</strong> ({{ actuator.type }})
      </p>
      <button @click="toggleActuator(actuator)" :class="{ active: actuator.active }">
        {{ actuator.active ? 'Stop' : 'Start' }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const actuators = ref([])

const fetchActuators = async () => {
  try {
    const res = await axios.get('/api/actuators')
    actuators.value = res.data
  } catch (e) {
    console.error('Failed to fetch actuators', e)
  }
}

const toggleActuator = async (actuator) => {
  try {
    const action = actuator.active ? 'stop' : 'start'
    await axios.post(`/api/actuators/${actuator.id}/${action}`)
    actuator.active = !actuator.active
  } catch (e) {
    console.error('Actuator toggle failed', e)
  }
}

onMounted(() => {
  fetchActuators()
})
</script>

<style scoped>
.actuator-control {
  padding: 20px;
}
.actuator-item {
  margin-bottom: 15px;
}
button {
  padding: 8px 12px;
  border: none;
  background-color: #3498db;
  color: white;
  cursor: pointer;
}
button.active {
  background-color: #e74c3c;
}
</style>
