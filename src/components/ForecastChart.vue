<template>
  <div id="app">
    <div id="ForecastChart" style="width: 1200px;height:800px;"></div>
  </div>
</template>
<script>
var echarts = require("echarts");
// 引入 ECharts 主模块
//ForecastChart (预测视图，分为整体预测柱状图，订单具体细化预测花型散点图）用于展示海口市订单整体分布情况
var echarts = require("echarts/lib/echarts");

export default {
  name: "ForecastChart",
  data() {

    return {
      ThreeDhotChart:"",
      hotChartOption:{
        
      }

    };
  },
  components: {},
  computed: {},
  methods: {},
  mounted: function() {}
};
</script>