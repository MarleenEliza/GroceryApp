<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <PingTest />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import PingTest from "../components/PingTest.vue"; // @ is an alias to /src

export default Vue.extend({
  name: "Ping",
  components: {
    PingTest,
  },
});
</script>
