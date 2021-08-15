<template>
  <div class="button big" :class="extraClass">
    <div class="flex items-center justify-around w-10/12">
      <font-awesome-icon class="text-4xl" :icon="['fa', icon]" />
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
    icon: {
      type: String,
      required: true,
    },
    extraClass: {
      type: String,
      required: false,
    },
  },
});
</script>

<style scoped lang="scss">
.button.big {
  @apply bg-gray my-6 w-10/12 py-9 text-2xl flex items-center text-white;
  border-radius: 0.5rem;
}
.green {
  background-color: #bce08a !important;
}
</style>
