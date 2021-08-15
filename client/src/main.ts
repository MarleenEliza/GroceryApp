import Vue from "vue";
import App from "./App.vue";
import './index.css'
import router from "./router";
import store from "./store";
import { library } from '@fortawesome/fontawesome-svg-core'
import { faCarrot, faCashRegister, faCog, faShoppingBasket, faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

Vue.component('font-awesome-icon', FontAwesomeIcon)
library.add(faShoppingBasket, faCarrot, faCashRegister, faCog)
new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
