import Vue from "vue";
import Router from "vue-router";
import home from "../pages/home";
const ControlMap = () =>
    import ("../pages/ControlMap");
const notfound = () =>
    import ("../pages/notfound");
p
Vue.use(Router);

export default new Router({
    mode: "history",
    routes: [{
            path: "/",
            component: home,
            meta: { title: '交通流量时空演变特征可视分析' }
        },
        {
            path: "/home",
            component: home,
            meta: { title: '交通流量时空演变特征可视分析' }
        },
        {
            path: "/ControlMap",
            component: ControlMap,
            meta: { title: '地图整体操控界面' }
        },
        {
            path: "*",
            component: notfound,
            meta: { title: '页面走丢了...' }
        }
    ]
});