<script setup>
import { ref } from "vue";

const companies = ref([
  {
    name: "Company A",
    SI: 10,
    EIR: 5,
    CT: 7,
    CE: 6,
    IFE: 0,
    RM: 12,
    EL: 22,
    ESC: 12,
    total: 65,
  },
  {
    name: "Company B",
    SI: 10,
    EIR: 5,
    CT: 7,
    CE: 6,
    IFE: 0,
    RM: 12,
    EL: 22,
    ESC: 12,
    total: 65,
  },
  {
    name: "Company C",
    SI: 10,
    EIR: 5,
    CT: 7,
    CE: 6,
    IFE: 0,
    RM: 12,
    EL: 22,
    ESC: 12,
    total: 65,
  },
  {
    name: "Company D",
    SI: 10,
    EIR: 5,
    CT: 7,
    CE: 6,
    IFE: 0,
    RM: 12,
    EL: 22,
    ESC: 12,
    total: 65,
  },
  {
    name: "Company E",
    SI: 10,
    EIR: 5,
    CT: 7,
    CE: 6,
    IFE: 0,
    RM: 12,
    EL: 22,
    ESC: 12,
    total: 65,
  },
  {
    name: "Company A",
    SI: 10,
    EIR: 5,
    CT: 7,
    CE: 6,
    IFE: 0,
    RM: 12,
    EL: 22,
    ESC: 12,
    total: 65,
  },
  {
    name: "Company B",
    SI: 10,
    EIR: 5,
    CT: 7,
    CE: 6,
    IFE: 0,
    RM: 12,
    EL: 22,
    ESC: 12,
    total: 65,
  },
  {
    name: "Company C",
    SI: 10,
    EIR: 5,
    CT: 7,
    CE: 6,
    IFE: 0,
    RM: 12,
    EL: 22,
    ESC: 12,
    total: 65,
  },
  {
    name: "Company D",
    SI: 10,
    EIR: 5,
    CT: 7,
    CE: 6,
    IFE: 0,
    RM: 12,
    EL: 22,
    ESC: 12,
    total: 65,
  },
  {
    name: "Company E",
    SI: 10,
    EIR: 5,
    CT: 7,
    CE: 6,
    IFE: 0,
    RM: 12,
    EL: 22,
    ESC: 12,
    total: 65,
  },
  {
    name: "Company A",
    SI: 10,
    EIR: 5,
    CT: 7,
    CE: 6,
    IFE: 0,
    RM: 12,
    EL: 22,
    ESC: 12,
    total: 65,
  },
  {
    name: "Company B",
    SI: 10,
    EIR: 5,
    CT: 7,
    CE: 6,
    IFE: 0,
    RM: 12,
    EL: 22,
    ESC: 12,
    total: 65,
  },
  {
    name: "Company C",
    SI: 10,
    EIR: 5,
    CT: 7,
    CE: 6,
    IFE: 0,
    RM: 12,
    EL: 22,
    ESC: 12,
    total: 65,
  },
  {
    name: "Company D",
    SI: 10,
    EIR: 5,
    CT: 7,
    CE: 6,
    IFE: 0,
    RM: 12,
    EL: 22,
    ESC: 12,
    total: 65,
  },
  {
    name: "Company E",
    SI: 10,
    EIR: 5,
    CT: 7,
    CE: 6,
    IFE: 0,
    RM: 12,
    EL: 22,
    ESC: 12,
    total: 65,
  },
]);

function handleSubmit() {
  text.value = inputText.value; // Only update text on submit
  inputText.value = "";
  return inputText.value;

  input_text = handleSubmit();
}

function handleRankingClick(ranking) {
  text.value = ranking; // Update text when a ranking is clicked
}
</script>
<template>
  <div class="main">
    <div class="rankings">
      <div class="urlsubmitter">
        <form @submit.prevent="handleSubmit">
          <input
            v-model="inputText"
            id="url-upload"
            type="url"
            placeholder="Enter website URL"
          />
          <input type="submit" value="Submit" class="submit" />
        </form>
      </div>

      <div class="rank">
        <div class="ranking-container"></div>
      </div>
    </div>
    <div class="content">
      <h1 class="titletext">{{ text }}</h1>
      <p></p>
    </div>
  </div>

  <div id="app">
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Environmental Impact Reduction:</th>
          <th>Sustainability Initiatives</th>
          <th>Corporate Transparency</th>
          <th>Community Engagement</th>
          <th>Innovation and Future Efforts</th>
          <th>Risk Management</th>
          <th>Environmental Leadership</th>
          <th>Economic and Social Considerations</th>
          <th>Total</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(company, index) in companies" :key="index">
          <td>{{ company.name }}</td>
          <td>{{ company.SI }}</td>
          <td>{{ company.EIR }}</td>
          <td>{{ company.CT }}</td>
          <td>{{ company.CE }}</td>
          <td>{{ company.IFE }}</td>
          <td>{{ company.RM }}</td>
          <td>{{ company.EL }}</td>
          <td>{{ company.ESC }}</td>
          <td>{{ company.total }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
