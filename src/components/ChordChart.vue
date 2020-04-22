<template>
  <div class="hello">
    <div id="container"></div>
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
  mounted() {
    this.moreChart();
  },
  methods: {
    moreChart() {
      if (this.chart) {
        this.chart.destroy();
      }
      this.$axios.get("../../static/data/hexiantu/2017-05-13_hexiantu.json").then(res => {
        var chData = res.data; //res.data可根据你的数据格式来，看需求
        console.log(chData);
        // 具体图表设置
        let optionchord={
          title: {
            text: '订单情况和弦图'
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
            
          series: [{
              keys: ['from', 'to', 'weight'],
              data: this.chData.get("value"),
            //   data: [
            //   ['Brazil', 'Portugal', 5],
            //   ['Brazil', 'France', 1],
            //   ['Brazil', 'Spain', 1],
            //   ['Brazil', 'England', 1],
            //   ['Canada', 'Portugal', 1],
            //   ['Canada', 'France', 5],
            //   ['Canada', 'England', 1],
            //   ['Mexico', 'Portugal', 1],
            //   ['Mexico', 'France', 1],
            //   ['Mexico', 'Spain', 5],
            //   ['Mexico', 'England', 1],
            //   ['USA', 'Portugal', 1],
            //   ['USA', 'France', 1],
            //   ['USA', 'Spain', 1],
            //   ['USA', 'England', 5],
            //   ['Portugal', 'Angola', 2],
            //   ['Portugal', 'Senegal', 1],
            //   ['Portugal', 'Morocco', 1],
            //   ['Portugal', 'South Africa', 3],
            //   ['France', 'Angola', 1],
            //   ['France', 'Senegal', 3],
            //   ['France', 'Mali', 3],
            //   ['France', 'Morocco', 3],
            //   ['France', 'South Africa', 1],
            //   ['Spain', 'Senegal', 1],
            //   ['Spain', 'Morocco', 3],
            //   ['Spain', 'South Africa', 1],
            //   ['England', 'Angola', 1],
            //   ['England', 'Senegal', 1],
            //   ['England', 'Morocco', 2],
            //   ['England', 'South Africa', 7],
            //   ['South Africa', 'China', 5],
            //   ['South Africa', 'India', 1],
            //   ['South Africa', 'Japan', 3],
            //   ['Angola', 'China', 5],
            //   ['Angola', 'India', 1],
            //   ['Angola', 'Japan', 3],
            //   ['Senegal', 'China', 5],
            //   ['Senegal', 'India', 1],
            //   ['Senegal', 'Japan', 3],
            //   ['Mali', 'China', 5],
            //   ['Mali', 'India', 1],
            //   ['Mali', 'Japan', 3],
            //   ['Morocco', 'China', 5],
            //   ['Morocco', 'India', 1],
            //   ['Morocco', 'Japan', 3],
            //   ['Japan', 'Brazil', 1]
            // ],
              type: 'dependencywheel',
              name: 'Dependency wheel series',
              dataLabels: {
              color: "#42b983",
              textPath: {
                enabled: true,
                attributes: {
                  dy: 5
                }
              },
              distance: 12
            },
            size: '95%'
          }],
          subtitle: {
            text: "测试..."
          },
          //*************************************************************/
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
.container{
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