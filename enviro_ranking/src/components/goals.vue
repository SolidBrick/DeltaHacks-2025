<script setup>
import { ref, onMounted } from "vue";

onMounted(async () => {
  try {
    console.log("Fetching data from the server...");
    const response = await fetch("http://127.0.0.1:5000/get-sentiments", {
      method: "GET",
    });

    // Check if the response is successful (status 2xx)
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    // Get the JSON response
    const data = await response.json();
    console.log(data); // Log the parsed JSON data
  } catch (error) {
    console.error("Error during fetch:", error);
  }
});


const goalsList = ref([
  {
    title: "No Poverty",
    name: "No Poverty",
    link: "/nopoverty",
    posScore: 42, // Positive score
    negScore: 39, // Negative score
    posheadlines: [
      {
        name: "No Poverty - Great Progress",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "No Poverty - Achievements",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "No Poverty - New Initiatives",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "No Poverty - World Leaders Praise",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "No Poverty - Global Awareness Grows",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
    ],
    negheadlines: [
      {
        name: "No Poverty - Areas Still Struggling",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "No Poverty - Underfunding Concerns",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "No Poverty - Economic Downturn Affects Progress",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "No Poverty - Political Challenges",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "No Poverty - Slow Policy Implementation",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
    ],
  },
  {
    title: "Climate Change",
    name: "Climate Change",
    link: "/nopoverty",
    posScore: 12, // Positive score
    negScore: 50, // Negative score
    posheadlines: [
      {
        name: "Climate Change - Great Progress",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "Climate Change - Achievements",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "Climate Change - New Initiatives",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "Climate Change - World Leaders Praise",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "Climate Change - Global Awareness Grows",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
    ],
    negheadlines: [
      {
        name: "Climate Change - Areas Still Struggling",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "Climate Change - Underfunding Concerns",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "Climate Change - Economic Downturn Affects Progress",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "Climate Change - Political Challenges",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "Climate Change - Slow Policy Implementation",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
    ],
  },
  {
    title: "Clean Energy",
    name: "Clean Energy",
    link: "/nopoverty",
    posScore: 42, // Positive score
    negScore: 39, // Negative score
    posheadlines: [
      {
        name: "Clean Energy - Great Progress",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "Clean Energy - Achievements",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "Clean Energy - New Initiatives",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "Clean Energy - World Leaders Praise",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "Clean Energy- Global Awareness Grows",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
    ],
    negheadlines: [
      {
        name: "Clean Energy - Areas Still Struggling",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "Clean Energy - Underfunding Concerns",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "Clean Energy - Economic Downturn Affects Progress",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "Clean Energy - Political Challenges",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
      {
        name: "Clean Energy - Slow Policy Implementation",
        link: "https://great.com",
        summary:
          "this is a summary Minim fugiat culpa amet veniam sint laboris minim magna laboris. Elit sint adipisicing sit id quis magna incididunt commodo ea deserunt dolor ad dolor et. Deserunt mollit enim irure elit et fugiat et reprehenderit sit eu amet esse tempor non exercitation. Aliqua ut est exercitation laboris dolore exercitation. Mollit ullamco officia officia consequat ullamco elit incididunt laborum veniam voluptate et ut duis aliqua nostrud. Excepteur dolore enim laboris esse. Fugiat tempor nostrud enim elit elit reprehenderit dolor occaecat quis pariatur aliqua.",
      },
    ],
  },
]);
</script>

<template>
  <div class="titlecontent">
    <h1>UN Sustainable Development Goals</h1>
    <p>
      Find out how the UN is progressing with its Sustainable Development Goals, in realtime.
    </p>
  </div>
  <div class="flex-container">
    <div v-for="(goal, index) in goalsList" :key="index" class="flex-item" :style="{ backgroundImage: `url(${goal.image})` }" >
      <router-link
        class="name"
        :to="{
          path: goal.link,
          query: {
            title: goal.title,
            posScore: goal.posScore,
            negScore: goal.negScore,
            posHeadlines: JSON.stringify(goal.posheadlines),
            negHeadlines: JSON.stringify(goal.negheadlines),
          },
        }"
      >
        {{ goal.name }}
      </router-link>
    </div>
  </div>
</template>
