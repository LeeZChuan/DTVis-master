<template>
  <div id="app">
    <div id="HeatMapChart" style="width: 1200px;height:800px;"></div>
  </div>
</template>
<script>
var echarts = require("echarts");
// 引入 ECharts 主模块
//3DhotChart (3D热力图）用于展示海口市订单整体分布情况-目前只做出发地点的订单情况热力图
// var echarts = require("echarts/lib/echarts");
require("echarts-extension-amap");

export default {
  name: "3DhotChart",
  data() {
    return {};
  },
  computed: {},
  mounted() {
    this.drawHeatMapChart();
  },
  methods: {
    drawHeatMapChart() {
      //获取数据json起点订单数量热力图
      // var heatmapData = require("../../static/data/3DhotChart/start/2017-05-13/10.json");
      // var heatmapData2 = require('../../static/data/3DhotChart/dest/2017-05-13/10.json');
      var myChartks = echarts.init(document.getElementById("HeatMapChart"));
      this.$axios
        // 读取json文件到didiData
        .get("../../static/data/3DhotChart/start/2017-05-13/10.json")
        .then(res => {
          var heatmap = new AMap.Heatmap(map, heatmapOpts); //初始化heatmap对象
          var didiStartHotData = res.data;
          console.log(didiStartHotData);
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

          //没有加载出来使用加载动画
          myChartks.showLoading();
          var layer = myChartks
            .getModel()
            .getComponent("amap")
            .getLayer();
          var map = myChartks
            .getModel()
            .getComponent("amap")
            .getAMap();
          layer.setzIndex(2019);
          map.addControl(
            new AMap.ControlBar({
              showZoomBar: false,
              showControlButton: true,
              position: {
                right: "10px",
                top: "10px"
              }
            })
          );

          // var heatmap2 = new AMap.Heatmap(map, heatmapOpts2);

          //*模块五：3d热力图
          var heatmapOpts = {
            //出发区域
            gradient: {
              0.5: "rgb(0,255,0)",
              0.65: "rgb(0,255,127)",
              0.7: "rgb(0,255,255)",
              0.9: "rgb(0,127,255)",
              1.0: "rgb(0,0,255)"
            }
          };
          // var heatmapOpts2 = {
          //   //到达区域
          //   gradient: {
          //     0.5: "rgb(255,255,0)",
          //     0.65: "rgb(255,180,0)",
          //     0.7: "rgb(255,200,0)",
          //     0.9: "rgb(255,80,0)",
          //     1.0: "rgb(255,0,0)"
          //   }
          // };

          // heatmap2.setDataSet({
          //   data: heatmapData2,
          //   max: 20
          // });
          heatmap.setDataSet({
            data: didiStartHotData,
            max: 20
          });

          setTimeout(() => {
            //未来让加载动画效果明显,这里加入了setTimeout,实现2s延时
            myChartks.hideLoading(); //没有加载出来隐藏加载动画
            myChartks.setOption(option, true); //初始化蝌蚪图样例
          }, 5000);
        });
    }
  }
};
</script>