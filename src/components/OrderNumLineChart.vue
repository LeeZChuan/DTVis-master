<template>
  <div>
    <div id="OrderNumLineChart" style="width: 1050px;height:300px;"></div>
  </div>
</template>

<!--订单的出行距离与该订单出行距离数量组合折线图-->

<script>
var echarts = require("echarts"); // 引入 ECharts 主模块
export default {
  name: "OrderNumLineChart",
  data() {
    return {
      msg: "Welcome to OrderNumLineChart"
    };
  },
  computed: {
    TimeDate() {
      return this.$store.state.TimeDate;
    }
  },
  watch: {
    TimeDate: function(curVal, oldVal) {
      //需要执行的画图代码,用于时刻监听该图的日期更换
      // console.log(curVal, oldVal, "watch监听事件"); //打印出结果isRed的前世和今生值
      this.drawOrderLine(curVal, this.$store.state.TimeDate);
    }
  },
  mounted() {
    //页面初始化函数
    this.drawOrderLine(this.$store.state.TimeDate);
  },
  methods: {
    drawOrderLine(Date) {
      //基于准备好的DOM，初始化Echarts实例
      let myChart_line = echarts.init(document.getElementById("OrderNumLineChart"));
      //没有加载出来使用加载动画
      myChart_line.showLoading();
      //获取数据
      this.$axios.get("../../static/data/LineChart/"+Date+"_lineChart.json").then(res => {
        this.orderData = res.data; //res.data可根据你的数据格式来，看需求res
        let colors = ['rgba(76,180,231,0.4)', '#d14a61', '#675bba'];
        var fontColor = '#cdddf7';
        let optionCalen = {
          color: colors,
          tooltip: {
            trigger: "item",
          },
          // 网格
          grid: {
            left: '3%',
            right: '0%',
            top: '20%',
            bottom: '0%',
            containLabel: true
          },
          // 图例
          legend: {
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
          // 横轴 时间
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
              data: this.orderData.map(function (item) {
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
          // 两组数据：[出行距离， 订单数量]
          series: [{
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
            data: this.orderData.map(function (item) {
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
            data: this.orderData.map(function (item) { 
              return item[1];
            })
          }]
        };

        setTimeout(() => {
          //未来让加载动画效果明显,这里加入了setTimeout,实现2s延时
          myChart_line.hideLoading(); //没有加载出来隐藏加载动画
          myChart_line.setOption(optionCalen);
        }, 2000);
      },
    )}
  },
  computed: {
    //计算属性 取存在状态库中的值
  },
  watch: {}
}
</script>