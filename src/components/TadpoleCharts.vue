<template>
  <div id="container">
    <el-amap id="TadpoleChart">
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
    </el-amap>
    <!-- 添加图表的操作事件，添加点击事件 -->
  </div>
</template>

<!--蝌蚪图：用于展示整体主图的效果,后面需要补充按钮功能效果-finsh-->
<script>
require("echarts-extension-amap");
var echarts = require("echarts");

export default {
  name: "TadpoleCharts",
  data() {
    return {
      msg: "Welcome to TadpoleCharts"
    };
  },
  computed: {
    TimeDate() {
      return this.$store.state.TimeDate;
    },
    TimeHour() {
      return this.$store.state.TimeHour;
    }
  },
  watch: {
    TimeDate: function(curVal, oldVal) {
      //需要执行的画图代码,用于时刻监听该图的日期更换
      if (true) {
        if (curVal) {
          this.drawTadpoleChart(curVal, this.$store.state.TimeHour);
        } else {
          this.drawTadpoleChart(oldVal, this.$store.state.TimeHour);
        }
      }
    },
    TimeHour: function(CurVal, OldVal) {
      //需要执行的画图代码,用于时刻监听该图的日期更换
      if (true) {
        if (CurVal) {
          this.drawTadpoleChart(this.$store.state.TimeDate, CurVal);
        } else {
          this.drawTadpoleChart(this.$store.state.TimeDate, OldVal);
        }
      }
    }
  },
  mounted() {
    //页面初始化函数
    this.drawTadpoleChart(
      this.$store.state.TimeDate,
      this.$store.state.TimeHour
    );
  },
  methods: {
    drawTadpoleChart(Date, Hour) {
      /*ECharts图表*/
      var tempbusLinesk = new Array(); //这是普通蝌蚪图颜色保存
      var tempbusLinesk2 = new Array(); //这是预测分析按钮的颜色储存
      var myChartk = echarts.init(document.getElementById("TadpoleChart"));
      myChartk.clear();
      myChartk.showLoading();
      //数据读取需要改动
      this.$axios
        .get(
          "../../static/data/TadpoleChart/" + Date + "/" + Hour + "小时.json"
        )
        .then(res => {
          var didiData = res.data;
          var hStep = 300 / (didiData.length - 1); //路径颜色
          let busLinesk = [].concat.apply(
            [],
            didiData.map(function(busLine, idx) {
              var points = [];
              for (var i = 0; i < busLine[0].length; i += 2) {
                //每条轨迹的数据
                var pt = [busLine[0][i], busLine[0][i + 1]]; //初始化pt坐标
                points.push([pt[0], pt[1]]); //存入points
              }
              return {
                //往buslines返回数据，多种颜色
                // coords: points,
                // lineStyle: {
                //   normal: {
                //     color: echarts.color.modifyHSL(
                //       "rgb(255,122,0)",
                //       Math.round(hStep * idx)
                //     )
                //   }
                // }
                //这里就只有一种颜色添加（红色）
                coords: points,
                lineStyle: {
                    normal: {
                        color: 'rgb(255,0,0)'
                    }
                }
              };
            })
          );
          tempbusLinesk = busLinesk;
          //用于蝌蚪图画线，数据处理待优化
          let busLinesk2 = [].concat.apply(
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
          setTimeout(() => {
            //未来让加载动画效果明显,这里加入了setTimeout,实现2s延时
            myChartk.hideLoading(); //没有加载出来隐藏加载动画
            myChartk.setOption(option, true); //初始化蝌蚪图样例
          }, 5000);
          // myChartk.setOption(option,);
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
        });
    }
  }
};

//模块一：使用订单类别分析功能
function analysis(Date, Hour) {
  var myChartk = echarts.init(document.getElementById("TadpoleChart"));
  myChartk.clear();
  //数据读取需要改动
  this.$axios
    .get("../../static/data/TadpoleChart/" + Date + "/" + Hour + "小时.json")
    .then(res => {
      var didiData = res.data;
      var hStep = 300 / (didiData.length - 1); //路径颜色
      let busLinesk = [].concat.apply(
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
      let busLinesk2 = [].concat.apply(
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
      setTimeout(() => {
        //未来让加载动画效果明显,这里加入了setTimeout,实现2s延时
        myChartk.hideLoading(); //没有加载出来隐藏加载动画
        myChartk.setOption(option, true); //初始化蝌蚪图样例
      }, 5000);
      // myChartk.setOption(option,);
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
    });
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

<style>
#TadpoleChart {
  width: 950px;
  height: 400px;
}
</style>