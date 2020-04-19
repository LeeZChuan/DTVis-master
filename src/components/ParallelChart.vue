<template>
  <div>
    <div id="ParallelChart" style="width: 1050px;height:300px;"></div>
  </div>
</template>

<!--平行坐标系：
    目的：分析多个因素对出行量的影响
    x1：日期（月1-30）
    x2：天气（晴、多云、阴、小雨、中雨、大雨、暴雨）
    x3：出行距离（km）
    x4：上车时间（24h）
    x5：上车街区（四个区域或更多）
    x6：订单数量（次）
    -->

<script>
var echarts = require("echarts"); // 引入 ECharts 主模块
export default {
  name: "ParallelChart",
  data() {
    return {
      msg: "Welcome to ParallelChart"
    };
  },
  mounted() {
    //页面初始化函数
    // console.log("平行坐标系");
    this.drawLineTest();
  },
  methods: {
    drawLineTest() {
      //基于准备好的DOM，初始化Echarts实例
      let paraChart = echarts.init(document.getElementById("ParallelChart"));
      //没有加载出来使用加载动画
      paraChart.showLoading();
      //获取数据
      // console.log("平行坐标系：[x1，x2，x3，...]");
      this.$axios.get("").then(res => {
        this.paraData = res.data;
        let colors = ['rgba(76,180,231,0.4)', '#d14a61', '#675bba'];
        var fontColor = '#cdddf7';
        let optionpara = {
   
        };

        setTimeout(() => {
          //加载动画效果,2s延时
          paraChart.hideLoading(); 
          paraChart.setOption(optionpara);
        }, 2000);
      },
    )}
  },
  computed: {
  },
  watch: {}
}
</script>