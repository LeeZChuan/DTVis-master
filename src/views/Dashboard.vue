<script>
import exp from '../components/exp.vue'
import TadpoleChart from '../components/TadpoleChart/TadpoleChineart.vue'//蝌蚪图
import LineChart from '../components/LineChart/LineChart.vue'//蝌蚪图
// 网页界面设计
// import dashboardVue from '../view/dashboard.vue';
// import Forecast from'../components/Forecast/Forecast'//预测界面
// import HeatMap from'./components/3Dhot/3Dhot chart.vue'//热力图界面
// import multiputeMap from'./components/multiputeMap.vue'//用于展示海口市地区订单情况散点雷达图
// export 作用
export default {
  // name:'dashboard',
  components: {
    exp,
    TadpoleChart
  },
};
</script>

<template>
<div>
    <exp></exp>
    <TadpoleChart></TadpoleChart>
    <LineChart></LineChart>
</div>
</template>