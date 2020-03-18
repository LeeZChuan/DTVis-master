<template>
  <div id="app">
    <div id="LineChart" style="width: 600px;height:400px;"></div>
  </div>
</template>

<!--底部 柱状图-->
<script type="text/javascript">
import axios from "axios";
var echarts = require("echarts"); //引入echarts模块
var dom = document.getElementById("LineChart");
var myChart_line = echarts.init(dom);
var app = {};
option = null;
var app = {};
app.title = "海口市滴滴订单数量折线图 ";

$.get("data/calendarHeatMap.json", function(data) {
  var colors = ["rgb(72,137,251)", "#f69617", "#675bba"];
  myChart_line.setOption(
    (optionCalen = {
      color: colors,
      tooltip: {
        trigger: "axis",
        axisPointer: {
          type: "cross"
        }
      },
      grid: {
        right: "15%"
      },
      legend: {
        //还可以展现很多信息（例如，节假日，具体天气情况等等），在这里添加在series里添加数据调用即可
        top: 15,
        textStyle: {
          color: "#cdddf7"
        }
      },
      xAxis: [
        {
          type: "category",
          axisTick: {
            alignWithLabel: true
          },
          data: data.map(function(item) {
            return item[0];
          }),
          axisLine: {
            lineStyle: {
              color: "#cdddf7",
              width: 1 //这里是为了突出显示加上的
            }
          }
        }
      ],
      yAxis: [
        {
          // 左边坐标轴-订单数量
          name: "订单数量",
          type: "value",
          axisLine: {
            lineStyle: {
              color: "rgb(72,137,251)",
              width: 1 //这里是为了突出显示加上的
            }
          },
          splitLine: {
            show: true
          }
        },
        {
          // 右边坐标轴-平均温度
          name: "平均温度",
          type: "value",
          max: 40,
          position: "right",
          offset: 15,
          axisLine: {
            lineStyle: {
              color: "#A6C840",
              width: 1 //这里是为了突出显示加上的
            }
          },
          axisLabel: {
            formatter: "{value} ℃"
          },
          splitLine: {
            show: true,
            lineStyle: {
              type: "dashed"
            }
          }
        }
      ],
      dataZoom: [
        {
          type: "slider",
          start: 20,
          end: 45,
          dataBackground: {
            lineStyle: {
              color: "#fff",
              width: 1
            }
          },
          textStyle: {
            color: "#cdddf7"
          }
        },
        {
          type: "inside",
          start: 0,
          end: 100,
          lineStyle: {
            color: "#cdddf7"
          }
        },
        {
          show: true,
          yAxisIndex: 0,
          filterMode: "empty",
          width: 30,
          height: "60%",
          showDataShadow: false,
          left: "93%",
          textStyle: {
            color: "#cdddf7"
          }
        }
      ],
      series: [
        //这里是数据读取
        {
          name: "订单数量",
          type: "bar",
          areaStyle: {
            color: "rgba(5,140,255, 0.2)"
          },
          itemStyle: {
            normal: {
              color: new echarts.graphic.LinearGradient(
                0,
                1,
                0,
                0,
                [
                  {
                    offset: 0,
                    color: "rgba(72,137,251,1)" // 0% 处的颜色
                  },
                  {
                    offset: 1,
                    color: "rgba(72,137,251,0.5)" // 100% 处的颜色
                  }
                ],
                false
              )
            }
          },
          data: data.map(function(item) {
            return item[1];
          })
        },
        {
          name: "最高温度",
          type: "line",
          yAxisIndex: [1],
          itemStyle: {
            color: "#f69617"
          },
          data: data.map(function(item) {
            return item[4];
          })
        },
        {
          name: "最低温度",
          type: "line",
          yAxisIndex: [1],
          data: data.map(function(item) {
            return item[5];
          }),
          itemStyle: {
            color: "#6ec5cf"
          }
        },
        {
          name: "平均温度",
          type: "line",
          yAxisIndex: [1],
          data: data.map(function(item) {
            return item[6];
          }),
          itemStyle: {
            color: "#A6C840"
          }
        }
      ]
    })
  );
});

