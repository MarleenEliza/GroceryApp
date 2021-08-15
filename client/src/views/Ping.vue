<template>
  <div class="home">
    <PingTest />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import PingTest from "../components/PingTest.vue";

export default Vue.extend({
  name: "Ping",
  components: {
    PingTest,
  },
});
</script>
