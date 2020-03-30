<template>
  <div id="app">
    <div id="myChart" style="width: 1000px;height:450px;"></div>
  </div>
</template>
<script>
var echarts = require("echarts");
// 引入 ECharts 主模块
// var echarts = require("echarts/lib/echarts");
// // 引入柱状图
// require("echarts/lib/chart/bar");
// // 引入提示框和标题组件
// require("echarts/lib/component/tooltip");
// require("echarts/lib/component/title");
export default {
  name: "Bank",
  data() {
    return {};
  },
  components: {},
  computed: {},
  methods: {},
  mounted() {
    /*ECharts图表*/
    // console.log("这是示例图")
    var myChart = echarts.init(document.getElementById("myChart"));
    myChart.setOption({
      series: [
        {
          name: "访问来源",
          type: "pie",
          radius: "55%",
          itemStyle: {
            normal: {
              // 阴影的大小
              shadowBlur: 200,
              // 阴影水平方向上的偏移
              shadowOffsetX: 0,
              // 阴影垂直方向上的偏移
              shadowOffsetY: 0,
              // 阴影颜色
              shadowColor: "rgba(0, 0, 0, 0.5)"
            }
          },
          data: [
            { value: 400, name: "搜索引擎" },
            { value: 335, name: "直接访问" },
            { value: 310, name: "邮件营销" },
            { value: 274, name: "联盟广告" },
            { value: 235, name: "视频广告" }
          ]
        }
      ]
    });
  }
}
</script>