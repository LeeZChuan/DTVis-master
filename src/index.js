import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Dashboard',
      component: resolve => require(['./views/Dashboard2.vue'], resolve),
    },
  ],
});
