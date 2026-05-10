<template>
  <div class="actuator-control">
    <h2>Actuator Control</h2>
    <form @submit.prevent="sendCommand">
      <label for="actuatorId">Actuator ID:</label>
      <input id="actuatorId" v-model="actuatorId" type="number" required />
      <label for="command">Command:>
      <input id="command" v-model="command" type="text" required />
      <button type="submit">Send</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const actuatorId = ref(1);
const command = ref('');

const sendCommand = async () => {
  await axios.post('/api/actuators/control', {
    actuator_id: actuatorId.value,
    command: command.value,
  });
  command.value = '';
};
</script>

<style scoped>
.actuator-control { padding: 1rem; }
form { display: flex; flex-direction: column; gap: 0.5rem; }
</style>
