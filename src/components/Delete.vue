<template>
<div id="container">
   <el-amap id="ForecastPointChart"></el-amap>
</div>
</template>

<script>
// 引入地图模块 和 echarts模块
require("echarts-extension-amap");
var echarts = require("echarts");

export default {
  name: "ForecastPointChart",
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
      this.GaodeMap(curVal, this.$store.state.TimeDate);
    },
  },
  methods: {
     GaodeMap(Date) {
        // 读数据
        this.$axios.get("../../static/data/yuce/chezhan/"+Date+".json").then(res => {
          // 从文件加载数据
          var fpdata = res.data;
          // [这是个啥？待查...]
          var lnglat = new AMap.LngLat(110.32835483551025, 20.01996791722277);
          // 定义 map 生成3D地图或2D地图 [部分内容待查]
          var map = new AMap.Map("ForecastPointChart", {
            viewMode: "2D", //3D
            pitch: 0, //俯仰角度，默认0，[0,83]，2D地图下无效 。
            resizeEnable: true, //是否监控地图容器尺寸变化，默认值为false
            center: lnglat,
            zoom: 13,
            mapStyle: "amap://styles/grey", //地图样式
            echartsLayerZIndex: 2019, // 高德地图自定义EchartsLayer的zIndex，默认2000
            buildingAnimation: true,
            rotateEnable: true, //可以旋转
            pitchEnable: true,
            resizeEnable: true
          });
          // 定义标记点 和 聚类 数组
          var cluster, markers = [];
          // 生成标记点
          // demo是随机生成，改为读取文件生成 markers[] 数组
          for (var i = 0; i < fpdata.length; i += 1) {
            // 如果不将marker，push到markers里面，生成的永远都只是一个marker，地图上也只是展示一个 语句： markers.push(marker);
            markers.push(new AMap.Marker({ //生成markers
            // 位置信息，data数据格式是否正确
            // position: points[i]['lnglat'], 读取数据 [ {  "time":"","truVal":"","proVal":""  },{},{},...,{},]
            position: fpdata.value[2],
            // 标记中间的数字样式 [????]
            // 疑问：怎么显示想要的数据 fpdata.value[1]
            content: '<div style="background-color: hsla(180, 100%, 50%, 0.7); height: 24px; width: 24px; border: 1px solid hsl(180, 100%, 40%); border-radius: 12px; box-shadow: hsl(180, 100%, 50%) 0px 0px 1px;"></div>',
            // ???
            offset: new AMap.Pixel(-15, -15)
            })
          )}


          // 定义个数
           var count = markers.length;
          // 标记的具体样式设置  [??????] 
          // 同上疑问：怎么显示想要的数据 fpdata.value[1]
          // context = fpdata.value[1] ??
          var _renderClusterMarker = function (context) {
            var factor = Math.pow(context.count / count, 1 / 18);
            var div = document.createElement('div');
            // **颜色
            var Hue = 180 - factor * 180;
            var bgColor = 'hsla(' + Hue + ',100%,50%,0.7)';
            var fontColor = 'hsla(' + Hue + ',100%,20%,1)';
            var borderColor = 'hsla(' + Hue + ',100%,40%,1)';
            var shadowColor = 'hsla(' + Hue + ',100%,50%,1)';
            div.style.backgroundColor = bgColor;
             // **颜色
            var size = Math.round(30 + Math.pow(context.count / count, 1 / 5) * 20);
            div.style.width = div.style.height = size + 'px';
            div.style.border = 'solid 1px ' + borderColor;
            div.style.borderRadius = size / 2 + 'px';
            div.style.boxShadow = '0 0 1px ' + shadowColor;
            div.innerHTML = context.count;
            // 大小，颜色，居中
            div.style.lineHeight = size + 'px';
            div.style.color = fontColor;
            div.style.fontSize = '14px';
            div.style.textAlign = 'center';
            context.marker.setOffset(new AMap.Pixel(-size / 2, -size / 2));
            context.marker.setContent(div)
          };


          // ***** 应该和按钮相关 ***** 选择以后改变样式 ***** 放在这个地方？
          // 标记点选择
          addCluster();
          function addCluster(tag) {
            // 默认格式
            if (cluster) {
                cluster.setMap(null);
            }
            //完全自定义
            if (tag == 2) {
                cluster = new AMap.MarkerClusterer(map, markers, {
                    gridSize: 80,
                    renderClusterMarker: _renderClusterMarker
                });
            //自定义图标
            } else if (tag == 1) {
                var sts = [{
                    url: "https://a.amap.com/jsapi_demos/static/images/blue.png",
                    size: new AMap.Size(32, 32),
                    offset: new AMap.Pixel(-16, -16)
                }, {
                    url: "https://a.amap.com/jsapi_demos/static/images/green.png",
                    size: new AMap.Size(32, 32),
                    offset: new AMap.Pixel(-16, -16)
                }, {
                    url: "https://a.amap.com/jsapi_demos/static/images/orange.png",
                    size: new AMap.Size(36, 36),
                    offset: new AMap.Pixel(-18, -18)
                }, {
                    url: "https://a.amap.com/jsapi_demos/static/images/red.png",
                    size: new AMap.Size(48, 48),
                    offset: new AMap.Pixel(-24, -24)
                }, {
                    url: "https://a.amap.com/jsapi_demos/static/images/darkRed.png",
                    size: new AMap.Size(48, 48),
                    offset: new AMap.Pixel(-24, -24)
                }];
                cluster = new AMap.MarkerClusterer(map, markers, {
                    styles: sts,
                    gridSize: 80
                });
            } else {//默认样式
                cluster = new AMap.MarkerClusterer(map, markers, {gridSize: 80});
            }
        };

          //定义散点图
          var fpoptions = {
            "3d": {
              //高度控制
              heightBezier: [0.465, 0.115, 0.8, 0.36],
              //精度控制
              gridSize: 2,
              heightScale: 1
            }

          };
          //显示图像，初始化
          var fpmap = new AMap.Heatmap(map, fpoptions);
          //设置数据集
          fpmap.setDataSet({
            data: fpdata,
            max: 20
          });
        });
     },
    },
};
</script>

<style>
#ForecastPointChart {
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