import Vue from 'vue'
import App from './App.vue' 
import router from './router'
import Axios from 'axios'
import { BootstrapVue } from 'bootstrap-vue'

Vue.prototype.$http = Axios;
Vue.config.productionTip = false

Vue.use(BootstrapVue)

new Vue({
  router,
  // store,
  render: h => h(App),
}).$mount('#app')
