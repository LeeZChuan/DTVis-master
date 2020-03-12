import Vue from 'vue';
// main文件
// import Vuex from 'vuex'
import App from './App.vue';
import router from './router';
import axios from 'axios';
import echarts from 'echarts';
// import iView from 'iview';
import 'echarts-gl';
// import 'iview/dist/styles/iview.css';
// import './assets/dark';

Vue.config.productionTip = false;
Vue.prototype.$axios = axios;
Vue.prototype.$bus = new Vue();
Vue.use(echarts);
// Vue.use(iView);
new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
