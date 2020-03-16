// main文件
import Vue from 'vue';
// import Vuex from 'vuex'
import App from './App.vue';
import router from './router';
import axios from 'axios';
import echarts from 'echarts';
import ElementUI from 'element-ui';//引入element-ui
import 'element-ui/lib/theme-chalk/index.css';
import 'echarts-gl';
import "./assets/css/default.css";
import "./assets/css/mobile.css";
import "./assets/css/jquery-ui.css";

// import 'iview/dist/styles/iview.css';
// import './assets/dark';
// import iView from 'iview';

Vue.config.productionTip = false;
Vue.prototype.$axios = axios;
Vue.prototype.$bus = new Vue();
Vue.use(ElementUI);
Vue.use(echarts);
// Vue.use(iView);
new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
