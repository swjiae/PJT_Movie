import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'

import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueCarousel from 'vue-carousel'


Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(VueCarousel)

Vue.config.productionTip = false


new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
