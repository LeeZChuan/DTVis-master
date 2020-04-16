<template>
  <div>
    <div id="LineTest" style="width: 1050px;height:300px;"></div>
  </div>
</template>

<!--学习使用 vue ： 画 订单数量折线图-->

<script>
var echarts = require("echarts"); // 引入 ECharts 主模块
export default {
  name: "LineTest",
  data() {
    return {
      msg: "Welcome to LineTest"
    };
  },
  mounted() {
    //页面初始化函数
    // console.log("订单数量折线图初始化成功");
    this.drawLineTest();
  },
  methods: {
    drawLineTest() {
      //基于准备好的DOM，初始化Echarts实例
      let myChart_line = echarts.init(document.getElementById("LineTest"));
      //没有加载出来使用加载动画
        myChart_line.showLoading();
      //获取数据
      // console.log("这是订单数量折线图");
      this.$axios.get("../../static/data/LineChart/2017-05-13_lineChart.json").then(res => {
        this.areaData = res.data; //res.data可根据你的数据格式来，看需求res
        console.log(this.areaData); //打印看看数据吧
        // let areaData=
        let colors = ['rgba(76,180,231,0.4)', '#d14a61', '#675bba'];
        let optionCalen = {
          color: colors,
          // tooltip: {
          //   trigger: "item",
          // },
          grid: {
            left: '3%',
            right: '0%',
            top: '20%',
            bottom: '0%',
            containLabel: true
          },
          // 图例
          legend: {
            //还可以展现很多信息（例如，节假日，具体天气情况等等），在这里添加在series里添加数据调用即可
            show: true,
            right: '0%',
            icon: 'stack',
            itemWidth: 10,
            itemHeight: 10,
            textStyle: {
            color: '#cdddf7'
            },
            data: ['出行时间', '出行距离', '订单数量']
          },
          // 横轴
          xAxis:[
            {
              type: 'category',
              boundaryGap: false,
              axisLabel: {
                color: fontColor
              },
              axisLine: {
                show: true,
                lineStyle: {
                  color: '#397cbc'
                }
              },
              axisTick: {
                show: false,
              },
              splitLine: {
                show: true,
                lineStyle: {
                  color: '#57617B'
                }
              },
              data: this.areaData.map(function (item) {
                return item[0];
              },)
            }
          ],
          // y轴
          yAxis: [
            {
              // 左边坐标轴-订单数量
              name: "订单数量",
              type: "value",
              min: 0,
              max: 15000,
              axisLabel: {
                formatter: '{value}',
                textStyle: {
                  color: 'rgb(97,165,207)'
                }
              },
              axisLine: {
                lineStyle: {
                  color: 'rgb(97,165,207)'
                }
              },
              axisTick: {
                show: false,
              },
              splitLine: {
                show: true,
                lineStyle: {
                  color: 'rgb(97,165,207)'
                }
              }
            },
            {
              type: 'value',
              name: '出行距离',
              min: 0,
              max: 25,
              axisLabel: {
                formatter: '{value} km',
                textStyle: {
                  color: 'rgb(246,150,23)'
                }
              },
              axisLine: {
                lineStyle: {
                  color: 'rgb(246,150,23)'
                }
              },
              axisTick: {
                show: false,
              },
              splitLine: {
                show: true,
                lineStyle: {
                  color: '#11366e',
                  type: 'dashed',
                }
              }
            }
          ],
          series: [{
            //这里是数据读取
            name: '出行距离',
            type: 'line',
            stack: '总量',
            symbol: 'circle',
            symbolSize: 8,
            yAxisIndex: 1,
            itemStyle: {
              emphasis: {
                color: 'rgb(246,150,23)',
                borderColor: 'rgba(246,150,23,0.2)',
                extraCssText: 'box-shadow: 8px 8px 8px rgba(0, 0, 0, 1);',
                borderWidth: 10
              },
              normal: {
                color: 'rgb(246,150,23)',
                lineStyle: {
                  color: "rgb(246,150,23)",
                  width: 1
                },
                areaStyle: {
                  //color: '#94C9EC'
                  color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                    offset: 0,
                    color: 'rgba(7,44,90,0.1)'
                  }, 
                  {
                    offset: 1,
                    color: 'rgba(246,150,23,0.9)'
                  }]),
                 }
              }
            },
            data: this.areaData.map(function (item) {
              return item[2];
            })
          },
          {
            name: '订单数量',
            type: 'line',
            stack: '总量',
            symbol: 'circle',
            symbolSize: 8,
            itemStyle: {
              emphasis: {
                color: 'rgb(97,165,207)',
                borderColor: 'rgba(97,165,207,0.2)',
                extraCssText: 'box-shadow: 8px 8px 8px rgba(0, 0, 0, 1);',
                borderWidth: 10
              },
              normal: {
                color: 'rgb(97,165,207)',
                lineStyle: {
                  color: "rgb(97,165,207)",
                  width: 1
                },
                areaStyle: {
                  color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                  offset: 0,
                  color: 'rgba(7,44,90,0.1)'
                },{
                  offset: 1,
                  color: 'rgba(97,165,207,0.9)'
                  }]),
                }
              }
            },
            data: this.areaData.map(function (item) { 
              return item[1];
            })
          }]
        };
      },
    )}
  },
  computed: {
    //计算属性 取存在状态库中的值
  },
  watch: {}
}
</script>