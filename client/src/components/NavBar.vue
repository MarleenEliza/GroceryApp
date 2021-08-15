<template>
  <div class="bg-gray h-16 text-2xl text-white flex items-center">
    <div class="flex items-center justify-around w-8/12 ml-6">
      <font-awesome-icon class="text-4xl" :icon="['fa', 'shopping-basket']" />
      <strong>{{ title }}</strong>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  props: {
    title: {
      type: String,
      required: true,
    },
  },
});
</script>
<style scoped lang="scss"></style>
