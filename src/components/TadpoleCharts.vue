<template>
  <div id="app">
    <div id="TadpoleChart" style="width: 1000px;height:450px;">
      <!-- <div class="input-card" id>
        <input
          id="analysis"
          class="btn"
          onclick="analysis()"
          type="button"
          style="margin-bottom: 5px; margin-left: 90px; width: 150px"
          value="订单类别"
        />
        <input
          id="pushData"
          class="btn"
          onclick="pushData()"
          type="button"
          style="margin-bottom: 5px; margin-left: 90px; width: 150px"
          value="拥塞分析"
        />
        <input
          id="hotmap3d"
          class="btn"
          onclick="hotmap3d()"
          type="button"
          style="margin-bottom: -20px;margin-left: 90px; width: 150px"
          value="添加3D热力图"
      />-->
      <!--                <input id="hotmap3dd" class="btn" onclick="hotmap3dd()" type="button" style="margin-bottom: -20px;margin-left: 90px; width: 150px" value="删除3D热力图" />-->

      <!-- </div> -->
    </div>
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
    console.log("蝌蚪图初始化成功！");
    this.drawTadpoleChart();
  },
  methods: {
    drawTadpoleChart() {
      // console.log(1);
      /*ECharts图表*/
      var tempbusLinesk = new Array();
      var tempbusLinesk2 = new Array();
      let myChartk = echarts.init(document.getElementById("TadpoleChart"));
      var didiData = new Array();
      //没有加载出来使用加载动画
      myChartk.showLoading();
      // console.log("这是蝌蚪图");
      this.$axios
        // 读取json文件到didiData
        .get("../../static/data/TadpoleChart/2017-05-13/0小时.json")
        .then(res => {
          didiData = res.data;
          // console.log("这是蝌蚪图数据" + didiData); //打印看看数据吧
          // console.log(didiData.type)
        });
        
      var hStep = 300 / (didiData.length - 1); //路径颜色
      //*********************buslinesk这里出现问题了**************需要修正  */
      var busLinesk = [].concat.apply(
        [],
        didiData.map(function(busLine, idx) {
          var points = []; //每条轨迹的数据
          for (var i = 0; i < busLine[0].length; i += 2) {
            var pt = [busLine[0][i], busLine[0][i + 1]]; //初始化pt坐标
            points.push([pt[0], pt[1]]); //存入points
            // console.log(points);
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
      console.log("1"+busLinesk);
      tempbusLinesk = busLinesk;

      var busLinesk2 = [].concat.apply(
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
      let option = {
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
      };

      setTimeout(() => {
        //未来让加载动画效果明显,这里加入了setTimeout,实现2s延时
        myChartk.hideLoading(); //没有加载出来隐藏加载动画
        myChartk.setOption(option); //初始化蝌蚪图样例
      }, 2000);
    }
  }
};

//模块一：使用订单类别分析功能
function analysis() {
  var g = document.getElementById("demo1").textContent.split("时")[0];
  var f = document.getElementById("demo").textContent;
  var myChartk = echarts.init(document.getElementById("TadpoleChart"));
  myChartk.clear();
  var didiData = new Array();

  //数据读取需要改动
  this.$axios
    .get("../../static/data/TadpoleChart/2017-05-13/0小时.json")
    .then(res => {
      didiData = res.data;
      // console.log(didiData); //打印看看数据吧
    });

  var hStep = 300 / (didiData.length - 1); //路径颜色
  busLinesk = [].concat.apply(
    [],
    didiData.map(function(busLine, idx) {
      var points = [];
      for (var i = 0; i < busLine[0].length; i += 2) {
        //每条轨迹的数据
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
            )
          }
        }
      };
    })
  );
  tempbusLinesk = busLinesk;
  //用于蝌蚪图画线，数据处理待优化
  var busLinesk2 = [].concat.apply(
    [],
    didiData.map(function(busLine, idx) {
      var points = [];
      for (var i = 0; i < busLine[0].length; i += 2) {
        var pt = [busLine[0][i], busLine[0][i + 1]];
        points.push([pt[0], pt[1]]); //存入points
      }
      return {
        //往buslines返回数据
        coords: points
      };
    })
  );
  tempbusLinesk2 = busLinesk2;
  let option = {
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
        // coordinateSystem: 'bmap',
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
  };
  //初始化订单类型分析
  myChartk.setOption(option);
  var series = [
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
  ];
  if (document.getElementById("pushData").value === "订单类别") {
    series.push({
      type: "lines",
      coordinateSystem: "amap",
      polyline: true,
      data: busLinesk2,
      silent: true,
      lineStyle: {
        normal: {
          opacity: 0.2,
          width: 1
        }
      },
      progressiveThreshold: 500,
      progressive: 200
    });
  }
}

//*模块二：添加/删除线
function pushData(f, g) {
  var g = document.getElementById("demo1").textContent.split("时")[0];
  var f = document.getElementById("demo").textContent;
  var myChartk = echarts.init(document.getElementById("TadpoleChart"));
  var didiData = new Array();

  //数据读取需要改动
  this.$axios
    .get("../../static/data/TadpoleChart/2017-05-13/0小时.json")
    .then(res => {
      didiData = res.data;
      console.log(didiData); //打印看看数据吧
    });

  var hStep = 300 / (didiData.length - 1); //路径颜色
  busLinesk = [].concat.apply(
    [],
    didiData.map(function(busLine, idx) {
      var points = [];
      for (var i = 0; i < busLine[0].length; i += 2) {
        //每条轨迹的数据
        var pt = [busLine[0][i], busLine[0][i + 1]]; //初始化pt坐标
        points.push([pt[0], pt[1]]); //存入points
      }
      return {
        //往buslines返回数据
        coords: points,
        lineStyle: {
          normal: {
            color: "rgb(255,0,0)"
          }
        }
      };
    })
  );
  tempbusLinesk = busLinesk;

  myChartk.setOption(
    (option = {
      amap: {
        // 加载 amap 组件  高德地图支持的初始化地图配置
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
          effect: {
            constantSpeed: 20,
            show: true,
            trailLength: 0.1,
            symbolSize: 1.5
          },
          zlevel: 1
        }
      ]
    })
  );
  myChartk.setDataSet(busLinesk1);
}

