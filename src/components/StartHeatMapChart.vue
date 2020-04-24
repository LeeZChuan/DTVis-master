<template>
  <div id="container">
    <!-- 订单起点情况热力图，宽度很合适，实现了地图的旋转以及放大缩小 -->
    <el-amap id="HeatMapChart"></el-amap>

    <!-- <div class="input-card">
      <div class="input-item">
        <input type="checkbox" onclick="toggleScale(this)" />比例尺
      </div>

      <div class="input-item">
        <input type="checkbox" id="toolbar" onclick="toggleToolBar(this)" />工具条
      </div>

      <div class="input-item">
        <input
          type="checkbox"
          id="toolbarDirection"
          disabled
          onclick="toggleToolBarDirection(this)"
        />工具条方向盘
      </div>

      <div class="input-item">
        <input type="checkbox" id="toolbarRuler" disabled onclick="toggleToolBarRuler(this)" />工具条标尺
      </div>

      <div class="input-item">
        <input type="checkbox" id="overview" onclick="toggleOverViewShow(this)" />显示鹰眼
      </div>

      <div class="input-item">
        <input type="checkbox" id="overviewOpen" disabled onclick="toggleOverViewOpen(this)" />展开鹰眼
      </div>
    </div>-->
    <!-- <div class="input-card" style="width: auto;">
      <div class="input-item">
        <button class="btn" onclick="map.show()">显示热力图</button>
      </div>
      <div class="input-item">
        <button class="btn" onclick="map.hide()">关闭热力图</button>
      </div>
    </div>-->
  </div>
</template>

<script>
// import { lazyAmapApiLoaderInstanse } from "vue-amap";
require("echarts-extension-amap");
var echarts = require("echarts");
export default {
  name: "HeatMapChart",
  data() {
    return {};
  },
  comptude:{
    TimeDate()
    {
      return this.$store.state.TimeDate
    }
  },
  mounted() {
    this.drawHeatMapChart();
  },
  methods: {
    drawHeatMapChart() {
      // console.log("这是热力图的数据"+TimeDate);
      //   var HeatmapChart = echarts.init(document.getElementById("HeatMapChart"));
      this.$axios
        // 读取json文件到didiData
        .get("../../static/data/3DhotChart/start/"+{{msg2}}+"/10.json")
        .then(res => {
          var heatmap = new AMap.Heatmap(map, heatmapOpts); //初始化heatmap对象
          var didiStartHotData = res.data;
          var lnglat = new AMap.LngLat(110.32835483551025, 20.01996791722277);
          var map = new AMap.Map("HeatMapChart", {
            viewMode: "3D",
            pitch: 0, //俯仰角度，默认0，[0,83]，2D地图下无效 。
            resizeEnable: true, //是否监控地图容器尺寸变化，默认值为false
            center: lnglat,
            zoom: 13,
            mapStyle: "amap://styles/grey", // 自定义地图样式主题
            // echartsLayerZIndex: 2019, // 高德地图自定义EchartsLayer的zIndex，默认2000
            buildingAnimation: true,
            rotateEnable: true, //可以旋转
            pitchEnable: true,
            resizeEnable: true
          });

          //3D罗盘控制
          AMap.plugin(["AMap.ControlBar"], function() {
            // 添加 3D 罗盘控制
            map.addControl(new AMap.ControlBar());
          });

          //热力图相关参数
          var heatmapOpts = {
            //3d 相关的参数
            "3d": {
              //热度转高度的曲线控制参数，可以利用左侧的控制面板获取
              heightBezier: [0.465, 0.115, 0.8, 0.36],
              //取样精度，值越小，曲面效果越精细，但同时性能消耗越大
              gridSize: 2,
              heightScale: 1
            }
          };
          //初始化heatmap对象
          var heatmap = new AMap.Heatmap(map, heatmapOpts);
          //设置数据集
          heatmap.setDataSet({
            data: didiStartHotData,
            max: 20
          });
        });
    }
  }
};
</script>
<style>
#HeatMapChart {
  width: 950px;
  height: 400px;
}
.input-card {
  width: 150px;
  top: 10px;
  bottom: auto;
}
.context_menu {
  position: relative;
  min-width: 12rem;
  padding: 0;
  background:white;
}

.context_menu p {
  cursor: pointer;
  padding: 0.25rem 1.25rem;
}

.context_menu p:hover {
  background: #ccc;
}
</style>