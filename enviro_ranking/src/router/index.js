// src/router/index.js
import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../components/goals.vue";
import ComparePage from "../components/ComparePage.vue";
import SentimentPage from "../components/goals.vue";
import NOPOVERTY from "../components/nopoverty.vue";

const routes = [
  { path: "/", name: "Home", component: HomePage },
  { path: "/compare", name: "Compare", component: ComparePage },
  { path: "/sentiment", name: "Sentiment", component: SentimentPage },
  { path: "/nopoverty", name: "nopoverty", component: NOPOVERTY },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
