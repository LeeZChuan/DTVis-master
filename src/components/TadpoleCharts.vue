<template>
  <div id="app">
    <div id="TadpoleChart" style="width: 1000px;height:450px;"></div>
<!-- 添加图表的操作事件，添加点击事件 -->
  </div>
</template>

<!--蝌蚪图：用于展示整体主图的效果-->
<script>
var echarts = require("echarts");

export default {
  name: "TadpoleCharts",
  data() {
    return {
      msg: "Welcome to TadpoleCharts"
    };
  },
  mounted() {
    //页面初始化函数
    console.log("蝌蚪图初始化成功");
    this.drawTadpoleChart();
  },
  methods: {
    drawTadpoleChart() {
      /*ECharts图表*/
      // function kedoutu(f, g) {}
      var tempbusLinesk = new Array();
      var tempbusLinesk2 = new Array();
      var myChartk = echarts.init(document.getElementById("TadpoleChart"));
      var didiData = new Array();
      this.$axios
        .get("../../static/data/TadpoleChart/2017-05-13/0小时.json")
        .then(res => {
          didiData = res.data;
          console.log(didiData); //打印看看数据吧
          // 读取json文件到didiData
          var hStep = 300 / (didiData.length - 1); //路径颜色
              busLinesk = [].concat.apply(
                [],
                didiData.map(function(busLine, idx) {
                  var points = []; //每条轨迹的数据
                  for (var i = 0; i < busLine[0].length; i += 2) {
                    var pt = [busLine[0][i], busLine[0][i + 1]]; //初始化pt坐标
                    points.push([pt[0], pt[1]]); //存入points
                  }
                  return {
                    //往buslines返回数据
                    coords: points,
                    lineStyle: {
                      normal: {
                        color: echarts.color.modifyHSL(
                          "rgb(255,122,0)",
                          Math.round(hStep * idx)
                        ) //
                      }
                    }
                  };
                })
              );
              tempbusLinesk = busLinesk;
    
              let busLinesk2 = [].concat.apply(
                [],
                didiData.map(function(busLine, idx) {
                  //用于蝌蚪图画线，数据处理待优化
                  var points = [];
                  for (var i = 0; i < busLine[0].length; i += 2) {
                    var pt = [busLine[0][i], busLine[0][i + 1]];
                    points.push([pt[0], pt[1]]); //存入points
                  }
                  return {
                    coords: points //往buslines返回数据
                  };
                })
              );
              tempbusLinesk2 = busLinesk2;
          //初始化蝌蚪图属性
          let option= {
              //标题
              title: {
                text: "海口市车流量蝌蚪图",
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
              // 加载 amap 组件
              amap: {
                // 高德地图支持的初始化地图配置
                center: [110.32835483551025, 20.01996791722277], // 高德地图初始中心经纬度
                zoom: 13, // 高德地图初始缩放级别
                resizeEnable: true, // 是否开启resize
                mapStyle: "amap://styles/grey", // 自定义地图样式主题
                echartsLayerZIndex: 2019, // 高德地图自定义EchartsLayer的zIndex，默认2000
                // 说明：如果想要添加卫星、路网等图层
                // 暂时先不要使用layers配置，因为存在Bug
                // 建议使用amap.add的方式，使用方式参见最下方代码
                viewMode: "3D", //开启3D视图,默认为关闭
                buildingAnimation: true //楼块出现是否带动画
              },
              series: [
                {
                  type: "lines",
                  coordinateSystem: "amap",
                  polyline: true,
                  data: busLinesk,
                  lineStyle: {
                    normal: {
                      width: 0
                    }
                  },
                  effect: {
                    constantSpeed: 20,
                    show: true,
                    trailLength: 0.1,
                    symbolSize: 1.5
                  },
                  zlevel: 1
                }
              ]
            }
          //初始化蝌蚪图样例
          myChartk.setOption(option);
        });
    }
  }
};
</script>