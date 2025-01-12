<script setup>
import { ref, computed, onMounted } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();

const title = ref("");
const posScore = ref(0);
const negScore = ref(0);
const posheadlines = ref([]);
const negheadlines = ref([]);
const summary = ref("");
const checklist = ref([]);

// On component mount, get data from the route query
onMounted(() => {
  summary.value = route.query.summary || "No summary provided"; // Default summary if not provided
  title.value = route.query.title || "No Poverty"; // Default title if not provided
  checklist.value = JSON.parse(route.query.checklist || "[]"); // Default to empty array if not provided
  posScore.value = parseInt(route.query.posScore) || 0; // Default to 0 if not provided
  negScore.value = parseInt(route.query.negScore) || 0; // Default to 0 if not provided

  posheadlines.value = JSON.parse(route.query.posHeadlines || "[]").map(
    (headline) => ({
      ...headline,
      showSummary: false, // Initialize showSummary for each headline
    })
  );

  negheadlines.value = JSON.parse(route.query.negHeadlines || "[]").map(
    (headline) => ({
      ...headline,
      showSummary: false, // Initialize showSummary for each headline
    })
  );
});

// Track the currently visible headline index for both positive and negative
const visiblePosIndex = ref(null);
const visibleNegIndex = ref(null);

// Toggling summaries using computed properties (only one summary at a time)
const toggleSummary = (index, type) => {
  if (type === "positive") {
    // If the clicked one is already visible, hide it; otherwise, show it and hide the other
    visiblePosIndex.value = visiblePosIndex.value === index ? null : index;
    visibleNegIndex.value = null; // Hide the negative summary if a positive is shown
  } else if (type === "negative") {
    visibleNegIndex.value = visibleNegIndex.value === index ? null : index;
    visiblePosIndex.value = null; // Hide the positive summary if a negative is shown
  }
};

// Computed properties for each list of headlines
const positiveHeadlines = computed(() => {
  return posheadlines.value.map((headline, index) => ({
    ...headline,
    toggleVisibility: () => toggleSummary(index, "positive"),
  }));
});

const negativeHeadlines = computed(() => {
  return negheadlines.value.map((headline, index) => ({
    ...headline,
    toggleVisibility: () => toggleSummary(index, "negative"),
  }));
});
</script>

<template>
  <div class="titlecontent">
    <h1>{{ title }}</h1>
    <p>{{summary}}</p>
  </div>
  <div class="allModules">
    <div class = "checkliststoo">
    <div class="positiveToNegative">
      <h2>This topic is mainly:</h2>
      <h1
        :class="{
          positive: posScore > negScore + 2,
          negative: negScore > posScore + 2,
          neutral: Math.abs(posScore - negScore) <= 2,
        }"
      >
        {{
          posScore > negScore + 2
            ? "POSITIVE"
            : negScore > posScore + 2
            ? "NEGATIVE"
            : "NEUTRAL"
        }}
      </h1>
      <p>
        <span class="positive-number">{{ posScore }}</span> |
        <span class="negative-number">{{ negScore }}</span>
      </p>
    
    </div>
    <div class="checklists-goals">
        <h2>Checklist</h2>
        <ul class="checklist-goals-items">
            <li
              v-for="(item, index) in checklist"
              :key="index"
              class="checklists-goals-items"
            >
              <label class="checklist-goals-label">
                <input type="checkbox" class="checklist-checkbox" />
                <span>{{ item }}</span>
              </label>
            </li>
          </ul>
      </div>
    </div>
    
    <div class="topHeadlines">
      <div class="positiveHeadlines">
        <h1>Positive Headlines</h1>
        <div
          v-for="(headline, index) in positiveHeadlines"
          :key="index"
          class="headline"
        >
          <p @click="headline.toggleVisibility">
            <span
              class="arrow"
              :class="{
                'up-arrow': visiblePosIndex === index,
                'down-arrow': visiblePosIndex !== index,
              }"
            >
            ▸ </span
            >{{ headline.name }}
          </p>
          <div v-show="visiblePosIndex === index">
            <p>Link: <a :href="headline.link" target="_blank">Click Here</a></p>
            <p>{{ headline.summary }}</p>
            <!-- Assuming headline has a 'summary' property -->
          </div>
        </div>
      </div>
      <div class="negativeHeadlines">
        <h1>Negative Headlines</h1>
        <div
          v-for="(headline, index) in negativeHeadlines"
          :key="index"
          class="headline"
        >
          <p @click="headline.toggleVisibility">
            <span
              class="arrow"
              :class="{
                'up-arrow': visibleNegIndex === index,
                'down-arrow': visibleNegIndex !== index,
              }"
            >
            ▸ </span
            >{{ headline.name }}
          </p>
          <div v-show="visibleNegIndex === index">
            <p>Link: <a :href="headline.link" target="_blank">Click Here</a></p>
            <p>{{ headline.summary }}</p>
            <!-- Assuming headline has a 'summary' property -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.arrow {
  margin-left: 8px;
  margin-right: 8px;
  display: inline-block;
  transition: transform 0.3s ease;
}

.down-arrow {
  transform: rotate(0deg);
}

.up-arrow {
  transform: rotate(90deg);
}
</style>
