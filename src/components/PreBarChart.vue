<template>
  <div>
    <div id="PreBarChart" style="width: 1100px;height:300px;"></div>
  </div>
</template>

<!-- 订单数量预测柱状图 -->
<!-- 使用算法进行预测，储存结果 -->

<script>
var echarts = require("echarts"); // 引入 ECharts 主模块
export default {
  name: "PreBarChart",  
  data() {
    return {
      msg: "Welcome to PreBarChart"
    };
  },
  mounted() {
    //页面初始化函数
    // console.log("预测柱状图初始化成功");
    this.drawBar();
  },
  methods: {
    drawBar() {
        //基于准备好的DOM，初始化Echarts实例
        let barChart = echarts.init(document.getElementById("PreBarChart"));
        //没有加载出来使用加载动画
        barChart.showLoading();
        //**** 获取预测数据 ****
        this.$axios.get("../../static/data/prediction.json").then(res => {
        this.preData = res.data; //res.data为数据
        let colors = ['rgba(76,180,231,0.4)', '#d14a61', '#675bba'];
        // 字体颜色
        var fontColor = '#cdddf7';
        let optionPre = {
            // 标题
            title: {
                top: '4%',
                left: '2%',
                text: '海口市订单数量预测',
                textStyle: {
                    color: '#cdddf7',
                },
                subtext: '根据算法进行合理预测'
            },
            // 提示
            tooltip: {
                trigger: 'axis'
            },
            // 图例
            legend: {
                top: 15,
                textStyle: {
                    color: '#cdddf7'
                },
                data: ['实际订单', '预测订单']
            },
            // 网格
            grid: {
                top: '28%'
            },
            toolbox: {
                top: '2%',
                show: true,
                feature: {
                    dataView: { show: true, readOnly: false },
                    magicType: { show: true, type: ['line', 'bar'] },
                    restore: { show: true },
                    saveAsImage: { show: true }
                }
            },
            calculable: true,
            xAxis: [
                {
                    type: 'category',
                    axisLine: {
                        lineStyle: {
                            color: '#cdddf7',
                            width: 1,    //这里是为了突出显示加上的                                                                               
                        }
                    },
                    //日期数据导入
                    data: this.preData.map(function (item) {                                                                    
                        return item[0];
                    }),
                }
            ],
            yAxis: [
                {
                    type: 'value',
                    axisLine: {
                        lineStyle: {
                            color: 'rgb(72,137,251)',
                            width: 1,
                        }
                    },
                }
            ],
            dataZoom: [
                {
                    show: true,
                    start: 80,
                    end: 100,
                    dataBackground: {
                        lineStyle: {
                            color: '#fff',
                            width: 1
                        }
                    },
                    textStyle: {
                        color: '#cdddf7'
                    }
                },
                {
                    type: 'inside',
                    start: 80,
                    end: 100,
                    dataBackground: {
                        lineStyle: {
                            color: '#fff',
                            width: 1
                        }
                    },
                    textStyle: {
                        color: '#cdddf7'
                    }
                },
                {
                    show: true,
                    yAxisIndex: 0,
                    filterMode: 'empty',
                    width: 30,
                    height: '60%',
                    showDataShadow: false,
                    left: '93%',
                    textStyle: {
                        color: '#cdddf7'
                    }
                }
            ],
            series: [
                {
                    //实际滴滴订单数量
                    name: '实际订单',
                    type: 'bar',
                    itemStyle: {
                        normal: {
                            color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                                offset: 0,
                                color: "rgba(72,137,251,1)"  // 0% 处的颜色
                            }, {
                                offset: 1,
                                color: "rgba(72,137,251,0.5)" // 100% 处的颜色
                            }], false)
                        },
                    },
                    data: this.preData.map(function (item) {
                        return item[1];
                    }),
                    markPoint: {
                        data: [
                            { type: 'max', name: '最大值' },
                            { type: 'min', name: '最小值' }
                        ]
                    },
                    markLine: {
                        lineStyle: {
                            color: 'rgba(72,137,251,1)',
                        },
                        data: [
                            { type: 'average', name: '平均值' }
                        ]
                    }
                },
                {
                    name: '预测订单',
                    type: 'bar',
                    itemStyle: {
                        normal: {
                            color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [{
                                offset: 0,
                                color: "rgb(246,150,23)"  // 0% 处的颜色
                            }, {
                                offset: 1,
                                color: "rgba(246,150,23,0.5)" // 100% 处的颜色
                            }], false)
                        },
                    },
                    //预测订单数量
                    data: this.preData.map(function (item) {
                        return item[2];
                    }),
                    markPoint: {
                        data: [
                            { type: 'max', name: '最大值' },
                            { type: 'min', name: '最小值' }
                        ]
                    },
                    markLine: {
                        lineStyle: {
                            color: 'rgb(246,150,23)',
                        },
                        data: [
                            { type: 'average', name: '平均值' }
                        ]
                    }
                }
            ]
        };
        setTimeout(() => {
          //未来让加载动画效果明显,这里加入了setTimeout,实现2s延时
          barChart.hideLoading(); //没有加载出来隐藏加载动画
          barChart.setOption(optionPre);
        }, 2000);
      },
    )},
    computed: {
    //计算属性 取存在状态库中的值
    },
    watch: {}
    }
}
</script>