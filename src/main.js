import Vue from "vue";
import App from "./App.vue";
import VueSocketIO from "vue-socket.io";
import "./registerServiceWorker";
import "@/assets/style.css";

Vue.config.productionTip = false;

Vue.use(
  new VueSocketIO({
    debug: true,
    connection: "http://0.0.0.0:5000"
  })
);

new Vue({
  render: (h) => h(App)
}).$mount("#app");
