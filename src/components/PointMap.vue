<template>
  <div id="container">
    <!-- 订单起点情况三维气泡图，宽度很合适，实现了地图的旋转以及放大缩小 -->
    <el-amap id="PointMapChart"></el-amap>
  </div>
</template>

<script>
require("echarts-extension-amap");
var echarts = require("echarts");
export default {
  name: "PointMapChart",
  data() {
    return {};
  },
  computed: {
    TimeDate() {
      return this.$store.state.TimeDate;
    }
  },
  watch: {
    TimeDate: function(curVal, oldVal) {
      //需要执行的画图代码,用于时刻监听该图的日期更换
      this.drawPointMapChart(curVal, this.$store.state.TimeDate);
    }
  },
  mounted() {
    //执行方法
    this.drawPointMapChart(this.$store.state.TimeDate);
  },
  methods: {
    drawPointMapChart(Date) {
      //画起点热力图的方法
      this.$axios
        // 读取json文件到didiData
        .get("../../static/data/3DhotChart/start/" + Date + "/10.json")
        .then(res => {
          var didiStartHotData = res.data;
          var lnglat = new AMap.LngLat(110.32835483551025, 20.01996791722277);
          var map = new AMap.Map("PointMapChart", {
            viewMode: "3D",
            defaultCursor: "pointer",
            pitch: 10, //俯仰角度，默认0，[0,83]，2D地图下无效 。
            resizeEnable: true, //是否监控地图容器尺寸变化，默认值为false
            center: lnglat,
            zooms: [3, 20],
            mapStyle: "amap://styles/grey", // 自定义地图样式主题
            expandZoomRange: true, //
            // zoom: 13,
            zoom: 5
          });

          // 气球点添加
          var object3Dlayer = new AMap.Object3DLayer({
            zIndex: 110,
            opacity: 1
          });
          map.add(object3Dlayer);

          var lines = new AMap.Object3D.Line();
          var lineGeo = lines.geometry;

          // var provinces = result.districtList[0].districtList;
          var points3D = new AMap.Object3D.RoundPoints();
          points3D.transparent = true;
          var pointsGeo = points3D.geometry;
          //数据添加
          //写到这里了后面再改
          for (var p = 0; p < didiStartHotData.length; p++) {
            // console.log(didiStartHotData[p].lng);
            // console.log(p);
            // var center = lnglatToG20(didiStartHotData[p].lng,didiStartHotData[p].lat);
            var center = didiStartHotData[p];
            var size = didiStartHotData[p].count;
            var height = -size * 100000;
            // 连线
            lineGeo.vertices.push(center.lng, center.lat, 0);
            lineGeo.vertexColors.push(0, 1, 1, 1);
            lineGeo.vertices.push(center.lng, center.lat, height);
            lineGeo.vertexColors.push(0, 1, 1, 1);
            pointsGeo.vertices.push(center.lng, center.lat, 0); // 尾部小点
            pointsGeo.pointSizes.push(5);
            pointsGeo.vertexColors.push(0, 0, 1, 1);
            pointsGeo.vertices.push(center.lng, center.lat, height); // 空中点
            pointsGeo.pointSizes.push(size);
            pointsGeo.vertexColors.push(p * 0.029, p * 0.015, p * 0.01, 1);
          }

          points3D.borderColor = [0.4, 0.8, 1, 1];
          points3D.borderWeight = 3;
          object3Dlayer.add(lines);
          object3Dlayer.add(points3D);
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