$.get("data/prediction.json", function(data) {
  //显示预测订单
  // console.log(data[1][1]);
  optionYuce = {
    title: {
      top: "4%",
      left: "2%",
      text: "海口市订单数量预测",
      textStyle: {
        color: "#cdddf7"
      },
      subtext: "根据算法进行合理预测"
    },
    tooltip: {
      trigger: "axis"
    },
    legend: {
      top: 15,
      textStyle: {
        color: "#cdddf7"
      },
      data: ["实际订单", "预测订单"]
    },
    grid: {
      top: "28%"
    },
    toolbox: {
      top: "2%",
      show: true,
      feature: {
        dataView: { show: true, readOnly: false },
        magicType: { show: true, type: ["line", "bar"] },
        restore: { show: true },
        saveAsImage: { show: true }
      }
    },
    calculable: true,
    xAxis: [
      {
        type: "category",
        axisLine: {
          lineStyle: {
            color: "#cdddf7",
            width: 1 //这里是为了突出显示加上的
          }
        },
        data: data.map(function(item) {
          //日期数据导入
          return item[0];
        })
      }
    ],
    yAxis: [
      {
        type: "value",
        axisLine: {
          lineStyle: {
            color: "rgb(72,137,251)",
            width: 1 //这里是为了突出显示加上的
          }
        }
      }
    ],
    dataZoom: [
      {
        show: true,
        start: 80,
        end: 100,
        dataBackground: {
          lineStyle: {
            color: "#fff",
            width: 1
          }
        },
        textStyle: {
          color: "#cdddf7"
        }
      },
      {
        type: "inside",
        start: 80,
        end: 100,
        dataBackground: {
          lineStyle: {
            color: "#fff",
            width: 1
          }
        },
        textStyle: {
          color: "#cdddf7"
        }
      },
      {
        show: true,
        yAxisIndex: 0,
        filterMode: "empty",
        width: 30,
        height: "60%",
        showDataShadow: false,
        left: "93%",
        textStyle: {
          color: "#cdddf7"
        }
      }
    ],
    series: [
      {
        name: "实际订单", //实际滴滴订单数量
        type: "bar",
        itemStyle: {
          normal: {
            color: new echarts.graphic.LinearGradient(
              0,
              1,
              0,
              0,
              [
                {
                  offset: 0,
                  color: "rgba(72,137,251,1)" // 0% 处的颜色
                },
                {
                  offset: 1,
                  color: "rgba(72,137,251,0.5)" // 100% 处的颜色
                }
              ],
              false
            )
          }
        },
        data: data.map(function(item) {
          return item[1];
        }),
        markPoint: {
          data: [
            { type: "max", name: "最大值" },
            { type: "min", name: "最小值" }
          ]
        },
        markLine: {
          lineStyle: {
            color: "rgba(72,137,251,1)"
          },
          data: [{ type: "average", name: "平均值" }]
        }
      },
      {
        name: "预测订单",
        type: "bar",
        itemStyle: {
          normal: {
            color: new echarts.graphic.LinearGradient(
              0,
              1,
              0,
              0,
              [
                {
                  offset: 0,
                  color: "rgb(246,150,23)" // 0% 处的颜色
                },
                {
                  offset: 1,
                  color: "rgba(246,150,23,0.5)" // 100% 处的颜色
                }
              ],
              false
            )
          }
        },
        data: data.map(function(item) {
          //预测订单数量
          return item[2];
        }),
        markPoint: {
          data: [
            { type: "max", name: "最大值" },
            { type: "min", name: "最小值" }
          ]
        },
        markLine: {
          lineStyle: {
            color: "rgb(246,150,23)"
          },
          data: [{ type: "average", name: "平均值" }]
        }
      }
    ]
  };
});
</script>