<template>
  <div class="hello">
    <div id="highcharts-container"></div>
  </div>
</template>
<script>

// var Highcharts = require("highcharts");
// require("highcharts/modules/exporting")(Highcharts);

import Highcharts from "highcharts/highstock";
import HighchartsMore from "highcharts/highcharts-more";
import HighchartsDrilldown from "highcharts/modules/drilldown";
import Highcharts3D from "highcharts/highcharts-3d";

HighchartsMore(Highcharts);
HighchartsDrilldown(Highcharts);
Highcharts3D(Highcharts);


export default {
  name: "SnakyChart",
  data() {
    return {
    };
  },
  mounted() {
    //页面初始化函数
    this.drawChart();
  },
  methods: {
    drawChart() {
      if (this.chart) {
        this.chart.destroy();
      }
      //获取数据
      this.$axios
        .get("../../static/data/hexiantu/2017-05-13_hexiantu.json")
        .then(res => {
          var sankeyData = res.data; //res.data可根据你的数据格式来，看需求
          let chartOptions = {
            title: {
              text: "订单情况和弦图"
            },
            credits: {
              enabled: false
            },
            navigation: {
              buttonOptions: {
                align: "left"
              }
            },
            colors: [
              "#A6C840",
              "#003d73",
              "#edd170",
              "#0878a4",
              "#c05640",
              "#f2a104",
              "#00743f",
              "#72a2c0",
              "#f05837",
              "#c0334d"
            ],
            chart: {
              backgroundColor: "rgba(128, 128, 128, 0)"
            },
            series: [
              {
                keys: ["from", "to", "weight"],
                data: sankeyData,
                type: "dependencywheel",
                name: "Dependency wheel series",
                dataLabels: {
                  color: "white",
                  textPath: {
                    enabled: true,
                    attributes: {
                      dy: 5
                    }
                  },
                  distance: 10
                },
                size: "95%"
              }
            ]
          };

          this.chart = new Highcharts.Chart("highcharts-container", chartOptions);
        });
    }
  },
  computed: {
    //计算属性 取存在状态库中的值
  },
  watch: {}
};
</script>

<style scoped>
/* 容器 */
.highcharts-container {
  width: 600px;
  height: 600px;
  border: 1px solid #ddd;
  margin: auto;
}
</style>