<template>
  <div id="container">
    <!-- 订单起点情况热力图，宽度很合适，实现了地图的旋转以及放大缩小 -->
    <el-amap id="StartHeatMapChart"></el-amap>
  </div>
</template>

<script>
// import { lazyAmapApiLoaderInstanse } from "vue-amap";
require("echarts-extension-amap");
var echarts = require("echarts");
export default {
  name: "StartHeatMapChart",
  data() {
    return {};
  },
  computed: {
    TimeDate() {
      return this.$store.state.TimeDate;
    },
    TimeHour() {
      return this.$store.state.TimeHour;
    }
  },
  watch: {
    TimeDate: function(curVal, oldVal) {
      //需要执行的画图代码,用于时刻监听该图的日期更换
      if (true) {
        if (curVal) {
          this.drawStartHeatMapChart(curVal, this.$store.state.TimeHour);
        } else {
          this.drawStartHeatMapChart(oldVal, this.$store.state.TimeHour);
        }
      }
    },
    TimeHour: function(CurVal, OldVal) {
      //需要执行的画图代码,用于时刻监听该图的日期更换
      if (true) {
        if (CurVal) {
          this.drawStartHeatMapChart(this.$store.state.TimeDate, CurVal);
        } else {
          this.drawStartHeatMapChart(this.$store.state.TimeDate, OldVal);
        }
      }
    }
  },
  mounted() {
    //执行方法
    this.drawStartHeatMapChart(
      this.$store.state.TimeDate,
      this.$store.state.TimeHour
    );
  },
  methods: {
    drawStartHeatMapChart(Date, Hour) {
      //画起点热力图的方法
      this.$axios
        // 读取json文件到didiData
        .get(
          "../../static/data/3DhotChart/start/" + Date + "/" + Hour + ".json"
        )
        .then(res => {
          var heatmap = new AMap.Heatmap(map, heatmapOpts); //初始化heatmap对象
          var didiStartHotData = res.data;
          var lnglat = new AMap.LngLat(110.32835483551025, 20.01996791722277);
          var map = new AMap.Map("StartHeatMapChart", {
            viewMode: "3D",
            defaultCursor: "pointer",
            pitch: 0, //俯仰角度，默认0，[0,83]，2D地图下无效 。
            resizeEnable: true, //是否监控地图容器尺寸变化，默认值为false
            center: lnglat,
            zoom: 13,
            mapStyle: "amap://styles/grey", // 自定义地图样式主题
            // echartsLayerZIndex: 2019, // 高德地图自定义EchartsLayer的zIndex，默认2000
            buildingAnimation: true,
            rotateEnable: true, //可以旋转
            pitchEnable: true,
            resizeEnable: true
          });

          //3D罗盘控制添加
          AMap.plugin(["AMap.ControlBar"], function() {
            // 添加 3D 罗盘控制
            map.addControl(new AMap.ControlBar());
          });
          //热力图相关参数
          var heatmapOpts = {
            //3d 相关的参数
            "3d": {
              //热度转高度的曲线控制参数，可以利用左侧的控制面板获取
              heightBezier: [0.465, 0.115, 0.8, 0.36],
              //取样精度，值越小，曲面效果越精细，但同时性能消耗越大
              gridSize: 2,
              heightScale: 1
            }
          };
          //初始化heatmap对象
          var heatmap = new AMap.Heatmap(map, heatmapOpts);
          //设置数据集
          heatmap.setDataSet({
            data: didiStartHotData,
            max: 20
          });

          // //创建右键菜单
          // var contextMenu = new AMap.ContextMenu();

          // //右键放大
          // contextMenu.addItem(
          //   "放大一级",
          //   function() {
          //     map.zoomIn();
          //   },
          //   0
          // );

          // //右键缩小
          // contextMenu.addItem(
          //   "缩小一级",
          //   function() {
          //     map.zoomOut();
          //   },
          //   1
          // );

          // //右键显示全国范围
          // contextMenu.addItem(
          //   "缩放至全国范围",
          //   function(e) {
          //     map.setZoomAndCenter(4, [108.946609, 34.262324]);
          //   },
          //   2
          // );

          // //地图绑定鼠标右击事件——弹出右键菜单
          // map.on("rightclick", function(e) {
          //   contextMenu.open(map, e.lnglat);
          //   contextMenuPositon = e.lnglat;
          //   console.log(contextMenuPositon);
          // });

          // //右键添加Marker标记
          // contextMenu.addItem(
          //   "添加标记",
          //   function(e) {
          //     var marker = new AMap.Marker({
          //       map: map,
          //       position: contextMenuPositon //基点位置
          //       //position: e.lnglat,//右键菜单位置 //基点位置
          //     });
          //   },
          //   3
          // );

          // contextMenu.open(map, lnglat);

          // //创建右键菜单
          // var menu = new ContextMenu(map);

          // //自定义菜单类
          // function ContextMenu(map) {
          //   var me = this;

          //   //地图中添加鼠标工具MouseTool插件
          //   this.mouseTool = new AMap.MouseTool(map);

          //   this.contextMenuPositon = null;

          //   var content = [];

          //   content.push("<div class='info context_menu'>");
          //   content.push("  <p onclick='menu.zoomMenu(0)'>缩小</p>");
          //   content.push(
          //     "  <p class='split_line' onclick='menu.zoomMenu(1)'>放大</p>"
          //   );
          //   content.push(
          //     "  <p class='split_line' onclick='menu.distanceMeasureMenu()'>距离量测</p>"
          //   );
          //   content.push("  <p onclick='menu.addMarkerMenu()'>添加标记</p>");
          //   content.push("</div>");

          //   //通过content自定义右键菜单内容
          //   this.contextMenu = new AMap.ContextMenu({
          //     isCustom: true,
          //     content: content.join("")
          //   });
          //   //地图绑定鼠标右击事件——弹出右键菜单
          //   map.on("rightclick", function(e) {
          //     me.contextMenu.open(map, e.lnglat);
          //     me.contextMenuPositon = e.lnglat; //右键菜单位置
          //   });
          // }

          // ContextMenu.prototype.zoomMenu = function zoomMenu(tag) {
          //   //右键菜单缩放地图
          //   if (tag === 0) {
          //     map.zoomOut();
          //   }
          //   if (tag === 1) {
          //     map.zoomIn();
          //   }
          //   this.contextMenu.close();
          // };

          // ContextMenu.prototype.distanceMeasureMenu = function() {
          //   //右键菜单距离量测
          //   this.mouseTool.rule();
          //   this.contextMenu.close();
          // };

          // ContextMenu.prototype.addMarkerMenu = function() {
          //   //右键菜单添加Marker标记
          //   this.mouseTool.close();
          //   var marker = new AMap.Marker({
          //     map: map,
          //     position: this.contextMenuPositon //基点位置
          //   });
          //   this.contextMenu.close();
          // };

          // menu.contextMenu.open(map, lnglat);
        });
    }
  }
};
// export default Hour;
</script>
<style>
#StartHeatMapChart {
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