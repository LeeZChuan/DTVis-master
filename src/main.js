// main文件
import Vue from 'vue';
import Vuex from 'vuex';
import VueRouter from'vue-router';
import App from './App.vue';
import router from './router';
import axios from 'axios';
import echarts from 'echarts';
import ElementUI from 'element-ui';//引入element-ui
import 'element-ui/lib/theme-chalk/index.css'
import layer from 'vue-layer'//引入layer弹窗样式
import 'vue-layer/lib/vue-layer.css';
import 'echarts-gl';
import HighchartsVue from 'highcharts-vue'
import VueResource from 'vue-resource';


Vue.config.productionTip = false;
Vue.prototype.$axios = axios;//本地数据读取
Vue.prototype.$bus = new Vue();
Vue.prototype.$layer = layer(Vue);
Vue.use(HighchartsVue);
Vue.use(ElementUI);
Vue.use(echarts);
Vue.use(Vuex);
Vue.use(VueRouter);
Vue.use(VueResource);

new Vue({
  router,
  render: h => h(App),
  components: { App },
  template: '<App/>'
}).$mount('#app');
