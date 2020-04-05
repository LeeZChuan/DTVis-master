<template>
  <div>
    <div id="MoveToChart" style="width: 1000px;height:450px;"></div>
  </div>
</template>

<!--操作台控制的街道情况迁徙图，用于展示订单整体情况与城市区域的关系-->
<script>
var echarts = require("echarts"); // 引入 ECharts 主模块
import geoCoordMap from "../../static/data/qianxitu/qianxitupoint.json"; //固定死数据读取
export default {
  name: "MoveToChart",
  data() {
    return {
      msg: "Welcome to MoveToChart"
    };
  },
  mounted() {
    //页面初始化函数
    this.drawqianxituChart();
  },
  methods: {
    drawqianxituChart() {
      //基于准备好的DOM，初始化Echarts实例
      let myChartqianxitu = echarts.init(
        document.getElementById("MoveToChart")
      );
      //没有加载出来使用加载动画
      myChartqianxitu.showLoading();
      //获取数据
      //读取数据
      // var geoCoordMap = new Array();
      // var GZData = new Array();

      // this.$axios
      //   .get("../../static/data/qianxitu/" + a + "qianxitu.json")
      //   .then(res => {
      //     GZData = res.data; //res.data可根据你的数据格式来，看需求
      //     // console.log(dailyData); //打印看看数据吧
      //   });
      this.$axios
        .get("../../static/data/qianxitu/2017-05-13qianxitu.json")
        .then(respone => {
          var GZData = respone.data; //res.data可根据你的数据格式来，看需求

          var result = new Array();
          for (let i = 0; i < GZData.length; i += 3) {
            result.push(GZData.slice(i, i + 3));
          }

          var QSsheng = []; //琼山数据
          var QSshi = [];
          var QSche = [];
          for (let i = 0; i < 3; i++) {
            QSsheng[i] = result[0][i][1].name;
            QSshi[i] = result[0][i][1].name;
            QSche[i] = result[0][i][1].value;
          }

          var QSobj = {}; //琼山对象
          for (let i = 0; i < QSsheng.length; i++) {
            QSobj[QSshi[i]] = QSsheng[i];
          }

          var LHsheng = []; //龙华数据
          var LHshi = [];
          var LHche = [];
          for (let i = 0; i < 3; i++) {
            LHsheng[i] = result[1][i][1].name;
            LHshi[i] = result[1][i][1].name;
            LHche[i] = result[1][i][1].value;
          }

          var XYsheng = []; //秀英数据
          var XYshi = [];
          var XYche = [];
          for (let i = 0; i < 3; i++) {
            XYsheng[i] = result[2][i][1].name;
            XYshi[i] = result[2][i][1].name;
            XYche[i] = result[2][i][1].value;
          }

          var MLsheng = []; //美兰数据
          var MLshi = [];
          var MLche = [];
          for (let i = 0; i < 3; i++) {
            MLsheng[i] = result[3][i][1].name;
            MLshi[i] = result[3][i][1].name;
            MLche[i] = result[3][i][1].value;
          }
          console.log(MLsheng);

          var carPath =
            "path://M4560,4996.6c-530.4-68.2-932.1-239.8-1201.2-514.8c-156-159.9-508.9-803.4-598.6-1092c-50.7-161.9-52.7-384.2-11.7-840.5c39-421.2,42.9-386.1-54.6-432.9c-117-56.5-208.7-138.4-241.8-216.4c-23.4-58.5-23.4-72.2,7.8-136.5c44.8-93.6,93.6-99.4,263.2-31.2l134.6,54.6l58.5-58.5l58.5-58.5l-48.8-536.3C2822.5-3.2,2808.9-360.1,2846-1095.2c9.7-218.4,5.8-386.1-19.5-663c-66.3-723.5-2-1550.3,159.9-2039.7c72.1-216.4,157.9-366.6,278.8-487.5c87.8-89.7,142.3-122.9,304.2-189.2c349.1-146.3,805.3-257.4,1232.4-302.3c173.6-17.5,269.1-17.5,438.8,0c659.1,74.1,1347.5,298.3,1544.4,505.1c140.4,146.3,255.4,399.7,329.6,733.2c101.4,440.7,134.6,1197.3,80,1758.9c-42.9,432.9-46.8,838.5-11.7,982.8c40.9,165.8,9.8,733.2-107.2,1959.8l-50.7,524.6l58.5,56.6l56.6,56.6l150.1-62.4c175.5-74.1,228.1-64.3,265.2,48.8c39,122.9-42.9,235.9-251.6,341.3l-85.8,44.8l13.6,157.9c7.8,87.8,21.4,261.3,31.2,384.2c25.4,300.3,23.4,503.1-1.9,627.9c-29.3,128.7-397.8,863.9-514.8,1019.9c-222.3,298.3-563.6,489.5-1066.6,596.7C5470.7,5004.4,4797.9,5025.8,4560,4996.6z M5517.5,3073.9c444.6-76.1,811.2-255.5,1051.1-516.8c195-208.7,189.1-152.1,85.8-906.7c-48.8-358.8-93.6-657.2-97.5-661.1c-5.9-5.8-117,11.7-247.7,39c-544,111.2-762.4,134.6-1269.4,134.6c-522.6,2-717.6-19.5-1271.4-128.7c-169.6-33.1-312-56.5-315.9-52.6c-3.9,3.9-48.8,304.2-99.4,664.9l-89.7,657.2l48.8,85.8c56.5,93.6,232,273,356.9,362.7c255.4,183.3,663,313.9,1127.1,360.8C4936.4,3126.5,5338.1,3105.1,5517.5,3073.9z M6443.7-2179.4v-702l-70.2-76.1c-187.2-210.6-573.3-321.8-1197.3-347.1c-717.6-29.2-1302.6,101.4-1519.1,335.4l-80,87.8v692.3c0,380.2,7.8,692.2,15.6,692.2c9.8,0,81.9-17.5,161.9-37c319.8-81.9,618.1-107.3,1236.3-107.3c631.8,0,920.4,25.4,1255.8,113.1c91.6,25.3,173.6,46.8,183.3,48.8C6437.9-1479.4,6443.7-1793.3,6443.7-2179.4z";
          var type = "流出";
          var convertData = function(data) {
            var res = [];
            for (let i = 0; i < data.length; i++) {
              // console.log(2);
              // console.log(geoCoordMap);
              var dataItem = data[i];
              var fromCoord = geoCoordMap[dataItem[0].name];//geoCoordMap是一个对象
              var toCoord = geoCoordMap[dataItem[1].name];
              if (fromCoord && toCoord) {
                res.push({
                  fromName: dataItem[0].name,
                  toName: dataItem[1].name,
                  coords: [fromCoord, toCoord],
                  value: dataItem[1].value
                });
              }
            }
            console.log(res);
            return res;
          };

          ///////////////////// 主要修改迁徙图颜色///////////////////////////////
          var color = [
            "rgba(235,255,163,0.8)",
            "rgba(213,241,112,8)",
            "rgba(161,194,63,8)",
            "rgba(114,165,56,8)"
          ];
          var series = [];

          [
            ["琼山区", result[0]],
            ["龙华区", result[1]],
            ["秀英区", result[2]],
            ["美兰区", result[3]]
          ].forEach(function(item, i) {
            series.push(
              {
                //设置飞行线
                name: item[0],
                type: "lines",
                coordinateSystem: "amap",
                zlevel: 1,
                effect: {
                  show: true,
                  period: 6,
                  trailLength: 0.7,
                  color: "#fff",
                  symbolSize: 3
                },
                lineStyle: {
                  //流动线颜色
                  normal: {
                    color: color[i],
                    width: 0,
                    curveness: 0.2
                  }
                },
                data: convertData(item[1])
              },
              {
                //设置轨迹线
                name: item[0],
                type: "lines",
                coordinateSystem: "amap",
                zlevel: 2,
                symbol: ["none", "arrow"],
                symbolSize: 10,
                effect: {
                  show: true,
                  period: 6,
                  trailLength: 0,
                  symbol: carPath,
                  symbolSize: [20, 30]
                },
                lineStyle: {
                  normal: {
                    color: color[i],
                    width: 1,
                    opacity: 0.6,
                    curveness: 0.2
                  }
                },
                data: convertData(item[1])
              },
              {
                //设置点
                name: item[0],
                type: "effectScatter",
                coordinateSystem: "amap",
                zlevel: 2,
                rippleEffect: {
                  brushType: "stroke"
                },
                label: {
                  normal: {
                    show: true,
                    position: "inside",
                    formatter: "{b}"
                  }
                },
                symbolSize: function(val) {
                  return val[2] / 10;
                },
                itemStyle: {
                  normal: {
                    color: "#A6C840"
                  }
                },
                data: item[1].map(function(dataItem) {
                  let name = "123";
                  if (dataItem[0].name === "琼山区") {
                    name = result[0][dataItem[1].name];
                  }
                  if (dataItem[0].name === "龙华区") {
                    name = result[1][dataItem[1].name];
                  }
                  if (dataItem[0].name === "秀英区") {
                    name = result[2][dataItem[1].name];
                  }
                  if (dataItem[0].name === "美兰区") {
                    name = result[3][dataItem[1].name];
                  }
                  return {
                    name: name ? name : dataItem[1].name,
                    value: geoCoordMap[dataItem[1].name].concat([
                      dataItem[1].value / 7
                    ]) //改变圆形大小
                  };
                })
              }
            );
          })

          let option = {
            amap: {
              // 加载 amap 组件 高德地图支持的初始化地图配置
              center: [110.33255483551025, 20.01716791722277], // 高德地图初始中心经纬度
              zoom: 13.3, // 高德地图初始缩放级别
              resizeEnable: true, // 是否开启resize
              mapStyle: "amap://styles/grey", // 自定义地图样式主题
              echartsLayerZIndex: 2019, // 高德地图自定义EchartsLayer的zIndex，默认2000
              // 说明：如果想要添加卫星、路网等图层
              // 暂时先不要使用layers配置，因为存在Bug
              // 建议使用amap.add的方式，使用方式参见最下方代码
              viewMode: "3D", //开启3D视图,默认为关闭
              buildingAnimation: true //楼块出现是否带动画
            },
            title: {
              text: "海口市车流量区域迁徙图",
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
            tooltip: {
              trigger: "item",
              formatter: function(params, ticket, callback) {
                // console.log(params);
                if (params.seriesType == "lines") {
                  return (
                    params.data.fromName +
                    ">" +
                    params.data.toName +
                    "<br />" +
                    params.data.value
                  );
                } else {
                  return params.name;
                }
              }
            },
            legend: {
              orient: "vertical",
              top: "bottom",
              left: "right",
              data: ["琼山区", "龙华区", "秀英区", "美兰区"],
              textStyle: {
                color: "#fff"
              },
              selectedMode: "multiple"
            },
            series: series
          };

          setTimeout(() => {
            //未来让加载动画效果明显,这里加入了setTimeout,实现2s延时
            myChartqianxitu.hideLoading(); //没有加载出来隐藏加载动画
            myChartqianxitu.setOption(option, true);
          }, 2000);
        });

 
    }
  },
  computed: {
    //计算属性 取存在状态库中的值
  },
  watch: {}
};
</script>