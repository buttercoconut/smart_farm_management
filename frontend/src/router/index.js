import { createRouter, createWebHistory } from 'vue-router';
import SensorDashboard from '../components/SensorDashboard.vue';
import ActuatorControl from '../components/ActuatorControl.vue';
import FarmMap from '../components/FarmMap.vue';

const routes = [
  { path: '/sensors', component: SensorDashboard },
  { path: '/actuators', component: ActuatorControl },
  { path: '/map', component: FarmMap },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
