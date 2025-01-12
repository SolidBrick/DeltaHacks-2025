<template>
  <vue-gauge :refid="'type-unique-id'"></vue-gauge>
</template>

<script>
import VueGauge from "vue-gauge";
export default {
  components: { VueGauge },
};
</script>

Or to load as global component

<script>
import VueGauge from "vue-gauge";
Vue.component("vue-gauge", VueGauge);
</script>
