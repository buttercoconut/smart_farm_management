<template>
  <div id="app">
    <nav>
      <router-link to="/sensors">Sensors</router-link>
      <router-link to="/actuators">Actuators</router-link>
      <router-link to="/map">Map</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script setup>
import { createRouter, createWebHistory } from 'vue-router';
import SensorDashboard from './components/SensorDashboard.vue';
import ActuatorControl from './components/ActuatorControl.vue';
import FarmMap from './components/FarmMap.vue';

const routes = [
  { path: '/sensors', component: SensorDashboard },
  { path: '/actuators', component: ActuatorControl },
  { path: '/map', component: FarmMap },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});
</script>

<style>
nav { display: flex; gap: 1rem; padding: 1rem; background: #f0f0f0; }
</style>
