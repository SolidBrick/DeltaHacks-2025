<script setup>
import { ref } from "vue";

const companies = ref([
  { name: "Company A", score: 8, summary: "This is a summary for Company A." },
  { name: "Company B", score: 6, summary: "This is a summary for Company B." },
  { name: "Company C", score: 9, summary: "This is a summary for Company C." },
  { name: "Company D", score: 7, summary: "This is a summary for Company D." },
  { name: "Company E", score: 5, summary: "This is a summary for Company E." },
  { name: "Company A", score: 8, summary: "This is a summary for Company A." },
  { name: "Company B", score: 6, summary: "This is a summary for Company B." },
  { name: "Company C", score: 9, summary: "This is a summary for Company C." },
  { name: "Company D", score: 7, summary: "This is a summary for Company D." },
  { name: "Company E", score: 5, summary: "This is a summary for Company E." },
  { name: "Company A", score: 8, summary: "This is a summary for Company A." },
  { name: "Company B", score: 6, summary: "This is a summary for Company B." },
  { name: "Company C", score: 9, summary: "This is a summary for Company C." },
  { name: "Company D", score: 7, summary: "This is a summary for Company D." },
  { name: "Company E", score: 5, summary: "This is a summary for Company E." },
]);

const selectedCompanyLeft = ref(null);
const selectedCompanyRight = ref(null);
</script>

<template>
  <div class="split-screen">
    <!-- Left Side -->
    <div class="side">
      <h2>Select a Company</h2>
      <select v-model="selectedCompanyLeft">
        <option
          v-for="(company, index) in companies"
          :key="index"
          :value="company"
        >
          {{ company.name }}
        </option>
      </select>

      <div v-if="selectedCompanyLeft" class="company-info">
        <h3>{{ selectedCompanyLeft.name }}</h3>
        <p
          class="score"
          :data-score="selectedCompanyLeft?.score"
          :style="`--score-ratio: ${selectedCompanyLeft?.score / 10};`"
        >
          {{ selectedCompanyLeft.score }}
        </p>
        <p>{{ selectedCompanyLeft.summary }}</p>
      </div>
    </div>

    <!-- Right Side -->
    <div class="side">
      <h2>Select a Company</h2>
      <select v-model="selectedCompanyRight">
        <option
          v-for="(company, index) in companies"
          :key="index"
          :value="company"
        >
          {{ company.name }}
        </option>
      </select>

      <div v-if="selectedCompanyRight" class="company-info">
        <h3>{{ selectedCompanyRight.name }}</h3>
        <p
          class="score"
          :data-score="selectedCompanyRight?.score"
          :style="`--score-ratio: ${selectedCompanyRight?.score / 10};`"
        >
          {{ selectedCompanyRight.score }}
        </p>
        <p>{{ selectedCompanyRight.summary }}</p>
      </div>
    </div>
  </div>
</template>
