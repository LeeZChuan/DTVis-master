<template>
  <div id="app">
    <div id="BarChart" style="width: 700px;height:600px;"></div>
  </div>
</template>
<script>
var echarts = require("echarts");
// 引入 ECharts 主模块
//ForecastChart (预测视图，分为整体预测柱状图，订单具体细化预测花型散点图）用于展示海口市订单整体分布情况
//尚未完成
var echarts = require("echarts/lib/echarts");

export default {
  name: "BarChart",
  data() {
    return {
      ThreeDhotChart: "",
      hotChartOption: {}
    };
  },
  components: {},
  computed: {},
  mounted() {
    //页面初始化函数
    this.drawForecastChart();
  },
  methods: {
    drawForecastChart() {
      //基于准备好的DOM，初始化Echarts实例
      let my3DChart_bar = echarts.init(document.getElementById("BarChart"));
      //没有加载出来使用加载动画
      my3DChart_bar.showLoading();
      //获取数据
      // console.log("这是折线图");
      this.$axios.get("../../static/data/calendarHeatMap.json").then(res => {
        var BarData = res.data; //res.data可根据你的数据格式来，看需求
        var X = 0;
        var x = 0;
        var y = 0;
        var testData = new Array();
        for (let i = 0; i < 184; i++) {
          if (i % 7 == 0) {
            //判断下一周，x++
            x++;
            y = 0;
          }
          testData[X] = [y, x, BarData[i][1]];
          y++;
          X++;
        }
        var lenth = [
          "1",
          "2",
          "3",
          "4",
          "5",
          "6",
          "7",
          "8",
          "9",
          "10",
          "11a",
          "12p",
          "13p",
          "14p",
          "15p",
          "16p",
          "17p",
          "18p",
          "19p",
          "20p",
          "21p",
          "22p",
          "23p",
          "24p",
          "25p",
          "26p"
        ];
        var days = [
          "星期一",
          "星期二",
          "星期三",
          "星期四",
          "星期五",
          "星期六",
          "星期日"
        ];
        // [y,x,num]
        var data = testData;
        let optionCalen = {
          tooltip: {},
          visualMap: {
            max: 150000,
            inRange: {
              color: [
                "#313695",
                "#4575b4",
                "#74add1",
                "#abd9e9",
                "#e0f3f8",
                "#ffffbf",
                "#fee090",
                "#fdae61",
                "#f46d43",
                "#d73027",
                "#a50026"
              ]
            }
          },
          xAxis3D: {
            type: "category",
            data: lenth,
            textStyle: {
              fontSize: 20,
              color: "#900"
            }
          },
          yAxis3D: {
            type: "category",
            data: days,
            textStyle: {
              fontSize: 20,
              color: "#900"
            }
          },
          zAxis3D: {
            type: "value"
          },
          grid3D: {
            boxWidth: 200,
            boxDepth: 80,
            viewControl: {
              // projection: 'orthographic'
            },
            light: {
              main: {
                intensity: 1.2,
                shadow: true
              },
              ambient: {
                intensity: 0.3
              }
            }
          },
          series: [
            {
              type: "bar3D",
              data: data.map(function(item) {
                return {
                  value: [item[1], item[0], item[2]]
                };
              }),
              shading: "lambert",

              label: {
                show: false,
                textStyle: {
                  fontSize: 16,
                  borderWidth: 1
                }
              },

              itemStyle: {
                opacity: 0.8
              },

              emphasis: {
                label: {
                  textStyle: {
                    fontSize: 20,
                    color: "#900"
                  }
                },
                itemStyle: {
                  color: "#900"
                }
              }
            }
          ]
        };

        setTimeout(() => {
          //未来让加载动画效果明显,这里加入了setTimeout,实现2s延时
          my3DChart_bar.hideLoading(); //没有加载出来隐藏加载动画
          my3DChart_bar.setOption(optionCalen);
        }, 2000);
      });
    }
  }
};
</script>