// main文件
import Vue from 'vue';
import Vuex from 'vuex';
import VueRouter from'vue-router';
import App from './App.vue';
import router from './router';
import axios from 'axios';
import echarts from 'echarts';
import ElementUI from 'element-ui';//引入element-ui
import Index from'../static/js/index';//引入手写代码
// import 'element-ui/lib/theme-chalk/index.css';
import 'echarts-gl';
// import "./assets/css/default.css";
// import "./assets/css/mobile.css";
// import "./assets/css/jquery-ui.css";

// import 'iview/dist/styles/iview.css';
// import './assets/dark';
// imnpmport iView from 'iview';

Vue.config.productionTip = false;
Vue.prototype.$axios = axios;//本地数据读取
Vue.prototype.$bus = new Vue();
Vue.use(ElementUI);
Vue.use(echarts);
Vue.use(Vuex);
Vue.use(VueRouter);
Vue.use(Index);
// Vue.use(iView);
new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
