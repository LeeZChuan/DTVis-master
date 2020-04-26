import Vue from 'vue'
import Router from 'vue-router'
import login from '../components/login'
import Home from '../views/Dashboard'
import TadpoleCharts from '../components/TadpoleCharts'
import MoveToChart from '../components/MoveToChart'

// vue框架路由管理功能

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/Home',
      name: 'Home',
      component: Home,
      children:[{
        path:'/Home/TadpoleCharts',
        name:'TadpoleCharts',
        component:TadpoleCharts
      },
        {
          path:'/Home/MoveToChart',
          name:'MoveToChart',
          component:MoveToChart
        }]
    }
  ]
})
