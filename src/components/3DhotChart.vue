<template>
  <div id="app">
    <div id="HeatMapChart" style="width: 1200px;height:800px;"></div>
  </div>
</template>
<script>
var echarts = require("echarts");
// 引入 ECharts 主模块
//3DhotChart (3D热力图）用于展示海口市订单整体分布情况
var echarts = require("echarts/lib/echarts");

export default {
  name: "3DhotChart",
  data() {
    return {
      ThreeDhotChart: "",
      hotChartOption: {}
    };
  },
  computed: {},
  mounted() {
    this.drawHeatMapChart();
  },
  methods: {
    drawHeatMapChart() {
      let option = {
        title: {
          text: "海口市车流量热力图",
          left: "center",
          top: 20,
          textStyle: {
            color: "#cdddf7",
            fontSize: 20
          },
          subtextStyle: {
            color: "white",
            fontSize: 16
          }
        },
        amap: {
          center: [110.33835483551025, 20.01996791722277], // 高德地图初始化中心经纬度
          zoom: 12, // 高德地图初始缩放级别
          resizeEnable: true, // 是否开启resize
          mapStyle: "amap://styles/grey", // 自定义地图样式主题
          echartsLayerZIndex: 2019, // 高德地图自定义EchartsLayer的zIndex，默认2000
          viewMode: "3D", // 开启3D视图,默认为关闭
          buildingAnimation: true // 楼块出现是否带动画
        }
      };

      var layer = myChartks.getModel().getComponent('amap').getLayer();
        var map = myChartks.getModel().getComponent('amap').getAMap();
        layer.setzIndex(2019)
        map.addControl(new AMap.ControlBar({
            showZoomBar: false,
            showControlButton: true,
            position: {
                right: '10px',
                top: '10px'
            }
        }))

         var heatmap = new AMap.Heatmap(map, heatmapOpts);                                                               //初始化heatmap对象
        var heatmap2 = new AMap.Heatmap(map, heatmapOpts2);
        //获取数据json
        var heatmapData = require('../../static/data/start/3DhotChart/2017-05-13/10.json')
        var heatmapData2 = require('../../static/data/dest/3DhotChart/2017-05-13/10.json')
        console.log(heatmapData);
        console.log(heatmapData2);
    }
  }
};
</script>