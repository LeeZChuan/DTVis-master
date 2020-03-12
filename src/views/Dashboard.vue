<script>
import exp from '../components/exp.vue'//样例图
import TadpoleChart from '../components/TadpoleChart.vue'//蝌蚪图
import LineChart from '../components/LineChart.vue'//出行距离与出行次数折线图
// 网页界面设计
// import dashboardVue from '../view/dashboard.vue';
// import Forecast from'../components/Forecast'//预测界面
// import HeatMap from'./components/3Dhot chart.vue'//热力图界面
// import multiputeMap from'./components/multiputeMap.vue'//用于展示海口市地区订单情况散点雷达图
// export 作用
export default {
  // name:'dashboard',
  components: {
    exp,
    TadpoleChart,
    LineChart,
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