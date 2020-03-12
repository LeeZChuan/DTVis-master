<script>
import exp from "../components/exp.vue"; //样例图
import TadpoleChart from "../components/TadpoleChart.vue"; //蝌蚪图
import LineChart from "../components/LineChart.vue"; //出行距离与出行次数折线图
// import ForecastChart from "../components/ForecastChart"; //预测界面
// import HeatMapChart from "./components/3DhotChart.vue"; //热力图界面
// import multiputeMap from "./components/multiputeMap.vue"; //用于展示海口市地区订单情况散点雷达图
// 网页界面设计
// import dashboardVue from '../view/dashboard.vue';
// export 作用
export default {
  // name:'dashboard',
  components: {
    exp,
    TadpoleChart,
    LineChart,
    // ForecastChart,
    // HeatMapChart,
    // multiputeMap
  }
};
</script>



<template>

  <div id="wrapper">
    <h1>交通流量轨迹可视化</h1>
    <h2>
      <strong>重点关注</strong>
      <sub>Focus on the indicators</sub>
      <b class="logoline"></b>
      <b class="logoline1"></b>
      <b class="logoline2"></b>
      <b class="logoline3"></b>
      <b class="logoline4"></b>
    </h2>
    <!--时间区-->
    <div class="date-timer">
      <p>
        <strong id="H"></strong>
        <strong>:</strong>
        <strong id="M"></strong>
        <strong id="S" class="hide"></strong>
      </p>
      <em id="D"></em>
      <ul>
        <li id="Y"></li>
        <li id="MH"></li>
        <li id="TD"></li>
      </ul>
    </div>


    <exp></exp>
    <TadpoleChart></TadpoleChart>
    <LineChart></LineChart>
  </div>
</template>