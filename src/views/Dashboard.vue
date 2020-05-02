<script>
//该文件为网页效果的页面布局整体网页
import TadpoleChart from "../components/TadpoleCharts.vue"; //蝌蚪图
import MoveToChart from "../components/MoveToChart.vue"; //交通流量整体流量迁徙图
import LineCharts from "../components/LineCharts.vue"; //出行距离与出行次数折线图
import CalendarChart from "../components/CalendarChart.vue"; //日期订单情况热力图
// import ForecastChart from "../components/ForecastChart"; //预测情况散点图界面
import ForecastPointChart from "../components/ForecastPointChart"; //预测起终点散点界面
import StartHeatMapChart from "../components/StartHeatMapChart.vue"; //起点订单情况热力图界面
import EndHeatMapChart from "../components/EndHeatMapChart.vue"; //终点订单情况热力图界面
// import multiputeMap from "./components/multiputeMap.vue"; //用于展示海口市地区订单情况散点雷达图
import ChordChart from "../components/ChordChart.vue"; //订单情况街道和弦图
import centerOrderNumChart from "../components/OrderNumLineChart.vue"; //订单数量情况与出行距离折线图
import RateLineChart from "../components/RateLineChart.vue"; //订单情况每小时变化率折线图
import PreBarChart from "../components/PreBarChart.vue"; //预测界面的柱状图
// import PointMap from "../components/PointMap.vue";
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
    StartHeatMapChart,
    EndHeatMapChart,
    centerOrderNumChart,
    RateLineChart,
    // multiputeMap,
    ChordChart,
    // PointMap
  },
  data() {
    return {
      centerForcastVisible: false, //预测部分界面弹窗
      centerOrderNumVisible: false, //订单的出行距离与该订单出行距离数量组合折线图弹窗
      centerMoveToVisible: false, //订单情况区域迁徙图的弹窗
      centerDepVisible: false, //订单情况街道流向和弦图
      centerTadpoleVisible: false, //
      centerVisible: false, //热力图与蝌蚪图进行切换
      StartOrEnd: true, //起终点订单情况热力图切换按钮
      analysis: true, //蝌蚪图街道分析开关
      BubbleOpenorDown: false, //气泡图开关
      dateTime: "2017-10-1", //默认时间展示为2017-10-01
      drawer: false, //右侧抽屉
      Controldrawer: false, //下方抽屉
      direction: "rtl", //左开
      direction1: "btt",
      activeNames: "1" //手风琴展示初始化
    };
  },
  computed: {
    NowTimeHour() {
      return this.$store.getters.NowTime;
    },
    GetNowLongRecent()
    {
      return this.$store .getters.GetNowRecentLong;
    },
    GetNowFastRecent()
    {
      return this.$store.getters.GetNowRecentFast;
    },
    GetNowHighRecent()
    {
      return this.$store.getters.GetNowRecentHigh;
    },
    GetNowLongTimeRecent()
    {
      return this.$store.getters.GetNowRecentLongTime;
    },

  },
  methods: {
    upNowhour: function() {
      //获取当前展示具体天数的准确时间
      // this.$store.state.TimeHour++
      var i = this.$store.state.TimeHour;
      this.$store.commit("updateTimeHour", ++i);
    },
    downNowhour: function() {
      //获取当前展示具体天数的准确时间
      // this.$store.state.TimeHour--
      var i = this.$store.state.TimeHour;
      this.$store.commit("updateTimeHour", --i);
    },
    getNowDate: function(val) {
      //获取当前展示天数的方法
      this.nowTime = val;
      // this.$store.state.TimeDate = this.nowTime;
      this.$store.commit("updateTimeDate", this.nowTime);
      console.log(this.$store.getters.GetNowRecent[1]);
      // return this.$store.getters.GetNowRecent;
    },
    OpenAnalysis:function()
    {
      // let vm=this;
      this.$refs.TadpoleChart.analysis();
    },
    EndAnalysis:function()
    {
      this.$refs.TadpoleChart.drawTadpoleChart();
    },
    handleClose(done) {
      this.$confirm("确认关闭？")
        .then(_ => {
          done();
        })
        .catch(_ => {});
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
          <p>滴滴订单长途占比</p>
          <strong>{{GetNowLongRecent}}</strong>
        </li>
        <li>
          <b class="animation-1"></b>
          <b class="animation-2"></b>
          <b class="animation-3"></b>
          <p>滴滴订单快车占比</p>
          <strong>{{GetNowFastRecent}}</strong>
        </li>
        <li>
          <b class="animation-1"></b>
          <b class="animation-2"></b>
          <b class="animation-3"></b>
          <p>滴滴订单高费用占比</p>
          <strong>{{GetNowHighRecent}}</strong>
        </li>
        <li>
          <b class="animation-1"></b>
          <b class="animation-2"></b>
          <b class="animation-3"></b>
          <p>滴滴订单高时长占比</p>
          <strong>{{GetNowLongTimeRecent}}</strong>
        </li>
        <li>
          <b class="animation-1"></b>
          <b class="animation-2"></b>
          <b class="animation-3"></b>
          <p>滴滴订单整体占比</p>
          <strong>99.9%</strong>
        </li>
        <li>
          <b class="animation-1"></b>
          <b class="animation-2"></b>
          <b class="animation-3"></b>
          <p>滴滴订单时长占比</p>
          <strong>99.99%</strong>
        </li>
      </ul>
    </div>

    <!-- 操作台：用于操作交通流量可视化平台的参数与相关信息 -->
    <div class="submenu">
      <ul>
        <li>
          <a>
            <el-button type="text" @click="centerVisible = true ">交通流量蝌蚪图</el-button>
          </a>
        </li>
        <li>
          <a>
            <el-button type="text" @click="centerVisible = false ">交通流量热力图</el-button>
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
        <li>
          <a>
            <el-button @click="drawer = true" type="text" style="margin-left: 16px;">主图操控台</el-button>
          </a>
        </li>
        <li>
          <a>
            <el-button
              @click="Controldrawer = true"
              type="text"
              style="margin-left: 16px;"
            >该天交通流量确切时间点切换控制台</el-button>
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
    </el-dialog>

    <!-- 抽屉-->
    <!-- 下方抽屉 -->
    <el-drawer
      title="该天交通流量切换控制台"
      :visible.sync="Controldrawer"
      :direction="direction1"
      :before-close="handleClose"
      :modal="false"
      :with-header="false"
      size="20%"
    >
      <span>
        <el-col :span="6">
          <div class="grid-content bg-purple"></div>
        </el-col>
        <el-col :span="6">
          <div class="grid-content bg-purple"></div>
        </el-col>
        <el-col :span="6">
          <div class="grid-content bg-purple"></div>
        </el-col>
        <el-col :span="6">
          <div class="grid-content bg-purple"></div>
        </el-col>
        <el-col :span="4">
          <div class="grid-content bg-purple"></div>
        </el-col>
        <el-col :span="4">
          <div class="grid-content bg-purple-light">
            <el-button class="button" plain @click="downNowhour()">上一小时</el-button>
          </div>
        </el-col>
        <el-col :span="4">
          <div class="grid-content bg-purple">
            <el-button class="button" plain @click="upNowhour()">下一小时</el-button>
          </div>
        </el-col>
        <el-col :span="4">
          <div class="grid-content bg-purple-light">
            <!-- <div>三维气泡图标注开关</div>
            <el-switch v-model="openBubble" active-color="#13ce66" inactive-color="#ff4949"></el-switch> -->
          </div>
        </el-col>
        <el-col :span="4">
          <div class="grid-content bg-purple"></div>
        </el-col>
        <el-col :span="4">
          <div class="grid-content bg-purple-light"></div>
        </el-col>

        <!-- <el-button class="button" plain @click="downNowhour()">上一小时</el-button>
        <el-button class="button" plain @click="upNowhour()">下一小时</el-button>
        <el-switch v-model="openBubble" active-color="#13ce66" inactive-color="#ff4949"></el-switch>-->
      </span>
    </el-drawer>

    <!-- 右边抽屉 -->
    <el-drawer
      title="主图操控台"
      :visible.sync="drawer"
      :direction="direction"
      :before-close="handleClose"
      size="20%"
    >
      <span>
        <el-collapse v-model="activeNames" accordion>
          <el-collapse-item title="订单情况起终点热力图控制台" name="1">
            <strong style="line-height：20pt">订单起终点城区热力图:</strong>
            <el-switch
              style="display: block;line-height：20pt"
              v-model="StartOrEnd"
              active-color="#13ce66"
              inactive-color="#ff4949"
              active-text="起点热力图"
              inactive-text="终点热力图"
            ></el-switch>
            <strong style="line-height：20pt">三维气泡图整体分析:</strong>
            <el-switch
              style="display: block;line-height：20pt"
              v-model="BubbleOpenorDown"
              active-color="#13ce66"
              inactive-color="#ff4949"
              active-text="开启"
              inactive-text="关闭"
            ></el-switch>
          </el-collapse-item>
          <el-collapse-item title="订单情况流量蝌蚪图" name="2">
            <strong style="line-height：20pt">实时路况分析:</strong>
            <el-switch
              style="display: block"
              v-model="analysis"
              active-color="#13ce66"
              inactive-color="#ff4949"
              active-text="分析关闭"
              inactive-text="分析开启"
            ></el-switch>

            <el-button @change="OpenAnalysis()">开启路况分析</el-button>
            <el-button @change="EndAnalysis()">关闭路况分析</el-button>
          </el-collapse-item>
             <el-collapse-item title="订单预测情况散点图" name="3"></el-collapse-item>
        </el-collapse>
      </span>
    </el-drawer>

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
      <div>
        <div label="交通流量蝌蚪图" v-show="centerVisible">
          <TadpoleChart label="交通流量蝌蚪图"></TadpoleChart>
        </div>
        <!-- <HeatMapChart label="交通流量热力图" v-show="!centerVisible"></HeatMapChart> -->
        <div label="交通流量热力图" v-show="!centerVisible">
          <StartHeatMapChart label="交通流量起点热力图" v-show="StartOrEnd"></StartHeatMapChart>
          <!-- <div class="img-tip">{{ this.$store.getters.NowTime }}点</div>  -->
          <EndHeatMapChart label="交通流量终点热力图" v-show="!StartOrEnd"></EndHeatMapChart>
        </div>
        <div class="img-tip">{{ NowTimeHour }}点</div>
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
          <dt style="color:white">今日整体订单量</dt>
          <dd class="font12">
            <span>{{GetNowFastRecent}}</span>
            <b></b>
          </dd>
          <dt class="ml-20">今日订单高价占比率</dt>
          <dd class="font-red ml-20">
            <span>{{GetNowHighRecent}}</span>
            <b></b>
          </dd>
          <dt>今日订单高时长占比率</dt>
          <dd>
            <span>{{GetNowLongTimeRecent}}</span>
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
.img-tip {
  width: 100%;
  text-align: center;
  background: #000;
  color: #fff;
  opacity: 0.6;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
.el-row {
  margin-bottom: 20px;
}
.el-col {
  border-radius: 4px;
}
</style>




