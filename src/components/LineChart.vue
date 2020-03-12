<template>
  <div id="app">
    <div id="LineChart" style="width: 600px;height:400px;"></div>
  </div>
</template>


<script type="text/javascript">
import axios from "axios"; //获取本地数据
var echarts = require("echarts");
// 引入 ECharts 主模块
require("echarts/lib/component/tooltip");
require("echarts/lib/component/title");
// 引入提示框和标题组件
export default {
  name: "LineChart1",
  mounted() {
    /*ECharts图表*/
    var myChart1 = echarts.init(document.getElementById("LineChart"));
    option = null;
    var app = {};
    app.title = "海口市滴滴订单数量/以及出行相关情况折线图";
    var fontColor = "#cdddf7";
    $.ajax("../../static/data/LineChart/2017-05-13_lineChart.json").then(
      res => {
        console.log("json数据为:" + res.body); //此处的res对象包含了json的文件信息和数据
      }
    );
    // console.log(data);
    var colors = ["rgba(76,180,231,0.4)", "#d14a61", "#675bba"]; //修改颜色
    myChart1.setOption(
      (option = {
        color: colors,
        tooltip: {
          show: true,
          trigger: "item"
        },
        grid: {
          left: "3%",
          right: "0%",
          top: "20%",
          bottom: "0%",
          containLabel: true
        },
        legend: {
          //还可以展现很多信息（例如，节假日，具体天气情况等等），在这里添加在series里添加数据调用即可
          show: true,
          right: "0%",
          icon: "stack",
          itemWidth: 10,
          itemHeight: 10,
          textStyle: {
            color: "#cdddf7"
          },
          data: ["出行时间", "出行距离", "订单数量"]
        },
        xAxis: [
          {
            type: "category",
            boundaryGap: false,
            axisLabel: {
              color: fontColor
            },
            axisLine: {
              show: true,
              lineStyle: {
                color: "#397cbc"
              }
            },
            axisTick: {
              show: false
            },
            splitLine: {
              show: true,
              lineStyle: {
                color: "#57617B"
              }
            },
            data: data.map(function(item) {
              // 小时数据
              return item[0];
            })
          }
        ],
        yAxis: [
          {
            type: "value",
            name: "订单数量",
            min: 0,
            max: 15000,
            axisLabel: {
              formatter: "{value}",
              textStyle: {
                color: "rgb(97,165,207)"
              }
            },
            axisLine: {
              lineStyle: {
                color: "rgb(97,165,207)"
              }
            },
            axisTick: {
              show: false
            },
            splitLine: {
              show: true,
              lineStyle: {
                color: "rgb(97,165,207)"
              }
            }
          },
          {
            type: "value",
            name: "出行距离",
            min: 0,
            max: 25,
            axisLabel: {
              formatter: "{value} km",
              textStyle: {
                color: "rgb(246,150,23)"
              }
            },
            axisLine: {
              lineStyle: {
                color: "rgb(246,150,23)"
              }
            },
            axisTick: {
              show: false
            },
            splitLine: {
              show: true,
              lineStyle: {
                color: "#11366e",
                type: "dashed"
              }
            }
          }
        ],
        series: [
          {
            name: "出行距离",
            type: "line",
            stack: "总量",
            symbol: "circle",
            symbolSize: 8,
            yAxisIndex: 1,
            itemStyle: {
              emphasis: {
                color: "rgb(246,150,23)",
                borderColor: "rgba(246,150,23,0.2)",
                extraCssText: "box-shadow: 8px 8px 8px rgba(0, 0, 0, 1);",
                borderWidth: 10
              },
              normal: {
                color: "rgb(246,150,23)",
                lineStyle: {
                  color: "rgb(246,150,23)",
                  width: 1
                },
                areaStyle: {
                  //color: '#94C9EC'
                  color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [
                    {
                      offset: 0,
                      color: "rgba(7,44,90,0.1)"
                    },
                    {
                      offset: 1,
                      color: "rgba(246,150,23,0.9)"
                    }
                  ])
                }
              }
            },
            data: data.map(function(item) {
              //添加出行距离数据
              return item[2];
            })
          },
          {
            name: "订单数量",
            type: "line",
            stack: "总量",
            symbol: "circle",
            symbolSize: 8,
            itemStyle: {
              emphasis: {
                color: "rgb(97,165,207)",
                borderColor: "rgba(97,165,207,0.2)",
                extraCssText: "box-shadow: 8px 8px 8px rgba(0, 0, 0, 1);",
                borderWidth: 10
              },
              normal: {
                color: "rgb(97,165,207)",
                lineStyle: {
                  color: "rgb(97,165,207)",
                  width: 1
                },
                areaStyle: {
                  color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [
                    {
                      offset: 0,
                      color: "rgba(7,44,90,0.1)"
                    },
                    {
                      offset: 1,
                      color: "rgba(97,165,207,0.9)"
                    }
                  ])
                }
              }
            },
            data: data.map(function(item) {
              //添加订单数量数据
              return item[1];
            })
          }
        ]
      })
    );
    if (option && typeof option === "object") {
      myChart1.setOption(option, true);
    }
    myChart1.setOption(option, true);
  }
};
</script>