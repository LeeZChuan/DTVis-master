<template>
  <div>
    <el-amap id="Chart" style="width: 980px; height: 400px;"></el-amap>
  </div>
</template>

<script>
import { lazyAmapApiLoaderInstanse } from "vue-amap";
var echarts = require("echarts");
export default {
  name: "Chart",
  data() {
    return {};
  },
  mounted() {
    this.drawChart();
  },
  methods: {
    updateForecast() {
      // this.$store.commit("updateForecast", ;
    },
    drawChart() {
      var geoCoordMap = [
        [110.34600449319761, 19.982437787047544], // 车站
        [110.34134652693201, 19.99932256358843], // 大学
        [110.3419978414701, 20.028707619877615], // 广场
        [110.3003359682968, 20.02209205730502], // 酒店
        [110.28733273053196, 20.004736626542677], // 医院
        [110.32354199623335, 20.02158601280024], // 商场
        [110.33388648979098, 20.029357312123295], // 附属医院
        [110.34064896567928, 20.039496528046975], // 友谊商城
        [110.3486952530797, 20.01874102105557] // 政府
      ];
      var colors = [
        "#9fd0d5",
        "#f68e57",
        "#eed5eb",
        "#a65bc2",
        "#9ecfd4",
        "#f8ba7f",
        "#a9e2cb",
        "#eda3b8",
        "#eff3b8"
      ]; // 颜色(需要修改)
      var map = new AMap.Map("Chart", {
        viewMode: "3D",
        pitch: 0, //俯仰角度，默认0，[0,83]，2D地图下无效 。
        resizeEnable: true, //是否监控地图容器尺寸变化，默认值为false
        center: [110.32835483551025, 20.01996791722277],
        zoom: 13,
        mapStyle: "amap://styles/grey", // 自定义地图样式主题
        // echartsLayerZIndex: 2019, // 高德地图自定义EchartsLayer的zIndex，默认2000
        buildingAnimation: true,
        rotateEnable: true,
        pitchEnable: true
      });
      var name = [
        "Station",
        "University",
        "Square",
        "Hotal",
        "Hospital2",
        "Market",
        "Hospital1",
        "Friendship",
        "Government"
      ];
      var data = "2017-05-13";
      var timeindex = "15";

      var circles = new Array();
      for (var i = 0; i < 8; i++) {
        this.$axios
          .get("../../static/data/yuce/" + name[i] + "/" + data + ".json")
          .then(res => {
            var rads = new Array();
            var temp = res.data[timeindex];
            rads.push(temp.proVal);
            circles[i] = new AMap.Circle({
              // 数据读取
              center: new AMap.LngLat(geoCoordMap[i][0], geoCoordMap[i][1]), // 圆心位置
              // 半径 数据读取
              // radius: 500,//parseInt(rads),//500,
              radius: rads, //parseInt(rads),//500,
              strokeColor: colors[i], //线颜色
              strokeOpacity: 0.5, //线透明度
              strokeWeight: 1, //线粗细度
              fillColor: colors[i], //填充颜色
              fillOpacity: 0.5 //填充透明度
            });
          });
      }

      // console.log("1" + this.temp);
      // console.log("2" + this.rads);
      // console.log("3" + this.circles);
      map.add(circles);

      var Opts = {};
      //初始化heatmap对象
      var thismap = new AMap.Map(map, Opts);
      //设置数据集
      thismap.setDataSet({
        data: points, //thisData,
        resizeEnable: true,
        max: 20
      });
    }
  }
};
</script>
<style>
.info {
  position: relative;
  top: 0;
  right: 0;
  min-width: 0;
}
</style>