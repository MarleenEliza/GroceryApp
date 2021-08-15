<template>
  <div class="home">
    <nav-bar title="Grocery App"> </nav-bar>
    <div class="">
      <router-link to="/">
        <button-big
          title="Go Shop!"
          icon="shopping-basket"
          extraClass="green"
        />
      </router-link>
      <button-big title="Register" icon="cash-register" />
      <button-big title="Settings" icon="cog" />
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
});
</script>
<style scoped lang="scss">
.button.big {
  margin-left: auto;
  margin-right: auto;
}
</style>
