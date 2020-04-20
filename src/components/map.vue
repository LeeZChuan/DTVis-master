<template>
  <div>
    <el-amap id="HeatMapChart" style="height: 400px;"></el-amap>
    <!-- <div class="input-card" style="width: auto;">
      <div class="input-item">
        <button class="btn" onclick="map.show()">显示热力图</button>
      </div>
      <div class="input-item">
        <button class="btn" onclick="map.hide()">关闭热力图</button>
      </div>
    </div> -->
  </div>
</template>

<script>
import { lazyAmapApiLoaderInstanse } from "vue-amap";
var echarts = require("echarts");
export default {
  name: "HeatMapChart",
  data() {
    return {};
  },
  mounted() {
    this.drawHeatMapChart();
  },
  methods: {
    drawHeatMapChart() {
      //   var HeatmapChart = echarts.init(document.getElementById("HeatMapChart"));
      this.$axios
        // 读取json文件到didiData
        .get("../../static/data/3DhotChart/start/2017-05-13/10.json")
        .then(res => {
          var heatmap = new AMap.Heatmap(map, heatmapOpts); //初始化heatmap对象
          var didiStartHotData = res.data;
          var map = new AMap.Map("HeatMapChart", {
            viewMode: "3D",
            pitch: 70,
            resizeEnable: true,
            center: [110.32835483551025, 20.01996791722277],
            zoom: 13,
            resizeEnable: true, // 是否开启resize
            mapStyle: "amap://styles/grey", // 自定义地图样式主题
            echartsLayerZIndex: 2019, // 高德地图自定义EchartsLayer的zIndex，默认2000

            buildingAnimation: true
          });

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
</style>