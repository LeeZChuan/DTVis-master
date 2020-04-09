<script>
//该文件为网页效果的备份版本
// import exp from "../components/exp.vue"; //样例图
// import email from "../components/email.vue"; //样例2图
import TadpoleChart from "../components/TadpoleCharts.vue"; //蝌蚪图
import MoveToChart from "../components/MoveToChart.vue"; //蝌蚪图
import LineCharts from "../components/LineCharts.vue"; //出行距离与出行次数折线图
import CalendarChart from "../components/CalendarChart.vue"; //日期订单情况热力图
// import ForecastChart from "../components/ForecastChart"; //预测界面
// import HeatMapChart from "./components/3DhotChart.vue"; //热力图界面
// import multiputeMap from "./components/multiputeMap.vue"; //用于展示海口市地区订单情况散点雷达图
// 网页界面设计
export default {
  components: {
    // exp,
    // email,
    TadpoleChart,
    MoveToChart,
    LineCharts,
    CalendarChart
    // ForecastChart,
    // HeatMapChart,
    // multiputeMap
  }
};
</script>

<template>
  <div id="wrapper">
    <h1 style="color:rgb(255, 255, 255);">交通流量轨迹可视化</h1>
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

    <!-- 用于交通流量可视化情况所使用的订单情况展示 -->
    <div class="big-index-1">
      <ul>
        <li>
          <b class="animation-1"></b>
          <b class="animation-2"></b>
          <b class="animation-3"></b>
          <p>滴滴订单类型数量</p>
          <strong>174.6069</strong>
        </li>
        <li>
          <b class="animation-1"></b>
          <b class="animation-2"></b>
          <b class="animation-3"></b>
          <p>滴滴订单类型数量</p>
          <strong>174.6069</strong>
        </li>
        <li>
          <b class="animation-1"></b>
          <b class="animation-2"></b>
          <b class="animation-3"></b>
          <p>滴滴订单类型数量</p>
          <strong>174.6069</strong>
        </li>
        <li>
          <b class="animation-1"></b>
          <b class="animation-2"></b>
          <b class="animation-3"></b>
          <p>滴滴订单类型数量</p>
          <strong>174.6069</strong>
        </li>
        <li>
          <b class="animation-1"></b>
          <b class="animation-2"></b>
          <b class="animation-3"></b>
          <p>滴滴订单类型数量</p>
          <strong>174.6069</strong>
        </li>
        <li>
          <b class="animation-1"></b>
          <b class="animation-2"></b>
          <b class="animation-3"></b>
          <p>滴滴订单类型数量</p>
          <strong>174.6069</strong>
        </li>
      </ul>
    </div>

    <!-- 操作台：用于操作交通流量可视化平台的参数与相关信息 -->
    <div class="submenu">
      <ul>
        <li>
          <a href="#this" class="active">
            <b>1</b>
            <span>
              交通流量蝌蚪图
              <em></em>
            </span>
          </a>
        </li>
        <li>
          <a href="#this" class="active">
            <b>2</b>
            <span>
              交通流量热力图
              <em></em>
            </span>
          </a>
        </li>
        <li>
          <a href="#this" class="active">
            <b>3</b>
            <span>
              交通流量迁徙图
              <em></em>
            </span>
          </a>
        </li>
        <li>
          <a href="#this" class="active">
            <b>4</b>
            <span>
              交通流量站点预测
              <em></em>
            </span>
          </a>
        </li>
        <li>
          <a href="#this" class="active">
            <b>5</b>
            <span>
              具体街道情况交通流量和弦图
              <em></em>
            </span>
          </a>
        </li>
      </ul>
    </div>
    <!-- 官网上说了router全部都要渲染到这里 -->
    <router-view></router-view>
    <div class="center-area">
      <!-- 主图展示区 -->
      <!-- <div id="LineCharts" style="width: 600px;height:400px;"></div> -->
      <!-- LineCharts -->
      <!-- <exp style="background:black"></exp> -->
      <TadpoleChart></TadpoleChart>
      <!-- <MoveToChart></MoveToChart> -->
      <LineCharts></LineCharts>
      <!-- <CalendarChart></CalendarChart> -->
      <!-- <exp style="width: 600px;height:400px;"></exp> -->
      <!-- <HeatMapChart></HeatMapChart> -->
      <!-- <div id="LineCharts" style="width: 1200px;height:200px;"></div> -->
    </div>

    <div class="right-area">
      <h3>
        交通流量变化率
        <b></b>
      </h3>
      <div class="area-inbox-1">
        <dl>
          <dt style="color:white">上月平均值</dt>
          <dd class="font12">
            <span>76.525%</span>
            <b></b>
          </dd>
          <dt class="ml-20">今日交通流量变化率</dt>
          <dd class="font-red ml-20">
            <span>74.113%</span>
            <b></b>
          </dd>
          <dt>今日交通流量变化率</dt>
          <dd>
            <span>68.113%</span>
            <b></b>
          </dd>
        </dl>
        <div class="round-1"></div>
        <div class="round-2"></div>
        <div class="round-3">30%</div>
        <div class="round-4"></div>
      </div>
    </div>

    <div class="time-base-outer">
      <b class="line1"></b>
      <div class="time-base">
        <!--  <div class="slider2"></div> -->
        <!-- <script src="./static/js/jquery_and_jqueryui.js"></script> -->
        <!-- <script src="/DTVis-mastesr/static/js/index.js"></script> -->
      </div>
      <b class="line2"></b>
    </div>
  </div>
</template>
    

<style scoped>
@import "../assets/css/mobile.css";
/* @import "../assets/css/jqueryui.css"; */
@import "../assets/css/default.css";
</style>




