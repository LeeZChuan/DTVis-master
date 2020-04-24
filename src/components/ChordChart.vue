<template>
  <div class="hello">
    <div
      id="container"
      style=" width: 700px; height: 700px; position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        margin: auto;"
    ></div>
  </div>
</template>

<script>
import Highcharts from "highcharts/highstock";
import HighchartsMore from "highcharts/highcharts-more";
import HighchartsDrilldown from "highcharts/modules/drilldown";
import Highcharts3D from "highcharts/highcharts-3d";
import HighChartssankey from "highcharts/modules/sankey";
import dependency from "highcharts/modules/dependency-wheel";

HighchartsMore(Highcharts);
HighchartsDrilldown(Highcharts);
Highcharts3D(Highcharts);
HighChartssankey(Highcharts);
dependency(Highcharts);

export default {
  name: "ChordChart",
  props: {
    msg: String
  },
  computed: {
    TimeDate() {
      return this.$store.state.TimeDate;
    }
  },
  watch: {
    TimeDate: function(curVal, oldVal) {
      //需要执行的画图代码,用于时刻监听该图的日期更换
      this.ChordChart(curVal, this.$store.state.TimeDate);
    }
  },
  mounted() {
    this.ChordChart(this.$store.state.TimeDate);
  },
  methods: {
    ChordChart(Date) {
      if (this.chart) {
        this.chart.destroy();
      }
      this.$axios
        .get("../../static/data/ChordChart/"+Date+"_ChordChart.json")
        .then(res => {
          var chData = res.data; //chData可根据你的数据格式来，看需求
          // 具体图表设置
          let optionchord = {
            title: {
              text: "具体街道情况交通流量和弦图"
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
                data: chData.value,
                type: "dependencywheel",
                name: "Dependency wheel series",
                dataLabels: {
                  color: "#42b983",
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
          // 初始化 Highcharts 图表
          this.chart = new Highcharts.Chart("container", optionchord);
        });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  width: 800px;
  height: 800px;
  margin: auto;
}

/* h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
} */
</style>