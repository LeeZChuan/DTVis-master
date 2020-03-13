<script>
//该文件为网页效果的备份版本
import exp from "../components/exp.vue"; //样例图
import TadpoleChart from "../components/TadpoleChart.vue"; //蝌蚪图
import LineChart from "../components/LineChart.vue"; //出行距离与出行次数折线图
// import ForecastChart from "../components/ForecastChart"; //预测界面
// import HeatMapChart from "./components/3DhotChart.vue"; //热力图界面
// import multiputeMap from "./components/multiputeMap.vue"; //用于展示海口市地区订单情况散点雷达图
// 网页界面设计
// import dashboardVue from '../view/dashboard.vue';
// export 作用
import "../assets/css/style.css";
export default {
  components: {
    exp,
    TadpoleChart,
    LineChart
    // ForecastChart,
    // HeatMapChart,
    // multiputeMap
  }
};
</script>

<template>
  <div>
    <el-container>
      <el-header>Header</el-header>
      <el-main>Main</el-main>
    <exp></exp>
    <TadpoleChart></TadpoleChart>
    <LineChart></LineChart>
    </el-container>

  </div>
</template>