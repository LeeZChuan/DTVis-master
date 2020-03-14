<script>
import exp from "../components/exp.vue"; //样例图
// import TadpoleChart from "../components/TadpoleChart.vue"; //蝌蚪图
// import LineChart from "../components/LineChart.vue"; //出行距离与出行次数折线图
// import ForecastChart from "../components/ForecastChart"; //预测界面
// import HeatMapChart from "./components/3DhotChart.vue"; //热力图界面
// import multiputeMap from "./components/multiputeMap.vue"; //用于展示海口市地区订单情况散点雷达图
// 网页界面设计
// import dashboardVue from '../view/dashboard.vue';
// export 作用
export default {
  components: {
    exp
    // TadpoleChart,
    // LineChart,
    // ForecastChart,
    // HeatMapChart,
    // multiputeMap
  }
};
</script>

<script src="../../static/js/jquery_and_jqueryui.js"></script>
<script src="../../static/js/index.js"></script>
<script type="text/javascript" src="../../static/js/common.js"></script>
<script type="text/javascript" src="../../static/js/jquery-1.8.3.min.js"></script>
<template>
  <div>
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

      <!-- 用于交通流量可视化情况所使用的订单情况展示 -->
      <div class="big-index-1">
        <ul>
          <li>
            <b class="animation-1"></b>
            <b class="animation-2"></b>
            <b class="animation-3"></b>
            <p>VLR登记用户数</p>
            <strong>174.6069</strong>
          </li>
          <li>
            <b class="animation-1"></b>
            <b class="animation-2"></b>
            <b class="animation-3"></b>
            <p>VLR登记用户数</p>
            <strong>174.6069</strong>
          </li>
          <li>
            <b class="animation-1"></b>
            <b class="animation-2"></b>
            <b class="animation-3"></b>
            <p>VLR登记用户数</p>
            <strong>174.6069</strong>
          </li>
          <li>
            <b class="animation-1"></b>
            <b class="animation-2"></b>
            <b class="animation-3"></b>
            <p>VLR登记用户数</p>
            <strong>174.6069</strong>
          </li>
          <li>
            <b class="animation-1"></b>
            <b class="animation-2"></b>
            <b class="animation-3"></b>
            <p>VLR登记用户数</p>
            <strong>174.6069</strong>
          </li>
          <li>
            <b class="animation-1"></b>
            <b class="animation-2"></b>
            <b class="animation-3"></b>
            <p>VLR登记用户数</p>
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
        </ul>
      </div>
<exp></exp>
      <!-- <div class="center-area">
            <div class="pandect-area">
                <h3>
                    <p>当前08时<sub>8 points</sub></p>
                    <strong>总览</strong>
                    <em> 11时：29.742 Erl</em>
                </h3>
                <span class="pandect-area-left">
                    <b></b>
                </span>
                <div class="pandect-area-center">
                    <img src="images/charts.png" />
                </div>
                <span class="pandect-area-right">
                    <b></b>
                </span>
            </div>
            <div class="details1-area">
                <span class="detailsl-area-left"></span>
                <div class="details1-area-center">
                    <h3>VLR登录用户数</h3>
                    <dl>
                        <dt>上月平均值</dt>
                        <dd>
                            <ul>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li class="red"></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                            </ul>
                            448875
                        </dd>
                        <dt>昨日交通流量变化率</dt>
                        <dd>
                            <ul>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                            </ul>
                            448875
                        </dd>
                        <dt>今日交通流量变化率 </dt>
                        <dd>
                            <ul>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                            </ul>
                            448875
                        </dd>
                    </dl>
                    <b></b>
                </div>
                <span class="detailsl-area-right"></span>
            </div>
            <div class="details2-area">
                <span class="details2-area-left"></span>
                <div class="details2-area-center">
                    <h3>A口话务量</h3>
                    <dl>
                        <dt>上月平均值</dt>
                        <dd>
                            <ul>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li class="red"></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                            </ul>
                            448875
                        </dd>
                        <dt>昨日交通流量变化率</dt>
                        <dd>
                            <ul>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="yellow"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                            </ul>
                            448875
                        </dd>
                        <dt>今日交通流量变化率 </dt>
                        <dd>
                            <ul>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li class="red"></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                                <li></li>
                            </ul>
                            448875
                        </dd>
                    </dl>
                    <b></b>
                </div>
                <span class="details2-area-right"></span>
            </div>
      </div>-->
      <div class="right-area">
        <h3>
          交通流量变化率
          <b></b>
        </h3>
        <div class="area-inbox-1">
          <dl>
            <dt>上月平均值</dt>
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
        <div class="area-inbox-2">
          <ul>
            <li>
              <strong>12</strong>74.23%
              <b></b>
              <em></em>
            </li>
            <li>
              <strong>16</strong>71.19%
              <b></b>
              <em></em>
            </li>
            <li>
              <strong>18</strong>68.02%
              <b></b>
              <em></em>
            </li>
          </ul>
          <div class="area-text">
            <b class="animation-line1"></b>
            <h4>口径说明：</h4>
            <p class="text_container"></p>
            <b class="animation-line2"></b>
          </div>
        </div>
      </div>
      <div class="time-base-outer">
        <b class="line1"></b>
        <div class="time-base">
          <!--  <div class="slider2"></div> -->
        </div>
        <b class="line2"></b>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import "../assets/css/default.css";
@import "../assets/css/mobile.css";
@import "../assets/css/jquery-ui.css";
</style>