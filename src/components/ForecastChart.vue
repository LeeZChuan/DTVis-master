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
      ThreeDhotChart: "",
      hotChartOption: {}
    };
  },
  components: {},
  computed: {},
  mounted() {
    //页面初始化函数
    this.drawForecastChart();
  },
  methods: {
    drawForecastChart(){
      let myYuce = echarts.init(document.getElementById('ForecastChart'));
      var geoCoordMap = {
        "Market": [110.32354199623335, 20.02158601280024],                                                              // 商场
        "Hospital1": [110.33388648979098, 20.029357312123295],                                                          // 附属医院
        "Station": [110.34600449319761, 19.982437787047544],                                                            // 车站
        "Square": [110.3419978414701, 20.028707619877615],                                                              // 广场
        "Government": [110.3486952530797, 20.01874102105557],                                                           // 政府
        "University": [110.34134652693201, 19.99932256358843],                                                           // 大学
        "Friendship": [110.34064896567928, 20.039496528046975],                                                          // 友谊商城
        "Hotal": [110.3003359682968, 20.02209205730502],                                                                 // 酒店
        "Hospital2": [110.28733273053196, 20.004736626542677]                                                            // 医院
    };
    }
  },
};
</script>