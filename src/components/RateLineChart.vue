<template>
  <div>
    <div id="RateLineChart" style="width: 1050px;height:300px;"></div>
  </div>
</template>

<!-- 变化率折线图 -->

<script>
var echarts = require("echarts"); // 引入 ECharts 主模块
export default {
  name: "RateLineChart",
  data() {
    return {
      msg: "Welcome to RateLineChart"
    };
  },
  mounted() {
    //页面初始化函数
    // console.log("变化率折线图初始化成功");
    this.drawLineTest();
  },
  methods: {
    drawLineTest() {
        //基于准备好的DOM，初始化Echarts实例
        let rateChart = echarts.init(document.getElementById("RateLineChart"));
        //没有加载出来使用加载动画
        rateChart.showLoading();
        //获取数据
        // console.log("这是变化率折线图");
        this.$axios.get("../../static/data/increament/2017-05-13.json").then(res => {
        this.rateData = res.data; //res.data为数据
        let colors = ['rgba(76,180,231,0.4)', '#d14a61', '#675bba'];
        // 字体颜色
        var fontColor = '#cdddf7';
        let optionRate = {
            // 图表 背景色
            chart: {
                backgroundColor: 'rgba(128, 128, 128, 0)'
            },
            // 提示条
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    lineStyle: {
                        color: '#57617B'
                    }
                }
            },
            // 图例
            legend: {
                icon: 'rect',
                itemWidth: 18,
                itemHeight: 5,
                itemGap: 13,
                data: ['订单数量变化率', 'xxx', 'xxx'],                                                              
                //在这里添加你想要展示的变化的折现情况
                right: '0%',
                textStyle: {
                    fontSize: 12,
                    color: '#cdddf7'
                }
            },
            // 网格
            grid: {
                left: '5%',
                right: '5%',
                top: '15%',
                bottom: '10%',
                containLabel: true
            },
            // x轴
            xAxis: [{
                type: 'category',
                boundaryGap: false,
                axisLine: {
                    lineStyle: {
                        color: 'rgb(97,165,207)'
                    }
                },
                axisLabel: {
                    fontSize: 14,
                    color: '#cdddf7'
                },
                splitLine: {
                    show: true,
                    lineStyle: {
                        color: '#57617B',
                        type: 'dashed'
                    }
                },
                data: this.rateData.map(function (item) {                                                                    
                    //日期数据添加
                    return item[0];
                }),
            }],
            // y轴
            yAxis: [{
                type: 'value',
                name: '变化率（%）',
                axisTick: {
                    show: false
                },
                axisLine: {
                    lineStyle: {
                        color: 'rgb(97,165,207)'
                    }
                },
                axisLabel: {
                    margin: 10,
                    textStyle: {
                        fontSize: 14,
                        color: 'rgb(97,165,207)'
                    },
                },
                splitLine: {
                    show: true,
                    lineStyle: {
                        color: '#57617B'
                    }
                }
            }],
            series: [{                                                                                              
                //折线图的属性填写
                name: '订单数量变化率',
                type: 'line',
                smooth: true,
                symbol: 'circle',
                symbolSize: 5,
                showSymbol: false,
                lineStyle: {
                    normal: {
                        width: 3
                    }
                },
                areaStyle: {
                    normal: {
                        // 线性渐变
                        color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
                            offset: 0,
                            color: 'rgba(16,97,204, 0.3)'
                        }, {
                            offset: 0.8,
                            color: 'rgba(17,235,210, 0)'
                        }], false),
                        shadowColor: 'rgba(0, 0, 0, 0.1)',
                        shadowBlur: 10
                    }
                },
                itemStyle: {
                    normal: {
                        color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
                            offset: 0,
                            color: '#E9F4FA'
                        }, {
                            offset: 1,
                            color: '#125CA3'
                        }])
                    },
                    emphasis: {
                        color: 'rgb(233,244,255)',
                        borderColor: 'rgba(233,244,255,0.2)',
                        extraCssText: 'box-shadow: 8px 8px 8px rgba(0, 0, 0, 1);',
                        borderWidth: 10
                    }
                },
                data: this.rateData.map(function (item) {                                                                    
                    // 折现数据填写；如果想要添加新的数据在json文件的数组中添加新的即可，item数组依次加一
                    return item[1];
                }),
            },]
        };
        setTimeout(() => {
          //未来让加载动画效果明显,这里加入了setTimeout,实现2s延时
          rateChart.hideLoading(); //没有加载出来隐藏加载动画
          rateChart.setOption(optionRate);
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