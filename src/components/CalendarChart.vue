<template>
  <div>
    <div id="CalendarChart" style="width: 1050px;height:300px;"></div>
  </div>
</template>

<!--弹窗出现的日历热力图，用于展示订单整体情况与天气之间的关系时间选取功能按钮还没完成-->
<script>
var echarts = require("echarts"); // 引入 ECharts 主模块
export default {
  name: "CalendarChart",
  data() {
    return {
      msg: "Welcome to CalendarChart"
    };
  },
  mounted() {
    //页面初始化函数
    this.drawCalChart();
  },
  methods: {
    drawCalChart() {
      //基于准备好的DOM，初始化Echarts实例
      let myChart_rili = echarts.init(document.getElementById("CalendarChart"));
      //没有加载出来使用加载动画
      myChart_rili.showLoading();
      //获取数据
      // console.log("这是折线图");
      var dailyData = new Array();
      this.$axios.get("../../static/data/calendarHeatMap.json").then(res => {
        dailyData = res.data; //res.data可根据你的数据格式来，看需求
        function getVirtulData(year) {
          var temp = 0;
          if (year == 2018) {
            temp = 1;
            year = 2017;
          }
          year = year || "2017";
          var date = +echarts.number.parseDate(year + "-01-01");
          var end = +echarts.number.parseDate(+year + 1 + "-01-01");
          var dayTime = 3600 * 24 * 1000;
          var data = [];
          var data1 = [];
          for (let i = 0; i < dailyData.length; i++) {
            data.push([
              dailyData[i][0],
              dailyData[i][1],
              dailyData[i][2],
              dailyData[i][3],
              dailyData[i][7],
              dailyData[i][6],
              dailyData[i][1]
            ]);
            data1.push([dailyData[i][0], dailyData[i][1]]);
          }
          if (temp == 0) {
            return data;
          } else {
            return data1;
          }
        }

        var data = getVirtulData(2017);
        var weatherData = new Array();
        for (let i = 0; i < dailyData.length; i++) {
          weatherData.push([dailyData[i][0], dailyData[i][1]]);
        }
        // console.log(weatherData);

        let option = {
          title: {
            left: "center",
            textStyle: {
              color: "#cdddf7",
              fontSize: 14
            }
          },
          chart: {
            backgroundColor: "rgba(128, 128, 128, 0.1)"
          },
          tooltip: {
            trigger: "item",
            position: "bottom",
            formatter: function(params) {
              if (params.value[4] == "") {
                return (
                  "日期: " +
                  params.value[0] +
                  "<br/>" +
                  "交易量: " +
                  params.value[1] +
                  "<br/>" +
                  "天气: " +
                  params.value[2] +
                  "<br/>" +
                  "星期:" +
                  params.value[3] +
                  "<br/>" +
                  "平均温度:  " +
                  params.value[5] +
                  "<br/>" +
                  "节假日:  " +
                  "无"
                );
              } else {
                return (
                  "日期: " +
                  params.value[0] +
                  "<br/>" +
                  "交易量: " +
                  params.value[1] +
                  "<br/>" +
                  "天气: " +
                  params.value[2] +
                  "<br/>" +
                  "星期:" +
                  params.value[3] +
                  "<br/>" +
                  "平均温度:  " +
                  params.value[5] +
                  "<br/>" +
                  "节假日:" +
                  params.value[4]
                );
              }
            }
          },

          visualMap: {
            //更新了热力图的颜色范围展示
            left: "center",
            top: "8%",
            orient: "horizontal",
            min: 0,
            max: 120000,
            splitNumber: 6, //对于连续型数据，自动平均切分成几段。默认为5段
            pieces: [
              //自定义『分段式视觉映射组件（visualMapPiecewise）』的每一段的范围，以及每一段的文字，以及每一段的特别的样式
              { min: 100000, label: ">10万" },
              { min: 80000, max: 100000, label: "<10万" }, // 不指定 max，表示 max 为无限大（Infinity）。
              { min: 70000, max: 80000, label: "<8万" },
              { min: 40000, max: 70000, label: "<6万" },
              { min: 20000, max: 40000, label: "<4万" },
              { max: 20000, label: "<2万" } // 不指定 min，表示 min 为无限大（-Infinity）。
            ],
            inRange: {
              color: [
                "#E9F4FA",
                "#B8DAEA",
                "#BFD7EF",
                "#3F8FC6",
                "#18639E",
                "#073067"
              ]
            },
            textStyle: {
              color: "#cdddf7"
            }
          },
          calendar: [
            {
              top: "32%",
              bottom: "15%",
              cellSize: [16, 25],
              left: "8%",
              range: ["2017-05-01", "2017-10-31"],
              splitLine: {
                show: true,
                lineStyle: {
                  color: "#000",
                  width: 5,
                  type: "solid"
                }
              },
              yearLabel: {
                show: false
              },
              dayLabel: {
                firstDay: 1,
                nameMap: "cn",
                color: "#cdddf7"
              },
              monthLabel: {
                show: true,
                nameMap: "cn",
                color: "#cdddf7"
              },
              itemStyle: {
                normal: {
                  color: "#323c48",
                  borderWidth: 2,
                  borderColor: "#111"
                }
              }
            }
          ],
          series: [
            {
              name: "交易量：",
              type: "heatmap",
              coordinateSystem: "calendar",
              calendarIndex: 0,
              data: data
            }
          ]
        };

        setTimeout(() => {
          //未来让加载动画效果明显,这里加入了setTimeout,实现2s延时
          myChart_rili.hideLoading(); //没有加载出来隐藏加载动画
          myChart_rili.setOption(option);
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