//*模块三：添加订单热力图分析
function hotmap3d() {
  var g = document.getElementById("demo1").textContent.split("时")[0];
  var f = document.getElementById("demo").textContent;
  var myChartk = echarts.init(document.getElementById("TadpoleChart"));
  var didiData = new Array();
  myChartk.setOption(
    (option = {
      amap: {
        // 加载 amap 组件
        center: [110.32835483551025, 20.01996791722277], // 高德地图初始中心经纬度
        zoom: 13, // 高德地图初始缩放级别
        resizeEnable: true, // 是否开启resize
        mapStyle: "amap://styles/grey", // 自定义地图样式主题
        echartsLayerZIndex: 2019, // 高德地图自定义EchartsLayer的zIndex，默认2000
        viewMode: "3D", //开启3D视图,默认为关闭
        buildingAnimation: true //楼块出现是否带动画
      }
    })
  );

  var layer = myChartk
    .getModel()
    .getComponent("amap")
    .getLayer();
  var map = myChartk
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

  var heatmap = new AMap.Heatmap(map, heatmapOpts); //初始化heatmap对象
  var heatmap2 = new AMap.Heatmap(map, heatmapOpts2);

  var heatmapData = new Array(); //start                                                                            //3d热力图数据
  $.ajax({
    url: "data/" + f + "_start/" + g + ".json",
    async: false,
    success: function(data) {
      heatmapData = data;
    }
  });

  var heatmapData2 = new Array();
  $.ajax({
    url: "data/" + f + "_start/" + g + ".json",
    async: false,
    success: function(data) {
      heatmapData2 = data;
    }
  });

  //*模块五：3d热力图
  // -------------------------------------------------------------------------------------
  var heatmapOpts = {
    //出发
    gradient: {
      0.5: "rgb(0,255,0)",
      0.65: "rgb(0,255,127)",
      0.7: "rgb(0,255,255)",
      0.9: "rgb(0,127,255)",
      1.0: "rgb(0,0,255)"
    }
  };

  var heatmapOpts2 = {
    //到达
    gradient: {
      0.5: "rgb(255,255,0)",
      0.65: "rgb(255,180,0)",
      0.7: "rgb(255,200,0)",
      0.9: "rgb(255,80,0)",
      1.0: "rgb(255,0,0)"
    }
  };
  heatmap2.setDataSet({
    data: heatmapData2,
    max: 20
  });
  heatmap.setDataSet({
    data: heatmapData,
    max: 20
  });
}
</script>