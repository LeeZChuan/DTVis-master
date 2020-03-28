<template>
  <div id="app">
    <div id="ThreeDhotChart" style="width: 1200px;height:800px;"></div>
  </div>
</template>
<script>
var echarts = require("echarts");
// 引入 ECharts 主模块
//3DhotChart (3D热力图）用于展示海口市订单整体分布情况
var echarts = require("echarts/lib/echarts");

export default {
  name: "3DhotChart",
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