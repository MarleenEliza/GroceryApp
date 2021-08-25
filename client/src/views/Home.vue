<template>
  <div class="home">
    <nav-bar title="Grocery App"> </nav-bar>
    <div class="container">
      <router-link
        v-for="(button, index) in buttons"
        :key="index"
        :to="button.link"
      >
        <button-big v-bind="button" />
      </router-link>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import NavBar from "../components/NavBar.vue";
import ButtonBig from "../components/ui/ButtonBig.vue";

export default Vue.extend({
  name: "Home",
  components: {
    NavBar,
    ButtonBig,
  },
  data() {
    return {
      buttons: [
        {
          title: "Go Shop!",
          icon: "shopping-basket",
          extraClass: "green",
          link: "/viewTable",
        },
        {
          title: "Register",
          icon: "cash-register",
          link: "/",
        },
        { title: "Settings", icon: "cog", link: "/" },
      ],
    };
  },
});
</script>
<style scoped lang="scss">
.button.big {
  margin-left: auto;
  margin-right: auto;
}
</style>
