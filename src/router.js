import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      //Dashboard为该项目的整体设计页面
      component: resolve => require(['./views/Dashboard.vue'], resolve),
    },
  ],
});
