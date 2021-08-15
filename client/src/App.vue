<template>
  <div id="app">
    <div id="nav" class="text-gray">
      <!-- <router-link to="/">Home</router-link> -->
    </div>
    <router-view />
  </div>
</template>
<style lang="scss">
#app {
  font-family: Verdana;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.button {
  border-radius: 2%;
}
</style>
