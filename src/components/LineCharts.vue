<template>
  <div>
    <div id="LineChart" style="width: 1050px;height:300px;"></div>
  </div>
</template>

<!--底部柱状图，用于展示订单整体情况与天气之间的关系-finsh-->
<script>
var echarts = require("echarts"); // 引入 ECharts 主模块
export default {
  name: "LineChart",
  data() {
    return {
      msg: "Welcome to LineCharts"
    };
  },
  mounted() {
    //页面初始化函数
    // console.log("折线图初始化成功");
    this.drawLineChart();
  },
  methods: {
    drawLineChart() {
      //基于准备好的DOM，初始化Echarts实例
      let myChart_line = echarts.init(document.getElementById("LineChart"));
      //没有加载出来使用加载动画
      myChart_line.showLoading();
      //获取数据
      // console.log("这是折线图");
      this.$axios.get("../../static/data/calendarHeatMap.json").then(res => {
        this.areaData = res.data; //res.data可根据你的数据格式来，看需求
        let colors = ["rgb(72,137,251)", "#f69617", "#675bba"];
        let optionCalen = {
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
              data: this.areaData.map(function(item) {
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
              data: this.areaData.map(function(item) {
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
              data: this.areaData.map(function(item) {
                return item[4];
              })
            },
            {
              name: "最低温度",
              type: "line",
              yAxisIndex: [1],
              data: this.areaData.map(function(item) {
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
              data: this.areaData.map(function(item) {
                return item[6];
              }),
              itemStyle: {
                color: "#A6C840"
              }
            }
          ]
        };

        setTimeout(() => {
          //未来让加载动画效果明显,这里加入了setTimeout,实现2s延时
          myChart_line.hideLoading(); //没有加载出来隐藏加载动画
          myChart_line.setOption(optionCalen);
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