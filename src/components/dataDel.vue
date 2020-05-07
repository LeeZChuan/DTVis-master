<template>
  <div id="container">
    <!-- 宽度很合适，实现了地图的旋转以及放大缩小 -->
    <el-amap id="HeatMapChart"></el-amap>
  </div>
</template>

<script>
// import { lazyAmapApiLoaderInstanse } from "vue-amap";
require("echarts-extension-amap");
var echarts = require("echarts");
export default {
  name: "HeatMapChart",
  data() {
    return {};
  },
  mounted() {
    this.drawHeatMapChart();
  },
  methods: {
    drawHeatMapChart() {
      //   var HeatmapChart = echarts.init(document.getElementById("HeatMapChart"));
      this.$axios
        // 读取json文件到didiData
        .get("../../static/data/ChordChart/2017-05-16_ChordChart.json")
        .then(res => {
          var didiStartHotData = res.data;
          // console.log(didiStartHotData.value);
          var data1 = didiStartHotData.value;

          var startStreet = new Array();
          var endStreet = new Array();

          var temp = 1;
          var tempData = new Array();
          for (var i = 0; i < 1104; i++) {
            // console.log(data1[i]);
            if (data1[i][1] !== data1[i + 1][1]) {
              startStreet.push(data1[i + 1][1]);
              tempData.push(temp);
              var temp = 1;
            } else {
              temp++;
            }
          }
          // console.log(startStreet);
          var wordCloudData = new Array();
          for (let i = 0; i < startStreet.length; i++) {
            wordCloudData.push({
              "name": startStreet[i],
              "value": tempData[i]
            });
          }

          //以下方法为数据处理方法，并可以打印出数据
          function fakeClick(obj) {
            var ev = document.createEvent("MouseEvents");
            ev.initMouseEvent(
              "click",
              true,
              false,
              window,
              0,
              0,
              0,
              0,
              0,
              false,
              false,
              false,
              false,
              0,
              null
            );
            obj.dispatchEvent(ev);
          }
          function exportRaw(name, data) {
            var urlObject = window.URL || window.webkitURL || window;
            var export_blob = new Blob([data]);
            var save_link = document.createElementNS(
              "http://www.w3.org/1999/xhtml",
              "a"
            );
            save_link.href = urlObject.createObjectURL(export_blob);
            save_link.download = name;
            fakeClick(save_link);
          }
          exportRaw("2017-5-16.txt", JSON.stringify(wordCloudData));
        });
    }
  }
};
</script>
<style>
#HeatMapChart {
  width: 950px;
  height: 400px;
}
.input-card {
  width: 150px;
  top: 10px;
  bottom: auto;
}
.context_menu {
  position: relative;
  min-width: 12rem;
  padding: 0;
  background: white;
}

.context_menu p {
  cursor: pointer;
  padding: 0.25rem 1.25rem;
}

.context_menu p:hover {
  background: #ccc;
}
</style>