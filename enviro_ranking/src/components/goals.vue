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

    //povertyArticles(forEach(page =>
    //  ppovertyStore.push
    //      {
    //        name:[0]
    //         summary:page[1]
      //        link: page[2]
     //       }
    // )

    
    console.log(data); // Log the parsed JSON data
    const povertyArticles = data.poverty;
    const climateArticles = data.climate;
    const energyArticles = data.energy;
    let posPovertyStore = Array(0);
    let negPovertyStore = Array(0);
    let posClimateStore = Array(0);
    let negClimateStore = Array(0);
    let posEnergyStore = Array(0);
    let negEnergyStore = Array(0);
    let povPosCount = 0;
    let povNegCount = 0;
    let climatePosCount = 0;
    let climateNegCount = 0;
    let energyPosCount = 0;
    let energyNegCount = 0;

    povertyArticles.forEach(page => {
      const title = page[0];
      const desc = page[1];
      const url = page[2];
      if (page[3] == "good") {
        if (povPosCount < 5) {
          posPovertyStore.push
          ({
            name:title,
            summary:desc,
            link:url,
          });
        }
        povPosCount += 1;
      } else {
        if (povNegCount < 5) {
          negPovertyStore.push
          ({
            name:title,
            summary:desc,
            link:url
          });
        }
        povNegCount += 1;
      }
    })
    
    climateArticles.forEach(page => {
      const title = page[0];
      const desc = page[1];
      const url = page[2];
      if (page[3] == "good") {
        if (climatePosCount < 5) {
          posClimateStore.push
          ({
            name:title,
            summary:desc,
            link:url,
          });
        }
        climatePosCount += 1;
      } else {
        if (climateNegCount < 5) {
          negClimateStore.push
          ({
            name:title,
            summary:desc,
            link:url
          });
        }
        climateNegCount += 1;
      }
    })

    energyArticles.forEach(page => {
      const title = page[0];
      const desc = page[1];
      const url = page[2];
      if (page[3] == "good") {
        if (energyPosCount < 5) {
          posEnergyStore.push
          ({
            name:title,
            summary:desc,
            link:url,
          });
        }
        energyPosCount += 1;
      } else {
        if (energyNegCount < 5) {
          negEnergyStore.push
          ({
            name:title,
            summary:desc,
            link:url
          });
        }
        energyNegCount += 1;
      }
    })

    
    const newGoalPov = {
      title: "No Poverty",
      name: "No Poverty",
      link: "/nopoverty",
      posScore: povPosCount, // Positive score
      negScore: povNegCount, // Negative score
      posheadlines: posPovertyStore,
      negheadlines: negPovertyStore,
      summary: "This goal is about ending poverty in all its forms everywhere.",
      /* checklist of personal actions an individual can take to help achieve this goal */
      checklist: [
        "Donate to a charity that helps people in poverty",
        "Volunteer at a local food bank",
        "Buy a fair trade product",
        "Read five articles about poverty",
      ],
    };
    const newGoalClim = {
      title: "Climate Action",
      name: "Climate Action",
      link: "/nopoverty",
      posScore: climatePosCount, // Positive score
      negScore: climateNegCount, // Negative score
      posheadlines: posClimateStore,
      negheadlines: negClimateStore,
      summary: "This goal is about taking urgent action to combat climate change and its impacts.",
            /* checklist of personal actions an individual can take to help achieve this goal */
      checklist: [
        "Recycle one time a day",
        "Use public transportation to commute",
        "Plant one tree and support reforestation efforts",
        "Check for improperly sealed doors and windows"
      ],
    };
    const newGoalEnergy = {
      title: "Affordable and Clean Energy",
      name: "Affordable and Clean Energy",
      link: "/nopoverty",
      posScore: energyPosCount, // Positive score
      negScore: energyNegCount, // Negative score
      posheadlines: posEnergyStore,
      negheadlines: negEnergyStore,
      summary: "This goal is about ensuring access to affordable, reliable, sustainable and modern energy for all.",
            /* checklist of QUANTIFIABLE AND SPECIFIC personal actions an individual can take to help achieve this goal */
      checklist: [
        "Switch to LED light bulbs",
        "Unplug electronics when not in use",
        "Use a programmable thermostat",
        "Drive less once a day",
        "Switch to green energy providers",
      ],
    };
    goalsList.value.push(newGoalPov);
    goalsList.value.push(newGoalClim);
    goalsList.value.push(newGoalEnergy);
  } catch (error) {
    console.error("Error during fetch:", error);
  }
});

const goalsList = ref([]);
</script>

<template>
  <div class="titlecontent">
    <div class = "brand">
    Eco<span class = "other">Dash</span>  
    </div>
  <div class = "tagline">
      Find out how the UN is progressing with its Sustainable Development Goals,
      in realtime.
    </div>
  </div>
  <div class="flex-container">
    <div
      v-for="(goal, index) in goalsList"
      :key="index"
      class="flex-item"
      :style="{ backgroundImage: `url(${goal.image})` }"
    >
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
            summary: goal.summary,
            checklist: JSON.stringify(goal.checklist),
          },
        }"
      >
        {{ goal.name }}
      </router-link>
    </div>
  </div>
</template>
