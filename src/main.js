// main文件
import Vue from 'vue';
import Vuex from 'vuex';
import store from './vuex/store'
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
import AMap from  'vue-amap'  
// import VueAMap from 'vue-amap'


// Vue.use(VueAMap);
// VueAMap.initAMapApiLoader({
//   key:'c380530aa9ffc519378dd30409c0d370',
//   plugin: [
//     "AMap.Autocomplete", //输入提示插件
//     "AMap.PlaceSearch", //POI搜索插件
//     "AMap.Scale", //右下角缩略图插件 比例尺
//     "AMap.OverView", //地图鹰眼插件
//     "AMap.ToolBar", //地图工具条
//     "AMap.MapType", //类别切换控件，实现默认图层与卫星图、实施交通图层之间切换的控制
//     "AMap.PolyEditor", //编辑 折线多，边形
//     "AMap.CircleEditor", //圆形编辑器插件
//     "AMap.Geolocation", //定位控件，用来获取和展示用户主机所在的经纬度位置
//     "AMap.Heatmap"//热力图插件
//   ],
//   v: '1.4.15',
//   uiVersion: '1.0'
// })


Vue.use(AMap);
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
  store,
  render: h => h(App),
  components: { App },
  template: '<App/>'
}).$mount('#app');
