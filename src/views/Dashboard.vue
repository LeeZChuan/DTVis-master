<script>
//该文件为网页效果的页面布局整体网页
import TadpoleChart from "../components/TadpoleCharts.vue"; //蝌蚪图
import MoveToChart from "../components/MoveToChart.vue"; //交通流量整体流量迁徙图
import LineCharts from "../components/LineCharts.vue"; //出行距离与出行次数折线图
import CalendarChart from "../components/CalendarChart.vue"; //日期订单情况热力图
// import ForecastChart from "../components/ForecastChart"; //预测情况散点图界面
import ForecastPointChart from "../components/ForecastPointChart"; //预测起终点散点界面
import HeatMapChart from "../components/StartHeatMapChart.vue"; //热力图界面
// import multiputeMap from "./components/multiputeMap.vue"; //用于展示海口市地区订单情况散点雷达图
import ChordChart from "../components/ChordChart.vue"; //订单情况街道和弦图
import centerOrderNumChart from "../components/OrderNumLineChart.vue"; //订单数量情况与出行距离折线图
import RateLineChart from "../components/RateLineChart.vue"; //订单情况每小时变化率折线图
import PreBarChart from "../components/PreBarChart.vue"; //预测界面的柱状图
import kmap from "../components/map";
// 网页界面设计
export default {
  name: "Home",
  components: {
    TadpoleChart,
    MoveToChart,
    LineCharts,
    CalendarChart,
    PreBarChart,
    // ForecastChart,
    ForecastPointChart,
    HeatMapChart,
    centerOrderNumChart,
    RateLineChart,
    // multiputeMap,
    ChordChart,
    kmap
  },
  data() {
    return {
      centerForcastVisible: false, //预测部分界面弹窗
      centerOrderNumVisible: false, //订单的出行距离与该订单出行距离数量组合折线图弹窗
      centerMoveToVisible: false, //订单情况区域迁徙图的弹窗
      centerDepVisible: false, //订单情况街道流向和弦图
      centerTadpoleVisible: false, //
      centerVisible: true, //热力图与蝌蚪图进行切换
      dateTime: "2017-10-1", //默认时间展示为2017-10-01
      //默认第一个选项卡
      activeName: "first",
      tabPosition: "left"
    };
  },
  methods: {
    open() {
      this.$alert("这是一段内容", "标题名称", {
        confirmButtonText: "确定",
        callback: action => {
          this.$message({
            type: "info",
            message: `action: ${action}`
          });
        }
      });
    },
    open1() {
      const h = this.$createElement;

      this.$notify({
        title: "海口市交通流量蝌蚪图",
        message: h("i", { style: "color: teal" }, "切换成为街道蝌蚪图")
      });
    },
    getNowDate:function(val) {
      this.nowTime = val;
      console.log("这是在Dashboard里面的时间" + this.nowTime);
      this.$store.state.TimeDate=this.nowTime;
      console.log("修改state"+this.$store.state.TimeDate);
    }
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
          <a>
            <el-button type="text" @click="centerVisible = true ; ">交通流量蝌蚪图</el-button>
          </a>
        </li>
        <li>
          <a>
            <el-button type="text" @click="centerVisible = false ;">交通流量热力图</el-button>
          </a>
        </li>
        <li>
          <a>
            <el-button type="text" @click="centerMoveToVisible = true">交通流量迁徙图</el-button>
          </a>
        </li>
        <li>
          <a>
            <el-button type="text" @click="centerForcastVisible = true">交通流量预测组合图</el-button>
          </a>
        </li>
        <li>
          <a>
            <el-button type="text" @click="centerDepVisible = true">具体街道情况交通流量和弦图</el-button>
          </a>
        </li>
        <li>
          <a>
            <el-button type="text" @click="centerOrderNumVisible = true">订单的出行距离与该订单整体数量组合折线图</el-button>
          </a>
        </li>
      </ul>
    </div>
    <!-- 弹窗部分 -->
    <el-dialog title="交通流量预测组合图" :visible.sync="centerForcastVisible" width="75%" center>
      <span>
        <!-- 整体预测柱状图 -->
        <PreBarChart></PreBarChart>
      </span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="centerForcastVisible = false">取 消</el-button>
        <el-button type="primary" @click="centerForcastVisible = false">确 定</el-button>
      </span>
    </el-dialog>

    <el-dialog title="该天订单的出行距离与整体数量组合折线图" :visible.sync="centerOrderNumVisible" width="75%" center>
      <span>
        <centerOrderNumChart></centerOrderNumChart>
        <RateLineChart></RateLineChart>
      </span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="centerOrderNumVisible = false">取 消</el-button>
        <el-button type="primary" @click="centerOrderNumVisible = false">确 定</el-button>
      </span>
    </el-dialog>

    <el-dialog title="该天交通流量迁徙图" :visible.sync="centerMoveToVisible" width="75%" center>
      <span>
        <MoveToChart></MoveToChart>
      </span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="centerMoveToVisible = false">取 消</el-button>
        <el-button type="primary" @click="centerMoveToVisible = false">确 定</el-button>
      </span>
    </el-dialog>

    <el-dialog :visible.sync="centerDepVisible" width="75%" fullscreen="true" center>
      <span>
        <ChordChart></ChordChart>
      </span>
      <!-- <span slot="footer" class="dialog-footer">
        <el-button @click="centerDepVisible = false">取 消</el-button>
        <el-button type="primary" @click="centerDepVisible = false">确 定</el-button>
      </span>-->
    </el-dialog>

    <!-- 时间选择器 -->
    <div class="block">
      <!-- <el-date-picker v-model="value1" type="date"  placeholder="选择日期"></el-date-picker> -->
      <el-date-picker
        v-model="dateTime"
        type="date"
        value-format="yyyy-MM-dd"
        placeholder="选择日期"
        @change="getNowDate"
      ></el-date-picker>
    </div>

    <!-- 官网上说了router全部都要渲染到这里 -->
    <div class="center-area">
      <!-- 主图展示区 -->
      <!-- <el-container>
        <el-main style="height:400px;width: 950px;">
          <el-tabs v-model="activeName" :tab-position="tabPosition">
            <el-tab-pane label="交通流量蝌蚪图" name="first" :key="'first'">
              <TadpoleChart></TadpoleChart>
            </el-tab-pane>
            <el-tab-pane label="交通流量热力图" name="second" :key="'second'">
              <MoveToChart></MoveToChart>
            </el-tab-pane>
            <el-tab-pane label="交通流量花弦图" name="third" :key="'third'">交通流量花弦图</el-tab-pane>
            <el-tab-pane label="交通流量订单预测散点图" name="fourth" :key="'fourth'">交通流量散点图</el-tab-pane>
          </el-tabs>
        </el-main>
        <el-footer>
          <LineCharts></LineCharts>
        </el-footer>
      </el-container>-->

      <!-- 版本2 -->
      <!-- <el-container>
        <el-main style="height:400px;width: 950px;">
            <el-main label="交通流量蝌蚪图" v-show="centerVisible" style="overflow:hidden">
              <TadpoleChart></TadpoleChart>
            </el-main>
            <el-main label="交通流量热力图" v-show="!centerVisible" style="overflow:hidden">
               <HeatMapChart></HeatMapChart>
            </el-main>
            <el-main label="交通流量花弦图" name="third" :key="'third'">交通流量花弦图</el-main>
            <el-main label="交通流量订单预测散点图" name="fourth" :key="'fourth'">交通流量散点图</el-main>
        </el-main>
        <el-footer>
          <LineCharts></LineCharts>
        </el-footer>
      </el-container>-->

      <!-- 版本3 -->
      <!-- <el-container>
        <el-main style="height:400px;width: 950px;">
          <TadpoleChart label="交通流量蝌蚪图" v-show="centerVisible" style="overflow:hidden"></TadpoleChart>
          <HeatMapChart label="交通流量热力图" v-show="!centerVisible" style="overflow:hidden"></HeatMapChart>
        </el-main>
        <el-footer>
          <LineCharts></LineCharts>
        </el-footer>
      </el-container>-->

      <!-- 版本4 -->
      <div style="width: 950px;height:400px;">
        <TadpoleChart label="交通流量蝌蚪图" v-show="centerVisible"></TadpoleChart>
        <HeatMapChart label="交通流量热力图" v-show="!centerVisible"></HeatMapChart>
      </div>
      <div style="width: 950px;height:300px;">
        <LineCharts></LineCharts>
      </div>
    </div>

    <div class="right-area">
      <h3 style="color:white">
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
      <div class="time-base"></div>
      <b class="line2"></b>
    </div>
  </div>
</template>
    

<style scoped>
@import "../assets/css/mobile.css";
/* @import "../assets/css/jqueryui.css"; */
@import "../assets/css/default.css";

.menu {
  height: 100vh;
}
.el-menu-item {
  text-align: left;
  border-bottom: 1px solid gray;
}
.aside-col {
  display: inline-block;
  float: left;
  width: 200px;
}
.main-col {
  position: fixed;
  left: 220px;
  display: inline-block;
  width: calc(100% - 240px);
  overflow: hidden;
}
.block {
  position: fixed;
  right: 0;
  text-align: center;
}
</style>




